from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tgift_card_recipients_response_201_data import POSTgiftCardRecipientsResponse201Data


T = TypeVar("T", bound="POSTgiftCardRecipientsResponse201")


@attr.s(auto_attribs=True)
class POSTgiftCardRecipientsResponse201:
    """
    Attributes:
        data (Union[Unset, POSTgiftCardRecipientsResponse201Data]):
    """

    data: Union[Unset, "POSTgiftCardRecipientsResponse201Data"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tgift_card_recipients_response_201_data import POSTgiftCardRecipientsResponse201Data

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTgiftCardRecipientsResponse201Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTgiftCardRecipientsResponse201Data.from_dict(_data)

        pos_tgift_card_recipients_response_201 = cls(
            data=data,
        )

        pos_tgift_card_recipients_response_201.additional_properties = d
        return pos_tgift_card_recipients_response_201

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
