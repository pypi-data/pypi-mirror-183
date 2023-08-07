from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tskus_response_200_data_item_attributes_inventory import (
        GETskusResponse200DataItemAttributesInventory,
    )
    from ..models.ge_tskus_response_200_data_item_attributes_metadata import (
        GETskusResponse200DataItemAttributesMetadata,
    )


T = TypeVar("T", bound="GETskusResponse200DataItemAttributes")


@attr.s(auto_attribs=True)
class GETskusResponse200DataItemAttributes:
    """
    Attributes:
        code (Union[Unset, str]): The SKU code, that uniquely identifies the SKU within the organization. Example:
            TSHIRTMM000000FFFFFFXLXX.
        name (Union[Unset, str]): The internal name of the SKU. Example: Black Men T-shirt with White Logo (XL).
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
        inventory (Union[Unset, GETskusResponse200DataItemAttributesInventory]): Aggregated information about the SKU's
            inventory. Returned only when retrieving a single SKU. Example: {'available': True, 'quantity': 10, 'levels':
            [{'quantity': 4, 'delivery_lead_times': [{'shipping_method': {'name': 'Standard Shipping', 'reference': None,
            'price_amount_cents': 700, 'free_over_amount_cents': 9900, 'formatted_price_amount': '€7,00',
            'formatted_free_over_amount': '€99,00'}, 'min': {'hours': 72, 'days': 3}, 'max': {'hours': 120, 'days': 5}},
            {'shipping_method': {'name': 'Express Delivery', 'reference': None, 'price_amount_cents': 1200,
            'free_over_amount_cents': None, 'formatted_price_amount': '€12,00', 'formatted_free_over_amount': None}, 'min':
            {'hours': 48, 'days': 2}, 'max': {'hours': 72, 'days': 3}}]}, {'quantity': 6, 'delivery_lead_times':
            [{'shipping_method': {'name': 'Standard Shipping', 'reference': None, 'price_amount_cents': 700,
            'free_over_amount_cents': 9900, 'formatted_price_amount': '€7,00', 'formatted_free_over_amount': '€99,00'},
            'min': {'hours': 96, 'days': 4}, 'max': {'hours': 144, 'days': 6}}, {'shipping_method': {'name': 'Express
            Delivery', 'reference': None, 'price_amount_cents': 1200, 'free_over_amount_cents': None,
            'formatted_price_amount': '€12,00', 'formatted_free_over_amount': None}, 'min': {'hours': 72, 'days': 3}, 'max':
            {'hours': 96, 'days': 4}}]}]}.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETskusResponse200DataItemAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    pieces_per_pack: Union[Unset, int] = UNSET
    weight: Union[Unset, float] = UNSET
    unit_of_weight: Union[Unset, str] = UNSET
    hs_tariff_number: Union[Unset, str] = UNSET
    do_not_ship: Union[Unset, bool] = UNSET
    do_not_track: Union[Unset, bool] = UNSET
    inventory: Union[Unset, "GETskusResponse200DataItemAttributesInventory"] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETskusResponse200DataItemAttributesMetadata"] = UNSET
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
        inventory: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = self.inventory.to_dict()

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
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
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
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
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
        from ..models.ge_tskus_response_200_data_item_attributes_inventory import (
            GETskusResponse200DataItemAttributesInventory,
        )
        from ..models.ge_tskus_response_200_data_item_attributes_metadata import (
            GETskusResponse200DataItemAttributesMetadata,
        )

        d = src_dict.copy()
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        image_url = d.pop("image_url", UNSET)

        pieces_per_pack = d.pop("pieces_per_pack", UNSET)

        weight = d.pop("weight", UNSET)

        unit_of_weight = d.pop("unit_of_weight", UNSET)

        hs_tariff_number = d.pop("hs_tariff_number", UNSET)

        do_not_ship = d.pop("do_not_ship", UNSET)

        do_not_track = d.pop("do_not_track", UNSET)

        _inventory = d.pop("inventory", UNSET)
        inventory: Union[Unset, GETskusResponse200DataItemAttributesInventory]
        if isinstance(_inventory, Unset):
            inventory = UNSET
        else:
            inventory = GETskusResponse200DataItemAttributesInventory.from_dict(_inventory)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETskusResponse200DataItemAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETskusResponse200DataItemAttributesMetadata.from_dict(_metadata)

        ge_tskus_response_200_data_item_attributes = cls(
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
            inventory=inventory,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_tskus_response_200_data_item_attributes.additional_properties = d
        return ge_tskus_response_200_data_item_attributes

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
