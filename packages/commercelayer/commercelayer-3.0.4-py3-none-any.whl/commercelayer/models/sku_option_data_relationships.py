from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sku_option_data_relationships_attachments import SkuOptionDataRelationshipsAttachments
    from ..models.sku_option_data_relationships_market import SkuOptionDataRelationshipsMarket


T = TypeVar("T", bound="SkuOptionDataRelationships")


@attr.s(auto_attribs=True)
class SkuOptionDataRelationships:
    """
    Attributes:
        market (Union[Unset, SkuOptionDataRelationshipsMarket]):
        attachments (Union[Unset, SkuOptionDataRelationshipsAttachments]):
    """

    market: Union[Unset, "SkuOptionDataRelationshipsMarket"] = UNSET
    attachments: Union[Unset, "SkuOptionDataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sku_option_data_relationships_attachments import SkuOptionDataRelationshipsAttachments
        from ..models.sku_option_data_relationships_market import SkuOptionDataRelationshipsMarket

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, SkuOptionDataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = SkuOptionDataRelationshipsMarket.from_dict(_market)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, SkuOptionDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = SkuOptionDataRelationshipsAttachments.from_dict(_attachments)

        sku_option_data_relationships = cls(
            market=market,
            attachments=attachments,
        )

        sku_option_data_relationships.additional_properties = d
        return sku_option_data_relationships

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
