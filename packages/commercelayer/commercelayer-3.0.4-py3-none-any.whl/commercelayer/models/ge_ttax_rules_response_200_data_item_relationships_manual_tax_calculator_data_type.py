from enum import Enum


class GETtaxRulesResponse200DataItemRelationshipsManualTaxCalculatorDataType(str, Enum):
    MANUAL_TAX_CALCULATOR = "manual_tax_calculator"

    def __str__(self) -> str:
        return str(self.value)
