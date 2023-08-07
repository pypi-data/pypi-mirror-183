from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hcustomerscustomer_id_response_200_data_relationships_orders_data import (
        PATCHcustomerscustomerIdResponse200DataRelationshipsOrdersData,
    )
    from ..models.patc_hcustomerscustomer_id_response_200_data_relationships_orders_links import (
        PATCHcustomerscustomerIdResponse200DataRelationshipsOrdersLinks,
    )


T = TypeVar("T", bound="PATCHcustomerscustomerIdResponse200DataRelationshipsOrders")


@attr.s(auto_attribs=True)
class PATCHcustomerscustomerIdResponse200DataRelationshipsOrders:
    """
    Attributes:
        links (Union[Unset, PATCHcustomerscustomerIdResponse200DataRelationshipsOrdersLinks]):
        data (Union[Unset, PATCHcustomerscustomerIdResponse200DataRelationshipsOrdersData]):
    """

    links: Union[Unset, "PATCHcustomerscustomerIdResponse200DataRelationshipsOrdersLinks"] = UNSET
    data: Union[Unset, "PATCHcustomerscustomerIdResponse200DataRelationshipsOrdersData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hcustomerscustomer_id_response_200_data_relationships_orders_data import (
            PATCHcustomerscustomerIdResponse200DataRelationshipsOrdersData,
        )
        from ..models.patc_hcustomerscustomer_id_response_200_data_relationships_orders_links import (
            PATCHcustomerscustomerIdResponse200DataRelationshipsOrdersLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, PATCHcustomerscustomerIdResponse200DataRelationshipsOrdersLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHcustomerscustomerIdResponse200DataRelationshipsOrdersLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PATCHcustomerscustomerIdResponse200DataRelationshipsOrdersData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHcustomerscustomerIdResponse200DataRelationshipsOrdersData.from_dict(_data)

        patc_hcustomerscustomer_id_response_200_data_relationships_orders = cls(
            links=links,
            data=data,
        )

        patc_hcustomerscustomer_id_response_200_data_relationships_orders.additional_properties = d
        return patc_hcustomerscustomer_id_response_200_data_relationships_orders

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
