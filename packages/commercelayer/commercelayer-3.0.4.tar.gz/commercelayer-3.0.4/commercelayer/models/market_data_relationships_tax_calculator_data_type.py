from enum import Enum


class MarketDataRelationshipsTaxCalculatorDataType(str, Enum):
    TAX_CALCULATORS = "tax_calculators"

    def __str__(self) -> str:
        return str(self.value)
