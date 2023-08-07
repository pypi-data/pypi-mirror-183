from enum import Enum


class POSTorderCopiesResponse201DataType(str, Enum):
    ORDER_COPIES = "order_copies"

    def __str__(self) -> str:
        return str(self.value)
