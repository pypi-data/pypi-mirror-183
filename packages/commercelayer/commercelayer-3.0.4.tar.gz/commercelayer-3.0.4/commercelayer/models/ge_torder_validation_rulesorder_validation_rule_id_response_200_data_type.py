from enum import Enum


class GETorderValidationRulesorderValidationRuleIdResponse200DataType(str, Enum):
    ORDER_VALIDATION_RULES = "order_validation_rules"

    def __str__(self) -> str:
        return str(self.value)
