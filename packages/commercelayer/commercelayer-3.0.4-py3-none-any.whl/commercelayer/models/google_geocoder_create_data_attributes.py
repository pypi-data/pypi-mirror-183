from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_geocoder_create_data_attributes_metadata import GoogleGeocoderCreateDataAttributesMetadata


T = TypeVar("T", bound="GoogleGeocoderCreateDataAttributes")


@attr.s(auto_attribs=True)
class GoogleGeocoderCreateDataAttributes:
    """
    Attributes:
        name (str): The geocoder's internal name Example: Default geocoder.
        api_key (str): The Google Map API key Example: xxxx-yyyy-zzzz.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GoogleGeocoderCreateDataAttributesMetadata]): Set of key-value pairs that you can attach
            to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    name: str
    api_key: str
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GoogleGeocoderCreateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        api_key = self.api_key
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
                "api_key": api_key,
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
        from ..models.google_geocoder_create_data_attributes_metadata import GoogleGeocoderCreateDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name")

        api_key = d.pop("api_key")

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GoogleGeocoderCreateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GoogleGeocoderCreateDataAttributesMetadata.from_dict(_metadata)

        google_geocoder_create_data_attributes = cls(
            name=name,
            api_key=api_key,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        google_geocoder_create_data_attributes.additional_properties = d
        return google_geocoder_create_data_attributes

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
