from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tshipping_categories_response_200_data_item_relationships_attachments import (
        GETshippingCategoriesResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tshipping_categories_response_200_data_item_relationships_skus import (
        GETshippingCategoriesResponse200DataItemRelationshipsSkus,
    )


T = TypeVar("T", bound="GETshippingCategoriesResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETshippingCategoriesResponse200DataItemRelationships:
    """
    Attributes:
        skus (Union[Unset, GETshippingCategoriesResponse200DataItemRelationshipsSkus]):
        attachments (Union[Unset, GETshippingCategoriesResponse200DataItemRelationshipsAttachments]):
    """

    skus: Union[Unset, "GETshippingCategoriesResponse200DataItemRelationshipsSkus"] = UNSET
    attachments: Union[Unset, "GETshippingCategoriesResponse200DataItemRelationshipsAttachments"] = UNSET
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
        from ..models.ge_tshipping_categories_response_200_data_item_relationships_attachments import (
            GETshippingCategoriesResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tshipping_categories_response_200_data_item_relationships_skus import (
            GETshippingCategoriesResponse200DataItemRelationshipsSkus,
        )

        d = src_dict.copy()
        _skus = d.pop("skus", UNSET)
        skus: Union[Unset, GETshippingCategoriesResponse200DataItemRelationshipsSkus]
        if isinstance(_skus, Unset):
            skus = UNSET
        else:
            skus = GETshippingCategoriesResponse200DataItemRelationshipsSkus.from_dict(_skus)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETshippingCategoriesResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETshippingCategoriesResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        ge_tshipping_categories_response_200_data_item_relationships = cls(
            skus=skus,
            attachments=attachments,
        )

        ge_tshipping_categories_response_200_data_item_relationships.additional_properties = d
        return ge_tshipping_categories_response_200_data_item_relationships

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
