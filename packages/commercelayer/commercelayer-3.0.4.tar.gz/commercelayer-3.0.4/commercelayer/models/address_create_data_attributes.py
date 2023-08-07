from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_create_data_attributes_metadata import AddressCreateDataAttributesMetadata


T = TypeVar("T", bound="AddressCreateDataAttributes")


@attr.s(auto_attribs=True)
class AddressCreateDataAttributes:
    """
    Attributes:
        line_1 (str): Address line 1, i.e. Street address, PO Box Example: 2883 Geraldine Lane.
        city (str): Address city Example: New York.
        state_code (str): State, province or region code. Example: NY.
        country_code (str): The international 2-letter country code as defined by the ISO 3166-1 standard Example: US.
        phone (str): Phone number (including extension). Example: (212) 646-338-1228.
        business (Union[Unset, bool]): Indicates if it's a business or a personal address
        first_name (Union[Unset, str]): Address first name (personal) Example: John.
        last_name (Union[Unset, str]): Address last name (personal) Example: Smith.
        company (Union[Unset, str]): Address company name (business) Example: The Red Brand Inc..
        line_2 (Union[Unset, str]): Address line 2, i.e. Apartment, Suite, Building Example: Apt.23.
        zip_code (Union[Unset, str]): ZIP or postal code Example: 10013.
        email (Union[Unset, str]): Email address. Example: john@example.com.
        notes (Union[Unset, str]): A free notes attached to the address. When used as a shipping address, this can be
            useful to let the customers add specific delivery instructions. Example: Please ring the bell twice.
        lat (Union[Unset, float]): The address geocoded latitude. This is automatically generated when creating a
            shipping/billing address for an order and a valid geocoder is attached to the order's market. Example:
            40.6971494.
        lng (Union[Unset, float]): The address geocoded longitude. This is automatically generated when creating a
            shipping/billing address for an order and a valid geocoder is attached to the order's market. Example:
            -74.2598672.
        billing_info (Union[Unset, str]): Customer's billing information (i.e. VAT number, codice fiscale) Example: VAT
            ID IT02382940977.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, AddressCreateDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    line_1: str
    city: str
    state_code: str
    country_code: str
    phone: str
    business: Union[Unset, bool] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    company: Union[Unset, str] = UNSET
    line_2: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    lat: Union[Unset, float] = UNSET
    lng: Union[Unset, float] = UNSET
    billing_info: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "AddressCreateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_1 = self.line_1
        city = self.city
        state_code = self.state_code
        country_code = self.country_code
        phone = self.phone
        business = self.business
        first_name = self.first_name
        last_name = self.last_name
        company = self.company
        line_2 = self.line_2
        zip_code = self.zip_code
        email = self.email
        notes = self.notes
        lat = self.lat
        lng = self.lng
        billing_info = self.billing_info
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "line_1": line_1,
                "city": city,
                "state_code": state_code,
                "country_code": country_code,
                "phone": phone,
            }
        )
        if business is not UNSET:
            field_dict["business"] = business
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if company is not UNSET:
            field_dict["company"] = company
        if line_2 is not UNSET:
            field_dict["line_2"] = line_2
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code
        if email is not UNSET:
            field_dict["email"] = email
        if notes is not UNSET:
            field_dict["notes"] = notes
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng
        if billing_info is not UNSET:
            field_dict["billing_info"] = billing_info
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address_create_data_attributes_metadata import AddressCreateDataAttributesMetadata

        d = src_dict.copy()
        line_1 = d.pop("line_1")

        city = d.pop("city")

        state_code = d.pop("state_code")

        country_code = d.pop("country_code")

        phone = d.pop("phone")

        business = d.pop("business", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        company = d.pop("company", UNSET)

        line_2 = d.pop("line_2", UNSET)

        zip_code = d.pop("zip_code", UNSET)

        email = d.pop("email", UNSET)

        notes = d.pop("notes", UNSET)

        lat = d.pop("lat", UNSET)

        lng = d.pop("lng", UNSET)

        billing_info = d.pop("billing_info", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, AddressCreateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AddressCreateDataAttributesMetadata.from_dict(_metadata)

        address_create_data_attributes = cls(
            line_1=line_1,
            city=city,
            state_code=state_code,
            country_code=country_code,
            phone=phone,
            business=business,
            first_name=first_name,
            last_name=last_name,
            company=company,
            line_2=line_2,
            zip_code=zip_code,
            email=email,
            notes=notes,
            lat=lat,
            lng=lng,
            billing_info=billing_info,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        address_create_data_attributes.additional_properties = d
        return address_create_data_attributes

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
