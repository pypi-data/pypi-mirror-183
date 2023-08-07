from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_volume_tier_data_attributes_metadata import PriceVolumeTierDataAttributesMetadata


T = TypeVar("T", bound="PriceVolumeTierDataAttributes")


@attr.s(auto_attribs=True)
class PriceVolumeTierDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The price tier's name Example: six pack.
        up_to (Union[Unset, float]): The tier upper limit. When 'null' it means infinity (useful to have an always
            matching tier). Example: 20.5.
        price_amount_cents (Union[Unset, int]): The price of this price tier, in cents. Example: 1000.
        price_amount_float (Union[Unset, float]): The price of this price tier, float. Example: 10.0.
        formatted_price_amount (Union[Unset, str]): The price of this price tier, formatted. Example: €10,00.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PriceVolumeTierDataAttributesMetadata]): Set of key-value pairs that you can attach to
            the resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    up_to: Union[Unset, float] = UNSET
    price_amount_cents: Union[Unset, int] = UNSET
    price_amount_float: Union[Unset, float] = UNSET
    formatted_price_amount: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PriceVolumeTierDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        up_to = self.up_to
        price_amount_cents = self.price_amount_cents
        price_amount_float = self.price_amount_float
        formatted_price_amount = self.formatted_price_amount
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
        if up_to is not UNSET:
            field_dict["up_to"] = up_to
        if price_amount_cents is not UNSET:
            field_dict["price_amount_cents"] = price_amount_cents
        if price_amount_float is not UNSET:
            field_dict["price_amount_float"] = price_amount_float
        if formatted_price_amount is not UNSET:
            field_dict["formatted_price_amount"] = formatted_price_amount
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
        from ..models.price_volume_tier_data_attributes_metadata import PriceVolumeTierDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        up_to = d.pop("up_to", UNSET)

        price_amount_cents = d.pop("price_amount_cents", UNSET)

        price_amount_float = d.pop("price_amount_float", UNSET)

        formatted_price_amount = d.pop("formatted_price_amount", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PriceVolumeTierDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PriceVolumeTierDataAttributesMetadata.from_dict(_metadata)

        price_volume_tier_data_attributes = cls(
            name=name,
            up_to=up_to,
            price_amount_cents=price_amount_cents,
            price_amount_float=price_amount_float,
            formatted_price_amount=formatted_price_amount,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        price_volume_tier_data_attributes.additional_properties = d
        return price_volume_tier_data_attributes

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
