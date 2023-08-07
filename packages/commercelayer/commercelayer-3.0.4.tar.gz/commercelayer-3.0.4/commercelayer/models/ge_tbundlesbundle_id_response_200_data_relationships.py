from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tbundlesbundle_id_response_200_data_relationships_attachments import (
        GETbundlesbundleIdResponse200DataRelationshipsAttachments,
    )
    from ..models.ge_tbundlesbundle_id_response_200_data_relationships_market import (
        GETbundlesbundleIdResponse200DataRelationshipsMarket,
    )
    from ..models.ge_tbundlesbundle_id_response_200_data_relationships_sku_list import (
        GETbundlesbundleIdResponse200DataRelationshipsSkuList,
    )
    from ..models.ge_tbundlesbundle_id_response_200_data_relationships_skus import (
        GETbundlesbundleIdResponse200DataRelationshipsSkus,
    )


T = TypeVar("T", bound="GETbundlesbundleIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETbundlesbundleIdResponse200DataRelationships:
    """
    Attributes:
        market (Union[Unset, GETbundlesbundleIdResponse200DataRelationshipsMarket]):
        sku_list (Union[Unset, GETbundlesbundleIdResponse200DataRelationshipsSkuList]):
        skus (Union[Unset, GETbundlesbundleIdResponse200DataRelationshipsSkus]):
        attachments (Union[Unset, GETbundlesbundleIdResponse200DataRelationshipsAttachments]):
    """

    market: Union[Unset, "GETbundlesbundleIdResponse200DataRelationshipsMarket"] = UNSET
    sku_list: Union[Unset, "GETbundlesbundleIdResponse200DataRelationshipsSkuList"] = UNSET
    skus: Union[Unset, "GETbundlesbundleIdResponse200DataRelationshipsSkus"] = UNSET
    attachments: Union[Unset, "GETbundlesbundleIdResponse200DataRelationshipsAttachments"] = UNSET
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
        from ..models.ge_tbundlesbundle_id_response_200_data_relationships_attachments import (
            GETbundlesbundleIdResponse200DataRelationshipsAttachments,
        )
        from ..models.ge_tbundlesbundle_id_response_200_data_relationships_market import (
            GETbundlesbundleIdResponse200DataRelationshipsMarket,
        )
        from ..models.ge_tbundlesbundle_id_response_200_data_relationships_sku_list import (
            GETbundlesbundleIdResponse200DataRelationshipsSkuList,
        )
        from ..models.ge_tbundlesbundle_id_response_200_data_relationships_skus import (
            GETbundlesbundleIdResponse200DataRelationshipsSkus,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, GETbundlesbundleIdResponse200DataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = GETbundlesbundleIdResponse200DataRelationshipsMarket.from_dict(_market)

        _sku_list = d.pop("sku_list", UNSET)
        sku_list: Union[Unset, GETbundlesbundleIdResponse200DataRelationshipsSkuList]
        if isinstance(_sku_list, Unset):
            sku_list = UNSET
        else:
            sku_list = GETbundlesbundleIdResponse200DataRelationshipsSkuList.from_dict(_sku_list)

        _skus = d.pop("skus", UNSET)
        skus: Union[Unset, GETbundlesbundleIdResponse200DataRelationshipsSkus]
        if isinstance(_skus, Unset):
            skus = UNSET
        else:
            skus = GETbundlesbundleIdResponse200DataRelationshipsSkus.from_dict(_skus)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETbundlesbundleIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETbundlesbundleIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        ge_tbundlesbundle_id_response_200_data_relationships = cls(
            market=market,
            sku_list=sku_list,
            skus=skus,
            attachments=attachments,
        )

        ge_tbundlesbundle_id_response_200_data_relationships.additional_properties = d
        return ge_tbundlesbundle_id_response_200_data_relationships

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
