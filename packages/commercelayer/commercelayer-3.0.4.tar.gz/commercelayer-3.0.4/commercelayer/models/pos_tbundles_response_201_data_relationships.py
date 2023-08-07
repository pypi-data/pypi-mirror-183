from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tbundles_response_201_data_relationships_attachments import (
        POSTbundlesResponse201DataRelationshipsAttachments,
    )
    from ..models.pos_tbundles_response_201_data_relationships_market import (
        POSTbundlesResponse201DataRelationshipsMarket,
    )
    from ..models.pos_tbundles_response_201_data_relationships_sku_list import (
        POSTbundlesResponse201DataRelationshipsSkuList,
    )
    from ..models.pos_tbundles_response_201_data_relationships_skus import POSTbundlesResponse201DataRelationshipsSkus


T = TypeVar("T", bound="POSTbundlesResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTbundlesResponse201DataRelationships:
    """
    Attributes:
        market (Union[Unset, POSTbundlesResponse201DataRelationshipsMarket]):
        sku_list (Union[Unset, POSTbundlesResponse201DataRelationshipsSkuList]):
        skus (Union[Unset, POSTbundlesResponse201DataRelationshipsSkus]):
        attachments (Union[Unset, POSTbundlesResponse201DataRelationshipsAttachments]):
    """

    market: Union[Unset, "POSTbundlesResponse201DataRelationshipsMarket"] = UNSET
    sku_list: Union[Unset, "POSTbundlesResponse201DataRelationshipsSkuList"] = UNSET
    skus: Union[Unset, "POSTbundlesResponse201DataRelationshipsSkus"] = UNSET
    attachments: Union[Unset, "POSTbundlesResponse201DataRelationshipsAttachments"] = UNSET
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
        from ..models.pos_tbundles_response_201_data_relationships_attachments import (
            POSTbundlesResponse201DataRelationshipsAttachments,
        )
        from ..models.pos_tbundles_response_201_data_relationships_market import (
            POSTbundlesResponse201DataRelationshipsMarket,
        )
        from ..models.pos_tbundles_response_201_data_relationships_sku_list import (
            POSTbundlesResponse201DataRelationshipsSkuList,
        )
        from ..models.pos_tbundles_response_201_data_relationships_skus import (
            POSTbundlesResponse201DataRelationshipsSkus,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, POSTbundlesResponse201DataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = POSTbundlesResponse201DataRelationshipsMarket.from_dict(_market)

        _sku_list = d.pop("sku_list", UNSET)
        sku_list: Union[Unset, POSTbundlesResponse201DataRelationshipsSkuList]
        if isinstance(_sku_list, Unset):
            sku_list = UNSET
        else:
            sku_list = POSTbundlesResponse201DataRelationshipsSkuList.from_dict(_sku_list)

        _skus = d.pop("skus", UNSET)
        skus: Union[Unset, POSTbundlesResponse201DataRelationshipsSkus]
        if isinstance(_skus, Unset):
            skus = UNSET
        else:
            skus = POSTbundlesResponse201DataRelationshipsSkus.from_dict(_skus)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, POSTbundlesResponse201DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = POSTbundlesResponse201DataRelationshipsAttachments.from_dict(_attachments)

        pos_tbundles_response_201_data_relationships = cls(
            market=market,
            sku_list=sku_list,
            skus=skus,
            attachments=attachments,
        )

        pos_tbundles_response_201_data_relationships.additional_properties = d
        return pos_tbundles_response_201_data_relationships

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
