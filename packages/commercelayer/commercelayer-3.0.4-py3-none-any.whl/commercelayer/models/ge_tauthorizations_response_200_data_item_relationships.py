from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tauthorizations_response_200_data_item_relationships_captures import (
        GETauthorizationsResponse200DataItemRelationshipsCaptures,
    )
    from ..models.ge_tauthorizations_response_200_data_item_relationships_order import (
        GETauthorizationsResponse200DataItemRelationshipsOrder,
    )
    from ..models.ge_tauthorizations_response_200_data_item_relationships_voids import (
        GETauthorizationsResponse200DataItemRelationshipsVoids,
    )


T = TypeVar("T", bound="GETauthorizationsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETauthorizationsResponse200DataItemRelationships:
    """
    Attributes:
        order (Union[Unset, GETauthorizationsResponse200DataItemRelationshipsOrder]):
        captures (Union[Unset, GETauthorizationsResponse200DataItemRelationshipsCaptures]):
        voids (Union[Unset, GETauthorizationsResponse200DataItemRelationshipsVoids]):
    """

    order: Union[Unset, "GETauthorizationsResponse200DataItemRelationshipsOrder"] = UNSET
    captures: Union[Unset, "GETauthorizationsResponse200DataItemRelationshipsCaptures"] = UNSET
    voids: Union[Unset, "GETauthorizationsResponse200DataItemRelationshipsVoids"] = UNSET
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
        from ..models.ge_tauthorizations_response_200_data_item_relationships_captures import (
            GETauthorizationsResponse200DataItemRelationshipsCaptures,
        )
        from ..models.ge_tauthorizations_response_200_data_item_relationships_order import (
            GETauthorizationsResponse200DataItemRelationshipsOrder,
        )
        from ..models.ge_tauthorizations_response_200_data_item_relationships_voids import (
            GETauthorizationsResponse200DataItemRelationshipsVoids,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, GETauthorizationsResponse200DataItemRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = GETauthorizationsResponse200DataItemRelationshipsOrder.from_dict(_order)

        _captures = d.pop("captures", UNSET)
        captures: Union[Unset, GETauthorizationsResponse200DataItemRelationshipsCaptures]
        if isinstance(_captures, Unset):
            captures = UNSET
        else:
            captures = GETauthorizationsResponse200DataItemRelationshipsCaptures.from_dict(_captures)

        _voids = d.pop("voids", UNSET)
        voids: Union[Unset, GETauthorizationsResponse200DataItemRelationshipsVoids]
        if isinstance(_voids, Unset):
            voids = UNSET
        else:
            voids = GETauthorizationsResponse200DataItemRelationshipsVoids.from_dict(_voids)

        ge_tauthorizations_response_200_data_item_relationships = cls(
            order=order,
            captures=captures,
            voids=voids,
        )

        ge_tauthorizations_response_200_data_item_relationships.additional_properties = d
        return ge_tauthorizations_response_200_data_item_relationships

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
