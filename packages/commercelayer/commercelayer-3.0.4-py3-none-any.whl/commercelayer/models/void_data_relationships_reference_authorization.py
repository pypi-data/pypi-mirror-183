from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.void_data_relationships_reference_authorization_data import (
        VoidDataRelationshipsReferenceAuthorizationData,
    )


T = TypeVar("T", bound="VoidDataRelationshipsReferenceAuthorization")


@attr.s(auto_attribs=True)
class VoidDataRelationshipsReferenceAuthorization:
    """
    Attributes:
        data (Union[Unset, VoidDataRelationshipsReferenceAuthorizationData]):
    """

    data: Union[Unset, "VoidDataRelationshipsReferenceAuthorizationData"] = UNSET
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
        from ..models.void_data_relationships_reference_authorization_data import (
            VoidDataRelationshipsReferenceAuthorizationData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, VoidDataRelationshipsReferenceAuthorizationData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = VoidDataRelationshipsReferenceAuthorizationData.from_dict(_data)

        void_data_relationships_reference_authorization = cls(
            data=data,
        )

        void_data_relationships_reference_authorization.additional_properties = d
        return void_data_relationships_reference_authorization

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
