from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stock_location_data_attributes_metadata import StockLocationDataAttributesMetadata


T = TypeVar("T", bound="StockLocationDataAttributes")


@attr.s(auto_attribs=True)
class StockLocationDataAttributes:
    """
    Attributes:
        number (Union[Unset, int]): Unique identifier for the stock location (numeric) Example: 1234.
        name (Union[Unset, str]): The stock location's internal name. Example: Primary warehouse.
        label_format (Union[Unset, str]): The shipping label format for this stock location. Can be one of 'PDF', 'ZPL',
            'EPL2', or 'PNG' Example: PDF.
        suppress_etd (Union[Unset, bool]): Flag it if you want to skip the electronic invoice creation when generating
            the customs info for this stock location shipments.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, StockLocationDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    number: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    label_format: Union[Unset, str] = UNSET
    suppress_etd: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "StockLocationDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        name = self.name
        label_format = self.label_format
        suppress_etd = self.suppress_etd
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
        if number is not UNSET:
            field_dict["number"] = number
        if name is not UNSET:
            field_dict["name"] = name
        if label_format is not UNSET:
            field_dict["label_format"] = label_format
        if suppress_etd is not UNSET:
            field_dict["suppress_etd"] = suppress_etd
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
        from ..models.stock_location_data_attributes_metadata import StockLocationDataAttributesMetadata

        d = src_dict.copy()
        number = d.pop("number", UNSET)

        name = d.pop("name", UNSET)

        label_format = d.pop("label_format", UNSET)

        suppress_etd = d.pop("suppress_etd", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, StockLocationDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = StockLocationDataAttributesMetadata.from_dict(_metadata)

        stock_location_data_attributes = cls(
            number=number,
            name=name,
            label_format=label_format,
            suppress_etd=suppress_etd,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        stock_location_data_attributes.additional_properties = d
        return stock_location_data_attributes

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
