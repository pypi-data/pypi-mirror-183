from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.in_stock_subscription_data_attributes_metadata import InStockSubscriptionDataAttributesMetadata


T = TypeVar("T", bound="InStockSubscriptionDataAttributes")


@attr.s(auto_attribs=True)
class InStockSubscriptionDataAttributes:
    """
    Attributes:
        status (Union[Unset, str]): The subscription status. One of 'active' (default), 'inactive', or 'notified'
            Example: active.
        customer_email (Union[Unset, str]): The email of the associated customer, replace the relationship Example:
            john@example.com.
        sku_code (Union[Unset, str]): The code of the associated SKU, replace the relationship Example:
            TSHIRTMM000000FFFFFFXLXX.
        stock_threshold (Union[Unset, int]): The threshold at which to trigger the back in stock notification, default
            to 1. Example: 3.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, InStockSubscriptionDataAttributesMetadata]): Set of key-value pairs that you can attach
            to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    status: Union[Unset, str] = UNSET
    customer_email: Union[Unset, str] = UNSET
    sku_code: Union[Unset, str] = UNSET
    stock_threshold: Union[Unset, int] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "InStockSubscriptionDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        customer_email = self.customer_email
        sku_code = self.sku_code
        stock_threshold = self.stock_threshold
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
        if status is not UNSET:
            field_dict["status"] = status
        if customer_email is not UNSET:
            field_dict["customer_email"] = customer_email
        if sku_code is not UNSET:
            field_dict["sku_code"] = sku_code
        if stock_threshold is not UNSET:
            field_dict["stock_threshold"] = stock_threshold
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
        from ..models.in_stock_subscription_data_attributes_metadata import InStockSubscriptionDataAttributesMetadata

        d = src_dict.copy()
        status = d.pop("status", UNSET)

        customer_email = d.pop("customer_email", UNSET)

        sku_code = d.pop("sku_code", UNSET)

        stock_threshold = d.pop("stock_threshold", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, InStockSubscriptionDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = InStockSubscriptionDataAttributesMetadata.from_dict(_metadata)

        in_stock_subscription_data_attributes = cls(
            status=status,
            customer_email=customer_email,
            sku_code=sku_code,
            stock_threshold=stock_threshold,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        in_stock_subscription_data_attributes.additional_properties = d
        return in_stock_subscription_data_attributes

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
