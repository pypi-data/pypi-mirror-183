from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tadjustments_response_200_data_item_attributes_metadata import (
        GETadjustmentsResponse200DataItemAttributesMetadata,
    )


T = TypeVar("T", bound="GETadjustmentsResponse200DataItemAttributes")


@attr.s(auto_attribs=True)
class GETadjustmentsResponse200DataItemAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The adjustment name Example: Additional service.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard.
            Example: EUR.
        amount_cents (Union[Unset, int]): The adjustment amount, in cents. Example: 1500.
        amount_float (Union[Unset, float]): The adjustment amount, float. Example: 15.0.
        formatted_amount (Union[Unset, str]): The adjustment amount, formatted. Example: €15,00.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETadjustmentsResponse200DataItemAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    amount_cents: Union[Unset, int] = UNSET
    amount_float: Union[Unset, float] = UNSET
    formatted_amount: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETadjustmentsResponse200DataItemAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        currency_code = self.currency_code
        amount_cents = self.amount_cents
        amount_float = self.amount_float
        formatted_amount = self.formatted_amount
        created_at = self.created_at
        updated_at = self.updated_at
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
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if amount_cents is not UNSET:
            field_dict["amount_cents"] = amount_cents
        if amount_float is not UNSET:
            field_dict["amount_float"] = amount_float
        if formatted_amount is not UNSET:
            field_dict["formatted_amount"] = formatted_amount
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tadjustments_response_200_data_item_attributes_metadata import (
            GETadjustmentsResponse200DataItemAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        amount_cents = d.pop("amount_cents", UNSET)

        amount_float = d.pop("amount_float", UNSET)

        formatted_amount = d.pop("formatted_amount", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETadjustmentsResponse200DataItemAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETadjustmentsResponse200DataItemAttributesMetadata.from_dict(_metadata)

        ge_tadjustments_response_200_data_item_attributes = cls(
            name=name,
            currency_code=currency_code,
            amount_cents=amount_cents,
            amount_float=amount_float,
            formatted_amount=formatted_amount,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_tadjustments_response_200_data_item_attributes.additional_properties = d
        return ge_tadjustments_response_200_data_item_attributes

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
