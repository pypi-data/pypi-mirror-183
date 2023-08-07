from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.market_update_data_attributes_metadata import MarketUpdateDataAttributesMetadata


T = TypeVar("T", bound="MarketUpdateDataAttributes")


@attr.s(auto_attribs=True)
class MarketUpdateDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The market's internal name Example: EU Market.
        facebook_pixel_id (Union[Unset, str]): The Facebook Pixed ID Example: 1234567890.
        checkout_url (Union[Unset, str]): The checkout URL for this market Example:
            https://checkout.yourbrand.com/:order_id.
        external_prices_url (Union[Unset, str]): The URL used to fetch prices from an external source Example:
            https://external_prices.yourbrand.com.
        disable (Union[Unset, bool]): Send this attribute if you want to mark the market as disabled. Example: True.
        enable (Union[Unset, bool]): Send this attribute if you want to mark the market as enabled. Example: True.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, MarketUpdateDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    facebook_pixel_id: Union[Unset, str] = UNSET
    checkout_url: Union[Unset, str] = UNSET
    external_prices_url: Union[Unset, str] = UNSET
    disable: Union[Unset, bool] = UNSET
    enable: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "MarketUpdateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        facebook_pixel_id = self.facebook_pixel_id
        checkout_url = self.checkout_url
        external_prices_url = self.external_prices_url
        disable = self.disable
        enable = self.enable
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
        if facebook_pixel_id is not UNSET:
            field_dict["facebook_pixel_id"] = facebook_pixel_id
        if checkout_url is not UNSET:
            field_dict["checkout_url"] = checkout_url
        if external_prices_url is not UNSET:
            field_dict["external_prices_url"] = external_prices_url
        if disable is not UNSET:
            field_dict["_disable"] = disable
        if enable is not UNSET:
            field_dict["_enable"] = enable
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.market_update_data_attributes_metadata import MarketUpdateDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        facebook_pixel_id = d.pop("facebook_pixel_id", UNSET)

        checkout_url = d.pop("checkout_url", UNSET)

        external_prices_url = d.pop("external_prices_url", UNSET)

        disable = d.pop("_disable", UNSET)

        enable = d.pop("_enable", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, MarketUpdateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = MarketUpdateDataAttributesMetadata.from_dict(_metadata)

        market_update_data_attributes = cls(
            name=name,
            facebook_pixel_id=facebook_pixel_id,
            checkout_url=checkout_url,
            external_prices_url=external_prices_url,
            disable=disable,
            enable=enable,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        market_update_data_attributes.additional_properties = d
        return market_update_data_attributes

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
