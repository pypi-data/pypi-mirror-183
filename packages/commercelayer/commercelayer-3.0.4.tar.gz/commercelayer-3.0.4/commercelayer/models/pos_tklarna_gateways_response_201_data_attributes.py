from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tklarna_gateways_response_201_data_attributes_metadata import (
        POSTklarnaGatewaysResponse201DataAttributesMetadata,
    )


T = TypeVar("T", bound="POSTklarnaGatewaysResponse201DataAttributes")


@attr.s(auto_attribs=True)
class POSTklarnaGatewaysResponse201DataAttributes:
    """
    Attributes:
        name (str): The payment gateway's internal name. Example: US payment gateway.
        country_code (str): The gateway country code one of EU, US, or OC. Example: EU.
        api_key (str): The public key linked to your API credential. Example: xxxx-yyyy-zzzz.
        api_secret (str): The gateway API key. Example: xxxx-yyyy-zzzz.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, POSTklarnaGatewaysResponse201DataAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    name: str
    country_code: str
    api_key: str
    api_secret: str
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "POSTklarnaGatewaysResponse201DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        country_code = self.country_code
        api_key = self.api_key
        api_secret = self.api_secret
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "country_code": country_code,
                "api_key": api_key,
                "api_secret": api_secret,
            }
        )
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tklarna_gateways_response_201_data_attributes_metadata import (
            POSTklarnaGatewaysResponse201DataAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name")

        country_code = d.pop("country_code")

        api_key = d.pop("api_key")

        api_secret = d.pop("api_secret")

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, POSTklarnaGatewaysResponse201DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = POSTklarnaGatewaysResponse201DataAttributesMetadata.from_dict(_metadata)

        pos_tklarna_gateways_response_201_data_attributes = cls(
            name=name,
            country_code=country_code,
            api_key=api_key,
            api_secret=api_secret,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        pos_tklarna_gateways_response_201_data_attributes.additional_properties = d
        return pos_tklarna_gateways_response_201_data_attributes

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
