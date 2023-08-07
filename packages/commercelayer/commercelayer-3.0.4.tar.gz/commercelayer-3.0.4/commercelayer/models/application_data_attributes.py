from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_data_attributes_metadata import ApplicationDataAttributesMetadata


T = TypeVar("T", bound="ApplicationDataAttributes")


@attr.s(auto_attribs=True)
class ApplicationDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The application's internal name. Example: My app.
        kind (Union[Unset, str]): The application's kind, can be one of: 'sales_channel', 'integration' and 'webapp'.
            Example: sales-channel.
        public_access (Union[Unset, bool]): Indicates if the application has public access. Example: True.
        redirect_uri (Union[Unset, str]): The application's redirect URI. Example: https://bluebrand.com/img/logo.svg.
        scopes (Union[Unset, str]): The application's scopes. Example: market:all market:9 market:122 market:6
            stock_location:6 stock_location:33.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, ApplicationDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    public_access: Union[Unset, bool] = UNSET
    redirect_uri: Union[Unset, str] = UNSET
    scopes: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ApplicationDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        kind = self.kind
        public_access = self.public_access
        redirect_uri = self.redirect_uri
        scopes = self.scopes
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
        if kind is not UNSET:
            field_dict["kind"] = kind
        if public_access is not UNSET:
            field_dict["public_access"] = public_access
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
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
        from ..models.application_data_attributes_metadata import ApplicationDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        kind = d.pop("kind", UNSET)

        public_access = d.pop("public_access", UNSET)

        redirect_uri = d.pop("redirect_uri", UNSET)

        scopes = d.pop("scopes", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ApplicationDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ApplicationDataAttributesMetadata.from_dict(_metadata)

        application_data_attributes = cls(
            name=name,
            kind=kind,
            public_access=public_access,
            redirect_uri=redirect_uri,
            scopes=scopes,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        application_data_attributes.additional_properties = d
        return application_data_attributes

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
