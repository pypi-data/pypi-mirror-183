from enum import Enum


class MarketCreateDataRelationshipsTaxCalculatorDataType(str, Enum):
    TAX_CALCULATORS = "tax_calculators"

    def __str__(self) -> str:
        return str(self.value)
