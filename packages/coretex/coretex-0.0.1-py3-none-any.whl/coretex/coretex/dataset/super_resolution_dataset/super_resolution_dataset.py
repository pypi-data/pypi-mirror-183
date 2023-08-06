from ..image_dataset import BaseImageDataset
from ...item import SuperResolutionItem
from ....codable import KeyDescriptor


class SuperResolutionDataset(BaseImageDataset):

    items: list[SuperResolutionItem]  # type: ignore

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()
        descriptors["items"] = KeyDescriptor("sessions", SuperResolutionItem, list)

        return descriptors
