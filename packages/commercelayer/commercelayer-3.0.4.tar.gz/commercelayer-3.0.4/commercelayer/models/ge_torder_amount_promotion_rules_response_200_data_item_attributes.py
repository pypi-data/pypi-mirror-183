from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_torder_amount_promotion_rules_response_200_data_item_attributes_metadata import (
        GETorderAmountPromotionRulesResponse200DataItemAttributesMetadata,
    )


T = TypeVar("T", bound="GETorderAmountPromotionRulesResponse200DataItemAttributes")


@attr.s(auto_attribs=True)
class GETorderAmountPromotionRulesResponse200DataItemAttributes:
    """
    Attributes:
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETorderAmountPromotionRulesResponse200DataItemAttributesMetadata]): Set of key-value
            pairs that you can attach to the resource. This can be useful for storing additional information about the
            resource in a structured format. Example: {'foo': 'bar'}.
        order_amount_cents (Union[Unset, int]): Apply the promotion only when order is over this amount, in cents.
            Example: 1000.
        order_amount_float (Union[Unset, float]): Apply the promotion only when order is over this amount, float.
            Example: 10.0.
        formatted_order_amount (Union[Unset, str]): Apply the promotion only when order is over this amount, formatted.
            Example: €10,00.
    """

    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETorderAmountPromotionRulesResponse200DataItemAttributesMetadata"] = UNSET
    order_amount_cents: Union[Unset, int] = UNSET
    order_amount_float: Union[Unset, float] = UNSET
    formatted_order_amount: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at
        updated_at = self.updated_at
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        order_amount_cents = self.order_amount_cents
        order_amount_float = self.order_amount_float
        formatted_order_amount = self.formatted_order_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if order_amount_cents is not UNSET:
            field_dict["order_amount_cents"] = order_amount_cents
        if order_amount_float is not UNSET:
            field_dict["order_amount_float"] = order_amount_float
        if formatted_order_amount is not UNSET:
            field_dict["formatted_order_amount"] = formatted_order_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_torder_amount_promotion_rules_response_200_data_item_attributes_metadata import (
            GETorderAmountPromotionRulesResponse200DataItemAttributesMetadata,
        )

        d = src_dict.copy()
        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETorderAmountPromotionRulesResponse200DataItemAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETorderAmountPromotionRulesResponse200DataItemAttributesMetadata.from_dict(_metadata)

        order_amount_cents = d.pop("order_amount_cents", UNSET)

        order_amount_float = d.pop("order_amount_float", UNSET)

        formatted_order_amount = d.pop("formatted_order_amount", UNSET)

        ge_torder_amount_promotion_rules_response_200_data_item_attributes = cls(
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
            order_amount_cents=order_amount_cents,
            order_amount_float=order_amount_float,
            formatted_order_amount=formatted_order_amount,
        )

        ge_torder_amount_promotion_rules_response_200_data_item_attributes.additional_properties = d
        return ge_torder_amount_promotion_rules_response_200_data_item_attributes

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
