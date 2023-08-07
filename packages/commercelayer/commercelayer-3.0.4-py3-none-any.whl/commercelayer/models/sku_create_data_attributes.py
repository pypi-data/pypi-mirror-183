from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sku_create_data_attributes_metadata import SkuCreateDataAttributesMetadata


T = TypeVar("T", bound="SkuCreateDataAttributes")


@attr.s(auto_attribs=True)
class SkuCreateDataAttributes:
    """
    Attributes:
        code (str): The SKU code, that uniquely identifies the SKU within the organization. Example:
            TSHIRTMM000000FFFFFFXLXX.
        name (str): The internal name of the SKU. Example: Black Men T-shirt with White Logo (XL).
        description (Union[Unset, str]): An internal description of the SKU. Example: Lorem ipsum dolor sit amet,
            consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua..
        image_url (Union[Unset, str]): The URL of an image that represents the SKU. Example:
            https://img.yourdomain.com/skus/xYZkjABcde.png.
        pieces_per_pack (Union[Unset, int]): The number of pieces that compose the SKU. This is useful to describe sets
            and bundles. Example: 6.
        weight (Union[Unset, float]): The weight of the SKU. If present, it will be used to calculate the shipping
            rates. Example: 300.0.
        unit_of_weight (Union[Unset, str]): Can be one of 'gr', 'lb', or 'oz' Example: gr.
        hs_tariff_number (Union[Unset, str]): The Harmonized System Code used by customs to identify the products
            shipped across international borders. Example: 4901.91.0020.
        do_not_ship (Union[Unset, bool]): Indicates if the SKU doesn't generate shipments.
        do_not_track (Union[Unset, bool]): Indicates if the SKU doesn't track the stock inventory.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, SkuCreateDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    code: str
    name: str
    description: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    pieces_per_pack: Union[Unset, int] = UNSET
    weight: Union[Unset, float] = UNSET
    unit_of_weight: Union[Unset, str] = UNSET
    hs_tariff_number: Union[Unset, str] = UNSET
    do_not_ship: Union[Unset, bool] = UNSET
    do_not_track: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "SkuCreateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        name = self.name
        description = self.description
        image_url = self.image_url
        pieces_per_pack = self.pieces_per_pack
        weight = self.weight
        unit_of_weight = self.unit_of_weight
        hs_tariff_number = self.hs_tariff_number
        do_not_ship = self.do_not_ship
        do_not_track = self.do_not_track
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if pieces_per_pack is not UNSET:
            field_dict["pieces_per_pack"] = pieces_per_pack
        if weight is not UNSET:
            field_dict["weight"] = weight
        if unit_of_weight is not UNSET:
            field_dict["unit_of_weight"] = unit_of_weight
        if hs_tariff_number is not UNSET:
            field_dict["hs_tariff_number"] = hs_tariff_number
        if do_not_ship is not UNSET:
            field_dict["do_not_ship"] = do_not_ship
        if do_not_track is not UNSET:
            field_dict["do_not_track"] = do_not_track
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sku_create_data_attributes_metadata import SkuCreateDataAttributesMetadata

        d = src_dict.copy()
        code = d.pop("code")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        image_url = d.pop("image_url", UNSET)

        pieces_per_pack = d.pop("pieces_per_pack", UNSET)

        weight = d.pop("weight", UNSET)

        unit_of_weight = d.pop("unit_of_weight", UNSET)

        hs_tariff_number = d.pop("hs_tariff_number", UNSET)

        do_not_ship = d.pop("do_not_ship", UNSET)

        do_not_track = d.pop("do_not_track", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, SkuCreateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = SkuCreateDataAttributesMetadata.from_dict(_metadata)

        sku_create_data_attributes = cls(
            code=code,
            name=name,
            description=description,
            image_url=image_url,
            pieces_per_pack=pieces_per_pack,
            weight=weight,
            unit_of_weight=unit_of_weight,
            hs_tariff_number=hs_tariff_number,
            do_not_ship=do_not_ship,
            do_not_track=do_not_track,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        sku_create_data_attributes.additional_properties = d
        return sku_create_data_attributes

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
