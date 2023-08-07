from enum import Enum


class GETtaxCategoriesResponse200DataItemType(str, Enum):
    TAX_CATEGORIES = "tax_categories"

    def __str__(self) -> str:
        return str(self.value)
