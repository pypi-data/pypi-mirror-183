from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_subscription_create_data_attributes_metadata import (
        OrderSubscriptionCreateDataAttributesMetadata,
    )
    from ..models.order_subscription_create_data_attributes_options import OrderSubscriptionCreateDataAttributesOptions


T = TypeVar("T", bound="OrderSubscriptionCreateDataAttributes")


@attr.s(auto_attribs=True)
class OrderSubscriptionCreateDataAttributes:
    """
    Attributes:
        frequency (str): The frequency of the subscription. One of 'hourly', 'daily', 'weekly', 'monthly', 'two-month',
            'three-month', 'four-month', 'six-month', or 'yearly'. Example: monthly.
        activate_by_source_order (Union[Unset, bool]): Indicates if the subscription will be activated considering the
            placed source order as its first run, default to true. Example: True.
        starts_at (Union[Unset, str]): The activation date/time of this subscription. Example: 2018-01-01T12:00:00.000Z.
        expires_at (Union[Unset, str]): The expiration date/time of this subscription (must be after starts_at).
            Example: 2018-01-02T12:00:00.000Z.
        options (Union[Unset, OrderSubscriptionCreateDataAttributesOptions]): The subscription options used to create
            the order copy (check order_copies for more information). For subscriptions the `place_target_order` is enabled
            by default, specify custom options to overwrite it. Example: {'place_target_order': False}.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, OrderSubscriptionCreateDataAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    frequency: str
    activate_by_source_order: Union[Unset, bool] = UNSET
    starts_at: Union[Unset, str] = UNSET
    expires_at: Union[Unset, str] = UNSET
    options: Union[Unset, "OrderSubscriptionCreateDataAttributesOptions"] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "OrderSubscriptionCreateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        frequency = self.frequency
        activate_by_source_order = self.activate_by_source_order
        starts_at = self.starts_at
        expires_at = self.expires_at
        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "frequency": frequency,
            }
        )
        if activate_by_source_order is not UNSET:
            field_dict["activate_by_source_order"] = activate_by_source_order
        if starts_at is not UNSET:
            field_dict["starts_at"] = starts_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if options is not UNSET:
            field_dict["options"] = options
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_subscription_create_data_attributes_metadata import (
            OrderSubscriptionCreateDataAttributesMetadata,
        )
        from ..models.order_subscription_create_data_attributes_options import (
            OrderSubscriptionCreateDataAttributesOptions,
        )

        d = src_dict.copy()
        frequency = d.pop("frequency")

        activate_by_source_order = d.pop("activate_by_source_order", UNSET)

        starts_at = d.pop("starts_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, OrderSubscriptionCreateDataAttributesOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = OrderSubscriptionCreateDataAttributesOptions.from_dict(_options)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OrderSubscriptionCreateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OrderSubscriptionCreateDataAttributesMetadata.from_dict(_metadata)

        order_subscription_create_data_attributes = cls(
            frequency=frequency,
            activate_by_source_order=activate_by_source_order,
            starts_at=starts_at,
            expires_at=expires_at,
            options=options,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        order_subscription_create_data_attributes.additional_properties = d
        return order_subscription_create_data_attributes

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
