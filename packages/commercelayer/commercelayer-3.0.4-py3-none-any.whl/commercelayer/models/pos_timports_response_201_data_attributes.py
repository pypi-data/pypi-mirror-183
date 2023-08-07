from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_timports_response_201_data_attributes_inputs_item import (
        POSTimportsResponse201DataAttributesInputsItem,
    )
    from ..models.pos_timports_response_201_data_attributes_metadata import POSTimportsResponse201DataAttributesMetadata


T = TypeVar("T", bound="POSTimportsResponse201DataAttributes")


@attr.s(auto_attribs=True)
class POSTimportsResponse201DataAttributes:
    """
    Attributes:
        resource_type (str): The type of resource being imported. Example: skus.
        inputs (List['POSTimportsResponse201DataAttributesInputsItem']): Array of objects representing the resources
            that are being imported. Example: [{'code': 'ABC', 'name': 'Foo'}, {'code': 'DEF', 'name': 'Bar'}].
        format_ (Union[Unset, str]): The format of the import inputs one of 'json' (default) or 'csv'. Example: json.
        parent_resource_id (Union[Unset, str]): The ID of the parent resource to be associated with imported data.
            Example: 1234.
        cleanup_records (Union[Unset, bool]): Indicates if the import should cleanup records that are not included in
            the inputs array. Example: True.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, POSTimportsResponse201DataAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    resource_type: str
    inputs: List["POSTimportsResponse201DataAttributesInputsItem"]
    format_: Union[Unset, str] = UNSET
    parent_resource_id: Union[Unset, str] = UNSET
    cleanup_records: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "POSTimportsResponse201DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource_type = self.resource_type
        inputs = []
        for inputs_item_data in self.inputs:
            inputs_item = inputs_item_data.to_dict()

            inputs.append(inputs_item)

        format_ = self.format_
        parent_resource_id = self.parent_resource_id
        cleanup_records = self.cleanup_records
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
                "inputs": inputs,
            }
        )
        if format_ is not UNSET:
            field_dict["format"] = format_
        if parent_resource_id is not UNSET:
            field_dict["parent_resource_id"] = parent_resource_id
        if cleanup_records is not UNSET:
            field_dict["cleanup_records"] = cleanup_records
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_timports_response_201_data_attributes_inputs_item import (
            POSTimportsResponse201DataAttributesInputsItem,
        )
        from ..models.pos_timports_response_201_data_attributes_metadata import (
            POSTimportsResponse201DataAttributesMetadata,
        )

        d = src_dict.copy()
        resource_type = d.pop("resource_type")

        inputs = []
        _inputs = d.pop("inputs")
        for inputs_item_data in _inputs:
            inputs_item = POSTimportsResponse201DataAttributesInputsItem.from_dict(inputs_item_data)

            inputs.append(inputs_item)

        format_ = d.pop("format", UNSET)

        parent_resource_id = d.pop("parent_resource_id", UNSET)

        cleanup_records = d.pop("cleanup_records", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, POSTimportsResponse201DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = POSTimportsResponse201DataAttributesMetadata.from_dict(_metadata)

        pos_timports_response_201_data_attributes = cls(
            resource_type=resource_type,
            inputs=inputs,
            format_=format_,
            parent_resource_id=parent_resource_id,
            cleanup_records=cleanup_records,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        pos_timports_response_201_data_attributes.additional_properties = d
        return pos_timports_response_201_data_attributes

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
