from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tauthorizationsauthorization_id_response_200_data_relationships_captures import (
        GETauthorizationsauthorizationIdResponse200DataRelationshipsCaptures,
    )
    from ..models.ge_tauthorizationsauthorization_id_response_200_data_relationships_order import (
        GETauthorizationsauthorizationIdResponse200DataRelationshipsOrder,
    )
    from ..models.ge_tauthorizationsauthorization_id_response_200_data_relationships_voids import (
        GETauthorizationsauthorizationIdResponse200DataRelationshipsVoids,
    )


T = TypeVar("T", bound="GETauthorizationsauthorizationIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETauthorizationsauthorizationIdResponse200DataRelationships:
    """
    Attributes:
        order (Union[Unset, GETauthorizationsauthorizationIdResponse200DataRelationshipsOrder]):
        captures (Union[Unset, GETauthorizationsauthorizationIdResponse200DataRelationshipsCaptures]):
        voids (Union[Unset, GETauthorizationsauthorizationIdResponse200DataRelationshipsVoids]):
    """

    order: Union[Unset, "GETauthorizationsauthorizationIdResponse200DataRelationshipsOrder"] = UNSET
    captures: Union[Unset, "GETauthorizationsauthorizationIdResponse200DataRelationshipsCaptures"] = UNSET
    voids: Union[Unset, "GETauthorizationsauthorizationIdResponse200DataRelationshipsVoids"] = UNSET
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
        from ..models.ge_tauthorizationsauthorization_id_response_200_data_relationships_captures import (
            GETauthorizationsauthorizationIdResponse200DataRelationshipsCaptures,
        )
        from ..models.ge_tauthorizationsauthorization_id_response_200_data_relationships_order import (
            GETauthorizationsauthorizationIdResponse200DataRelationshipsOrder,
        )
        from ..models.ge_tauthorizationsauthorization_id_response_200_data_relationships_voids import (
            GETauthorizationsauthorizationIdResponse200DataRelationshipsVoids,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, GETauthorizationsauthorizationIdResponse200DataRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = GETauthorizationsauthorizationIdResponse200DataRelationshipsOrder.from_dict(_order)

        _captures = d.pop("captures", UNSET)
        captures: Union[Unset, GETauthorizationsauthorizationIdResponse200DataRelationshipsCaptures]
        if isinstance(_captures, Unset):
            captures = UNSET
        else:
            captures = GETauthorizationsauthorizationIdResponse200DataRelationshipsCaptures.from_dict(_captures)

        _voids = d.pop("voids", UNSET)
        voids: Union[Unset, GETauthorizationsauthorizationIdResponse200DataRelationshipsVoids]
        if isinstance(_voids, Unset):
            voids = UNSET
        else:
            voids = GETauthorizationsauthorizationIdResponse200DataRelationshipsVoids.from_dict(_voids)

        ge_tauthorizationsauthorization_id_response_200_data_relationships = cls(
            order=order,
            captures=captures,
            voids=voids,
        )

        ge_tauthorizationsauthorization_id_response_200_data_relationships.additional_properties = d
        return ge_tauthorizationsauthorization_id_response_200_data_relationships

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
