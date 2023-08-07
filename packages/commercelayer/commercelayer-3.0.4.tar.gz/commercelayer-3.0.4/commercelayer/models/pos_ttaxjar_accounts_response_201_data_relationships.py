from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_ttaxjar_accounts_response_201_data_relationships_attachments import (
        POSTtaxjarAccountsResponse201DataRelationshipsAttachments,
    )
    from ..models.pos_ttaxjar_accounts_response_201_data_relationships_markets import (
        POSTtaxjarAccountsResponse201DataRelationshipsMarkets,
    )
    from ..models.pos_ttaxjar_accounts_response_201_data_relationships_tax_categories import (
        POSTtaxjarAccountsResponse201DataRelationshipsTaxCategories,
    )


T = TypeVar("T", bound="POSTtaxjarAccountsResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTtaxjarAccountsResponse201DataRelationships:
    """
    Attributes:
        markets (Union[Unset, POSTtaxjarAccountsResponse201DataRelationshipsMarkets]):
        attachments (Union[Unset, POSTtaxjarAccountsResponse201DataRelationshipsAttachments]):
        tax_categories (Union[Unset, POSTtaxjarAccountsResponse201DataRelationshipsTaxCategories]):
    """

    markets: Union[Unset, "POSTtaxjarAccountsResponse201DataRelationshipsMarkets"] = UNSET
    attachments: Union[Unset, "POSTtaxjarAccountsResponse201DataRelationshipsAttachments"] = UNSET
    tax_categories: Union[Unset, "POSTtaxjarAccountsResponse201DataRelationshipsTaxCategories"] = UNSET
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
        from ..models.pos_ttaxjar_accounts_response_201_data_relationships_attachments import (
            POSTtaxjarAccountsResponse201DataRelationshipsAttachments,
        )
        from ..models.pos_ttaxjar_accounts_response_201_data_relationships_markets import (
            POSTtaxjarAccountsResponse201DataRelationshipsMarkets,
        )
        from ..models.pos_ttaxjar_accounts_response_201_data_relationships_tax_categories import (
            POSTtaxjarAccountsResponse201DataRelationshipsTaxCategories,
        )

        d = src_dict.copy()
        _markets = d.pop("markets", UNSET)
        markets: Union[Unset, POSTtaxjarAccountsResponse201DataRelationshipsMarkets]
        if isinstance(_markets, Unset):
            markets = UNSET
        else:
            markets = POSTtaxjarAccountsResponse201DataRelationshipsMarkets.from_dict(_markets)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, POSTtaxjarAccountsResponse201DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = POSTtaxjarAccountsResponse201DataRelationshipsAttachments.from_dict(_attachments)

        _tax_categories = d.pop("tax_categories", UNSET)
        tax_categories: Union[Unset, POSTtaxjarAccountsResponse201DataRelationshipsTaxCategories]
        if isinstance(_tax_categories, Unset):
            tax_categories = UNSET
        else:
            tax_categories = POSTtaxjarAccountsResponse201DataRelationshipsTaxCategories.from_dict(_tax_categories)

        pos_ttaxjar_accounts_response_201_data_relationships = cls(
            markets=markets,
            attachments=attachments,
            tax_categories=tax_categories,
        )

        pos_ttaxjar_accounts_response_201_data_relationships.additional_properties = d
        return pos_ttaxjar_accounts_response_201_data_relationships

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
