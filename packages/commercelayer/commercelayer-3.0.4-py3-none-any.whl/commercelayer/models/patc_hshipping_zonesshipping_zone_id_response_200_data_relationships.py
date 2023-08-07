from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hshipping_zonesshipping_zone_id_response_200_data_relationships_attachments import (
        PATCHshippingZonesshippingZoneIdResponse200DataRelationshipsAttachments,
    )


T = TypeVar("T", bound="PATCHshippingZonesshippingZoneIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHshippingZonesshippingZoneIdResponse200DataRelationships:
    """
    Attributes:
        attachments (Union[Unset, PATCHshippingZonesshippingZoneIdResponse200DataRelationshipsAttachments]):
    """

    attachments: Union[Unset, "PATCHshippingZonesshippingZoneIdResponse200DataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hshipping_zonesshipping_zone_id_response_200_data_relationships_attachments import (
            PATCHshippingZonesshippingZoneIdResponse200DataRelationshipsAttachments,
        )

        d = src_dict.copy()
        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHshippingZonesshippingZoneIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PATCHshippingZonesshippingZoneIdResponse200DataRelationshipsAttachments.from_dict(
                _attachments
            )

        patc_hshipping_zonesshipping_zone_id_response_200_data_relationships = cls(
            attachments=attachments,
        )

        patc_hshipping_zonesshipping_zone_id_response_200_data_relationships.additional_properties = d
        return patc_hshipping_zonesshipping_zone_id_response_200_data_relationships

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
