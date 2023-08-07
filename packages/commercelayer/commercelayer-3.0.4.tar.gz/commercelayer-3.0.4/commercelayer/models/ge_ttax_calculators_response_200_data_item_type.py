from enum import Enum


class GETtaxCalculatorsResponse200DataItemType(str, Enum):
    TAX_CALCULATORS = "tax_calculators"

    def __str__(self) -> str:
        return str(self.value)
