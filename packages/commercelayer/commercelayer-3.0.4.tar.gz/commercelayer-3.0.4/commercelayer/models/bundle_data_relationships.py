from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bundle_data_relationships_attachments import BundleDataRelationshipsAttachments
    from ..models.bundle_data_relationships_market import BundleDataRelationshipsMarket
    from ..models.bundle_data_relationships_sku_list import BundleDataRelationshipsSkuList
    from ..models.bundle_data_relationships_skus import BundleDataRelationshipsSkus


T = TypeVar("T", bound="BundleDataRelationships")


@attr.s(auto_attribs=True)
class BundleDataRelationships:
    """
    Attributes:
        market (Union[Unset, BundleDataRelationshipsMarket]):
        sku_list (Union[Unset, BundleDataRelationshipsSkuList]):
        skus (Union[Unset, BundleDataRelationshipsSkus]):
        attachments (Union[Unset, BundleDataRelationshipsAttachments]):
    """

    market: Union[Unset, "BundleDataRelationshipsMarket"] = UNSET
    sku_list: Union[Unset, "BundleDataRelationshipsSkuList"] = UNSET
    skus: Union[Unset, "BundleDataRelationshipsSkus"] = UNSET
    attachments: Union[Unset, "BundleDataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        sku_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku_list, Unset):
            sku_list = self.sku_list.to_dict()

        skus: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.skus, Unset):
            skus = self.skus.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market
        if sku_list is not UNSET:
            field_dict["sku_list"] = sku_list
        if skus is not UNSET:
            field_dict["skus"] = skus
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bundle_data_relationships_attachments import BundleDataRelationshipsAttachments
        from ..models.bundle_data_relationships_market import BundleDataRelationshipsMarket
        from ..models.bundle_data_relationships_sku_list import BundleDataRelationshipsSkuList
        from ..models.bundle_data_relationships_skus import BundleDataRelationshipsSkus

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, BundleDataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = BundleDataRelationshipsMarket.from_dict(_market)

        _sku_list = d.pop("sku_list", UNSET)
        sku_list: Union[Unset, BundleDataRelationshipsSkuList]
        if isinstance(_sku_list, Unset):
            sku_list = UNSET
        else:
            sku_list = BundleDataRelationshipsSkuList.from_dict(_sku_list)

        _skus = d.pop("skus", UNSET)
        skus: Union[Unset, BundleDataRelationshipsSkus]
        if isinstance(_skus, Unset):
            skus = UNSET
        else:
            skus = BundleDataRelationshipsSkus.from_dict(_skus)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, BundleDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = BundleDataRelationshipsAttachments.from_dict(_attachments)

        bundle_data_relationships = cls(
            market=market,
            sku_list=sku_list,
            skus=skus,
            attachments=attachments,
        )

        bundle_data_relationships.additional_properties = d
        return bundle_data_relationships

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
