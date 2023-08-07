from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.avalara_account_data_relationships_tax_categories_data import (
        AvalaraAccountDataRelationshipsTaxCategoriesData,
    )


T = TypeVar("T", bound="AvalaraAccountDataRelationshipsTaxCategories")


@attr.s(auto_attribs=True)
class AvalaraAccountDataRelationshipsTaxCategories:
    """
    Attributes:
        data (Union[Unset, AvalaraAccountDataRelationshipsTaxCategoriesData]):
    """

    data: Union[Unset, "AvalaraAccountDataRelationshipsTaxCategoriesData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.avalara_account_data_relationships_tax_categories_data import (
            AvalaraAccountDataRelationshipsTaxCategoriesData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, AvalaraAccountDataRelationshipsTaxCategoriesData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = AvalaraAccountDataRelationshipsTaxCategoriesData.from_dict(_data)

        avalara_account_data_relationships_tax_categories = cls(
            data=data,
        )

        avalara_account_data_relationships_tax_categories.additional_properties = d
        return avalara_account_data_relationships_tax_categories

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
