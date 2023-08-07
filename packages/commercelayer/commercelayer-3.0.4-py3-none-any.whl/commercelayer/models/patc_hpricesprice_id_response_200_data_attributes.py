from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hpricesprice_id_response_200_data_attributes_metadata import (
        PATCHpricespriceIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="PATCHpricespriceIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHpricespriceIdResponse200DataAttributes:
    """
    Attributes:
        sku_code (Union[Unset, str]): The code of the associated SKU. When creating a price, either a valid sku_code or
            a SKU relationship must be present. Example: TSHIRTMM000000FFFFFFXLXX.
        amount_cents (Union[Unset, int]): The SKU price amount for the associated price list, in cents. Example: 10000.
        compare_at_amount_cents (Union[Unset, int]): The compared price amount, in cents. Useful to display a percentage
            discount. Example: 13000.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHpricespriceIdResponse200DataAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    sku_code: Union[Unset, str] = UNSET
    amount_cents: Union[Unset, int] = UNSET
    compare_at_amount_cents: Union[Unset, int] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHpricespriceIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku_code = self.sku_code
        amount_cents = self.amount_cents
        compare_at_amount_cents = self.compare_at_amount_cents
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
        if amount_cents is not UNSET:
            field_dict["amount_cents"] = amount_cents
        if compare_at_amount_cents is not UNSET:
            field_dict["compare_at_amount_cents"] = compare_at_amount_cents
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hpricesprice_id_response_200_data_attributes_metadata import (
            PATCHpricespriceIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        sku_code = d.pop("sku_code", UNSET)

        amount_cents = d.pop("amount_cents", UNSET)

        compare_at_amount_cents = d.pop("compare_at_amount_cents", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHpricespriceIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHpricespriceIdResponse200DataAttributesMetadata.from_dict(_metadata)

        patc_hpricesprice_id_response_200_data_attributes = cls(
            sku_code=sku_code,
            amount_cents=amount_cents,
            compare_at_amount_cents=compare_at_amount_cents,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        patc_hpricesprice_id_response_200_data_attributes.additional_properties = d
        return patc_hpricesprice_id_response_200_data_attributes

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
