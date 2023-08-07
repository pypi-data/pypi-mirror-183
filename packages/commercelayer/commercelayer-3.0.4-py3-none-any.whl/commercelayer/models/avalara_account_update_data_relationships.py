from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.avalara_account_update_data_relationships_tax_categories import (
        AvalaraAccountUpdateDataRelationshipsTaxCategories,
    )


T = TypeVar("T", bound="AvalaraAccountUpdateDataRelationships")


@attr.s(auto_attribs=True)
class AvalaraAccountUpdateDataRelationships:
    """
    Attributes:
        tax_categories (Union[Unset, AvalaraAccountUpdateDataRelationshipsTaxCategories]):
    """

    tax_categories: Union[Unset, "AvalaraAccountUpdateDataRelationshipsTaxCategories"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tax_categories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_categories, Unset):
            tax_categories = self.tax_categories.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tax_categories is not UNSET:
            field_dict["tax_categories"] = tax_categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.avalara_account_update_data_relationships_tax_categories import (
            AvalaraAccountUpdateDataRelationshipsTaxCategories,
        )

        d = src_dict.copy()
        _tax_categories = d.pop("tax_categories", UNSET)
        tax_categories: Union[Unset, AvalaraAccountUpdateDataRelationshipsTaxCategories]
        if isinstance(_tax_categories, Unset):
            tax_categories = UNSET
        else:
            tax_categories = AvalaraAccountUpdateDataRelationshipsTaxCategories.from_dict(_tax_categories)

        avalara_account_update_data_relationships = cls(
            tax_categories=tax_categories,
        )

        avalara_account_update_data_relationships.additional_properties = d
        return avalara_account_update_data_relationships

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
