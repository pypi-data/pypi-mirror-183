from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.capture_data_relationships_refunds_data import CaptureDataRelationshipsRefundsData


T = TypeVar("T", bound="CaptureDataRelationshipsRefunds")


@attr.s(auto_attribs=True)
class CaptureDataRelationshipsRefunds:
    """
    Attributes:
        data (Union[Unset, CaptureDataRelationshipsRefundsData]):
    """

    data: Union[Unset, "CaptureDataRelationshipsRefundsData"] = UNSET
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
        from ..models.capture_data_relationships_refunds_data import CaptureDataRelationshipsRefundsData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, CaptureDataRelationshipsRefundsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CaptureDataRelationshipsRefundsData.from_dict(_data)

        capture_data_relationships_refunds = cls(
            data=data,
        )

        capture_data_relationships_refunds.additional_properties = d
        return capture_data_relationships_refunds

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
