from enum import Enum


class GETavalaraAccountsResponse200DataItemRelationshipsTaxCategoriesDataType(str, Enum):
    TAX_CATEGORIES = "tax_categories"

    def __str__(self) -> str:
        return str(self.value)
