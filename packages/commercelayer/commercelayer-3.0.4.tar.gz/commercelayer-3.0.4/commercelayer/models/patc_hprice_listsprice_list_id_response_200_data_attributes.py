from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hprice_listsprice_list_id_response_200_data_attributes_metadata import (
        PATCHpriceListspriceListIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="PATCHpriceListspriceListIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHpriceListspriceListIdResponse200DataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The price list's internal name Example: EU Price list.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard.
            Example: EUR.
        tax_included (Union[Unset, bool]): Indicates if the associated prices include taxes. Example: True.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHpriceListspriceListIdResponse200DataAttributesMetadata]): Set of key-value pairs
            that you can attach to the resource. This can be useful for storing additional information about the resource in
            a structured format. Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    tax_included: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHpriceListspriceListIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        currency_code = self.currency_code
        tax_included = self.tax_included
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if tax_included is not UNSET:
            field_dict["tax_included"] = tax_included
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hprice_listsprice_list_id_response_200_data_attributes_metadata import (
            PATCHpriceListspriceListIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        tax_included = d.pop("tax_included", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHpriceListspriceListIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHpriceListspriceListIdResponse200DataAttributesMetadata.from_dict(_metadata)

        patc_hprice_listsprice_list_id_response_200_data_attributes = cls(
            name=name,
            currency_code=currency_code,
            tax_included=tax_included,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        patc_hprice_listsprice_list_id_response_200_data_attributes.additional_properties = d
        return patc_hprice_listsprice_list_id_response_200_data_attributes

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
