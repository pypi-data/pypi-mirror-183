from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tprice_tiersprice_tier_id_response_200_data_relationships_attachments import (
        GETpriceTierspriceTierIdResponse200DataRelationshipsAttachments,
    )
    from ..models.ge_tprice_tiersprice_tier_id_response_200_data_relationships_price import (
        GETpriceTierspriceTierIdResponse200DataRelationshipsPrice,
    )


T = TypeVar("T", bound="GETpriceTierspriceTierIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETpriceTierspriceTierIdResponse200DataRelationships:
    """
    Attributes:
        price (Union[Unset, GETpriceTierspriceTierIdResponse200DataRelationshipsPrice]):
        attachments (Union[Unset, GETpriceTierspriceTierIdResponse200DataRelationshipsAttachments]):
    """

    price: Union[Unset, "GETpriceTierspriceTierIdResponse200DataRelationshipsPrice"] = UNSET
    attachments: Union[Unset, "GETpriceTierspriceTierIdResponse200DataRelationshipsAttachments"] = UNSET
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
        from ..models.ge_tprice_tiersprice_tier_id_response_200_data_relationships_attachments import (
            GETpriceTierspriceTierIdResponse200DataRelationshipsAttachments,
        )
        from ..models.ge_tprice_tiersprice_tier_id_response_200_data_relationships_price import (
            GETpriceTierspriceTierIdResponse200DataRelationshipsPrice,
        )

        d = src_dict.copy()
        _price = d.pop("price", UNSET)
        price: Union[Unset, GETpriceTierspriceTierIdResponse200DataRelationshipsPrice]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = GETpriceTierspriceTierIdResponse200DataRelationshipsPrice.from_dict(_price)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETpriceTierspriceTierIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETpriceTierspriceTierIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        ge_tprice_tiersprice_tier_id_response_200_data_relationships = cls(
            price=price,
            attachments=attachments,
        )

        ge_tprice_tiersprice_tier_id_response_200_data_relationships.additional_properties = d
        return ge_tprice_tiersprice_tier_id_response_200_data_relationships

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
