from __future__ import annotations

from typing import Optional, Type, TypeVar

import os

from PIL import Image

import numpy as np

from .image_format import ImageFormat
from ..item import Item
from ....codable import KeyDescriptor


T = TypeVar("T", bound = "BaseImageItem")


class BaseImageItem(Item):

    def __init__(self) -> None:
        super().__init__()

        self.imageData: Optional[np.ndarray] = None

    @property
    def imageExtension(self) -> str:
        for imageFormat in ImageFormat:
            imagePath = os.path.join(self.path, f"{self.name}.{imageFormat.extension}")
            if not os.path.exists(imagePath):
                continue

            return imageFormat.extension

        raise RuntimeError(f">> [Coretex] Image file not found for image item: {self.id} - {self.name}")

    @property
    def imagePath(self) -> str:
        return os.path.join(self.path, f"{self.name}.{self.imageExtension}")

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()
        descriptors["imageData"] = KeyDescriptor(isEncodable = False)

        return descriptors

    @classmethod
    def createImageItem(cls: Type[T], datasetId: int, imagePath: str) -> Optional[T]:
        """
            Creates a new image item with the provided dataset and path

            Parameters:
            datasetId: int -> id of dataset in which image item will be created
            imagePath: str -> path to the image item

            Returns:
            The created image item object
        """

        parameters = {
            "dataset_id": datasetId
        }

        return cls._genericItemImport("image-import", parameters, imagePath)

    def load(self) -> None:
        # load image
        imagePath = os.path.join(self.path, f"{self.name}.{self.imageExtension}")

        image = Image.open(imagePath)
        if image.mode != "RGB":
            image = image.convert("RGB")

        self.imageData = np.frombuffer(image.tobytes(), dtype = np.uint8)
        self.imageData = self.imageData.reshape((image.size[1], image.size[0], 3))
