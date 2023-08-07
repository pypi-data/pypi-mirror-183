from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tcleanups_response_201_data_attributes_filters import POSTcleanupsResponse201DataAttributesFilters
    from ..models.pos_tcleanups_response_201_data_attributes_metadata import (
        POSTcleanupsResponse201DataAttributesMetadata,
    )


T = TypeVar("T", bound="POSTcleanupsResponse201DataAttributes")


@attr.s(auto_attribs=True)
class POSTcleanupsResponse201DataAttributes:
    """
    Attributes:
        resource_type (str): The type of resource being cleaned. Example: skus.
        filters (Union[Unset, POSTcleanupsResponse201DataAttributesFilters]): The filters used to select the records to
            be cleaned. Example: {'code_eq': 'AAA'}.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, POSTcleanupsResponse201DataAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    resource_type: str
    filters: Union[Unset, "POSTcleanupsResponse201DataAttributesFilters"] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "POSTcleanupsResponse201DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource_type = self.resource_type
        filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_type": resource_type,
            }
        )
        if filters is not UNSET:
            field_dict["filters"] = filters
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tcleanups_response_201_data_attributes_filters import (
            POSTcleanupsResponse201DataAttributesFilters,
        )
        from ..models.pos_tcleanups_response_201_data_attributes_metadata import (
            POSTcleanupsResponse201DataAttributesMetadata,
        )

        d = src_dict.copy()
        resource_type = d.pop("resource_type")

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, POSTcleanupsResponse201DataAttributesFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = POSTcleanupsResponse201DataAttributesFilters.from_dict(_filters)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, POSTcleanupsResponse201DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = POSTcleanupsResponse201DataAttributesMetadata.from_dict(_metadata)

        pos_tcleanups_response_201_data_attributes = cls(
            resource_type=resource_type,
            filters=filters,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        pos_tcleanups_response_201_data_attributes.additional_properties = d
        return pos_tcleanups_response_201_data_attributes

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
