from enum import Enum


class POSTtaxRulesResponse201DataRelationshipsManualTaxCalculatorDataType(str, Enum):
    MANUAL_TAX_CALCULATOR = "manual_tax_calculator"

    def __str__(self) -> str:
        return str(self.value)
