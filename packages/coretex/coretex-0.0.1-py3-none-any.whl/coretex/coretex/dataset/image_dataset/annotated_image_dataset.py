from typing import Optional, TypeVar, Type

from .base_image_dataset import BaseImageDataset
from ...annotation import ImageDatasetClasses, ImageDatasetClass
from ...item import AnnotatedImageItem
from ....codable import KeyDescriptor
from ....networking.network_manager import NetworkManager
from ....networking.request_type import RequestType


T = TypeVar("T", bound = "AnnotatedImageDataset")


class AnnotatedImageDataset(BaseImageDataset):
    """
        Represents the Image Dataset object from Coretex.ai
    """

    items: list[AnnotatedImageItem]  # type: ignore
    classes: ImageDatasetClasses

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()

        descriptors["items"] = KeyDescriptor("sessions", AnnotatedImageItem, list)
        descriptors["classes"] = KeyDescriptor("classes", ImageDatasetClass, ImageDatasetClasses)

        return descriptors

    @classmethod
    def fetchById(cls: Type[T], objectId: int, queryParameters: Optional[list[str]] = None) -> Optional[T]:
        obj = super().fetchById(objectId, queryParameters)
        if obj is None:
            return None

        response = NetworkManager.instance().genericJSONRequest(
            endpoint=f"annotation-class?dataset_id={obj.id}",
            requestType=RequestType.get,
        )

        if not response.hasFailed():
            obj.classes = cls._decodeValue("classes", response.json)

        return obj

    def classByName(self, name: str) -> Optional[ImageDatasetClass]:
        for clazz in self.classes:
            if clazz.label == name:
                return clazz

        return None

    def saveClasses(self, classes: ImageDatasetClasses) -> bool:
        """
            Saves provided classes (including their color) to dataset.
            ImageDataset.classes property will be updated on successful save

            Parameters:
            classes: list[ImageDatasetClass] -> list of classes

            Returns:
            True if dataset classes were saved, False if failed to save dataset classes
        """

        parameters = {
            "dataset_id": self.id,
            "classes": [clazz.encode() for clazz in classes]
        }

        response = NetworkManager.instance().genericJSONRequest(
            endpoint="annotation-class",
            requestType=RequestType.post,
            parameters=parameters
        )

        if not response.hasFailed():
            self.classes = classes

        return not response.hasFailed()
