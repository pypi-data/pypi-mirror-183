from enum import Enum


class GETtaxRulesResponse200DataItemType(str, Enum):
    TAX_RULES = "tax_rules"

    def __str__(self) -> str:
        return str(self.value)
