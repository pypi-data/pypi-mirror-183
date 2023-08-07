from enum import Enum


class GETtaxCalculatorstaxCalculatorIdResponse200DataType(str, Enum):
    TAX_CALCULATORS = "tax_calculators"

    def __str__(self) -> str:
        return str(self.value)
