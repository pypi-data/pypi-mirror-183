from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hexternal_paymentsexternal_payment_id_response_200_data_relationships_wallet_data import (
        PATCHexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWalletData,
    )
    from ..models.patc_hexternal_paymentsexternal_payment_id_response_200_data_relationships_wallet_links import (
        PATCHexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWalletLinks,
    )


T = TypeVar("T", bound="PATCHexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWallet")


@attr.s(auto_attribs=True)
class PATCHexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWallet:
    """
    Attributes:
        links (Union[Unset, PATCHexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWalletLinks]):
        data (Union[Unset, PATCHexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWalletData]):
    """

    links: Union[Unset, "PATCHexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWalletLinks"] = UNSET
    data: Union[Unset, "PATCHexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWalletData"] = UNSET
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
        from ..models.patc_hexternal_paymentsexternal_payment_id_response_200_data_relationships_wallet_data import (
            PATCHexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWalletData,
        )
        from ..models.patc_hexternal_paymentsexternal_payment_id_response_200_data_relationships_wallet_links import (
            PATCHexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWalletLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, PATCHexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWalletLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWalletLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PATCHexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWalletData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWalletData.from_dict(_data)

        patc_hexternal_paymentsexternal_payment_id_response_200_data_relationships_wallet = cls(
            links=links,
            data=data,
        )

        patc_hexternal_paymentsexternal_payment_id_response_200_data_relationships_wallet.additional_properties = d
        return patc_hexternal_paymentsexternal_payment_id_response_200_data_relationships_wallet

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
