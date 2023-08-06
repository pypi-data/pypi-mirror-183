from ..dataset import Dataset
from ...item import IMUItem
from ....codable import KeyDescriptor


class IMUDataset(Dataset):

    items: list[IMUItem]  # type: ignore

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()
        descriptors["items"] = KeyDescriptor("sessions", IMUItem, list)

        return descriptors
