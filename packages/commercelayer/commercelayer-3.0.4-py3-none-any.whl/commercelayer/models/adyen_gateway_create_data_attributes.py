from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adyen_gateway_create_data_attributes_metadata import AdyenGatewayCreateDataAttributesMetadata


T = TypeVar("T", bound="AdyenGatewayCreateDataAttributes")


@attr.s(auto_attribs=True)
class AdyenGatewayCreateDataAttributes:
    """
    Attributes:
        name (str): The payment gateway's internal name. Example: US payment gateway.
        merchant_account (str): The gateway merchant account. Example: xxxx-yyyy-zzzz.
        api_key (str): The gateway API key. Example: xxxx-yyyy-zzzz.
        live_url_prefix (str): The prefix of the endpoint used for live transactions. Example:
            1797a841fbb37ca7-AdyenDemo.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, AdyenGatewayCreateDataAttributesMetadata]): Set of key-value pairs that you can attach to
            the resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
        public_key (Union[Unset, str]): The public key linked to your API credential. Example: xxxx-yyyy-zzzz.
    """

    name: str
    merchant_account: str
    api_key: str
    live_url_prefix: str
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "AdyenGatewayCreateDataAttributesMetadata"] = UNSET
    public_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        merchant_account = self.merchant_account
        api_key = self.api_key
        live_url_prefix = self.live_url_prefix
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        public_key = self.public_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "merchant_account": merchant_account,
                "api_key": api_key,
                "live_url_prefix": live_url_prefix,
            }
        )
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if public_key is not UNSET:
            field_dict["public_key"] = public_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adyen_gateway_create_data_attributes_metadata import AdyenGatewayCreateDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name")

        merchant_account = d.pop("merchant_account")

        api_key = d.pop("api_key")

        live_url_prefix = d.pop("live_url_prefix")

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, AdyenGatewayCreateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AdyenGatewayCreateDataAttributesMetadata.from_dict(_metadata)

        public_key = d.pop("public_key", UNSET)

        adyen_gateway_create_data_attributes = cls(
            name=name,
            merchant_account=merchant_account,
            api_key=api_key,
            live_url_prefix=live_url_prefix,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
            public_key=public_key,
        )

        adyen_gateway_create_data_attributes.additional_properties = d
        return adyen_gateway_create_data_attributes

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
