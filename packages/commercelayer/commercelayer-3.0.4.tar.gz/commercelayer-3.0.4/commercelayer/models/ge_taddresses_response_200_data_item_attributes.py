from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_taddresses_response_200_data_item_attributes_metadata import (
        GETaddressesResponse200DataItemAttributesMetadata,
    )


T = TypeVar("T", bound="GETaddressesResponse200DataItemAttributes")


@attr.s(auto_attribs=True)
class GETaddressesResponse200DataItemAttributes:
    """
    Attributes:
        business (Union[Unset, bool]): Indicates if it's a business or a personal address
        first_name (Union[Unset, str]): Address first name (personal) Example: John.
        last_name (Union[Unset, str]): Address last name (personal) Example: Smith.
        company (Union[Unset, str]): Address company name (business) Example: The Red Brand Inc..
        full_name (Union[Unset, str]): Company name (business) of first name and last name (personal) Example: John
            Smith.
        line_1 (Union[Unset, str]): Address line 1, i.e. Street address, PO Box Example: 2883 Geraldine Lane.
        line_2 (Union[Unset, str]): Address line 2, i.e. Apartment, Suite, Building Example: Apt.23.
        city (Union[Unset, str]): Address city Example: New York.
        zip_code (Union[Unset, str]): ZIP or postal code Example: 10013.
        state_code (Union[Unset, str]): State, province or region code. Example: NY.
        country_code (Union[Unset, str]): The international 2-letter country code as defined by the ISO 3166-1 standard
            Example: US.
        phone (Union[Unset, str]): Phone number (including extension). Example: (212) 646-338-1228.
        full_address (Union[Unset, str]): Compact description of the address location, without the full name Example:
            2883 Geraldine Lane Apt.23, 10013 New York NY (US) (212) 646-338-1228.
        name (Union[Unset, str]): Compact description of the address location, including the full name Example: John
            Smith, 2883 Geraldine Lane Apt.23, 10013 New York NY (US) (212) 646-338-1228.
        email (Union[Unset, str]): Email address. Example: john@example.com.
        notes (Union[Unset, str]): A free notes attached to the address. When used as a shipping address, this can be
            useful to let the customers add specific delivery instructions. Example: Please ring the bell twice.
        lat (Union[Unset, float]): The address geocoded latitude. This is automatically generated when creating a
            shipping/billing address for an order and a valid geocoder is attached to the order's market. Example:
            40.6971494.
        lng (Union[Unset, float]): The address geocoded longitude. This is automatically generated when creating a
            shipping/billing address for an order and a valid geocoder is attached to the order's market. Example:
            -74.2598672.
        is_localized (Union[Unset, bool]): Indicates if the latitude and logitude are present, either geocoded or
            manually updated Example: True.
        is_geocoded (Union[Unset, bool]): Indicates if the address has been successfully geocoded Example: True.
        provider_name (Union[Unset, str]): The geocoder provider name (either Google or Bing) Example: google.
        map_url (Union[Unset, str]): The map url of the geocoded address (if geocoded) Example:
            https://www.google.com/maps/search/?api=1&query=40.6971494,-74.2598672.
        static_map_url (Union[Unset, str]): The static map image url of the geocoded address (if geocoded) Example:
            https://maps.googleapis.com/maps/api/staticmap?center=40.6971494,-74.2598672&size=640x320&zoom=15.
        billing_info (Union[Unset, str]): Customer's billing information (i.e. VAT number, codice fiscale) Example: VAT
            ID IT02382940977.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETaddressesResponse200DataItemAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    business: Union[Unset, bool] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    company: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    line_1: Union[Unset, str] = UNSET
    line_2: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    state_code: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    full_address: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    lat: Union[Unset, float] = UNSET
    lng: Union[Unset, float] = UNSET
    is_localized: Union[Unset, bool] = UNSET
    is_geocoded: Union[Unset, bool] = UNSET
    provider_name: Union[Unset, str] = UNSET
    map_url: Union[Unset, str] = UNSET
    static_map_url: Union[Unset, str] = UNSET
    billing_info: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETaddressesResponse200DataItemAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        business = self.business
        first_name = self.first_name
        last_name = self.last_name
        company = self.company
        full_name = self.full_name
        line_1 = self.line_1
        line_2 = self.line_2
        city = self.city
        zip_code = self.zip_code
        state_code = self.state_code
        country_code = self.country_code
        phone = self.phone
        full_address = self.full_address
        name = self.name
        email = self.email
        notes = self.notes
        lat = self.lat
        lng = self.lng
        is_localized = self.is_localized
        is_geocoded = self.is_geocoded
        provider_name = self.provider_name
        map_url = self.map_url
        static_map_url = self.static_map_url
        billing_info = self.billing_info
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
        if business is not UNSET:
            field_dict["business"] = business
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if company is not UNSET:
            field_dict["company"] = company
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if line_1 is not UNSET:
            field_dict["line_1"] = line_1
        if line_2 is not UNSET:
            field_dict["line_2"] = line_2
        if city is not UNSET:
            field_dict["city"] = city
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code
        if state_code is not UNSET:
            field_dict["state_code"] = state_code
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if phone is not UNSET:
            field_dict["phone"] = phone
        if full_address is not UNSET:
            field_dict["full_address"] = full_address
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if notes is not UNSET:
            field_dict["notes"] = notes
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng
        if is_localized is not UNSET:
            field_dict["is_localized"] = is_localized
        if is_geocoded is not UNSET:
            field_dict["is_geocoded"] = is_geocoded
        if provider_name is not UNSET:
            field_dict["provider_name"] = provider_name
        if map_url is not UNSET:
            field_dict["map_url"] = map_url
        if static_map_url is not UNSET:
            field_dict["static_map_url"] = static_map_url
        if billing_info is not UNSET:
            field_dict["billing_info"] = billing_info
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
        from ..models.ge_taddresses_response_200_data_item_attributes_metadata import (
            GETaddressesResponse200DataItemAttributesMetadata,
        )

        d = src_dict.copy()
        business = d.pop("business", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        company = d.pop("company", UNSET)

        full_name = d.pop("full_name", UNSET)

        line_1 = d.pop("line_1", UNSET)

        line_2 = d.pop("line_2", UNSET)

        city = d.pop("city", UNSET)

        zip_code = d.pop("zip_code", UNSET)

        state_code = d.pop("state_code", UNSET)

        country_code = d.pop("country_code", UNSET)

        phone = d.pop("phone", UNSET)

        full_address = d.pop("full_address", UNSET)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        notes = d.pop("notes", UNSET)

        lat = d.pop("lat", UNSET)

        lng = d.pop("lng", UNSET)

        is_localized = d.pop("is_localized", UNSET)

        is_geocoded = d.pop("is_geocoded", UNSET)

        provider_name = d.pop("provider_name", UNSET)

        map_url = d.pop("map_url", UNSET)

        static_map_url = d.pop("static_map_url", UNSET)

        billing_info = d.pop("billing_info", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETaddressesResponse200DataItemAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETaddressesResponse200DataItemAttributesMetadata.from_dict(_metadata)

        ge_taddresses_response_200_data_item_attributes = cls(
            business=business,
            first_name=first_name,
            last_name=last_name,
            company=company,
            full_name=full_name,
            line_1=line_1,
            line_2=line_2,
            city=city,
            zip_code=zip_code,
            state_code=state_code,
            country_code=country_code,
            phone=phone,
            full_address=full_address,
            name=name,
            email=email,
            notes=notes,
            lat=lat,
            lng=lng,
            is_localized=is_localized,
            is_geocoded=is_geocoded,
            provider_name=provider_name,
            map_url=map_url,
            static_map_url=static_map_url,
            billing_info=billing_info,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_taddresses_response_200_data_item_attributes.additional_properties = d
        return ge_taddresses_response_200_data_item_attributes

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
