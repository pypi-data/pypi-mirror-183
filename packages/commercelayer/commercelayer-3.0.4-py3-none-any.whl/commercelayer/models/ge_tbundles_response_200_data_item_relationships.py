from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tbundles_response_200_data_item_relationships_attachments import (
        GETbundlesResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tbundles_response_200_data_item_relationships_market import (
        GETbundlesResponse200DataItemRelationshipsMarket,
    )
    from ..models.ge_tbundles_response_200_data_item_relationships_sku_list import (
        GETbundlesResponse200DataItemRelationshipsSkuList,
    )
    from ..models.ge_tbundles_response_200_data_item_relationships_skus import (
        GETbundlesResponse200DataItemRelationshipsSkus,
    )


T = TypeVar("T", bound="GETbundlesResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETbundlesResponse200DataItemRelationships:
    """
    Attributes:
        market (Union[Unset, GETbundlesResponse200DataItemRelationshipsMarket]):
        sku_list (Union[Unset, GETbundlesResponse200DataItemRelationshipsSkuList]):
        skus (Union[Unset, GETbundlesResponse200DataItemRelationshipsSkus]):
        attachments (Union[Unset, GETbundlesResponse200DataItemRelationshipsAttachments]):
    """

    market: Union[Unset, "GETbundlesResponse200DataItemRelationshipsMarket"] = UNSET
    sku_list: Union[Unset, "GETbundlesResponse200DataItemRelationshipsSkuList"] = UNSET
    skus: Union[Unset, "GETbundlesResponse200DataItemRelationshipsSkus"] = UNSET
    attachments: Union[Unset, "GETbundlesResponse200DataItemRelationshipsAttachments"] = UNSET
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
        from ..models.ge_tbundles_response_200_data_item_relationships_attachments import (
            GETbundlesResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tbundles_response_200_data_item_relationships_market import (
            GETbundlesResponse200DataItemRelationshipsMarket,
        )
        from ..models.ge_tbundles_response_200_data_item_relationships_sku_list import (
            GETbundlesResponse200DataItemRelationshipsSkuList,
        )
        from ..models.ge_tbundles_response_200_data_item_relationships_skus import (
            GETbundlesResponse200DataItemRelationshipsSkus,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, GETbundlesResponse200DataItemRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = GETbundlesResponse200DataItemRelationshipsMarket.from_dict(_market)

        _sku_list = d.pop("sku_list", UNSET)
        sku_list: Union[Unset, GETbundlesResponse200DataItemRelationshipsSkuList]
        if isinstance(_sku_list, Unset):
            sku_list = UNSET
        else:
            sku_list = GETbundlesResponse200DataItemRelationshipsSkuList.from_dict(_sku_list)

        _skus = d.pop("skus", UNSET)
        skus: Union[Unset, GETbundlesResponse200DataItemRelationshipsSkus]
        if isinstance(_skus, Unset):
            skus = UNSET
        else:
            skus = GETbundlesResponse200DataItemRelationshipsSkus.from_dict(_skus)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETbundlesResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETbundlesResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        ge_tbundles_response_200_data_item_relationships = cls(
            market=market,
            sku_list=sku_list,
            skus=skus,
            attachments=attachments,
        )

        ge_tbundles_response_200_data_item_relationships.additional_properties = d
        return ge_tbundles_response_200_data_item_relationships

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
