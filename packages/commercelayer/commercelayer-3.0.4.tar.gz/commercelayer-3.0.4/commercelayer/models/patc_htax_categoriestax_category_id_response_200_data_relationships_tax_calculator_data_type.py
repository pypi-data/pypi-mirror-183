from enum import Enum


class PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsTaxCalculatorDataType(str, Enum):
    TAX_CALCULATOR = "tax_calculator"

    def __str__(self) -> str:
        return str(self.value)
