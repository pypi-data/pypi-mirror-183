from enum import Enum


class POSTmarketsResponse201DataRelationshipsTaxCalculatorDataType(str, Enum):
    TAX_CALCULATOR = "tax_calculator"

    def __str__(self) -> str:
        return str(self.value)
