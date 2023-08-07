from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tprices_response_201_data_relationships_attachments import (
        POSTpricesResponse201DataRelationshipsAttachments,
    )
    from ..models.pos_tprices_response_201_data_relationships_price_list import (
        POSTpricesResponse201DataRelationshipsPriceList,
    )
    from ..models.pos_tprices_response_201_data_relationships_price_tiers import (
        POSTpricesResponse201DataRelationshipsPriceTiers,
    )
    from ..models.pos_tprices_response_201_data_relationships_price_volume_tiers import (
        POSTpricesResponse201DataRelationshipsPriceVolumeTiers,
    )
    from ..models.pos_tprices_response_201_data_relationships_sku import POSTpricesResponse201DataRelationshipsSku


T = TypeVar("T", bound="POSTpricesResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTpricesResponse201DataRelationships:
    """
    Attributes:
        price_list (Union[Unset, POSTpricesResponse201DataRelationshipsPriceList]):
        sku (Union[Unset, POSTpricesResponse201DataRelationshipsSku]):
        price_tiers (Union[Unset, POSTpricesResponse201DataRelationshipsPriceTiers]):
        price_volume_tiers (Union[Unset, POSTpricesResponse201DataRelationshipsPriceVolumeTiers]):
        attachments (Union[Unset, POSTpricesResponse201DataRelationshipsAttachments]):
    """

    price_list: Union[Unset, "POSTpricesResponse201DataRelationshipsPriceList"] = UNSET
    sku: Union[Unset, "POSTpricesResponse201DataRelationshipsSku"] = UNSET
    price_tiers: Union[Unset, "POSTpricesResponse201DataRelationshipsPriceTiers"] = UNSET
    price_volume_tiers: Union[Unset, "POSTpricesResponse201DataRelationshipsPriceVolumeTiers"] = UNSET
    attachments: Union[Unset, "POSTpricesResponse201DataRelationshipsAttachments"] = UNSET
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
        from ..models.pos_tprices_response_201_data_relationships_attachments import (
            POSTpricesResponse201DataRelationshipsAttachments,
        )
        from ..models.pos_tprices_response_201_data_relationships_price_list import (
            POSTpricesResponse201DataRelationshipsPriceList,
        )
        from ..models.pos_tprices_response_201_data_relationships_price_tiers import (
            POSTpricesResponse201DataRelationshipsPriceTiers,
        )
        from ..models.pos_tprices_response_201_data_relationships_price_volume_tiers import (
            POSTpricesResponse201DataRelationshipsPriceVolumeTiers,
        )
        from ..models.pos_tprices_response_201_data_relationships_sku import POSTpricesResponse201DataRelationshipsSku

        d = src_dict.copy()
        _price_list = d.pop("price_list", UNSET)
        price_list: Union[Unset, POSTpricesResponse201DataRelationshipsPriceList]
        if isinstance(_price_list, Unset):
            price_list = UNSET
        else:
            price_list = POSTpricesResponse201DataRelationshipsPriceList.from_dict(_price_list)

        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, POSTpricesResponse201DataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = POSTpricesResponse201DataRelationshipsSku.from_dict(_sku)

        _price_tiers = d.pop("price_tiers", UNSET)
        price_tiers: Union[Unset, POSTpricesResponse201DataRelationshipsPriceTiers]
        if isinstance(_price_tiers, Unset):
            price_tiers = UNSET
        else:
            price_tiers = POSTpricesResponse201DataRelationshipsPriceTiers.from_dict(_price_tiers)

        _price_volume_tiers = d.pop("price_volume_tiers", UNSET)
        price_volume_tiers: Union[Unset, POSTpricesResponse201DataRelationshipsPriceVolumeTiers]
        if isinstance(_price_volume_tiers, Unset):
            price_volume_tiers = UNSET
        else:
            price_volume_tiers = POSTpricesResponse201DataRelationshipsPriceVolumeTiers.from_dict(_price_volume_tiers)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, POSTpricesResponse201DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = POSTpricesResponse201DataRelationshipsAttachments.from_dict(_attachments)

        pos_tprices_response_201_data_relationships = cls(
            price_list=price_list,
            sku=sku,
            price_tiers=price_tiers,
            price_volume_tiers=price_volume_tiers,
            attachments=attachments,
        )

        pos_tprices_response_201_data_relationships.additional_properties = d
        return pos_tprices_response_201_data_relationships

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
