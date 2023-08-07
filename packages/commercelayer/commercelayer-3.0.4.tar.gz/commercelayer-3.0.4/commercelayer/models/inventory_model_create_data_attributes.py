from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_model_create_data_attributes_metadata import InventoryModelCreateDataAttributesMetadata


T = TypeVar("T", bound="InventoryModelCreateDataAttributes")


@attr.s(auto_attribs=True)
class InventoryModelCreateDataAttributes:
    """
    Attributes:
        name (str): The inventory model's internal name. Example: EU Inventory Model.
        strategy (Union[Unset, str]): The inventory model's shipping strategy: one between 'no_split' (default),
            'split_shipments', 'ship_from_primary' and 'ship_from_first_available_or_primary'. Example: no_split.
        stock_locations_cutoff (Union[Unset, int]): The maximum number of stock locations used for inventory computation
            Example: 3.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, InventoryModelCreateDataAttributesMetadata]): Set of key-value pairs that you can attach
            to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    name: str
    strategy: Union[Unset, str] = UNSET
    stock_locations_cutoff: Union[Unset, int] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "InventoryModelCreateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        strategy = self.strategy
        stock_locations_cutoff = self.stock_locations_cutoff
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
        if strategy is not UNSET:
            field_dict["strategy"] = strategy
        if stock_locations_cutoff is not UNSET:
            field_dict["stock_locations_cutoff"] = stock_locations_cutoff
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inventory_model_create_data_attributes_metadata import InventoryModelCreateDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name")

        strategy = d.pop("strategy", UNSET)

        stock_locations_cutoff = d.pop("stock_locations_cutoff", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, InventoryModelCreateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = InventoryModelCreateDataAttributesMetadata.from_dict(_metadata)

        inventory_model_create_data_attributes = cls(
            name=name,
            strategy=strategy,
            stock_locations_cutoff=stock_locations_cutoff,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        inventory_model_create_data_attributes.additional_properties = d
        return inventory_model_create_data_attributes

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
