from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipping_weight_tier_data_relationships_attachments import (
        ShippingWeightTierDataRelationshipsAttachments,
    )
    from ..models.shipping_weight_tier_data_relationships_shipping_method import (
        ShippingWeightTierDataRelationshipsShippingMethod,
    )


T = TypeVar("T", bound="ShippingWeightTierDataRelationships")


@attr.s(auto_attribs=True)
class ShippingWeightTierDataRelationships:
    """
    Attributes:
        shipping_method (Union[Unset, ShippingWeightTierDataRelationshipsShippingMethod]):
        attachments (Union[Unset, ShippingWeightTierDataRelationshipsAttachments]):
    """

    shipping_method: Union[Unset, "ShippingWeightTierDataRelationshipsShippingMethod"] = UNSET
    attachments: Union[Unset, "ShippingWeightTierDataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipping_method: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_method, Unset):
            shipping_method = self.shipping_method.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipping_method is not UNSET:
            field_dict["shipping_method"] = shipping_method
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shipping_weight_tier_data_relationships_attachments import (
            ShippingWeightTierDataRelationshipsAttachments,
        )
        from ..models.shipping_weight_tier_data_relationships_shipping_method import (
            ShippingWeightTierDataRelationshipsShippingMethod,
        )

        d = src_dict.copy()
        _shipping_method = d.pop("shipping_method", UNSET)
        shipping_method: Union[Unset, ShippingWeightTierDataRelationshipsShippingMethod]
        if isinstance(_shipping_method, Unset):
            shipping_method = UNSET
        else:
            shipping_method = ShippingWeightTierDataRelationshipsShippingMethod.from_dict(_shipping_method)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, ShippingWeightTierDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = ShippingWeightTierDataRelationshipsAttachments.from_dict(_attachments)

        shipping_weight_tier_data_relationships = cls(
            shipping_method=shipping_method,
            attachments=attachments,
        )

        shipping_weight_tier_data_relationships.additional_properties = d
        return shipping_weight_tier_data_relationships

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
