from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.taxjar_account_data_relationships_attachments import TaxjarAccountDataRelationshipsAttachments
    from ..models.taxjar_account_data_relationships_markets import TaxjarAccountDataRelationshipsMarkets
    from ..models.taxjar_account_data_relationships_tax_categories import TaxjarAccountDataRelationshipsTaxCategories


T = TypeVar("T", bound="TaxjarAccountDataRelationships")


@attr.s(auto_attribs=True)
class TaxjarAccountDataRelationships:
    """
    Attributes:
        markets (Union[Unset, TaxjarAccountDataRelationshipsMarkets]):
        attachments (Union[Unset, TaxjarAccountDataRelationshipsAttachments]):
        tax_categories (Union[Unset, TaxjarAccountDataRelationshipsTaxCategories]):
    """

    markets: Union[Unset, "TaxjarAccountDataRelationshipsMarkets"] = UNSET
    attachments: Union[Unset, "TaxjarAccountDataRelationshipsAttachments"] = UNSET
    tax_categories: Union[Unset, "TaxjarAccountDataRelationshipsTaxCategories"] = UNSET
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
        from ..models.taxjar_account_data_relationships_attachments import TaxjarAccountDataRelationshipsAttachments
        from ..models.taxjar_account_data_relationships_markets import TaxjarAccountDataRelationshipsMarkets
        from ..models.taxjar_account_data_relationships_tax_categories import (
            TaxjarAccountDataRelationshipsTaxCategories,
        )

        d = src_dict.copy()
        _markets = d.pop("markets", UNSET)
        markets: Union[Unset, TaxjarAccountDataRelationshipsMarkets]
        if isinstance(_markets, Unset):
            markets = UNSET
        else:
            markets = TaxjarAccountDataRelationshipsMarkets.from_dict(_markets)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, TaxjarAccountDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = TaxjarAccountDataRelationshipsAttachments.from_dict(_attachments)

        _tax_categories = d.pop("tax_categories", UNSET)
        tax_categories: Union[Unset, TaxjarAccountDataRelationshipsTaxCategories]
        if isinstance(_tax_categories, Unset):
            tax_categories = UNSET
        else:
            tax_categories = TaxjarAccountDataRelationshipsTaxCategories.from_dict(_tax_categories)

        taxjar_account_data_relationships = cls(
            markets=markets,
            attachments=attachments,
            tax_categories=tax_categories,
        )

        taxjar_account_data_relationships.additional_properties = d
        return taxjar_account_data_relationships

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
