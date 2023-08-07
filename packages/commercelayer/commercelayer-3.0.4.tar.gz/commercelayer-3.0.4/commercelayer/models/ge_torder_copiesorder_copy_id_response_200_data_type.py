from enum import Enum


class GETorderCopiesorderCopyIdResponse200DataType(str, Enum):
    ORDER_COPIES = "order_copies"

    def __str__(self) -> str:
        return str(self.value)
