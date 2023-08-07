from enum import Enum


class GETorderCopiesResponse200DataItemType(str, Enum):
    ORDER_COPIES = "order_copies"

    def __str__(self) -> str:
        return str(self.value)
