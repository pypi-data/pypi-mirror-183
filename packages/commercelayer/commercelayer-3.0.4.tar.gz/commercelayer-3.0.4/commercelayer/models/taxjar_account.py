from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.taxjar_account_data import TaxjarAccountData


T = TypeVar("T", bound="TaxjarAccount")


@attr.s(auto_attribs=True)
class TaxjarAccount:
    """
    Attributes:
        data (Union[Unset, TaxjarAccountData]):
    """

    data: Union[Unset, "TaxjarAccountData"] = UNSET
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
        from ..models.taxjar_account_data import TaxjarAccountData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, TaxjarAccountData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = TaxjarAccountData.from_dict(_data)

        taxjar_account = cls(
            data=data,
        )

        taxjar_account.additional_properties = d
        return taxjar_account

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
