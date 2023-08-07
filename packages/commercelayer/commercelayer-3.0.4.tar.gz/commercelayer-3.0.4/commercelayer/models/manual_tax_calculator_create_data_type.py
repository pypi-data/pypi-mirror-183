from enum import Enum


class ManualTaxCalculatorCreateDataType(str, Enum):
    MANUAL_TAX_CALCULATORS = "manual_tax_calculators"

    def __str__(self) -> str:
        return str(self.value)
