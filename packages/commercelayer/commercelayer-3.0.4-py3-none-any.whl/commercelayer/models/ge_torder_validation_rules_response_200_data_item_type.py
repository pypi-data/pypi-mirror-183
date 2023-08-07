from enum import Enum


class GETorderValidationRulesResponse200DataItemType(str, Enum):
    ORDER_VALIDATION_RULES = "order_validation_rules"

    def __str__(self) -> str:
        return str(self.value)
