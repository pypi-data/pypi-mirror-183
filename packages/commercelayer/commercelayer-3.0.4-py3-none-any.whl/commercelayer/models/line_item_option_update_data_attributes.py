from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_item_option_update_data_attributes_metadata import LineItemOptionUpdateDataAttributesMetadata
    from ..models.line_item_option_update_data_attributes_options import LineItemOptionUpdateDataAttributesOptions


T = TypeVar("T", bound="LineItemOptionUpdateDataAttributes")


@attr.s(auto_attribs=True)
class LineItemOptionUpdateDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The name of the line item option. When blank, it gets populated with the name of the
            associated SKU option. Example: Embossing.
        quantity (Union[Unset, int]): The line item option's quantity Example: 2.
        options (Union[Unset, LineItemOptionUpdateDataAttributesOptions]): Set of key-value pairs that represent the
            selected options. Example: {'embossing_text': 'Happy Birthday!'}.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, LineItemOptionUpdateDataAttributesMetadata]): Set of key-value pairs that you can attach
            to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    options: Union[Unset, "LineItemOptionUpdateDataAttributesOptions"] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "LineItemOptionUpdateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        quantity = self.quantity
        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

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
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if options is not UNSET:
            field_dict["options"] = options
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.line_item_option_update_data_attributes_metadata import LineItemOptionUpdateDataAttributesMetadata
        from ..models.line_item_option_update_data_attributes_options import LineItemOptionUpdateDataAttributesOptions

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        quantity = d.pop("quantity", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, LineItemOptionUpdateDataAttributesOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = LineItemOptionUpdateDataAttributesOptions.from_dict(_options)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, LineItemOptionUpdateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = LineItemOptionUpdateDataAttributesMetadata.from_dict(_metadata)

        line_item_option_update_data_attributes = cls(
            name=name,
            quantity=quantity,
            options=options,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        line_item_option_update_data_attributes.additional_properties = d
        return line_item_option_update_data_attributes

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
