from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcaptures_response_200_data_item_relationships_order import (
        GETcapturesResponse200DataItemRelationshipsOrder,
    )
    from ..models.ge_tcaptures_response_200_data_item_relationships_reference_authorization import (
        GETcapturesResponse200DataItemRelationshipsReferenceAuthorization,
    )
    from ..models.ge_tcaptures_response_200_data_item_relationships_refunds import (
        GETcapturesResponse200DataItemRelationshipsRefunds,
    )


T = TypeVar("T", bound="GETcapturesResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETcapturesResponse200DataItemRelationships:
    """
    Attributes:
        order (Union[Unset, GETcapturesResponse200DataItemRelationshipsOrder]):
        reference_authorization (Union[Unset, GETcapturesResponse200DataItemRelationshipsReferenceAuthorization]):
        refunds (Union[Unset, GETcapturesResponse200DataItemRelationshipsRefunds]):
    """

    order: Union[Unset, "GETcapturesResponse200DataItemRelationshipsOrder"] = UNSET
    reference_authorization: Union[Unset, "GETcapturesResponse200DataItemRelationshipsReferenceAuthorization"] = UNSET
    refunds: Union[Unset, "GETcapturesResponse200DataItemRelationshipsRefunds"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        reference_authorization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reference_authorization, Unset):
            reference_authorization = self.reference_authorization.to_dict()

        refunds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.refunds, Unset):
            refunds = self.refunds.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order
        if reference_authorization is not UNSET:
            field_dict["reference_authorization"] = reference_authorization
        if refunds is not UNSET:
            field_dict["refunds"] = refunds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tcaptures_response_200_data_item_relationships_order import (
            GETcapturesResponse200DataItemRelationshipsOrder,
        )
        from ..models.ge_tcaptures_response_200_data_item_relationships_reference_authorization import (
            GETcapturesResponse200DataItemRelationshipsReferenceAuthorization,
        )
        from ..models.ge_tcaptures_response_200_data_item_relationships_refunds import (
            GETcapturesResponse200DataItemRelationshipsRefunds,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, GETcapturesResponse200DataItemRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = GETcapturesResponse200DataItemRelationshipsOrder.from_dict(_order)

        _reference_authorization = d.pop("reference_authorization", UNSET)
        reference_authorization: Union[Unset, GETcapturesResponse200DataItemRelationshipsReferenceAuthorization]
        if isinstance(_reference_authorization, Unset):
            reference_authorization = UNSET
        else:
            reference_authorization = GETcapturesResponse200DataItemRelationshipsReferenceAuthorization.from_dict(
                _reference_authorization
            )

        _refunds = d.pop("refunds", UNSET)
        refunds: Union[Unset, GETcapturesResponse200DataItemRelationshipsRefunds]
        if isinstance(_refunds, Unset):
            refunds = UNSET
        else:
            refunds = GETcapturesResponse200DataItemRelationshipsRefunds.from_dict(_refunds)

        ge_tcaptures_response_200_data_item_relationships = cls(
            order=order,
            reference_authorization=reference_authorization,
            refunds=refunds,
        )

        ge_tcaptures_response_200_data_item_relationships.additional_properties = d
        return ge_tcaptures_response_200_data_item_relationships

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
