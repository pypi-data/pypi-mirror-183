from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hprice_volume_tiersprice_volume_tier_id_response_200_data_relationships_attachments import (
        PATCHpriceVolumeTierspriceVolumeTierIdResponse200DataRelationshipsAttachments,
    )
    from ..models.patc_hprice_volume_tiersprice_volume_tier_id_response_200_data_relationships_price import (
        PATCHpriceVolumeTierspriceVolumeTierIdResponse200DataRelationshipsPrice,
    )


T = TypeVar("T", bound="PATCHpriceVolumeTierspriceVolumeTierIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHpriceVolumeTierspriceVolumeTierIdResponse200DataRelationships:
    """
    Attributes:
        price (Union[Unset, PATCHpriceVolumeTierspriceVolumeTierIdResponse200DataRelationshipsPrice]):
        attachments (Union[Unset, PATCHpriceVolumeTierspriceVolumeTierIdResponse200DataRelationshipsAttachments]):
    """

    price: Union[Unset, "PATCHpriceVolumeTierspriceVolumeTierIdResponse200DataRelationshipsPrice"] = UNSET
    attachments: Union[Unset, "PATCHpriceVolumeTierspriceVolumeTierIdResponse200DataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price is not UNSET:
            field_dict["price"] = price
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hprice_volume_tiersprice_volume_tier_id_response_200_data_relationships_attachments import (
            PATCHpriceVolumeTierspriceVolumeTierIdResponse200DataRelationshipsAttachments,
        )
        from ..models.patc_hprice_volume_tiersprice_volume_tier_id_response_200_data_relationships_price import (
            PATCHpriceVolumeTierspriceVolumeTierIdResponse200DataRelationshipsPrice,
        )

        d = src_dict.copy()
        _price = d.pop("price", UNSET)
        price: Union[Unset, PATCHpriceVolumeTierspriceVolumeTierIdResponse200DataRelationshipsPrice]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = PATCHpriceVolumeTierspriceVolumeTierIdResponse200DataRelationshipsPrice.from_dict(_price)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHpriceVolumeTierspriceVolumeTierIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PATCHpriceVolumeTierspriceVolumeTierIdResponse200DataRelationshipsAttachments.from_dict(
                _attachments
            )

        patc_hprice_volume_tiersprice_volume_tier_id_response_200_data_relationships = cls(
            price=price,
            attachments=attachments,
        )

        patc_hprice_volume_tiersprice_volume_tier_id_response_200_data_relationships.additional_properties = d
        return patc_hprice_volume_tiersprice_volume_tier_id_response_200_data_relationships

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
