from enum import Enum


class GETpriceVolumeTierspriceVolumeTierIdResponse200DataType(str, Enum):
    PRICE_VOLUME_TIERS = "price_volume_tiers"

    def __str__(self) -> str:
        return str(self.value)
