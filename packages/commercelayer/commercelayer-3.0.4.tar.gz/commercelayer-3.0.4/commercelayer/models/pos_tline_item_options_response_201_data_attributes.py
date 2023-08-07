from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tline_item_options_response_201_data_attributes_metadata import (
        POSTlineItemOptionsResponse201DataAttributesMetadata,
    )
    from ..models.pos_tline_item_options_response_201_data_attributes_options import (
        POSTlineItemOptionsResponse201DataAttributesOptions,
    )


T = TypeVar("T", bound="POSTlineItemOptionsResponse201DataAttributes")


@attr.s(auto_attribs=True)
class POSTlineItemOptionsResponse201DataAttributes:
    """
    Attributes:
        quantity (int): The line item option's quantity Example: 2.
        options (POSTlineItemOptionsResponse201DataAttributesOptions): Set of key-value pairs that represent the
            selected options. Example: {'embossing_text': 'Happy Birthday!'}.
        name (Union[Unset, str]): The name of the line item option. When blank, it gets populated with the name of the
            associated SKU option. Example: Embossing.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, POSTlineItemOptionsResponse201DataAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    quantity: int
    options: "POSTlineItemOptionsResponse201DataAttributesOptions"
    name: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "POSTlineItemOptionsResponse201DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity
        options = self.options.to_dict()

        name = self.name
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantity": quantity,
                "options": options,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tline_item_options_response_201_data_attributes_metadata import (
            POSTlineItemOptionsResponse201DataAttributesMetadata,
        )
        from ..models.pos_tline_item_options_response_201_data_attributes_options import (
            POSTlineItemOptionsResponse201DataAttributesOptions,
        )

        d = src_dict.copy()
        quantity = d.pop("quantity")

        options = POSTlineItemOptionsResponse201DataAttributesOptions.from_dict(d.pop("options"))

        name = d.pop("name", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, POSTlineItemOptionsResponse201DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = POSTlineItemOptionsResponse201DataAttributesMetadata.from_dict(_metadata)

        pos_tline_item_options_response_201_data_attributes = cls(
            quantity=quantity,
            options=options,
            name=name,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        pos_tline_item_options_response_201_data_attributes.additional_properties = d
        return pos_tline_item_options_response_201_data_attributes

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
