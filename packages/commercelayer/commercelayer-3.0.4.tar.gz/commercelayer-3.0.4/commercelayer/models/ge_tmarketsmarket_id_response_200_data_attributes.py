from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tmarketsmarket_id_response_200_data_attributes_metadata import (
        GETmarketsmarketIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="GETmarketsmarketIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class GETmarketsmarketIdResponse200DataAttributes:
    """
    Attributes:
        number (Union[Unset, int]): Unique identifier for the market (numeric) Example: 1234.
        name (Union[Unset, str]): The market's internal name Example: EU Market.
        facebook_pixel_id (Union[Unset, str]): The Facebook Pixed ID Example: 1234567890.
        checkout_url (Union[Unset, str]): The checkout URL for this market Example:
            https://checkout.yourbrand.com/:order_id.
        external_prices_url (Union[Unset, str]): The URL used to fetch prices from an external source Example:
            https://external_prices.yourbrand.com.
        private (Union[Unset, bool]): Indicates if market belongs to a customer_group. Example: True.
        disabled_at (Union[Unset, str]): Time at which the market was disabled. Example: 2018-01-01T12:00:00.000Z.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETmarketsmarketIdResponse200DataAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    number: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    facebook_pixel_id: Union[Unset, str] = UNSET
    checkout_url: Union[Unset, str] = UNSET
    external_prices_url: Union[Unset, str] = UNSET
    private: Union[Unset, bool] = UNSET
    disabled_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETmarketsmarketIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        name = self.name
        facebook_pixel_id = self.facebook_pixel_id
        checkout_url = self.checkout_url
        external_prices_url = self.external_prices_url
        private = self.private
        disabled_at = self.disabled_at
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
        if number is not UNSET:
            field_dict["number"] = number
        if name is not UNSET:
            field_dict["name"] = name
        if facebook_pixel_id is not UNSET:
            field_dict["facebook_pixel_id"] = facebook_pixel_id
        if checkout_url is not UNSET:
            field_dict["checkout_url"] = checkout_url
        if external_prices_url is not UNSET:
            field_dict["external_prices_url"] = external_prices_url
        if private is not UNSET:
            field_dict["private"] = private
        if disabled_at is not UNSET:
            field_dict["disabled_at"] = disabled_at
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
        from ..models.ge_tmarketsmarket_id_response_200_data_attributes_metadata import (
            GETmarketsmarketIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        number = d.pop("number", UNSET)

        name = d.pop("name", UNSET)

        facebook_pixel_id = d.pop("facebook_pixel_id", UNSET)

        checkout_url = d.pop("checkout_url", UNSET)

        external_prices_url = d.pop("external_prices_url", UNSET)

        private = d.pop("private", UNSET)

        disabled_at = d.pop("disabled_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETmarketsmarketIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETmarketsmarketIdResponse200DataAttributesMetadata.from_dict(_metadata)

        ge_tmarketsmarket_id_response_200_data_attributes = cls(
            number=number,
            name=name,
            facebook_pixel_id=facebook_pixel_id,
            checkout_url=checkout_url,
            external_prices_url=external_prices_url,
            private=private,
            disabled_at=disabled_at,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_tmarketsmarket_id_response_200_data_attributes.additional_properties = d
        return ge_tmarketsmarket_id_response_200_data_attributes

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
