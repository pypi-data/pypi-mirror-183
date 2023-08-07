from enum import Enum


class GETtaxCategoriestaxCategoryIdResponse200DataType(str, Enum):
    TAX_CATEGORIES = "tax_categories"

    def __str__(self) -> str:
        return str(self.value)
