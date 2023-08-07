from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.klarna_gateway_update_data_attributes_metadata import KlarnaGatewayUpdateDataAttributesMetadata


T = TypeVar("T", bound="KlarnaGatewayUpdateDataAttributes")


@attr.s(auto_attribs=True)
class KlarnaGatewayUpdateDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The payment gateway's internal name. Example: US payment gateway.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, KlarnaGatewayUpdateDataAttributesMetadata]): Set of key-value pairs that you can attach
            to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
        country_code (Union[Unset, str]): The gateway country code one of EU, US, or OC. Example: EU.
        api_key (Union[Unset, str]): The public key linked to your API credential. Example: xxxx-yyyy-zzzz.
        api_secret (Union[Unset, str]): The gateway API key. Example: xxxx-yyyy-zzzz.
    """

    name: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "KlarnaGatewayUpdateDataAttributesMetadata"] = UNSET
    country_code: Union[Unset, str] = UNSET
    api_key: Union[Unset, str] = UNSET
    api_secret: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        country_code = self.country_code
        api_key = self.api_key
        api_secret = self.api_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if api_secret is not UNSET:
            field_dict["api_secret"] = api_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.klarna_gateway_update_data_attributes_metadata import KlarnaGatewayUpdateDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, KlarnaGatewayUpdateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = KlarnaGatewayUpdateDataAttributesMetadata.from_dict(_metadata)

        country_code = d.pop("country_code", UNSET)

        api_key = d.pop("api_key", UNSET)

        api_secret = d.pop("api_secret", UNSET)

        klarna_gateway_update_data_attributes = cls(
            name=name,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
            country_code=country_code,
            api_key=api_key,
            api_secret=api_secret,
        )

        klarna_gateway_update_data_attributes.additional_properties = d
        return klarna_gateway_update_data_attributes

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
