from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tsku_lists_response_200_data_item_attributes_metadata import (
        GETskuListsResponse200DataItemAttributesMetadata,
    )


T = TypeVar("T", bound="GETskuListsResponse200DataItemAttributes")


@attr.s(auto_attribs=True)
class GETskuListsResponse200DataItemAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The SKU list's internal name. Example: Personal list.
        slug (Union[Unset, str]): The SKU list's internal slug. Example: personal-list-1.
        description (Union[Unset, str]): An internal description of the SKU list. Example: Lorem ipsum dolor sit amet,
            consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua..
        image_url (Union[Unset, str]): The URL of an image that represents the SKU list. Example:
            https://img.yourdomain.com/skus/xYZkjABcde.png.
        manual (Union[Unset, bool]): Indicates if the SKU list is populated manually.
        sku_code_regex (Union[Unset, str]): The regex that will be evaluated to match the SKU codes. Example: ^(A|B).*$.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETskuListsResponse200DataItemAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    manual: Union[Unset, bool] = UNSET
    sku_code_regex: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETskuListsResponse200DataItemAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        slug = self.slug
        description = self.description
        image_url = self.image_url
        manual = self.manual
        sku_code_regex = self.sku_code_regex
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
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if manual is not UNSET:
            field_dict["manual"] = manual
        if sku_code_regex is not UNSET:
            field_dict["sku_code_regex"] = sku_code_regex
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
        from ..models.ge_tsku_lists_response_200_data_item_attributes_metadata import (
            GETskuListsResponse200DataItemAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        description = d.pop("description", UNSET)

        image_url = d.pop("image_url", UNSET)

        manual = d.pop("manual", UNSET)

        sku_code_regex = d.pop("sku_code_regex", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETskuListsResponse200DataItemAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETskuListsResponse200DataItemAttributesMetadata.from_dict(_metadata)

        ge_tsku_lists_response_200_data_item_attributes = cls(
            name=name,
            slug=slug,
            description=description,
            image_url=image_url,
            manual=manual,
            sku_code_regex=sku_code_regex,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_tsku_lists_response_200_data_item_attributes.additional_properties = d
        return ge_tsku_lists_response_200_data_item_attributes

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
