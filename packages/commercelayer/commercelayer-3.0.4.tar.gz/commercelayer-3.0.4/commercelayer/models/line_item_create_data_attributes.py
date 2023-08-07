from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_item_create_data_attributes_metadata import LineItemCreateDataAttributesMetadata


T = TypeVar("T", bound="LineItemCreateDataAttributes")


@attr.s(auto_attribs=True)
class LineItemCreateDataAttributes:
    """
    Attributes:
        quantity (int): The line item quantity. Example: 4.
        sku_code (Union[Unset, str]): The code of the associated SKU. Example: TSHIRTMM000000FFFFFFXLXX.
        bundle_code (Union[Unset, str]): The code of the associated bundle. Example: BUNDLEMM000000FFFFFFXLXX.
        external_price (Union[Unset, bool]): When creating or updating a new line item, set this attribute to '1' if you
            want to inject the unit_amount_cents price from an external source. Example: True.
        update_quantity (Union[Unset, bool]): When creating a new line item, set this attribute to '1' if you want to
            update the line item quantity (if present) instead of creating a new line item for the same SKU. Example: True.
        unit_amount_cents (Union[Unset, int]): The unit amount of the line item, in cents. Can be specified without an
            item, otherwise is automatically populated from the price list associated to the order's market. Example: 9900.
        name (Union[Unset, str]): The name of the line item. When blank, it gets populated with the name of the
            associated item (if present). Example: Black Men T-shirt with White Logo (XL).
        image_url (Union[Unset, str]): The image_url of the line item. When blank, it gets populated with the image_url
            of the associated item (if present, SKU only). Example: https://img.yourdomain.com/skus/xYZkjABcde.png.
        item_type (Union[Unset, str]): The type of the associate item. Can be one of 'sku', 'bundle', 'shipment',
            'payment_method', 'adjustment', 'gift_card', or a valid promotion type. Example: sku.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, LineItemCreateDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    quantity: int
    sku_code: Union[Unset, str] = UNSET
    bundle_code: Union[Unset, str] = UNSET
    external_price: Union[Unset, bool] = UNSET
    update_quantity: Union[Unset, bool] = UNSET
    unit_amount_cents: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    item_type: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "LineItemCreateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity
        sku_code = self.sku_code
        bundle_code = self.bundle_code
        external_price = self.external_price
        update_quantity = self.update_quantity
        unit_amount_cents = self.unit_amount_cents
        name = self.name
        image_url = self.image_url
        item_type = self.item_type
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
            }
        )
        if sku_code is not UNSET:
            field_dict["sku_code"] = sku_code
        if bundle_code is not UNSET:
            field_dict["bundle_code"] = bundle_code
        if external_price is not UNSET:
            field_dict["_external_price"] = external_price
        if update_quantity is not UNSET:
            field_dict["_update_quantity"] = update_quantity
        if unit_amount_cents is not UNSET:
            field_dict["unit_amount_cents"] = unit_amount_cents
        if name is not UNSET:
            field_dict["name"] = name
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.line_item_create_data_attributes_metadata import LineItemCreateDataAttributesMetadata

        d = src_dict.copy()
        quantity = d.pop("quantity")

        sku_code = d.pop("sku_code", UNSET)

        bundle_code = d.pop("bundle_code", UNSET)

        external_price = d.pop("_external_price", UNSET)

        update_quantity = d.pop("_update_quantity", UNSET)

        unit_amount_cents = d.pop("unit_amount_cents", UNSET)

        name = d.pop("name", UNSET)

        image_url = d.pop("image_url", UNSET)

        item_type = d.pop("item_type", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, LineItemCreateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = LineItemCreateDataAttributesMetadata.from_dict(_metadata)

        line_item_create_data_attributes = cls(
            quantity=quantity,
            sku_code=sku_code,
            bundle_code=bundle_code,
            external_price=external_price,
            update_quantity=update_quantity,
            unit_amount_cents=unit_amount_cents,
            name=name,
            image_url=image_url,
            item_type=item_type,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        line_item_create_data_attributes.additional_properties = d
        return line_item_create_data_attributes

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
