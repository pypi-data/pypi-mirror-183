from enum import Enum


class GETmanualTaxCalculatorsResponse200DataItemType(str, Enum):
    MANUAL_TAX_CALCULATORS = "manual_tax_calculators"

    def __str__(self) -> str:
        return str(self.value)
