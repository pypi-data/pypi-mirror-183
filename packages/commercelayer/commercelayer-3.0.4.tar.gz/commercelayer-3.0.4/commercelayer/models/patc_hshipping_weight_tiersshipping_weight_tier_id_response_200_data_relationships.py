from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hshipping_weight_tiersshipping_weight_tier_id_response_200_data_relationships_attachments import (
        PATCHshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsAttachments,
    )
    from ..models.patc_hshipping_weight_tiersshipping_weight_tier_id_response_200_data_relationships_shipping_method import (
        PATCHshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethod,
    )


T = TypeVar("T", bound="PATCHshippingWeightTiersshippingWeightTierIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHshippingWeightTiersshippingWeightTierIdResponse200DataRelationships:
    """
    Attributes:
        shipping_method (Union[Unset,
            PATCHshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethod]):
        attachments (Union[Unset, PATCHshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsAttachments]):
    """

    shipping_method: Union[
        Unset, "PATCHshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethod"
    ] = UNSET
    attachments: Union[
        Unset, "PATCHshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsAttachments"
    ] = UNSET
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
        from ..models.patc_hshipping_weight_tiersshipping_weight_tier_id_response_200_data_relationships_attachments import (
            PATCHshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsAttachments,
        )
        from ..models.patc_hshipping_weight_tiersshipping_weight_tier_id_response_200_data_relationships_shipping_method import (
            PATCHshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethod,
        )

        d = src_dict.copy()
        _shipping_method = d.pop("shipping_method", UNSET)
        shipping_method: Union[
            Unset, PATCHshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethod
        ]
        if isinstance(_shipping_method, Unset):
            shipping_method = UNSET
        else:
            shipping_method = (
                PATCHshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethod.from_dict(
                    _shipping_method
                )
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PATCHshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsAttachments.from_dict(
                _attachments
            )

        patc_hshipping_weight_tiersshipping_weight_tier_id_response_200_data_relationships = cls(
            shipping_method=shipping_method,
            attachments=attachments,
        )

        patc_hshipping_weight_tiersshipping_weight_tier_id_response_200_data_relationships.additional_properties = d
        return patc_hshipping_weight_tiersshipping_weight_tier_id_response_200_data_relationships

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
