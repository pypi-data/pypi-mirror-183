from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tgift_cards_response_201_data_attributes_metadata import (
        POSTgiftCardsResponse201DataAttributesMetadata,
    )


T = TypeVar("T", bound="POSTgiftCardsResponse201DataAttributes")


@attr.s(auto_attribs=True)
class POSTgiftCardsResponse201DataAttributes:
    """
    Attributes:
        balance_cents (int): The gift card balance, in cents. Example: 15000.
        code (Union[Unset, str]): The gift card code UUID. If not set, it's automatically generated. Example:
            32db311a-75d9-4c17-9e34-2be220137ad6.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard.
            Example: EUR.
        balance_max_cents (Union[Unset, str]): The gift card balance max, in cents. Example: 100000.
        single_use (Union[Unset, bool]): Indicates if the gift card can be used only one.
        rechargeable (Union[Unset, bool]): Indicates if the gift card can be recharged. Example: True.
        image_url (Union[Unset, str]): The URL of an image that represents the gift card. Example:
            https://img.yourdomain.com/gift_cards/32db311a.png.
        expires_at (Union[Unset, str]): Time at which the gift card will expire. Example: 2018-01-01T12:00:00.000Z.
        recipient_email (Union[Unset, str]): The email address of the associated recipient. When creating or updating a
            gift card, this is a shortcut to find or create the associated recipient by email. Example: john@example.com.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, POSTgiftCardsResponse201DataAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    balance_cents: int
    code: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    balance_max_cents: Union[Unset, str] = UNSET
    single_use: Union[Unset, bool] = UNSET
    rechargeable: Union[Unset, bool] = UNSET
    image_url: Union[Unset, str] = UNSET
    expires_at: Union[Unset, str] = UNSET
    recipient_email: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "POSTgiftCardsResponse201DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        balance_cents = self.balance_cents
        code = self.code
        currency_code = self.currency_code
        balance_max_cents = self.balance_max_cents
        single_use = self.single_use
        rechargeable = self.rechargeable
        image_url = self.image_url
        expires_at = self.expires_at
        recipient_email = self.recipient_email
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "balance_cents": balance_cents,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if balance_max_cents is not UNSET:
            field_dict["balance_max_cents"] = balance_max_cents
        if single_use is not UNSET:
            field_dict["single_use"] = single_use
        if rechargeable is not UNSET:
            field_dict["rechargeable"] = rechargeable
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if recipient_email is not UNSET:
            field_dict["recipient_email"] = recipient_email
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tgift_cards_response_201_data_attributes_metadata import (
            POSTgiftCardsResponse201DataAttributesMetadata,
        )

        d = src_dict.copy()
        balance_cents = d.pop("balance_cents")

        code = d.pop("code", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        balance_max_cents = d.pop("balance_max_cents", UNSET)

        single_use = d.pop("single_use", UNSET)

        rechargeable = d.pop("rechargeable", UNSET)

        image_url = d.pop("image_url", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        recipient_email = d.pop("recipient_email", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, POSTgiftCardsResponse201DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = POSTgiftCardsResponse201DataAttributesMetadata.from_dict(_metadata)

        pos_tgift_cards_response_201_data_attributes = cls(
            balance_cents=balance_cents,
            code=code,
            currency_code=currency_code,
            balance_max_cents=balance_max_cents,
            single_use=single_use,
            rechargeable=rechargeable,
            image_url=image_url,
            expires_at=expires_at,
            recipient_email=recipient_email,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        pos_tgift_cards_response_201_data_attributes.additional_properties = d
        return pos_tgift_cards_response_201_data_attributes

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
