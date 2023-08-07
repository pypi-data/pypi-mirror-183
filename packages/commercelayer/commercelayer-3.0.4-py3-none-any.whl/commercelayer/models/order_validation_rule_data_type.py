from enum import Enum


class OrderValidationRuleDataType(str, Enum):
    ORDER_VALIDATION_RULES = "order_validation_rules"

    def __str__(self) -> str:
        return str(self.value)
