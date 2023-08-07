from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipping_zone_data_relationships_attachments import ShippingZoneDataRelationshipsAttachments


T = TypeVar("T", bound="ShippingZoneDataRelationships")


@attr.s(auto_attribs=True)
class ShippingZoneDataRelationships:
    """
    Attributes:
        attachments (Union[Unset, ShippingZoneDataRelationshipsAttachments]):
    """

    attachments: Union[Unset, "ShippingZoneDataRelationshipsAttachments"] = UNSET
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
        from ..models.shipping_zone_data_relationships_attachments import ShippingZoneDataRelationshipsAttachments

        d = src_dict.copy()
        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, ShippingZoneDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = ShippingZoneDataRelationshipsAttachments.from_dict(_attachments)

        shipping_zone_data_relationships = cls(
            attachments=attachments,
        )

        shipping_zone_data_relationships.additional_properties = d
        return shipping_zone_data_relationships

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
