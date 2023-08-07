from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tavalara_accounts_response_200_data_item_relationships_attachments import (
        GETavalaraAccountsResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tavalara_accounts_response_200_data_item_relationships_markets import (
        GETavalaraAccountsResponse200DataItemRelationshipsMarkets,
    )
    from ..models.ge_tavalara_accounts_response_200_data_item_relationships_tax_categories import (
        GETavalaraAccountsResponse200DataItemRelationshipsTaxCategories,
    )


T = TypeVar("T", bound="GETavalaraAccountsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETavalaraAccountsResponse200DataItemRelationships:
    """
    Attributes:
        markets (Union[Unset, GETavalaraAccountsResponse200DataItemRelationshipsMarkets]):
        attachments (Union[Unset, GETavalaraAccountsResponse200DataItemRelationshipsAttachments]):
        tax_categories (Union[Unset, GETavalaraAccountsResponse200DataItemRelationshipsTaxCategories]):
    """

    markets: Union[Unset, "GETavalaraAccountsResponse200DataItemRelationshipsMarkets"] = UNSET
    attachments: Union[Unset, "GETavalaraAccountsResponse200DataItemRelationshipsAttachments"] = UNSET
    tax_categories: Union[Unset, "GETavalaraAccountsResponse200DataItemRelationshipsTaxCategories"] = UNSET
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
        from ..models.ge_tavalara_accounts_response_200_data_item_relationships_attachments import (
            GETavalaraAccountsResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tavalara_accounts_response_200_data_item_relationships_markets import (
            GETavalaraAccountsResponse200DataItemRelationshipsMarkets,
        )
        from ..models.ge_tavalara_accounts_response_200_data_item_relationships_tax_categories import (
            GETavalaraAccountsResponse200DataItemRelationshipsTaxCategories,
        )

        d = src_dict.copy()
        _markets = d.pop("markets", UNSET)
        markets: Union[Unset, GETavalaraAccountsResponse200DataItemRelationshipsMarkets]
        if isinstance(_markets, Unset):
            markets = UNSET
        else:
            markets = GETavalaraAccountsResponse200DataItemRelationshipsMarkets.from_dict(_markets)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETavalaraAccountsResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETavalaraAccountsResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        _tax_categories = d.pop("tax_categories", UNSET)
        tax_categories: Union[Unset, GETavalaraAccountsResponse200DataItemRelationshipsTaxCategories]
        if isinstance(_tax_categories, Unset):
            tax_categories = UNSET
        else:
            tax_categories = GETavalaraAccountsResponse200DataItemRelationshipsTaxCategories.from_dict(_tax_categories)

        ge_tavalara_accounts_response_200_data_item_relationships = cls(
            markets=markets,
            attachments=attachments,
            tax_categories=tax_categories,
        )

        ge_tavalara_accounts_response_200_data_item_relationships.additional_properties = d
        return ge_tavalara_accounts_response_200_data_item_relationships

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
