from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hgift_card_recipientsgift_card_recipient_id_response_200_data_relationships_attachments import (
        PATCHgiftCardRecipientsgiftCardRecipientIdResponse200DataRelationshipsAttachments,
    )
    from ..models.patc_hgift_card_recipientsgift_card_recipient_id_response_200_data_relationships_customer import (
        PATCHgiftCardRecipientsgiftCardRecipientIdResponse200DataRelationshipsCustomer,
    )


T = TypeVar("T", bound="PATCHgiftCardRecipientsgiftCardRecipientIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHgiftCardRecipientsgiftCardRecipientIdResponse200DataRelationships:
    """
    Attributes:
        customer (Union[Unset, PATCHgiftCardRecipientsgiftCardRecipientIdResponse200DataRelationshipsCustomer]):
        attachments (Union[Unset, PATCHgiftCardRecipientsgiftCardRecipientIdResponse200DataRelationshipsAttachments]):
    """

    customer: Union[Unset, "PATCHgiftCardRecipientsgiftCardRecipientIdResponse200DataRelationshipsCustomer"] = UNSET
    attachments: Union[
        Unset, "PATCHgiftCardRecipientsgiftCardRecipientIdResponse200DataRelationshipsAttachments"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer is not UNSET:
            field_dict["customer"] = customer
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hgift_card_recipientsgift_card_recipient_id_response_200_data_relationships_attachments import (
            PATCHgiftCardRecipientsgiftCardRecipientIdResponse200DataRelationshipsAttachments,
        )
        from ..models.patc_hgift_card_recipientsgift_card_recipient_id_response_200_data_relationships_customer import (
            PATCHgiftCardRecipientsgiftCardRecipientIdResponse200DataRelationshipsCustomer,
        )

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, PATCHgiftCardRecipientsgiftCardRecipientIdResponse200DataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = PATCHgiftCardRecipientsgiftCardRecipientIdResponse200DataRelationshipsCustomer.from_dict(
                _customer
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHgiftCardRecipientsgiftCardRecipientIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PATCHgiftCardRecipientsgiftCardRecipientIdResponse200DataRelationshipsAttachments.from_dict(
                _attachments
            )

        patc_hgift_card_recipientsgift_card_recipient_id_response_200_data_relationships = cls(
            customer=customer,
            attachments=attachments,
        )

        patc_hgift_card_recipientsgift_card_recipient_id_response_200_data_relationships.additional_properties = d
        return patc_hgift_card_recipientsgift_card_recipient_id_response_200_data_relationships

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
