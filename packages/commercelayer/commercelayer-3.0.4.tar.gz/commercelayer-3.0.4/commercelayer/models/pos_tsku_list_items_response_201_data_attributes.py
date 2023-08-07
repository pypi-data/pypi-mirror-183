from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tsku_list_items_response_201_data_attributes_metadata import (
        POSTskuListItemsResponse201DataAttributesMetadata,
    )


T = TypeVar("T", bound="POSTskuListItemsResponse201DataAttributes")


@attr.s(auto_attribs=True)
class POSTskuListItemsResponse201DataAttributes:
    """
    Attributes:
        position (Union[Unset, int]): The SKU list item's position. Example: 2.
        sku_code (Union[Unset, str]): The code of the associated SKU. Example: TSHIRTMM000000FFFFFFXLXX.
        quantity (Union[Unset, int]): The SKU quantity for this SKU list item. Example: 1.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, POSTskuListItemsResponse201DataAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    position: Union[Unset, int] = UNSET
    sku_code: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "POSTskuListItemsResponse201DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position
        sku_code = self.sku_code
        quantity = self.quantity
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if sku_code is not UNSET:
            field_dict["sku_code"] = sku_code
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tsku_list_items_response_201_data_attributes_metadata import (
            POSTskuListItemsResponse201DataAttributesMetadata,
        )

        d = src_dict.copy()
        position = d.pop("position", UNSET)

        sku_code = d.pop("sku_code", UNSET)

        quantity = d.pop("quantity", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, POSTskuListItemsResponse201DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = POSTskuListItemsResponse201DataAttributesMetadata.from_dict(_metadata)

        pos_tsku_list_items_response_201_data_attributes = cls(
            position=position,
            sku_code=sku_code,
            quantity=quantity,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        pos_tsku_list_items_response_201_data_attributes.additional_properties = d
        return pos_tsku_list_items_response_201_data_attributes

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
