from ..dataset import Dataset
from ...item import BodyTrackingItem
from ....codable import KeyDescriptor


class BodyTrackingDataset(Dataset):

    items: list[BodyTrackingItem]  # type: ignore

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()
        descriptors["items"] = KeyDescriptor("sessions", BodyTrackingItem, list)

        return descriptors
