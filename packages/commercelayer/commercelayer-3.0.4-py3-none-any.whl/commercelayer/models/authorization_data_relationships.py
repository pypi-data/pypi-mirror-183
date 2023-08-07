from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authorization_data_relationships_captures import AuthorizationDataRelationshipsCaptures
    from ..models.authorization_data_relationships_order import AuthorizationDataRelationshipsOrder
    from ..models.authorization_data_relationships_voids import AuthorizationDataRelationshipsVoids


T = TypeVar("T", bound="AuthorizationDataRelationships")


@attr.s(auto_attribs=True)
class AuthorizationDataRelationships:
    """
    Attributes:
        order (Union[Unset, AuthorizationDataRelationshipsOrder]):
        captures (Union[Unset, AuthorizationDataRelationshipsCaptures]):
        voids (Union[Unset, AuthorizationDataRelationshipsVoids]):
    """

    order: Union[Unset, "AuthorizationDataRelationshipsOrder"] = UNSET
    captures: Union[Unset, "AuthorizationDataRelationshipsCaptures"] = UNSET
    voids: Union[Unset, "AuthorizationDataRelationshipsVoids"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        captures: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.captures, Unset):
            captures = self.captures.to_dict()

        voids: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.voids, Unset):
            voids = self.voids.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order
        if captures is not UNSET:
            field_dict["captures"] = captures
        if voids is not UNSET:
            field_dict["voids"] = voids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.authorization_data_relationships_captures import AuthorizationDataRelationshipsCaptures
        from ..models.authorization_data_relationships_order import AuthorizationDataRelationshipsOrder
        from ..models.authorization_data_relationships_voids import AuthorizationDataRelationshipsVoids

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, AuthorizationDataRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = AuthorizationDataRelationshipsOrder.from_dict(_order)

        _captures = d.pop("captures", UNSET)
        captures: Union[Unset, AuthorizationDataRelationshipsCaptures]
        if isinstance(_captures, Unset):
            captures = UNSET
        else:
            captures = AuthorizationDataRelationshipsCaptures.from_dict(_captures)

        _voids = d.pop("voids", UNSET)
        voids: Union[Unset, AuthorizationDataRelationshipsVoids]
        if isinstance(_voids, Unset):
            voids = UNSET
        else:
            voids = AuthorizationDataRelationshipsVoids.from_dict(_voids)

        authorization_data_relationships = cls(
            order=order,
            captures=captures,
            voids=voids,
        )

        authorization_data_relationships.additional_properties = d
        return authorization_data_relationships

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
