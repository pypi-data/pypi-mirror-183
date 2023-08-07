from enum import Enum


class ExternalTaxCalculatorCreateDataType(str, Enum):
    EXTERNAL_TAX_CALCULATORS = "external_tax_calculators"

    def __str__(self) -> str:
        return str(self.value)
