from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_texternal_payments_response_200_data_item_relationships_wallet_data import (
        GETexternalPaymentsResponse200DataItemRelationshipsWalletData,
    )
    from ..models.ge_texternal_payments_response_200_data_item_relationships_wallet_links import (
        GETexternalPaymentsResponse200DataItemRelationshipsWalletLinks,
    )


T = TypeVar("T", bound="GETexternalPaymentsResponse200DataItemRelationshipsWallet")


@attr.s(auto_attribs=True)
class GETexternalPaymentsResponse200DataItemRelationshipsWallet:
    """
    Attributes:
        links (Union[Unset, GETexternalPaymentsResponse200DataItemRelationshipsWalletLinks]):
        data (Union[Unset, GETexternalPaymentsResponse200DataItemRelationshipsWalletData]):
    """

    links: Union[Unset, "GETexternalPaymentsResponse200DataItemRelationshipsWalletLinks"] = UNSET
    data: Union[Unset, "GETexternalPaymentsResponse200DataItemRelationshipsWalletData"] = UNSET
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
        from ..models.ge_texternal_payments_response_200_data_item_relationships_wallet_data import (
            GETexternalPaymentsResponse200DataItemRelationshipsWalletData,
        )
        from ..models.ge_texternal_payments_response_200_data_item_relationships_wallet_links import (
            GETexternalPaymentsResponse200DataItemRelationshipsWalletLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETexternalPaymentsResponse200DataItemRelationshipsWalletLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETexternalPaymentsResponse200DataItemRelationshipsWalletLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETexternalPaymentsResponse200DataItemRelationshipsWalletData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETexternalPaymentsResponse200DataItemRelationshipsWalletData.from_dict(_data)

        ge_texternal_payments_response_200_data_item_relationships_wallet = cls(
            links=links,
            data=data,
        )

        ge_texternal_payments_response_200_data_item_relationships_wallet.additional_properties = d
        return ge_texternal_payments_response_200_data_item_relationships_wallet

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
