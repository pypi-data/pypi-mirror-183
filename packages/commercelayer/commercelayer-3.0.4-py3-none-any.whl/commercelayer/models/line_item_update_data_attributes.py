from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_item_update_data_attributes_metadata import LineItemUpdateDataAttributesMetadata


T = TypeVar("T", bound="LineItemUpdateDataAttributes")


@attr.s(auto_attribs=True)
class LineItemUpdateDataAttributes:
    """
    Attributes:
        sku_code (Union[Unset, str]): The code of the associated SKU. Example: TSHIRTMM000000FFFFFFXLXX.
        bundle_code (Union[Unset, str]): The code of the associated bundle. Example: BUNDLEMM000000FFFFFFXLXX.
        quantity (Union[Unset, int]): The line item quantity. Example: 4.
        external_price (Union[Unset, bool]): When creating or updating a new line item, set this attribute to '1' if you
            want to inject the unit_amount_cents price from an external source. Example: True.
        name (Union[Unset, str]): The name of the line item. When blank, it gets populated with the name of the
            associated item (if present). Example: Black Men T-shirt with White Logo (XL).
        image_url (Union[Unset, str]): The image_url of the line item. When blank, it gets populated with the image_url
            of the associated item (if present, SKU only). Example: https://img.yourdomain.com/skus/xYZkjABcde.png.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, LineItemUpdateDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    sku_code: Union[Unset, str] = UNSET
    bundle_code: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    external_price: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "LineItemUpdateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku_code = self.sku_code
        bundle_code = self.bundle_code
        quantity = self.quantity
        external_price = self.external_price
        name = self.name
        image_url = self.image_url
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku_code is not UNSET:
            field_dict["sku_code"] = sku_code
        if bundle_code is not UNSET:
            field_dict["bundle_code"] = bundle_code
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if external_price is not UNSET:
            field_dict["_external_price"] = external_price
        if name is not UNSET:
            field_dict["name"] = name
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.line_item_update_data_attributes_metadata import LineItemUpdateDataAttributesMetadata

        d = src_dict.copy()
        sku_code = d.pop("sku_code", UNSET)

        bundle_code = d.pop("bundle_code", UNSET)

        quantity = d.pop("quantity", UNSET)

        external_price = d.pop("_external_price", UNSET)

        name = d.pop("name", UNSET)

        image_url = d.pop("image_url", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, LineItemUpdateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = LineItemUpdateDataAttributesMetadata.from_dict(_metadata)

        line_item_update_data_attributes = cls(
            sku_code=sku_code,
            bundle_code=bundle_code,
            quantity=quantity,
            external_price=external_price,
            name=name,
            image_url=image_url,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        line_item_update_data_attributes.additional_properties = d
        return line_item_update_data_attributes

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
