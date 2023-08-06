from __future__ import annotations

from typing import Optional

from ..item import Item


class IMUItem(Item):
    """
        Represents the custom Item object from Coretex.ai
    """

    @classmethod
    def createIMUItem(cls, name: str, datasetId: int, filePath: str) -> Optional[IMUItem]:
        """
            Creates a new item with the provided name and path

            Parameters:
            name: str -> item name
            datasetId: int -> id of dataset to which item will be added
            filePath: str -> path to the item

            Returns:
            The created item object or None if creation failed
        """

        raise NotImplementedError
