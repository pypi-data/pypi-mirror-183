from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_ttaxjar_accountstaxjar_account_id_response_200_data_relationships_attachments import (
        GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsAttachments,
    )
    from ..models.ge_ttaxjar_accountstaxjar_account_id_response_200_data_relationships_markets import (
        GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsMarkets,
    )
    from ..models.ge_ttaxjar_accountstaxjar_account_id_response_200_data_relationships_tax_categories import (
        GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsTaxCategories,
    )


T = TypeVar("T", bound="GETtaxjarAccountstaxjarAccountIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETtaxjarAccountstaxjarAccountIdResponse200DataRelationships:
    """
    Attributes:
        markets (Union[Unset, GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsMarkets]):
        attachments (Union[Unset, GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsAttachments]):
        tax_categories (Union[Unset, GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsTaxCategories]):
    """

    markets: Union[Unset, "GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsMarkets"] = UNSET
    attachments: Union[Unset, "GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsAttachments"] = UNSET
    tax_categories: Union[Unset, "GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsTaxCategories"] = UNSET
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
        from ..models.ge_ttaxjar_accountstaxjar_account_id_response_200_data_relationships_attachments import (
            GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsAttachments,
        )
        from ..models.ge_ttaxjar_accountstaxjar_account_id_response_200_data_relationships_markets import (
            GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsMarkets,
        )
        from ..models.ge_ttaxjar_accountstaxjar_account_id_response_200_data_relationships_tax_categories import (
            GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsTaxCategories,
        )

        d = src_dict.copy()
        _markets = d.pop("markets", UNSET)
        markets: Union[Unset, GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsMarkets]
        if isinstance(_markets, Unset):
            markets = UNSET
        else:
            markets = GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsMarkets.from_dict(_markets)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsAttachments.from_dict(
                _attachments
            )

        _tax_categories = d.pop("tax_categories", UNSET)
        tax_categories: Union[Unset, GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsTaxCategories]
        if isinstance(_tax_categories, Unset):
            tax_categories = UNSET
        else:
            tax_categories = GETtaxjarAccountstaxjarAccountIdResponse200DataRelationshipsTaxCategories.from_dict(
                _tax_categories
            )

        ge_ttaxjar_accountstaxjar_account_id_response_200_data_relationships = cls(
            markets=markets,
            attachments=attachments,
            tax_categories=tax_categories,
        )

        ge_ttaxjar_accountstaxjar_account_id_response_200_data_relationships.additional_properties = d
        return ge_ttaxjar_accountstaxjar_account_id_response_200_data_relationships

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
