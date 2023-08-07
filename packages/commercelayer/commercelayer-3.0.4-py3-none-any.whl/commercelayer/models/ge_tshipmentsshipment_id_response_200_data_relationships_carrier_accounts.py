from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tshipmentsshipment_id_response_200_data_relationships_carrier_accounts_data import (
        GETshipmentsshipmentIdResponse200DataRelationshipsCarrierAccountsData,
    )
    from ..models.ge_tshipmentsshipment_id_response_200_data_relationships_carrier_accounts_links import (
        GETshipmentsshipmentIdResponse200DataRelationshipsCarrierAccountsLinks,
    )


T = TypeVar("T", bound="GETshipmentsshipmentIdResponse200DataRelationshipsCarrierAccounts")


@attr.s(auto_attribs=True)
class GETshipmentsshipmentIdResponse200DataRelationshipsCarrierAccounts:
    """
    Attributes:
        links (Union[Unset, GETshipmentsshipmentIdResponse200DataRelationshipsCarrierAccountsLinks]):
        data (Union[Unset, GETshipmentsshipmentIdResponse200DataRelationshipsCarrierAccountsData]):
    """

    links: Union[Unset, "GETshipmentsshipmentIdResponse200DataRelationshipsCarrierAccountsLinks"] = UNSET
    data: Union[Unset, "GETshipmentsshipmentIdResponse200DataRelationshipsCarrierAccountsData"] = UNSET
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
        from ..models.ge_tshipmentsshipment_id_response_200_data_relationships_carrier_accounts_data import (
            GETshipmentsshipmentIdResponse200DataRelationshipsCarrierAccountsData,
        )
        from ..models.ge_tshipmentsshipment_id_response_200_data_relationships_carrier_accounts_links import (
            GETshipmentsshipmentIdResponse200DataRelationshipsCarrierAccountsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETshipmentsshipmentIdResponse200DataRelationshipsCarrierAccountsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETshipmentsshipmentIdResponse200DataRelationshipsCarrierAccountsLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETshipmentsshipmentIdResponse200DataRelationshipsCarrierAccountsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETshipmentsshipmentIdResponse200DataRelationshipsCarrierAccountsData.from_dict(_data)

        ge_tshipmentsshipment_id_response_200_data_relationships_carrier_accounts = cls(
            links=links,
            data=data,
        )

        ge_tshipmentsshipment_id_response_200_data_relationships_carrier_accounts.additional_properties = d
        return ge_tshipmentsshipment_id_response_200_data_relationships_carrier_accounts

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
