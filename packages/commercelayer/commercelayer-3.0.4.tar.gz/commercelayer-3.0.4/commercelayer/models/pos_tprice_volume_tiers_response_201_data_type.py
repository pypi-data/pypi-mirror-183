from enum import Enum


class POSTpriceVolumeTiersResponse201DataType(str, Enum):
    PRICE_VOLUME_TIERS = "price_volume_tiers"

    def __str__(self) -> str:
        return str(self.value)
