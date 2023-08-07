from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hbundlesbundle_id_response_200_data_attributes_metadata import (
        PATCHbundlesbundleIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="PATCHbundlesbundleIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHbundlesbundleIdResponse200DataAttributes:
    """
    Attributes:
        code (Union[Unset, str]): The bundle code, that uniquely identifies the bundle within the market. Example:
            BUNDMM000000FFFFFFXLXX.
        name (Union[Unset, str]): The internal name of the bundle. Example: Black Men T-shirt (XL) with Black Cap and
            Socks, all with White Logo.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard.
            Example: EUR.
        description (Union[Unset, str]): An internal description of the bundle. Example: Lorem ipsum dolor sit amet,
            consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua..
        image_url (Union[Unset, str]): The URL of an image that represents the bundle. Example:
            https://img.yourdomain.com/bundles/xYZkjABcde.png.
        price_amount_cents (Union[Unset, int]): The bundle price amount for the associated market, in cents. Example:
            10000.
        compare_at_amount_cents (Union[Unset, int]): The compared price amount, in cents. Useful to display a percentage
            discount. Example: 13000.
        compute_price_amount (Union[Unset, bool]): Send this attribute if you want to compute the price_amount_cents as
            the sum of the prices of the bundle SKUs for the market. Example: True.
        compute_compare_at_amount (Union[Unset, bool]): Send this attribute if you want to compute the
            compare_at_amount_cents as the sum of the prices of the bundle SKUs for the market. Example: True.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHbundlesbundleIdResponse200DataAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    price_amount_cents: Union[Unset, int] = UNSET
    compare_at_amount_cents: Union[Unset, int] = UNSET
    compute_price_amount: Union[Unset, bool] = UNSET
    compute_compare_at_amount: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHbundlesbundleIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        name = self.name
        currency_code = self.currency_code
        description = self.description
        image_url = self.image_url
        price_amount_cents = self.price_amount_cents
        compare_at_amount_cents = self.compare_at_amount_cents
        compute_price_amount = self.compute_price_amount
        compute_compare_at_amount = self.compute_compare_at_amount
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if description is not UNSET:
            field_dict["description"] = description
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if price_amount_cents is not UNSET:
            field_dict["price_amount_cents"] = price_amount_cents
        if compare_at_amount_cents is not UNSET:
            field_dict["compare_at_amount_cents"] = compare_at_amount_cents
        if compute_price_amount is not UNSET:
            field_dict["_compute_price_amount"] = compute_price_amount
        if compute_compare_at_amount is not UNSET:
            field_dict["_compute_compare_at_amount"] = compute_compare_at_amount
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hbundlesbundle_id_response_200_data_attributes_metadata import (
            PATCHbundlesbundleIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        description = d.pop("description", UNSET)

        image_url = d.pop("image_url", UNSET)

        price_amount_cents = d.pop("price_amount_cents", UNSET)

        compare_at_amount_cents = d.pop("compare_at_amount_cents", UNSET)

        compute_price_amount = d.pop("_compute_price_amount", UNSET)

        compute_compare_at_amount = d.pop("_compute_compare_at_amount", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHbundlesbundleIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHbundlesbundleIdResponse200DataAttributesMetadata.from_dict(_metadata)

        patc_hbundlesbundle_id_response_200_data_attributes = cls(
            code=code,
            name=name,
            currency_code=currency_code,
            description=description,
            image_url=image_url,
            price_amount_cents=price_amount_cents,
            compare_at_amount_cents=compare_at_amount_cents,
            compute_price_amount=compute_price_amount,
            compute_compare_at_amount=compute_compare_at_amount,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        patc_hbundlesbundle_id_response_200_data_attributes.additional_properties = d
        return patc_hbundlesbundle_id_response_200_data_attributes

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
