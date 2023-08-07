from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tsku_lists_response_201_data_attributes_metadata import (
        POSTskuListsResponse201DataAttributesMetadata,
    )


T = TypeVar("T", bound="POSTskuListsResponse201DataAttributes")


@attr.s(auto_attribs=True)
class POSTskuListsResponse201DataAttributes:
    """
    Attributes:
        name (str): The SKU list's internal name. Example: Personal list.
        description (Union[Unset, str]): An internal description of the SKU list. Example: Lorem ipsum dolor sit amet,
            consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua..
        image_url (Union[Unset, str]): The URL of an image that represents the SKU list. Example:
            https://img.yourdomain.com/skus/xYZkjABcde.png.
        manual (Union[Unset, bool]): Indicates if the SKU list is populated manually.
        sku_code_regex (Union[Unset, str]): The regex that will be evaluated to match the SKU codes. Example: ^(A|B).*$.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, POSTskuListsResponse201DataAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    name: str
    description: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    manual: Union[Unset, bool] = UNSET
    sku_code_regex: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "POSTskuListsResponse201DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        image_url = self.image_url
        manual = self.manual
        sku_code_regex = self.sku_code_regex
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
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if manual is not UNSET:
            field_dict["manual"] = manual
        if sku_code_regex is not UNSET:
            field_dict["sku_code_regex"] = sku_code_regex
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tsku_lists_response_201_data_attributes_metadata import (
            POSTskuListsResponse201DataAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        image_url = d.pop("image_url", UNSET)

        manual = d.pop("manual", UNSET)

        sku_code_regex = d.pop("sku_code_regex", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, POSTskuListsResponse201DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = POSTskuListsResponse201DataAttributesMetadata.from_dict(_metadata)

        pos_tsku_lists_response_201_data_attributes = cls(
            name=name,
            description=description,
            image_url=image_url,
            manual=manual,
            sku_code_regex=sku_code_regex,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        pos_tsku_lists_response_201_data_attributes.additional_properties = d
        return pos_tsku_lists_response_201_data_attributes

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
