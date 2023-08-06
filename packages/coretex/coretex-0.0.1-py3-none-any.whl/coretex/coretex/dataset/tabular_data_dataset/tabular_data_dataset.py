from ..dataset import Dataset
from ...item import TabularDataItem
from ....codable import KeyDescriptor


class TabularDataDataset(Dataset):

    items: list[TabularDataItem]  # type: ignore

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()
        descriptors["items"] = KeyDescriptor("sessions", TabularDataItem, list)

        return descriptors
