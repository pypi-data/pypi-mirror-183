from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gift_card_recipient_update_data_attributes_metadata import (
        GiftCardRecipientUpdateDataAttributesMetadata,
    )


T = TypeVar("T", bound="GiftCardRecipientUpdateDataAttributes")


@attr.s(auto_attribs=True)
class GiftCardRecipientUpdateDataAttributes:
    """
    Attributes:
        email (Union[Unset, str]): The recipient email address Example: john@example.com.
        first_name (Union[Unset, str]): The recipient first name Example: John.
        last_name (Union[Unset, str]): The recipient last name Example: Smith.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GiftCardRecipientUpdateDataAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    email: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GiftCardRecipientUpdateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        first_name = self.first_name
        last_name = self.last_name
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gift_card_recipient_update_data_attributes_metadata import (
            GiftCardRecipientUpdateDataAttributesMetadata,
        )

        d = src_dict.copy()
        email = d.pop("email", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GiftCardRecipientUpdateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GiftCardRecipientUpdateDataAttributesMetadata.from_dict(_metadata)

        gift_card_recipient_update_data_attributes = cls(
            email=email,
            first_name=first_name,
            last_name=last_name,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        gift_card_recipient_update_data_attributes.additional_properties = d
        return gift_card_recipient_update_data_attributes

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
