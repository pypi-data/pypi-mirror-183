from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tparcel_line_items_response_200_data_item_attributes_metadata import (
        GETparcelLineItemsResponse200DataItemAttributesMetadata,
    )


T = TypeVar("T", bound="GETparcelLineItemsResponse200DataItemAttributes")


@attr.s(auto_attribs=True)
class GETparcelLineItemsResponse200DataItemAttributes:
    """
    Attributes:
        sku_code (Union[Unset, str]): The code of the SKU of the associated shipment_line_item. Example:
            TSHIRTMM000000FFFFFFXLXX.
        quantity (Union[Unset, int]): The parcel line item quantity. Example: 4.
        name (Union[Unset, str]): The internal name of the associated line item. Example: Black Men T-shirt with White
            Logo (XL).
        image_url (Union[Unset, str]): The image_url of the associated line item. Example:
            https://img.yourdomain.com/skus/xYZkjABcde.png.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETparcelLineItemsResponse200DataItemAttributesMetadata]): Set of key-value pairs that
            you can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    sku_code: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETparcelLineItemsResponse200DataItemAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku_code = self.sku_code
        quantity = self.quantity
        name = self.name
        image_url = self.image_url
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
        if sku_code is not UNSET:
            field_dict["sku_code"] = sku_code
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if name is not UNSET:
            field_dict["name"] = name
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
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
        from ..models.ge_tparcel_line_items_response_200_data_item_attributes_metadata import (
            GETparcelLineItemsResponse200DataItemAttributesMetadata,
        )

        d = src_dict.copy()
        sku_code = d.pop("sku_code", UNSET)

        quantity = d.pop("quantity", UNSET)

        name = d.pop("name", UNSET)

        image_url = d.pop("image_url", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETparcelLineItemsResponse200DataItemAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETparcelLineItemsResponse200DataItemAttributesMetadata.from_dict(_metadata)

        ge_tparcel_line_items_response_200_data_item_attributes = cls(
            sku_code=sku_code,
            quantity=quantity,
            name=name,
            image_url=image_url,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_tparcel_line_items_response_200_data_item_attributes.additional_properties = d
        return ge_tparcel_line_items_response_200_data_item_attributes

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
