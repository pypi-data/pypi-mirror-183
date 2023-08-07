from enum import Enum


class POSTshippingMethodsResponse201DataRelationshipsDeliveryLeadTimeForShipmentDataType(str, Enum):
    DELIVERY_LEAD_TIME_FOR_SHIPMENT = "delivery_lead_time_for_shipment"

    def __str__(self) -> str:
        return str(self.value)
