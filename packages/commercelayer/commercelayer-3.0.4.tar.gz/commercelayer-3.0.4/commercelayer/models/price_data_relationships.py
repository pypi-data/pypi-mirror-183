from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_data_relationships_attachments import PriceDataRelationshipsAttachments
    from ..models.price_data_relationships_price_list import PriceDataRelationshipsPriceList
    from ..models.price_data_relationships_price_tiers import PriceDataRelationshipsPriceTiers
    from ..models.price_data_relationships_price_volume_tiers import PriceDataRelationshipsPriceVolumeTiers
    from ..models.price_data_relationships_sku import PriceDataRelationshipsSku


T = TypeVar("T", bound="PriceDataRelationships")


@attr.s(auto_attribs=True)
class PriceDataRelationships:
    """
    Attributes:
        price_list (Union[Unset, PriceDataRelationshipsPriceList]):
        sku (Union[Unset, PriceDataRelationshipsSku]):
        price_tiers (Union[Unset, PriceDataRelationshipsPriceTiers]):
        price_volume_tiers (Union[Unset, PriceDataRelationshipsPriceVolumeTiers]):
        attachments (Union[Unset, PriceDataRelationshipsAttachments]):
    """

    price_list: Union[Unset, "PriceDataRelationshipsPriceList"] = UNSET
    sku: Union[Unset, "PriceDataRelationshipsSku"] = UNSET
    price_tiers: Union[Unset, "PriceDataRelationshipsPriceTiers"] = UNSET
    price_volume_tiers: Union[Unset, "PriceDataRelationshipsPriceVolumeTiers"] = UNSET
    attachments: Union[Unset, "PriceDataRelationshipsAttachments"] = UNSET
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
        from ..models.price_data_relationships_attachments import PriceDataRelationshipsAttachments
        from ..models.price_data_relationships_price_list import PriceDataRelationshipsPriceList
        from ..models.price_data_relationships_price_tiers import PriceDataRelationshipsPriceTiers
        from ..models.price_data_relationships_price_volume_tiers import PriceDataRelationshipsPriceVolumeTiers
        from ..models.price_data_relationships_sku import PriceDataRelationshipsSku

        d = src_dict.copy()
        _price_list = d.pop("price_list", UNSET)
        price_list: Union[Unset, PriceDataRelationshipsPriceList]
        if isinstance(_price_list, Unset):
            price_list = UNSET
        else:
            price_list = PriceDataRelationshipsPriceList.from_dict(_price_list)

        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, PriceDataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = PriceDataRelationshipsSku.from_dict(_sku)

        _price_tiers = d.pop("price_tiers", UNSET)
        price_tiers: Union[Unset, PriceDataRelationshipsPriceTiers]
        if isinstance(_price_tiers, Unset):
            price_tiers = UNSET
        else:
            price_tiers = PriceDataRelationshipsPriceTiers.from_dict(_price_tiers)

        _price_volume_tiers = d.pop("price_volume_tiers", UNSET)
        price_volume_tiers: Union[Unset, PriceDataRelationshipsPriceVolumeTiers]
        if isinstance(_price_volume_tiers, Unset):
            price_volume_tiers = UNSET
        else:
            price_volume_tiers = PriceDataRelationshipsPriceVolumeTiers.from_dict(_price_volume_tiers)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PriceDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PriceDataRelationshipsAttachments.from_dict(_attachments)

        price_data_relationships = cls(
            price_list=price_list,
            sku=sku,
            price_tiers=price_tiers,
            price_volume_tiers=price_volume_tiers,
            attachments=attachments,
        )

        price_data_relationships.additional_properties = d
        return price_data_relationships

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
