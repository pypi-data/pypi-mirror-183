from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parcel_data_attributes_metadata import ParcelDataAttributesMetadata


T = TypeVar("T", bound="ParcelDataAttributes")


@attr.s(auto_attribs=True)
class ParcelDataAttributes:
    """
    Attributes:
        number (Union[Unset, str]): Unique identifier for the parcel Example: #1234/S/001/P/001.
        weight (Union[Unset, float]): The parcel weight, used to automatically calculate the tax rates from the
            available carrier accounts. Example: 1000.0.
        unit_of_weight (Union[Unset, str]): Can be one of 'gr', 'lb', or 'oz' Example: gr.
        eel_pfc (Union[Unset, str]): When shipping outside the US, you need to provide either an Exemption and Exclusion
            Legend (EEL) code or a Proof of Filing Citation (PFC). Which you need is based on the value of the goods being
            shipped. Value can be one of "EEL" o "PFC". Example: EEL.
        contents_type (Union[Unset, str]): The type of item you are sending. Can be one of 'merchandise', 'gift',
            'documents', 'returned_goods', 'sample', or 'other'. Example: merchandise.
        contents_explanation (Union[Unset, str]): If you specify 'other' in the 'contents_type' attribute, you must
            supply a brief description in this attribute.
        customs_certify (Union[Unset, bool]): Indicates if the provided information is accurate
        customs_signer (Union[Unset, str]): This is the name of the person who is certifying that the information
            provided on the customs form is accurate. Use a name of the person in your organization who is responsible for
            this. Example: John Doe.
        non_delivery_option (Union[Unset, str]): In case the shipment cannot be delivered, this option tells the carrier
            what you want to happen to the parcel. You can pass either 'return', or 'abandon'. The value defaults to
            'return'. If you pass 'abandon', you will not receive the parcel back if it cannot be delivered. Example:
            return.
        restriction_type (Union[Unset, str]): Describes if your parcel requires any special treatment or quarantine when
            entering the country. Can be one of 'none', 'other', 'quarantine', or 'sanitary_phytosanitary_inspection'.
            Example: none.
        restriction_comments (Union[Unset, str]): If you specify 'other' in the restriction type, you must supply a
            brief description of what is required.
        customs_info_required (Union[Unset, bool]): Indicates if the parcel requires customs info to get the shipping
            rates.
        shipping_label_url (Union[Unset, str]): The shipping label url, ready to be downloaded and printed. Example:
            https://bucket.s3-us-west-2.amazonaws.com/files/postage_label/20180101/123.pdf.
        shipping_label_file_type (Union[Unset, str]): The shipping label file type. One of 'application/pdf',
            'application/zpl', 'application/epl2', or 'image/png'. Example: application/pdf.
        shipping_label_size (Union[Unset, str]): The shipping label size. Example: 4x7.
        shipping_label_resolution (Union[Unset, str]): The shipping label resolution. Example: 200.
        tracking_number (Union[Unset, str]): The tracking number associated to this parcel. Example: 1Z4V2A000000000000.
        tracking_status (Union[Unset, str]): The tracking status for this parcel, automatically updated in real time by
            the shipping carrier. Example: delivered.
        tracking_status_detail (Union[Unset, str]): Additional information about the tracking status, automatically
            updated in real time by the shipping carrier. Example: arrived_at_destination.
        tracking_status_updated_at (Union[Unset, str]): Time at which the parcel's tracking status was last updated.
            Example: 2018-01-01T12:00:00.000Z.
        tracking_details (Union[Unset, str]): The parcel's full tracking history, automatically updated in real time by
            the shipping carrier.
        carrier_weight_oz (Union[Unset, str]): The weight of the parcel as measured by the carrier in ounces (if
            available) Example: 42.32.
        signed_by (Union[Unset, str]): The name of the person who signed for the parcel (if available) Example: John
            Smith.
        incoterm (Union[Unset, str]): The type of Incoterm (if available). Example: EXW.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, ParcelDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    number: Union[Unset, str] = UNSET
    weight: Union[Unset, float] = UNSET
    unit_of_weight: Union[Unset, str] = UNSET
    eel_pfc: Union[Unset, str] = UNSET
    contents_type: Union[Unset, str] = UNSET
    contents_explanation: Union[Unset, str] = UNSET
    customs_certify: Union[Unset, bool] = UNSET
    customs_signer: Union[Unset, str] = UNSET
    non_delivery_option: Union[Unset, str] = UNSET
    restriction_type: Union[Unset, str] = UNSET
    restriction_comments: Union[Unset, str] = UNSET
    customs_info_required: Union[Unset, bool] = UNSET
    shipping_label_url: Union[Unset, str] = UNSET
    shipping_label_file_type: Union[Unset, str] = UNSET
    shipping_label_size: Union[Unset, str] = UNSET
    shipping_label_resolution: Union[Unset, str] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    tracking_status: Union[Unset, str] = UNSET
    tracking_status_detail: Union[Unset, str] = UNSET
    tracking_status_updated_at: Union[Unset, str] = UNSET
    tracking_details: Union[Unset, str] = UNSET
    carrier_weight_oz: Union[Unset, str] = UNSET
    signed_by: Union[Unset, str] = UNSET
    incoterm: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ParcelDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        weight = self.weight
        unit_of_weight = self.unit_of_weight
        eel_pfc = self.eel_pfc
        contents_type = self.contents_type
        contents_explanation = self.contents_explanation
        customs_certify = self.customs_certify
        customs_signer = self.customs_signer
        non_delivery_option = self.non_delivery_option
        restriction_type = self.restriction_type
        restriction_comments = self.restriction_comments
        customs_info_required = self.customs_info_required
        shipping_label_url = self.shipping_label_url
        shipping_label_file_type = self.shipping_label_file_type
        shipping_label_size = self.shipping_label_size
        shipping_label_resolution = self.shipping_label_resolution
        tracking_number = self.tracking_number
        tracking_status = self.tracking_status
        tracking_status_detail = self.tracking_status_detail
        tracking_status_updated_at = self.tracking_status_updated_at
        tracking_details = self.tracking_details
        carrier_weight_oz = self.carrier_weight_oz
        signed_by = self.signed_by
        incoterm = self.incoterm
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
        if weight is not UNSET:
            field_dict["weight"] = weight
        if unit_of_weight is not UNSET:
            field_dict["unit_of_weight"] = unit_of_weight
        if eel_pfc is not UNSET:
            field_dict["eel_pfc"] = eel_pfc
        if contents_type is not UNSET:
            field_dict["contents_type"] = contents_type
        if contents_explanation is not UNSET:
            field_dict["contents_explanation"] = contents_explanation
        if customs_certify is not UNSET:
            field_dict["customs_certify"] = customs_certify
        if customs_signer is not UNSET:
            field_dict["customs_signer"] = customs_signer
        if non_delivery_option is not UNSET:
            field_dict["non_delivery_option"] = non_delivery_option
        if restriction_type is not UNSET:
            field_dict["restriction_type"] = restriction_type
        if restriction_comments is not UNSET:
            field_dict["restriction_comments"] = restriction_comments
        if customs_info_required is not UNSET:
            field_dict["customs_info_required"] = customs_info_required
        if shipping_label_url is not UNSET:
            field_dict["shipping_label_url"] = shipping_label_url
        if shipping_label_file_type is not UNSET:
            field_dict["shipping_label_file_type"] = shipping_label_file_type
        if shipping_label_size is not UNSET:
            field_dict["shipping_label_size"] = shipping_label_size
        if shipping_label_resolution is not UNSET:
            field_dict["shipping_label_resolution"] = shipping_label_resolution
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number
        if tracking_status is not UNSET:
            field_dict["tracking_status"] = tracking_status
        if tracking_status_detail is not UNSET:
            field_dict["tracking_status_detail"] = tracking_status_detail
        if tracking_status_updated_at is not UNSET:
            field_dict["tracking_status_updated_at"] = tracking_status_updated_at
        if tracking_details is not UNSET:
            field_dict["tracking_details"] = tracking_details
        if carrier_weight_oz is not UNSET:
            field_dict["carrier_weight_oz"] = carrier_weight_oz
        if signed_by is not UNSET:
            field_dict["signed_by"] = signed_by
        if incoterm is not UNSET:
            field_dict["incoterm"] = incoterm
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
        from ..models.parcel_data_attributes_metadata import ParcelDataAttributesMetadata

        d = src_dict.copy()
        number = d.pop("number", UNSET)

        weight = d.pop("weight", UNSET)

        unit_of_weight = d.pop("unit_of_weight", UNSET)

        eel_pfc = d.pop("eel_pfc", UNSET)

        contents_type = d.pop("contents_type", UNSET)

        contents_explanation = d.pop("contents_explanation", UNSET)

        customs_certify = d.pop("customs_certify", UNSET)

        customs_signer = d.pop("customs_signer", UNSET)

        non_delivery_option = d.pop("non_delivery_option", UNSET)

        restriction_type = d.pop("restriction_type", UNSET)

        restriction_comments = d.pop("restriction_comments", UNSET)

        customs_info_required = d.pop("customs_info_required", UNSET)

        shipping_label_url = d.pop("shipping_label_url", UNSET)

        shipping_label_file_type = d.pop("shipping_label_file_type", UNSET)

        shipping_label_size = d.pop("shipping_label_size", UNSET)

        shipping_label_resolution = d.pop("shipping_label_resolution", UNSET)

        tracking_number = d.pop("tracking_number", UNSET)

        tracking_status = d.pop("tracking_status", UNSET)

        tracking_status_detail = d.pop("tracking_status_detail", UNSET)

        tracking_status_updated_at = d.pop("tracking_status_updated_at", UNSET)

        tracking_details = d.pop("tracking_details", UNSET)

        carrier_weight_oz = d.pop("carrier_weight_oz", UNSET)

        signed_by = d.pop("signed_by", UNSET)

        incoterm = d.pop("incoterm", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ParcelDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ParcelDataAttributesMetadata.from_dict(_metadata)

        parcel_data_attributes = cls(
            number=number,
            weight=weight,
            unit_of_weight=unit_of_weight,
            eel_pfc=eel_pfc,
            contents_type=contents_type,
            contents_explanation=contents_explanation,
            customs_certify=customs_certify,
            customs_signer=customs_signer,
            non_delivery_option=non_delivery_option,
            restriction_type=restriction_type,
            restriction_comments=restriction_comments,
            customs_info_required=customs_info_required,
            shipping_label_url=shipping_label_url,
            shipping_label_file_type=shipping_label_file_type,
            shipping_label_size=shipping_label_size,
            shipping_label_resolution=shipping_label_resolution,
            tracking_number=tracking_number,
            tracking_status=tracking_status,
            tracking_status_detail=tracking_status_detail,
            tracking_status_updated_at=tracking_status_updated_at,
            tracking_details=tracking_details,
            carrier_weight_oz=carrier_weight_oz,
            signed_by=signed_by,
            incoterm=incoterm,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        parcel_data_attributes.additional_properties = d
        return parcel_data_attributes

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
