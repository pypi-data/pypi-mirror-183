from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gift_card_recipient_update_data_relationships_customer import (
        GiftCardRecipientUpdateDataRelationshipsCustomer,
    )


T = TypeVar("T", bound="GiftCardRecipientUpdateDataRelationships")


@attr.s(auto_attribs=True)
class GiftCardRecipientUpdateDataRelationships:
    """
    Attributes:
        customer (Union[Unset, GiftCardRecipientUpdateDataRelationshipsCustomer]):
    """

    customer: Union[Unset, "GiftCardRecipientUpdateDataRelationshipsCustomer"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer is not UNSET:
            field_dict["customer"] = customer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gift_card_recipient_update_data_relationships_customer import (
            GiftCardRecipientUpdateDataRelationshipsCustomer,
        )

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, GiftCardRecipientUpdateDataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = GiftCardRecipientUpdateDataRelationshipsCustomer.from_dict(_customer)

        gift_card_recipient_update_data_relationships = cls(
            customer=customer,
        )

        gift_card_recipient_update_data_relationships.additional_properties = d
        return gift_card_recipient_update_data_relationships

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
