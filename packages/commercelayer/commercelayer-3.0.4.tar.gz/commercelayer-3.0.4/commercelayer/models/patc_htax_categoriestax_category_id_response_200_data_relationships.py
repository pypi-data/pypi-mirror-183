from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_htax_categoriestax_category_id_response_200_data_relationships_attachments import (
        PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsAttachments,
    )
    from ..models.patc_htax_categoriestax_category_id_response_200_data_relationships_sku import (
        PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsSku,
    )
    from ..models.patc_htax_categoriestax_category_id_response_200_data_relationships_tax_calculator import (
        PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsTaxCalculator,
    )


T = TypeVar("T", bound="PATCHtaxCategoriestaxCategoryIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHtaxCategoriestaxCategoryIdResponse200DataRelationships:
    """
    Attributes:
        sku (Union[Unset, PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsSku]):
        tax_calculator (Union[Unset, PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsTaxCalculator]):
        attachments (Union[Unset, PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsAttachments]):
    """

    sku: Union[Unset, "PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsSku"] = UNSET
    tax_calculator: Union[Unset, "PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsTaxCalculator"] = UNSET
    attachments: Union[Unset, "PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsAttachments"] = UNSET
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
        from ..models.patc_htax_categoriestax_category_id_response_200_data_relationships_attachments import (
            PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsAttachments,
        )
        from ..models.patc_htax_categoriestax_category_id_response_200_data_relationships_sku import (
            PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsSku,
        )
        from ..models.patc_htax_categoriestax_category_id_response_200_data_relationships_tax_calculator import (
            PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsTaxCalculator,
        )

        d = src_dict.copy()
        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsSku.from_dict(_sku)

        _tax_calculator = d.pop("tax_calculator", UNSET)
        tax_calculator: Union[Unset, PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsTaxCalculator]
        if isinstance(_tax_calculator, Unset):
            tax_calculator = UNSET
        else:
            tax_calculator = PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsTaxCalculator.from_dict(
                _tax_calculator
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PATCHtaxCategoriestaxCategoryIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        patc_htax_categoriestax_category_id_response_200_data_relationships = cls(
            sku=sku,
            tax_calculator=tax_calculator,
            attachments=attachments,
        )

        patc_htax_categoriestax_category_id_response_200_data_relationships.additional_properties = d
        return patc_htax_categoriestax_category_id_response_200_data_relationships

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
