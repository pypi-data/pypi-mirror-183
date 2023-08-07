from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_subscription_data_attributes_metadata import OrderSubscriptionDataAttributesMetadata
    from ..models.order_subscription_data_attributes_options import OrderSubscriptionDataAttributesOptions


T = TypeVar("T", bound="OrderSubscriptionDataAttributes")


@attr.s(auto_attribs=True)
class OrderSubscriptionDataAttributes:
    """
    Attributes:
        number (Union[Unset, str]): Unique identifier for the subscription (numeric) Example: 1234.
        status (Union[Unset, str]): The subscription status. One of 'draft' (default), 'inactive', 'active', or
            'cancelled'. Example: draft.
        frequency (Union[Unset, str]): The frequency of the subscription. One of 'hourly', 'daily', 'weekly', 'monthly',
            'two-month', 'three-month', 'four-month', 'six-month', or 'yearly'. Example: monthly.
        activate_by_source_order (Union[Unset, bool]): Indicates if the subscription will be activated considering the
            placed source order as its first run, default to true. Example: True.
        customer_email (Union[Unset, str]): The email address of the customer, if any, associated to the source order.
            Example: john@example.com.
        starts_at (Union[Unset, str]): The activation date/time of this subscription. Example: 2018-01-01T12:00:00.000Z.
        expires_at (Union[Unset, str]): The expiration date/time of this subscription (must be after starts_at).
            Example: 2018-01-02T12:00:00.000Z.
        next_run_at (Union[Unset, str]): The date/time of the subscription next run. Example: 2018-01-01T12:00:00.000Z.
        occurrencies (Union[Unset, int]): The number of times this subscription has run. Example: 2.
        errors_count (Union[Unset, int]): Indicates the number of subscription errors, if any. Example: 3.
        succeeded_on_last_run (Union[Unset, bool]): Indicates if the subscription has succeeded on its last run.
            Example: True.
        options (Union[Unset, OrderSubscriptionDataAttributesOptions]): The subscription options used to create the
            order copy (check order_copies for more information). For subscriptions the `place_target_order` is enabled by
            default, specify custom options to overwrite it. Example: {'place_target_order': False}.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, OrderSubscriptionDataAttributesMetadata]): Set of key-value pairs that you can attach to
            the resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    number: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    frequency: Union[Unset, str] = UNSET
    activate_by_source_order: Union[Unset, bool] = UNSET
    customer_email: Union[Unset, str] = UNSET
    starts_at: Union[Unset, str] = UNSET
    expires_at: Union[Unset, str] = UNSET
    next_run_at: Union[Unset, str] = UNSET
    occurrencies: Union[Unset, int] = UNSET
    errors_count: Union[Unset, int] = UNSET
    succeeded_on_last_run: Union[Unset, bool] = UNSET
    options: Union[Unset, "OrderSubscriptionDataAttributesOptions"] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "OrderSubscriptionDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        status = self.status
        frequency = self.frequency
        activate_by_source_order = self.activate_by_source_order
        customer_email = self.customer_email
        starts_at = self.starts_at
        expires_at = self.expires_at
        next_run_at = self.next_run_at
        occurrencies = self.occurrencies
        errors_count = self.errors_count
        succeeded_on_last_run = self.succeeded_on_last_run
        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

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
        if status is not UNSET:
            field_dict["status"] = status
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if activate_by_source_order is not UNSET:
            field_dict["activate_by_source_order"] = activate_by_source_order
        if customer_email is not UNSET:
            field_dict["customer_email"] = customer_email
        if starts_at is not UNSET:
            field_dict["starts_at"] = starts_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if next_run_at is not UNSET:
            field_dict["next_run_at"] = next_run_at
        if occurrencies is not UNSET:
            field_dict["occurrencies"] = occurrencies
        if errors_count is not UNSET:
            field_dict["errors_count"] = errors_count
        if succeeded_on_last_run is not UNSET:
            field_dict["succeeded_on_last_run"] = succeeded_on_last_run
        if options is not UNSET:
            field_dict["options"] = options
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
        from ..models.order_subscription_data_attributes_metadata import OrderSubscriptionDataAttributesMetadata
        from ..models.order_subscription_data_attributes_options import OrderSubscriptionDataAttributesOptions

        d = src_dict.copy()
        number = d.pop("number", UNSET)

        status = d.pop("status", UNSET)

        frequency = d.pop("frequency", UNSET)

        activate_by_source_order = d.pop("activate_by_source_order", UNSET)

        customer_email = d.pop("customer_email", UNSET)

        starts_at = d.pop("starts_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        next_run_at = d.pop("next_run_at", UNSET)

        occurrencies = d.pop("occurrencies", UNSET)

        errors_count = d.pop("errors_count", UNSET)

        succeeded_on_last_run = d.pop("succeeded_on_last_run", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, OrderSubscriptionDataAttributesOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = OrderSubscriptionDataAttributesOptions.from_dict(_options)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OrderSubscriptionDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OrderSubscriptionDataAttributesMetadata.from_dict(_metadata)

        order_subscription_data_attributes = cls(
            number=number,
            status=status,
            frequency=frequency,
            activate_by_source_order=activate_by_source_order,
            customer_email=customer_email,
            starts_at=starts_at,
            expires_at=expires_at,
            next_run_at=next_run_at,
            occurrencies=occurrencies,
            errors_count=errors_count,
            succeeded_on_last_run=succeeded_on_last_run,
            options=options,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        order_subscription_data_attributes.additional_properties = d
        return order_subscription_data_attributes

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
