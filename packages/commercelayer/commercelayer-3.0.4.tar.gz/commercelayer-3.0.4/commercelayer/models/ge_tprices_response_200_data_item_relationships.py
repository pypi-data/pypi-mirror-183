from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tprices_response_200_data_item_relationships_attachments import (
        GETpricesResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tprices_response_200_data_item_relationships_price_list import (
        GETpricesResponse200DataItemRelationshipsPriceList,
    )
    from ..models.ge_tprices_response_200_data_item_relationships_price_tiers import (
        GETpricesResponse200DataItemRelationshipsPriceTiers,
    )
    from ..models.ge_tprices_response_200_data_item_relationships_price_volume_tiers import (
        GETpricesResponse200DataItemRelationshipsPriceVolumeTiers,
    )
    from ..models.ge_tprices_response_200_data_item_relationships_sku import (
        GETpricesResponse200DataItemRelationshipsSku,
    )


T = TypeVar("T", bound="GETpricesResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETpricesResponse200DataItemRelationships:
    """
    Attributes:
        price_list (Union[Unset, GETpricesResponse200DataItemRelationshipsPriceList]):
        sku (Union[Unset, GETpricesResponse200DataItemRelationshipsSku]):
        price_tiers (Union[Unset, GETpricesResponse200DataItemRelationshipsPriceTiers]):
        price_volume_tiers (Union[Unset, GETpricesResponse200DataItemRelationshipsPriceVolumeTiers]):
        attachments (Union[Unset, GETpricesResponse200DataItemRelationshipsAttachments]):
    """

    price_list: Union[Unset, "GETpricesResponse200DataItemRelationshipsPriceList"] = UNSET
    sku: Union[Unset, "GETpricesResponse200DataItemRelationshipsSku"] = UNSET
    price_tiers: Union[Unset, "GETpricesResponse200DataItemRelationshipsPriceTiers"] = UNSET
    price_volume_tiers: Union[Unset, "GETpricesResponse200DataItemRelationshipsPriceVolumeTiers"] = UNSET
    attachments: Union[Unset, "GETpricesResponse200DataItemRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_list, Unset):
            price_list = self.price_list.to_dict()

        sku: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku, Unset):
            sku = self.sku.to_dict()

        price_tiers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_tiers, Unset):
            price_tiers = self.price_tiers.to_dict()

        price_volume_tiers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_volume_tiers, Unset):
            price_volume_tiers = self.price_volume_tiers.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price_list is not UNSET:
            field_dict["price_list"] = price_list
        if sku is not UNSET:
            field_dict["sku"] = sku
        if price_tiers is not UNSET:
            field_dict["price_tiers"] = price_tiers
        if price_volume_tiers is not UNSET:
            field_dict["price_volume_tiers"] = price_volume_tiers
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tprices_response_200_data_item_relationships_attachments import (
            GETpricesResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tprices_response_200_data_item_relationships_price_list import (
            GETpricesResponse200DataItemRelationshipsPriceList,
        )
        from ..models.ge_tprices_response_200_data_item_relationships_price_tiers import (
            GETpricesResponse200DataItemRelationshipsPriceTiers,
        )
        from ..models.ge_tprices_response_200_data_item_relationships_price_volume_tiers import (
            GETpricesResponse200DataItemRelationshipsPriceVolumeTiers,
        )
        from ..models.ge_tprices_response_200_data_item_relationships_sku import (
            GETpricesResponse200DataItemRelationshipsSku,
        )

        d = src_dict.copy()
        _price_list = d.pop("price_list", UNSET)
        price_list: Union[Unset, GETpricesResponse200DataItemRelationshipsPriceList]
        if isinstance(_price_list, Unset):
            price_list = UNSET
        else:
            price_list = GETpricesResponse200DataItemRelationshipsPriceList.from_dict(_price_list)

        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, GETpricesResponse200DataItemRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = GETpricesResponse200DataItemRelationshipsSku.from_dict(_sku)

        _price_tiers = d.pop("price_tiers", UNSET)
        price_tiers: Union[Unset, GETpricesResponse200DataItemRelationshipsPriceTiers]
        if isinstance(_price_tiers, Unset):
            price_tiers = UNSET
        else:
            price_tiers = GETpricesResponse200DataItemRelationshipsPriceTiers.from_dict(_price_tiers)

        _price_volume_tiers = d.pop("price_volume_tiers", UNSET)
        price_volume_tiers: Union[Unset, GETpricesResponse200DataItemRelationshipsPriceVolumeTiers]
        if isinstance(_price_volume_tiers, Unset):
            price_volume_tiers = UNSET
        else:
            price_volume_tiers = GETpricesResponse200DataItemRelationshipsPriceVolumeTiers.from_dict(
                _price_volume_tiers
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETpricesResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETpricesResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        ge_tprices_response_200_data_item_relationships = cls(
            price_list=price_list,
            sku=sku,
            price_tiers=price_tiers,
            price_volume_tiers=price_volume_tiers,
            attachments=attachments,
        )

        ge_tprices_response_200_data_item_relationships.additional_properties = d
        return ge_tprices_response_200_data_item_relationships

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
