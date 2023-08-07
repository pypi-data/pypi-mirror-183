from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bundle_create_data_relationships_market import BundleCreateDataRelationshipsMarket
    from ..models.bundle_create_data_relationships_sku_list import BundleCreateDataRelationshipsSkuList


T = TypeVar("T", bound="BundleCreateDataRelationships")


@attr.s(auto_attribs=True)
class BundleCreateDataRelationships:
    """
    Attributes:
        sku_list (BundleCreateDataRelationshipsSkuList):
        market (Union[Unset, BundleCreateDataRelationshipsMarket]):
    """

    sku_list: "BundleCreateDataRelationshipsSkuList"
    market: Union[Unset, "BundleCreateDataRelationshipsMarket"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku_list = self.sku_list.to_dict()

        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sku_list": sku_list,
            }
        )
        if market is not UNSET:
            field_dict["market"] = market

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bundle_create_data_relationships_market import BundleCreateDataRelationshipsMarket
        from ..models.bundle_create_data_relationships_sku_list import BundleCreateDataRelationshipsSkuList

        d = src_dict.copy()
        sku_list = BundleCreateDataRelationshipsSkuList.from_dict(d.pop("sku_list"))

        _market = d.pop("market", UNSET)
        market: Union[Unset, BundleCreateDataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = BundleCreateDataRelationshipsMarket.from_dict(_market)

        bundle_create_data_relationships = cls(
            sku_list=sku_list,
            market=market,
        )

        bundle_create_data_relationships.additional_properties = d
        return bundle_create_data_relationships

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
