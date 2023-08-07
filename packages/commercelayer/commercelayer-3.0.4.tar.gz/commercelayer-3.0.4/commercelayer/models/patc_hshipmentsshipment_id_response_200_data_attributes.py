from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hshipmentsshipment_id_response_200_data_attributes_metadata import (
        PATCHshipmentsshipmentIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="PATCHshipmentsshipmentIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHshipmentsshipmentIdResponse200DataAttributes:
    """
    Attributes:
        on_hold (Union[Unset, bool]): Send this attribute if you want to put this shipment on hold. Example: True.
        picking (Union[Unset, bool]): Send this attribute if you want to start picking this shipment. Example: True.
        packing (Union[Unset, bool]): Send this attribute if you want to start packing this shipment. Example: True.
        ready_to_ship (Union[Unset, bool]): Send this attribute if you want to mark this shipment as ready to ship.
            Example: True.
        ship (Union[Unset, bool]): Send this attribute if you want to mark this shipment as shipped. Example: True.
        get_rates (Union[Unset, bool]): Send this attribute if you want get the shipping rates from the associated
            carrier accounts. Example: True.
        selected_rate_id (Union[Unset, str]): The selected purchase rate from the available shipping rates. Example:
            rate_f89e4663c3ed47ee94d37763f6d21d54.
        purchase (Union[Unset, bool]): Send this attribute if you want to purchase this shipment with the selected rate.
            Example: True.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHshipmentsshipmentIdResponse200DataAttributesMetadata]): Set of key-value pairs that
            you can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    on_hold: Union[Unset, bool] = UNSET
    picking: Union[Unset, bool] = UNSET
    packing: Union[Unset, bool] = UNSET
    ready_to_ship: Union[Unset, bool] = UNSET
    ship: Union[Unset, bool] = UNSET
    get_rates: Union[Unset, bool] = UNSET
    selected_rate_id: Union[Unset, str] = UNSET
    purchase: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        on_hold = self.on_hold
        picking = self.picking
        packing = self.packing
        ready_to_ship = self.ready_to_ship
        ship = self.ship
        get_rates = self.get_rates
        selected_rate_id = self.selected_rate_id
        purchase = self.purchase
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if on_hold is not UNSET:
            field_dict["_on_hold"] = on_hold
        if picking is not UNSET:
            field_dict["_picking"] = picking
        if packing is not UNSET:
            field_dict["_packing"] = packing
        if ready_to_ship is not UNSET:
            field_dict["_ready_to_ship"] = ready_to_ship
        if ship is not UNSET:
            field_dict["_ship"] = ship
        if get_rates is not UNSET:
            field_dict["_get_rates"] = get_rates
        if selected_rate_id is not UNSET:
            field_dict["selected_rate_id"] = selected_rate_id
        if purchase is not UNSET:
            field_dict["_purchase"] = purchase
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hshipmentsshipment_id_response_200_data_attributes_metadata import (
            PATCHshipmentsshipmentIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        on_hold = d.pop("_on_hold", UNSET)

        picking = d.pop("_picking", UNSET)

        packing = d.pop("_packing", UNSET)

        ready_to_ship = d.pop("_ready_to_ship", UNSET)

        ship = d.pop("_ship", UNSET)

        get_rates = d.pop("_get_rates", UNSET)

        selected_rate_id = d.pop("selected_rate_id", UNSET)

        purchase = d.pop("_purchase", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHshipmentsshipmentIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHshipmentsshipmentIdResponse200DataAttributesMetadata.from_dict(_metadata)

        patc_hshipmentsshipment_id_response_200_data_attributes = cls(
            on_hold=on_hold,
            picking=picking,
            packing=packing,
            ready_to_ship=ready_to_ship,
            ship=ship,
            get_rates=get_rates,
            selected_rate_id=selected_rate_id,
            purchase=purchase,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        patc_hshipmentsshipment_id_response_200_data_attributes.additional_properties = d
        return patc_hshipmentsshipment_id_response_200_data_attributes

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
