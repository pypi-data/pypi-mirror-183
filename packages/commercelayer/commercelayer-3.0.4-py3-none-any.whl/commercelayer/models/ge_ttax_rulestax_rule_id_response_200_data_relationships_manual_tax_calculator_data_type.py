from enum import Enum


class GETtaxRulestaxRuleIdResponse200DataRelationshipsManualTaxCalculatorDataType(str, Enum):
    MANUAL_TAX_CALCULATOR = "manual_tax_calculator"

    def __str__(self) -> str:
        return str(self.value)
