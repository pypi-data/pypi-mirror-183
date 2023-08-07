from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tshipmentsshipment_id_response_200_data_attributes_get_rates_errors_item import (
        GETshipmentsshipmentIdResponse200DataAttributesGetRatesErrorsItem,
    )
    from ..models.ge_tshipmentsshipment_id_response_200_data_attributes_metadata import (
        GETshipmentsshipmentIdResponse200DataAttributesMetadata,
    )
    from ..models.ge_tshipmentsshipment_id_response_200_data_attributes_rates_item import (
        GETshipmentsshipmentIdResponse200DataAttributesRatesItem,
    )


T = TypeVar("T", bound="GETshipmentsshipmentIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class GETshipmentsshipmentIdResponse200DataAttributes:
    """
    Attributes:
        number (Union[Unset, str]): Unique identifier for the shipment Example: #1234/S/001.
        status (Union[Unset, str]): The shipment status, one of 'draft', 'upcoming', 'cancelled', 'on_hold', 'picking',
            'packing', 'ready_to_ship', or 'shipped' Example: draft.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard,
            automatically inherited from the associated order. Example: EUR.
        cost_amount_cents (Union[Unset, int]): The cost of this shipment from the selected carrier account, in cents.
            Example: 1000.
        cost_amount_float (Union[Unset, float]): The cost of this shipment from the selected carrier account, float.
            Example: 10.0.
        formatted_cost_amount (Union[Unset, str]): The cost of this shipment from the selected carrier account,
            formatted. Example: €10,00.
        skus_count (Union[Unset, int]): The total number of SKUs in the shipment's line items. This can be useful to
            display a preview of the shipment content. Example: 2.
        selected_rate_id (Union[Unset, str]): The selected purchase rate from the available shipping rates. Example:
            rate_f89e4663c3ed47ee94d37763f6d21d54.
        rates (Union[Unset, List['GETshipmentsshipmentIdResponse200DataAttributesRatesItem']]): The available shipping
            rates. Example: [{'id': 'rate_f89e4663c3ed47ee94d37763f6d21d54', 'rate': '45.59', 'carrier': 'DHLExpress',
            'service': 'MedicalExpress'}].
        purchase_error_code (Union[Unset, str]): The shipping rate purchase error code, if any. Example:
            SHIPMENT.POSTAGE.FAILURE.
        purchase_error_message (Union[Unset, str]): The shipping rate purchase error message, if any. Example: Account
            not allowed for this service..
        get_rates_errors (Union[Unset, List['GETshipmentsshipmentIdResponse200DataAttributesGetRatesErrorsItem']]): Any
            errors collected when fetching shipping rates. Example: [{'carrier': 'DHLExpress', 'message':
            'to_address.postal_code: Shorter than minimum length 3', 'type': 'rate_error'}].
        get_rates_started_at (Union[Unset, str]): Time at which the getting of the shipping rates started. Example:
            2018-01-01T12:00:00.000Z.
        get_rates_completed_at (Union[Unset, str]): Time at which the getting of the shipping rates completed. Example:
            2018-01-01T12:00:00.000Z.
        purchase_started_at (Union[Unset, str]): Time at which the purchasing of the shipping rate started. Example:
            2018-01-01T12:00:00.000Z.
        purchase_completed_at (Union[Unset, str]): Time at which the purchasing of the shipping rate completed. Example:
            2018-01-01T12:00:00.000Z.
        purchase_failed_at (Union[Unset, str]): Time at which the purchasing of the shipping rate failed. Example:
            2018-01-01T12:00:00.000Z.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETshipmentsshipmentIdResponse200DataAttributesMetadata]): Set of key-value pairs that
            you can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    number: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    cost_amount_cents: Union[Unset, int] = UNSET
    cost_amount_float: Union[Unset, float] = UNSET
    formatted_cost_amount: Union[Unset, str] = UNSET
    skus_count: Union[Unset, int] = UNSET
    selected_rate_id: Union[Unset, str] = UNSET
    rates: Union[Unset, List["GETshipmentsshipmentIdResponse200DataAttributesRatesItem"]] = UNSET
    purchase_error_code: Union[Unset, str] = UNSET
    purchase_error_message: Union[Unset, str] = UNSET
    get_rates_errors: Union[Unset, List["GETshipmentsshipmentIdResponse200DataAttributesGetRatesErrorsItem"]] = UNSET
    get_rates_started_at: Union[Unset, str] = UNSET
    get_rates_completed_at: Union[Unset, str] = UNSET
    purchase_started_at: Union[Unset, str] = UNSET
    purchase_completed_at: Union[Unset, str] = UNSET
    purchase_failed_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETshipmentsshipmentIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        status = self.status
        currency_code = self.currency_code
        cost_amount_cents = self.cost_amount_cents
        cost_amount_float = self.cost_amount_float
        formatted_cost_amount = self.formatted_cost_amount
        skus_count = self.skus_count
        selected_rate_id = self.selected_rate_id
        rates: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rates, Unset):
            rates = []
            for rates_item_data in self.rates:
                rates_item = rates_item_data.to_dict()

                rates.append(rates_item)

        purchase_error_code = self.purchase_error_code
        purchase_error_message = self.purchase_error_message
        get_rates_errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.get_rates_errors, Unset):
            get_rates_errors = []
            for get_rates_errors_item_data in self.get_rates_errors:
                get_rates_errors_item = get_rates_errors_item_data.to_dict()

                get_rates_errors.append(get_rates_errors_item)

        get_rates_started_at = self.get_rates_started_at
        get_rates_completed_at = self.get_rates_completed_at
        purchase_started_at = self.purchase_started_at
        purchase_completed_at = self.purchase_completed_at
        purchase_failed_at = self.purchase_failed_at
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
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if cost_amount_cents is not UNSET:
            field_dict["cost_amount_cents"] = cost_amount_cents
        if cost_amount_float is not UNSET:
            field_dict["cost_amount_float"] = cost_amount_float
        if formatted_cost_amount is not UNSET:
            field_dict["formatted_cost_amount"] = formatted_cost_amount
        if skus_count is not UNSET:
            field_dict["skus_count"] = skus_count
        if selected_rate_id is not UNSET:
            field_dict["selected_rate_id"] = selected_rate_id
        if rates is not UNSET:
            field_dict["rates"] = rates
        if purchase_error_code is not UNSET:
            field_dict["purchase_error_code"] = purchase_error_code
        if purchase_error_message is not UNSET:
            field_dict["purchase_error_message"] = purchase_error_message
        if get_rates_errors is not UNSET:
            field_dict["get_rates_errors"] = get_rates_errors
        if get_rates_started_at is not UNSET:
            field_dict["get_rates_started_at"] = get_rates_started_at
        if get_rates_completed_at is not UNSET:
            field_dict["get_rates_completed_at"] = get_rates_completed_at
        if purchase_started_at is not UNSET:
            field_dict["purchase_started_at"] = purchase_started_at
        if purchase_completed_at is not UNSET:
            field_dict["purchase_completed_at"] = purchase_completed_at
        if purchase_failed_at is not UNSET:
            field_dict["purchase_failed_at"] = purchase_failed_at
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
        from ..models.ge_tshipmentsshipment_id_response_200_data_attributes_get_rates_errors_item import (
            GETshipmentsshipmentIdResponse200DataAttributesGetRatesErrorsItem,
        )
        from ..models.ge_tshipmentsshipment_id_response_200_data_attributes_metadata import (
            GETshipmentsshipmentIdResponse200DataAttributesMetadata,
        )
        from ..models.ge_tshipmentsshipment_id_response_200_data_attributes_rates_item import (
            GETshipmentsshipmentIdResponse200DataAttributesRatesItem,
        )

        d = src_dict.copy()
        number = d.pop("number", UNSET)

        status = d.pop("status", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        cost_amount_cents = d.pop("cost_amount_cents", UNSET)

        cost_amount_float = d.pop("cost_amount_float", UNSET)

        formatted_cost_amount = d.pop("formatted_cost_amount", UNSET)

        skus_count = d.pop("skus_count", UNSET)

        selected_rate_id = d.pop("selected_rate_id", UNSET)

        rates = []
        _rates = d.pop("rates", UNSET)
        for rates_item_data in _rates or []:
            rates_item = GETshipmentsshipmentIdResponse200DataAttributesRatesItem.from_dict(rates_item_data)

            rates.append(rates_item)

        purchase_error_code = d.pop("purchase_error_code", UNSET)

        purchase_error_message = d.pop("purchase_error_message", UNSET)

        get_rates_errors = []
        _get_rates_errors = d.pop("get_rates_errors", UNSET)
        for get_rates_errors_item_data in _get_rates_errors or []:
            get_rates_errors_item = GETshipmentsshipmentIdResponse200DataAttributesGetRatesErrorsItem.from_dict(
                get_rates_errors_item_data
            )

            get_rates_errors.append(get_rates_errors_item)

        get_rates_started_at = d.pop("get_rates_started_at", UNSET)

        get_rates_completed_at = d.pop("get_rates_completed_at", UNSET)

        purchase_started_at = d.pop("purchase_started_at", UNSET)

        purchase_completed_at = d.pop("purchase_completed_at", UNSET)

        purchase_failed_at = d.pop("purchase_failed_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETshipmentsshipmentIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETshipmentsshipmentIdResponse200DataAttributesMetadata.from_dict(_metadata)

        ge_tshipmentsshipment_id_response_200_data_attributes = cls(
            number=number,
            status=status,
            currency_code=currency_code,
            cost_amount_cents=cost_amount_cents,
            cost_amount_float=cost_amount_float,
            formatted_cost_amount=formatted_cost_amount,
            skus_count=skus_count,
            selected_rate_id=selected_rate_id,
            rates=rates,
            purchase_error_code=purchase_error_code,
            purchase_error_message=purchase_error_message,
            get_rates_errors=get_rates_errors,
            get_rates_started_at=get_rates_started_at,
            get_rates_completed_at=get_rates_completed_at,
            purchase_started_at=purchase_started_at,
            purchase_completed_at=purchase_completed_at,
            purchase_failed_at=purchase_failed_at,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_tshipmentsshipment_id_response_200_data_attributes.additional_properties = d
        return ge_tshipmentsshipment_id_response_200_data_attributes

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
