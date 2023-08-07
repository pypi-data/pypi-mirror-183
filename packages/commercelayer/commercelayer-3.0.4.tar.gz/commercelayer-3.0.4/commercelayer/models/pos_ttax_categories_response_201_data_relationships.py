from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_ttax_categories_response_201_data_relationships_attachments import (
        POSTtaxCategoriesResponse201DataRelationshipsAttachments,
    )
    from ..models.pos_ttax_categories_response_201_data_relationships_sku import (
        POSTtaxCategoriesResponse201DataRelationshipsSku,
    )
    from ..models.pos_ttax_categories_response_201_data_relationships_tax_calculator import (
        POSTtaxCategoriesResponse201DataRelationshipsTaxCalculator,
    )


T = TypeVar("T", bound="POSTtaxCategoriesResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTtaxCategoriesResponse201DataRelationships:
    """
    Attributes:
        sku (Union[Unset, POSTtaxCategoriesResponse201DataRelationshipsSku]):
        tax_calculator (Union[Unset, POSTtaxCategoriesResponse201DataRelationshipsTaxCalculator]):
        attachments (Union[Unset, POSTtaxCategoriesResponse201DataRelationshipsAttachments]):
    """

    sku: Union[Unset, "POSTtaxCategoriesResponse201DataRelationshipsSku"] = UNSET
    tax_calculator: Union[Unset, "POSTtaxCategoriesResponse201DataRelationshipsTaxCalculator"] = UNSET
    attachments: Union[Unset, "POSTtaxCategoriesResponse201DataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku, Unset):
            sku = self.sku.to_dict()

        tax_calculator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_calculator, Unset):
            tax_calculator = self.tax_calculator.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku is not UNSET:
            field_dict["sku"] = sku
        if tax_calculator is not UNSET:
            field_dict["tax_calculator"] = tax_calculator
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_ttax_categories_response_201_data_relationships_attachments import (
            POSTtaxCategoriesResponse201DataRelationshipsAttachments,
        )
        from ..models.pos_ttax_categories_response_201_data_relationships_sku import (
            POSTtaxCategoriesResponse201DataRelationshipsSku,
        )
        from ..models.pos_ttax_categories_response_201_data_relationships_tax_calculator import (
            POSTtaxCategoriesResponse201DataRelationshipsTaxCalculator,
        )

        d = src_dict.copy()
        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, POSTtaxCategoriesResponse201DataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = POSTtaxCategoriesResponse201DataRelationshipsSku.from_dict(_sku)

        _tax_calculator = d.pop("tax_calculator", UNSET)
        tax_calculator: Union[Unset, POSTtaxCategoriesResponse201DataRelationshipsTaxCalculator]
        if isinstance(_tax_calculator, Unset):
            tax_calculator = UNSET
        else:
            tax_calculator = POSTtaxCategoriesResponse201DataRelationshipsTaxCalculator.from_dict(_tax_calculator)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, POSTtaxCategoriesResponse201DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = POSTtaxCategoriesResponse201DataRelationshipsAttachments.from_dict(_attachments)

        pos_ttax_categories_response_201_data_relationships = cls(
            sku=sku,
            tax_calculator=tax_calculator,
            attachments=attachments,
        )

        pos_ttax_categories_response_201_data_relationships.additional_properties = d
        return pos_ttax_categories_response_201_data_relationships

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
