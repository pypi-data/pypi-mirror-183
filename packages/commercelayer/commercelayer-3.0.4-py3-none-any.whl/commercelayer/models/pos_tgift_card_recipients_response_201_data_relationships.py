from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tgift_card_recipients_response_201_data_relationships_attachments import (
        POSTgiftCardRecipientsResponse201DataRelationshipsAttachments,
    )
    from ..models.pos_tgift_card_recipients_response_201_data_relationships_customer import (
        POSTgiftCardRecipientsResponse201DataRelationshipsCustomer,
    )


T = TypeVar("T", bound="POSTgiftCardRecipientsResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTgiftCardRecipientsResponse201DataRelationships:
    """
    Attributes:
        customer (Union[Unset, POSTgiftCardRecipientsResponse201DataRelationshipsCustomer]):
        attachments (Union[Unset, POSTgiftCardRecipientsResponse201DataRelationshipsAttachments]):
    """

    customer: Union[Unset, "POSTgiftCardRecipientsResponse201DataRelationshipsCustomer"] = UNSET
    attachments: Union[Unset, "POSTgiftCardRecipientsResponse201DataRelationshipsAttachments"] = UNSET
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
        from ..models.pos_tgift_card_recipients_response_201_data_relationships_attachments import (
            POSTgiftCardRecipientsResponse201DataRelationshipsAttachments,
        )
        from ..models.pos_tgift_card_recipients_response_201_data_relationships_customer import (
            POSTgiftCardRecipientsResponse201DataRelationshipsCustomer,
        )

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, POSTgiftCardRecipientsResponse201DataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = POSTgiftCardRecipientsResponse201DataRelationshipsCustomer.from_dict(_customer)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, POSTgiftCardRecipientsResponse201DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = POSTgiftCardRecipientsResponse201DataRelationshipsAttachments.from_dict(_attachments)

        pos_tgift_card_recipients_response_201_data_relationships = cls(
            customer=customer,
            attachments=attachments,
        )

        pos_tgift_card_recipients_response_201_data_relationships.additional_properties = d
        return pos_tgift_card_recipients_response_201_data_relationships

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
