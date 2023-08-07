from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hshipping_weight_tiersshipping_weight_tier_id_response_200_data_attributes_metadata import (
        PATCHshippingWeightTiersshippingWeightTierIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="PATCHshippingWeightTiersshippingWeightTierIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHshippingWeightTiersshippingWeightTierIdResponse200DataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The shipping method tier's name Example: Light shipping under 3kg.
        up_to (Union[Unset, float]): The tier upper limit. When 'null' it means infinity (useful to have an always
            matching tier). Example: 20.5.
        price_amount_cents (Union[Unset, int]): The price of this shipping method tier, in cents. Example: 1000.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHshippingWeightTiersshippingWeightTierIdResponse200DataAttributesMetadata]): Set of
            key-value pairs that you can attach to the resource. This can be useful for storing additional information about
            the resource in a structured format. Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    up_to: Union[Unset, float] = UNSET
    price_amount_cents: Union[Unset, int] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHshippingWeightTiersshippingWeightTierIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        up_to = self.up_to
        price_amount_cents = self.price_amount_cents
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if up_to is not UNSET:
            field_dict["up_to"] = up_to
        if price_amount_cents is not UNSET:
            field_dict["price_amount_cents"] = price_amount_cents
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hshipping_weight_tiersshipping_weight_tier_id_response_200_data_attributes_metadata import (
            PATCHshippingWeightTiersshippingWeightTierIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        up_to = d.pop("up_to", UNSET)

        price_amount_cents = d.pop("price_amount_cents", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHshippingWeightTiersshippingWeightTierIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHshippingWeightTiersshippingWeightTierIdResponse200DataAttributesMetadata.from_dict(
                _metadata
            )

        patc_hshipping_weight_tiersshipping_weight_tier_id_response_200_data_attributes = cls(
            name=name,
            up_to=up_to,
            price_amount_cents=price_amount_cents,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        patc_hshipping_weight_tiersshipping_weight_tier_id_response_200_data_attributes.additional_properties = d
        return patc_hshipping_weight_tiersshipping_weight_tier_id_response_200_data_attributes

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
