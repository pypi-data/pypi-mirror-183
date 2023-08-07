from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hshipping_categoriesshipping_category_id_response_200_data_relationships_attachments import (
        PATCHshippingCategoriesshippingCategoryIdResponse200DataRelationshipsAttachments,
    )
    from ..models.patc_hshipping_categoriesshipping_category_id_response_200_data_relationships_skus import (
        PATCHshippingCategoriesshippingCategoryIdResponse200DataRelationshipsSkus,
    )


T = TypeVar("T", bound="PATCHshippingCategoriesshippingCategoryIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHshippingCategoriesshippingCategoryIdResponse200DataRelationships:
    """
    Attributes:
        skus (Union[Unset, PATCHshippingCategoriesshippingCategoryIdResponse200DataRelationshipsSkus]):
        attachments (Union[Unset, PATCHshippingCategoriesshippingCategoryIdResponse200DataRelationshipsAttachments]):
    """

    skus: Union[Unset, "PATCHshippingCategoriesshippingCategoryIdResponse200DataRelationshipsSkus"] = UNSET
    attachments: Union[
        Unset, "PATCHshippingCategoriesshippingCategoryIdResponse200DataRelationshipsAttachments"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        skus: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.skus, Unset):
            skus = self.skus.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if skus is not UNSET:
            field_dict["skus"] = skus
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hshipping_categoriesshipping_category_id_response_200_data_relationships_attachments import (
            PATCHshippingCategoriesshippingCategoryIdResponse200DataRelationshipsAttachments,
        )
        from ..models.patc_hshipping_categoriesshipping_category_id_response_200_data_relationships_skus import (
            PATCHshippingCategoriesshippingCategoryIdResponse200DataRelationshipsSkus,
        )

        d = src_dict.copy()
        _skus = d.pop("skus", UNSET)
        skus: Union[Unset, PATCHshippingCategoriesshippingCategoryIdResponse200DataRelationshipsSkus]
        if isinstance(_skus, Unset):
            skus = UNSET
        else:
            skus = PATCHshippingCategoriesshippingCategoryIdResponse200DataRelationshipsSkus.from_dict(_skus)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHshippingCategoriesshippingCategoryIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PATCHshippingCategoriesshippingCategoryIdResponse200DataRelationshipsAttachments.from_dict(
                _attachments
            )

        patc_hshipping_categoriesshipping_category_id_response_200_data_relationships = cls(
            skus=skus,
            attachments=attachments,
        )

        patc_hshipping_categoriesshipping_category_id_response_200_data_relationships.additional_properties = d
        return patc_hshipping_categoriesshipping_category_id_response_200_data_relationships

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
