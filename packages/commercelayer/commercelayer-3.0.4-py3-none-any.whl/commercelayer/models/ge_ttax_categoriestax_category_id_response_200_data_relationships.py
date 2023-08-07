from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_ttax_categoriestax_category_id_response_200_data_relationships_attachments import (
        GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsAttachments,
    )
    from ..models.ge_ttax_categoriestax_category_id_response_200_data_relationships_sku import (
        GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsSku,
    )
    from ..models.ge_ttax_categoriestax_category_id_response_200_data_relationships_tax_calculator import (
        GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsTaxCalculator,
    )


T = TypeVar("T", bound="GETtaxCategoriestaxCategoryIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETtaxCategoriestaxCategoryIdResponse200DataRelationships:
    """
    Attributes:
        sku (Union[Unset, GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsSku]):
        tax_calculator (Union[Unset, GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsTaxCalculator]):
        attachments (Union[Unset, GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsAttachments]):
    """

    sku: Union[Unset, "GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsSku"] = UNSET
    tax_calculator: Union[Unset, "GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsTaxCalculator"] = UNSET
    attachments: Union[Unset, "GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsAttachments"] = UNSET
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
        from ..models.ge_ttax_categoriestax_category_id_response_200_data_relationships_attachments import (
            GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsAttachments,
        )
        from ..models.ge_ttax_categoriestax_category_id_response_200_data_relationships_sku import (
            GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsSku,
        )
        from ..models.ge_ttax_categoriestax_category_id_response_200_data_relationships_tax_calculator import (
            GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsTaxCalculator,
        )

        d = src_dict.copy()
        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsSku.from_dict(_sku)

        _tax_calculator = d.pop("tax_calculator", UNSET)
        tax_calculator: Union[Unset, GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsTaxCalculator]
        if isinstance(_tax_calculator, Unset):
            tax_calculator = UNSET
        else:
            tax_calculator = GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsTaxCalculator.from_dict(
                _tax_calculator
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETtaxCategoriestaxCategoryIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        ge_ttax_categoriestax_category_id_response_200_data_relationships = cls(
            sku=sku,
            tax_calculator=tax_calculator,
            attachments=attachments,
        )

        ge_ttax_categoriestax_category_id_response_200_data_relationships.additional_properties = d
        return ge_ttax_categoriestax_category_id_response_200_data_relationships

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
