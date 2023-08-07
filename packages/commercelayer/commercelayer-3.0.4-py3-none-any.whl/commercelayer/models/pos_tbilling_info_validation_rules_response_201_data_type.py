from enum import Enum


class POSTbillingInfoValidationRulesResponse201DataType(str, Enum):
    BILLING_INFO_VALIDATION_RULES = "billing_info_validation_rules"

    def __str__(self) -> str:
        return str(self.value)
