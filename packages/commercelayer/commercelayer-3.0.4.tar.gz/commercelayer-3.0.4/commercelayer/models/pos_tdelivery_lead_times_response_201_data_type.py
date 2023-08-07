from enum import Enum


class POSTdeliveryLeadTimesResponse201DataType(str, Enum):
    DELIVERY_LEAD_TIMES = "delivery_lead_times"

    def __str__(self) -> str:
        return str(self.value)
