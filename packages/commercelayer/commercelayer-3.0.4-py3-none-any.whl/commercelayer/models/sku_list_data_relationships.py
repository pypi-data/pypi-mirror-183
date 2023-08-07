from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sku_list_data_relationships_attachments import SkuListDataRelationshipsAttachments
    from ..models.sku_list_data_relationships_bundles import SkuListDataRelationshipsBundles
    from ..models.sku_list_data_relationships_customer import SkuListDataRelationshipsCustomer
    from ..models.sku_list_data_relationships_sku_list_items import SkuListDataRelationshipsSkuListItems
    from ..models.sku_list_data_relationships_skus import SkuListDataRelationshipsSkus


T = TypeVar("T", bound="SkuListDataRelationships")


@attr.s(auto_attribs=True)
class SkuListDataRelationships:
    """
    Attributes:
        customer (Union[Unset, SkuListDataRelationshipsCustomer]):
        skus (Union[Unset, SkuListDataRelationshipsSkus]):
        sku_list_items (Union[Unset, SkuListDataRelationshipsSkuListItems]):
        bundles (Union[Unset, SkuListDataRelationshipsBundles]):
        attachments (Union[Unset, SkuListDataRelationshipsAttachments]):
    """

    customer: Union[Unset, "SkuListDataRelationshipsCustomer"] = UNSET
    skus: Union[Unset, "SkuListDataRelationshipsSkus"] = UNSET
    sku_list_items: Union[Unset, "SkuListDataRelationshipsSkuListItems"] = UNSET
    bundles: Union[Unset, "SkuListDataRelationshipsBundles"] = UNSET
    attachments: Union[Unset, "SkuListDataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        skus: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.skus, Unset):
            skus = self.skus.to_dict()

        sku_list_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku_list_items, Unset):
            sku_list_items = self.sku_list_items.to_dict()

        bundles: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bundles, Unset):
            bundles = self.bundles.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer is not UNSET:
            field_dict["customer"] = customer
        if skus is not UNSET:
            field_dict["skus"] = skus
        if sku_list_items is not UNSET:
            field_dict["sku_list_items"] = sku_list_items
        if bundles is not UNSET:
            field_dict["bundles"] = bundles
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sku_list_data_relationships_attachments import SkuListDataRelationshipsAttachments
        from ..models.sku_list_data_relationships_bundles import SkuListDataRelationshipsBundles
        from ..models.sku_list_data_relationships_customer import SkuListDataRelationshipsCustomer
        from ..models.sku_list_data_relationships_sku_list_items import SkuListDataRelationshipsSkuListItems
        from ..models.sku_list_data_relationships_skus import SkuListDataRelationshipsSkus

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, SkuListDataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = SkuListDataRelationshipsCustomer.from_dict(_customer)

        _skus = d.pop("skus", UNSET)
        skus: Union[Unset, SkuListDataRelationshipsSkus]
        if isinstance(_skus, Unset):
            skus = UNSET
        else:
            skus = SkuListDataRelationshipsSkus.from_dict(_skus)

        _sku_list_items = d.pop("sku_list_items", UNSET)
        sku_list_items: Union[Unset, SkuListDataRelationshipsSkuListItems]
        if isinstance(_sku_list_items, Unset):
            sku_list_items = UNSET
        else:
            sku_list_items = SkuListDataRelationshipsSkuListItems.from_dict(_sku_list_items)

        _bundles = d.pop("bundles", UNSET)
        bundles: Union[Unset, SkuListDataRelationshipsBundles]
        if isinstance(_bundles, Unset):
            bundles = UNSET
        else:
            bundles = SkuListDataRelationshipsBundles.from_dict(_bundles)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, SkuListDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = SkuListDataRelationshipsAttachments.from_dict(_attachments)

        sku_list_data_relationships = cls(
            customer=customer,
            skus=skus,
            sku_list_items=sku_list_items,
            bundles=bundles,
            attachments=attachments,
        )

        sku_list_data_relationships.additional_properties = d
        return sku_list_data_relationships

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
