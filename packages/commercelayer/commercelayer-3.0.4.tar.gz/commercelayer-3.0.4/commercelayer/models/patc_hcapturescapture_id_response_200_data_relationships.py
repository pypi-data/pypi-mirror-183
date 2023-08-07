from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hcapturescapture_id_response_200_data_relationships_order import (
        PATCHcapturescaptureIdResponse200DataRelationshipsOrder,
    )
    from ..models.patc_hcapturescapture_id_response_200_data_relationships_reference_authorization import (
        PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorization,
    )
    from ..models.patc_hcapturescapture_id_response_200_data_relationships_refunds import (
        PATCHcapturescaptureIdResponse200DataRelationshipsRefunds,
    )


T = TypeVar("T", bound="PATCHcapturescaptureIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHcapturescaptureIdResponse200DataRelationships:
    """
    Attributes:
        order (Union[Unset, PATCHcapturescaptureIdResponse200DataRelationshipsOrder]):
        reference_authorization (Union[Unset,
            PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorization]):
        refunds (Union[Unset, PATCHcapturescaptureIdResponse200DataRelationshipsRefunds]):
    """

    order: Union[Unset, "PATCHcapturescaptureIdResponse200DataRelationshipsOrder"] = UNSET
    reference_authorization: Union[
        Unset, "PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorization"
    ] = UNSET
    refunds: Union[Unset, "PATCHcapturescaptureIdResponse200DataRelationshipsRefunds"] = UNSET
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
        from ..models.patc_hcapturescapture_id_response_200_data_relationships_order import (
            PATCHcapturescaptureIdResponse200DataRelationshipsOrder,
        )
        from ..models.patc_hcapturescapture_id_response_200_data_relationships_reference_authorization import (
            PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorization,
        )
        from ..models.patc_hcapturescapture_id_response_200_data_relationships_refunds import (
            PATCHcapturescaptureIdResponse200DataRelationshipsRefunds,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, PATCHcapturescaptureIdResponse200DataRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = PATCHcapturescaptureIdResponse200DataRelationshipsOrder.from_dict(_order)

        _reference_authorization = d.pop("reference_authorization", UNSET)
        reference_authorization: Union[Unset, PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorization]
        if isinstance(_reference_authorization, Unset):
            reference_authorization = UNSET
        else:
            reference_authorization = (
                PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorization.from_dict(
                    _reference_authorization
                )
            )

        _refunds = d.pop("refunds", UNSET)
        refunds: Union[Unset, PATCHcapturescaptureIdResponse200DataRelationshipsRefunds]
        if isinstance(_refunds, Unset):
            refunds = UNSET
        else:
            refunds = PATCHcapturescaptureIdResponse200DataRelationshipsRefunds.from_dict(_refunds)

        patc_hcapturescapture_id_response_200_data_relationships = cls(
            order=order,
            reference_authorization=reference_authorization,
            refunds=refunds,
        )

        patc_hcapturescapture_id_response_200_data_relationships.additional_properties = d
        return patc_hcapturescapture_id_response_200_data_relationships

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
