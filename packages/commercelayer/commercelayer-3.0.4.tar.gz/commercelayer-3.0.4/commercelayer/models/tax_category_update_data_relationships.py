from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tax_category_update_data_relationships_sku import TaxCategoryUpdateDataRelationshipsSku


T = TypeVar("T", bound="TaxCategoryUpdateDataRelationships")


@attr.s(auto_attribs=True)
class TaxCategoryUpdateDataRelationships:
    """
    Attributes:
        sku (Union[Unset, TaxCategoryUpdateDataRelationshipsSku]):
    """

    sku: Union[Unset, "TaxCategoryUpdateDataRelationshipsSku"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku, Unset):
            sku = self.sku.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku is not UNSET:
            field_dict["sku"] = sku

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tax_category_update_data_relationships_sku import TaxCategoryUpdateDataRelationshipsSku

        d = src_dict.copy()
        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, TaxCategoryUpdateDataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = TaxCategoryUpdateDataRelationshipsSku.from_dict(_sku)

        tax_category_update_data_relationships = cls(
            sku=sku,
        )

        tax_category_update_data_relationships.additional_properties = d
        return tax_category_update_data_relationships

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
