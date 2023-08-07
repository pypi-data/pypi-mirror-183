from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcapturescapture_id_response_200_data_relationships_order import (
        GETcapturescaptureIdResponse200DataRelationshipsOrder,
    )
    from ..models.ge_tcapturescapture_id_response_200_data_relationships_reference_authorization import (
        GETcapturescaptureIdResponse200DataRelationshipsReferenceAuthorization,
    )
    from ..models.ge_tcapturescapture_id_response_200_data_relationships_refunds import (
        GETcapturescaptureIdResponse200DataRelationshipsRefunds,
    )


T = TypeVar("T", bound="GETcapturescaptureIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETcapturescaptureIdResponse200DataRelationships:
    """
    Attributes:
        order (Union[Unset, GETcapturescaptureIdResponse200DataRelationshipsOrder]):
        reference_authorization (Union[Unset, GETcapturescaptureIdResponse200DataRelationshipsReferenceAuthorization]):
        refunds (Union[Unset, GETcapturescaptureIdResponse200DataRelationshipsRefunds]):
    """

    order: Union[Unset, "GETcapturescaptureIdResponse200DataRelationshipsOrder"] = UNSET
    reference_authorization: Union[
        Unset, "GETcapturescaptureIdResponse200DataRelationshipsReferenceAuthorization"
    ] = UNSET
    refunds: Union[Unset, "GETcapturescaptureIdResponse200DataRelationshipsRefunds"] = UNSET
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
        from ..models.ge_tcapturescapture_id_response_200_data_relationships_order import (
            GETcapturescaptureIdResponse200DataRelationshipsOrder,
        )
        from ..models.ge_tcapturescapture_id_response_200_data_relationships_reference_authorization import (
            GETcapturescaptureIdResponse200DataRelationshipsReferenceAuthorization,
        )
        from ..models.ge_tcapturescapture_id_response_200_data_relationships_refunds import (
            GETcapturescaptureIdResponse200DataRelationshipsRefunds,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, GETcapturescaptureIdResponse200DataRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = GETcapturescaptureIdResponse200DataRelationshipsOrder.from_dict(_order)

        _reference_authorization = d.pop("reference_authorization", UNSET)
        reference_authorization: Union[Unset, GETcapturescaptureIdResponse200DataRelationshipsReferenceAuthorization]
        if isinstance(_reference_authorization, Unset):
            reference_authorization = UNSET
        else:
            reference_authorization = GETcapturescaptureIdResponse200DataRelationshipsReferenceAuthorization.from_dict(
                _reference_authorization
            )

        _refunds = d.pop("refunds", UNSET)
        refunds: Union[Unset, GETcapturescaptureIdResponse200DataRelationshipsRefunds]
        if isinstance(_refunds, Unset):
            refunds = UNSET
        else:
            refunds = GETcapturescaptureIdResponse200DataRelationshipsRefunds.from_dict(_refunds)

        ge_tcapturescapture_id_response_200_data_relationships = cls(
            order=order,
            reference_authorization=reference_authorization,
            refunds=refunds,
        )

        ge_tcapturescapture_id_response_200_data_relationships.additional_properties = d
        return ge_tcapturescapture_id_response_200_data_relationships

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
