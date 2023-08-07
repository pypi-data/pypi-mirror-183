from enum import Enum


class GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsTaxCategoriesDataType(str, Enum):
    TAX_CATEGORIES = "tax_categories"

    def __str__(self) -> str:
        return str(self.value)
