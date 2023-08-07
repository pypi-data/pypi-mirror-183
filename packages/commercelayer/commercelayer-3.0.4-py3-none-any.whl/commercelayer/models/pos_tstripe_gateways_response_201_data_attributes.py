from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tstripe_gateways_response_201_data_attributes_metadata import (
        POSTstripeGatewaysResponse201DataAttributesMetadata,
    )


T = TypeVar("T", bound="POSTstripeGatewaysResponse201DataAttributes")


@attr.s(auto_attribs=True)
class POSTstripeGatewaysResponse201DataAttributes:
    """
    Attributes:
        name (str): The payment gateway's internal name. Example: US payment gateway.
        login (str): The gateway login. Example: sk_live_xxxx-yyyy-zzzz.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, POSTstripeGatewaysResponse201DataAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
        publishable_key (Union[Unset, str]): The gateway publishable API key. Example: pk_live_xxxx-yyyy-zzzz.
    """

    name: str
    login: str
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "POSTstripeGatewaysResponse201DataAttributesMetadata"] = UNSET
    publishable_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        login = self.login
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        publishable_key = self.publishable_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "login": login,
            }
        )
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if publishable_key is not UNSET:
            field_dict["publishable_key"] = publishable_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tstripe_gateways_response_201_data_attributes_metadata import (
            POSTstripeGatewaysResponse201DataAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name")

        login = d.pop("login")

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, POSTstripeGatewaysResponse201DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = POSTstripeGatewaysResponse201DataAttributesMetadata.from_dict(_metadata)

        publishable_key = d.pop("publishable_key", UNSET)

        pos_tstripe_gateways_response_201_data_attributes = cls(
            name=name,
            login=login,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
            publishable_key=publishable_key,
        )

        pos_tstripe_gateways_response_201_data_attributes.additional_properties = d
        return pos_tstripe_gateways_response_201_data_attributes

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
