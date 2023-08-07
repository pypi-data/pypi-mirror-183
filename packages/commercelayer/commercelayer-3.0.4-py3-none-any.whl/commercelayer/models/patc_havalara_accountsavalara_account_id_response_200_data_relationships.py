from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_havalara_accountsavalara_account_id_response_200_data_relationships_attachments import (
        PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsAttachments,
    )
    from ..models.patc_havalara_accountsavalara_account_id_response_200_data_relationships_markets import (
        PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsMarkets,
    )
    from ..models.patc_havalara_accountsavalara_account_id_response_200_data_relationships_tax_categories import (
        PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsTaxCategories,
    )


T = TypeVar("T", bound="PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationships:
    """
    Attributes:
        markets (Union[Unset, PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsMarkets]):
        attachments (Union[Unset, PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsAttachments]):
        tax_categories (Union[Unset, PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsTaxCategories]):
    """

    markets: Union[Unset, "PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsMarkets"] = UNSET
    attachments: Union[Unset, "PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsAttachments"] = UNSET
    tax_categories: Union[
        Unset, "PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsTaxCategories"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        markets: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.markets, Unset):
            markets = self.markets.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        tax_categories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_categories, Unset):
            tax_categories = self.tax_categories.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if markets is not UNSET:
            field_dict["markets"] = markets
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if tax_categories is not UNSET:
            field_dict["tax_categories"] = tax_categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_havalara_accountsavalara_account_id_response_200_data_relationships_attachments import (
            PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsAttachments,
        )
        from ..models.patc_havalara_accountsavalara_account_id_response_200_data_relationships_markets import (
            PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsMarkets,
        )
        from ..models.patc_havalara_accountsavalara_account_id_response_200_data_relationships_tax_categories import (
            PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsTaxCategories,
        )

        d = src_dict.copy()
        _markets = d.pop("markets", UNSET)
        markets: Union[Unset, PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsMarkets]
        if isinstance(_markets, Unset):
            markets = UNSET
        else:
            markets = PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsMarkets.from_dict(_markets)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsAttachments.from_dict(
                _attachments
            )

        _tax_categories = d.pop("tax_categories", UNSET)
        tax_categories: Union[Unset, PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsTaxCategories]
        if isinstance(_tax_categories, Unset):
            tax_categories = UNSET
        else:
            tax_categories = PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsTaxCategories.from_dict(
                _tax_categories
            )

        patc_havalara_accountsavalara_account_id_response_200_data_relationships = cls(
            markets=markets,
            attachments=attachments,
            tax_categories=tax_categories,
        )

        patc_havalara_accountsavalara_account_id_response_200_data_relationships.additional_properties = d
        return patc_havalara_accountsavalara_account_id_response_200_data_relationships

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
