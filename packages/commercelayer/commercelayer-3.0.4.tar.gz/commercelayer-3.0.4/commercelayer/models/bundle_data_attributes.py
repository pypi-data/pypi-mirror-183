from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bundle_data_attributes_metadata import BundleDataAttributesMetadata


T = TypeVar("T", bound="BundleDataAttributes")


@attr.s(auto_attribs=True)
class BundleDataAttributes:
    """
    Attributes:
        code (Union[Unset, str]): The bundle code, that uniquely identifies the bundle within the market. Example:
            BUNDMM000000FFFFFFXLXX.
        name (Union[Unset, str]): The internal name of the bundle. Example: Black Men T-shirt (XL) with Black Cap and
            Socks, all with White Logo.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard.
            Example: EUR.
        description (Union[Unset, str]): An internal description of the bundle. Example: Lorem ipsum dolor sit amet,
            consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua..
        image_url (Union[Unset, str]): The URL of an image that represents the bundle. Example:
            https://img.yourdomain.com/bundles/xYZkjABcde.png.
        do_not_ship (Union[Unset, bool]): Indicates if the bundle doesn't generate shipments (all sku_list's SKUs must
            be do_not_ship).
        do_not_track (Union[Unset, bool]): Indicates if the bundle doesn't track the stock inventory (all sku_list's
            SKUs must be do_not_track).
        price_amount_cents (Union[Unset, int]): The bundle price amount for the associated market, in cents. Example:
            10000.
        price_amount_float (Union[Unset, float]): The bundle price amount for the associated market, float. Example:
            100.0.
        formatted_price_amount (Union[Unset, str]): The bundle price amount for the associated market, formatted.
            Example: €100,00.
        compare_at_amount_cents (Union[Unset, int]): The compared price amount, in cents. Useful to display a percentage
            discount. Example: 13000.
        compare_at_amount_float (Union[Unset, float]): The compared price amount, float. Example: 130.0.
        formatted_compare_at_amount (Union[Unset, str]): The compared price amount, formatted. Example: €130,00.
        skus_count (Union[Unset, int]): The total number of SKUs in the bundle. Example: 2.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, BundleDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    do_not_ship: Union[Unset, bool] = UNSET
    do_not_track: Union[Unset, bool] = UNSET
    price_amount_cents: Union[Unset, int] = UNSET
    price_amount_float: Union[Unset, float] = UNSET
    formatted_price_amount: Union[Unset, str] = UNSET
    compare_at_amount_cents: Union[Unset, int] = UNSET
    compare_at_amount_float: Union[Unset, float] = UNSET
    formatted_compare_at_amount: Union[Unset, str] = UNSET
    skus_count: Union[Unset, int] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "BundleDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        name = self.name
        currency_code = self.currency_code
        description = self.description
        image_url = self.image_url
        do_not_ship = self.do_not_ship
        do_not_track = self.do_not_track
        price_amount_cents = self.price_amount_cents
        price_amount_float = self.price_amount_float
        formatted_price_amount = self.formatted_price_amount
        compare_at_amount_cents = self.compare_at_amount_cents
        compare_at_amount_float = self.compare_at_amount_float
        formatted_compare_at_amount = self.formatted_compare_at_amount
        skus_count = self.skus_count
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
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if description is not UNSET:
            field_dict["description"] = description
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if do_not_ship is not UNSET:
            field_dict["do_not_ship"] = do_not_ship
        if do_not_track is not UNSET:
            field_dict["do_not_track"] = do_not_track
        if price_amount_cents is not UNSET:
            field_dict["price_amount_cents"] = price_amount_cents
        if price_amount_float is not UNSET:
            field_dict["price_amount_float"] = price_amount_float
        if formatted_price_amount is not UNSET:
            field_dict["formatted_price_amount"] = formatted_price_amount
        if compare_at_amount_cents is not UNSET:
            field_dict["compare_at_amount_cents"] = compare_at_amount_cents
        if compare_at_amount_float is not UNSET:
            field_dict["compare_at_amount_float"] = compare_at_amount_float
        if formatted_compare_at_amount is not UNSET:
            field_dict["formatted_compare_at_amount"] = formatted_compare_at_amount
        if skus_count is not UNSET:
            field_dict["skus_count"] = skus_count
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
        from ..models.bundle_data_attributes_metadata import BundleDataAttributesMetadata

        d = src_dict.copy()
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        description = d.pop("description", UNSET)

        image_url = d.pop("image_url", UNSET)

        do_not_ship = d.pop("do_not_ship", UNSET)

        do_not_track = d.pop("do_not_track", UNSET)

        price_amount_cents = d.pop("price_amount_cents", UNSET)

        price_amount_float = d.pop("price_amount_float", UNSET)

        formatted_price_amount = d.pop("formatted_price_amount", UNSET)

        compare_at_amount_cents = d.pop("compare_at_amount_cents", UNSET)

        compare_at_amount_float = d.pop("compare_at_amount_float", UNSET)

        formatted_compare_at_amount = d.pop("formatted_compare_at_amount", UNSET)

        skus_count = d.pop("skus_count", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, BundleDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = BundleDataAttributesMetadata.from_dict(_metadata)

        bundle_data_attributes = cls(
            code=code,
            name=name,
            currency_code=currency_code,
            description=description,
            image_url=image_url,
            do_not_ship=do_not_ship,
            do_not_track=do_not_track,
            price_amount_cents=price_amount_cents,
            price_amount_float=price_amount_float,
            formatted_price_amount=formatted_price_amount,
            compare_at_amount_cents=compare_at_amount_cents,
            compare_at_amount_float=compare_at_amount_float,
            formatted_compare_at_amount=formatted_compare_at_amount,
            skus_count=skus_count,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        bundle_data_attributes.additional_properties = d
        return bundle_data_attributes

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
