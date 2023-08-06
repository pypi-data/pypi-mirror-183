from __future__ import annotations

from ..dataset import Dataset
from ...item import BaseImageItem
from ....codable import KeyDescriptor


class BaseImageDataset(Dataset):
    """
        Represents the Image Dataset object from Coretex.ai
    """

    items: list[BaseImageItem]  # type: ignore

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()
        descriptors["items"] = KeyDescriptor("sessions", BaseImageItem, list)

        return descriptors
