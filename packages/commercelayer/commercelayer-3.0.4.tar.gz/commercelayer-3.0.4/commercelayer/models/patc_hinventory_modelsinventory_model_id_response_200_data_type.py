from enum import Enum


class PATCHinventoryModelsinventoryModelIdResponse200DataType(str, Enum):
    INVENTORY_MODELS = "inventory_models"

    def __str__(self) -> str:
        return str(self.value)
