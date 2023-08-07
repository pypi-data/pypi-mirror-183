from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.market_data_relationships_attachments import MarketDataRelationshipsAttachments
    from ..models.market_data_relationships_customer_group import MarketDataRelationshipsCustomerGroup
    from ..models.market_data_relationships_inventory_model import MarketDataRelationshipsInventoryModel
    from ..models.market_data_relationships_merchant import MarketDataRelationshipsMerchant
    from ..models.market_data_relationships_price_list import MarketDataRelationshipsPriceList
    from ..models.market_data_relationships_tax_calculator import MarketDataRelationshipsTaxCalculator


T = TypeVar("T", bound="MarketDataRelationships")


@attr.s(auto_attribs=True)
class MarketDataRelationships:
    """
    Attributes:
        merchant (Union[Unset, MarketDataRelationshipsMerchant]):
        price_list (Union[Unset, MarketDataRelationshipsPriceList]):
        inventory_model (Union[Unset, MarketDataRelationshipsInventoryModel]):
        tax_calculator (Union[Unset, MarketDataRelationshipsTaxCalculator]):
        customer_group (Union[Unset, MarketDataRelationshipsCustomerGroup]):
        attachments (Union[Unset, MarketDataRelationshipsAttachments]):
    """

    merchant: Union[Unset, "MarketDataRelationshipsMerchant"] = UNSET
    price_list: Union[Unset, "MarketDataRelationshipsPriceList"] = UNSET
    inventory_model: Union[Unset, "MarketDataRelationshipsInventoryModel"] = UNSET
    tax_calculator: Union[Unset, "MarketDataRelationshipsTaxCalculator"] = UNSET
    customer_group: Union[Unset, "MarketDataRelationshipsCustomerGroup"] = UNSET
    attachments: Union[Unset, "MarketDataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        merchant: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        price_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_list, Unset):
            price_list = self.price_list.to_dict()

        inventory_model: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_model, Unset):
            inventory_model = self.inventory_model.to_dict()

        tax_calculator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_calculator, Unset):
            tax_calculator = self.tax_calculator.to_dict()

        customer_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_group, Unset):
            customer_group = self.customer_group.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if price_list is not UNSET:
            field_dict["price_list"] = price_list
        if inventory_model is not UNSET:
            field_dict["inventory_model"] = inventory_model
        if tax_calculator is not UNSET:
            field_dict["tax_calculator"] = tax_calculator
        if customer_group is not UNSET:
            field_dict["customer_group"] = customer_group
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.market_data_relationships_attachments import MarketDataRelationshipsAttachments
        from ..models.market_data_relationships_customer_group import MarketDataRelationshipsCustomerGroup
        from ..models.market_data_relationships_inventory_model import MarketDataRelationshipsInventoryModel
        from ..models.market_data_relationships_merchant import MarketDataRelationshipsMerchant
        from ..models.market_data_relationships_price_list import MarketDataRelationshipsPriceList
        from ..models.market_data_relationships_tax_calculator import MarketDataRelationshipsTaxCalculator

        d = src_dict.copy()
        _merchant = d.pop("merchant", UNSET)
        merchant: Union[Unset, MarketDataRelationshipsMerchant]
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = MarketDataRelationshipsMerchant.from_dict(_merchant)

        _price_list = d.pop("price_list", UNSET)
        price_list: Union[Unset, MarketDataRelationshipsPriceList]
        if isinstance(_price_list, Unset):
            price_list = UNSET
        else:
            price_list = MarketDataRelationshipsPriceList.from_dict(_price_list)

        _inventory_model = d.pop("inventory_model", UNSET)
        inventory_model: Union[Unset, MarketDataRelationshipsInventoryModel]
        if isinstance(_inventory_model, Unset):
            inventory_model = UNSET
        else:
            inventory_model = MarketDataRelationshipsInventoryModel.from_dict(_inventory_model)

        _tax_calculator = d.pop("tax_calculator", UNSET)
        tax_calculator: Union[Unset, MarketDataRelationshipsTaxCalculator]
        if isinstance(_tax_calculator, Unset):
            tax_calculator = UNSET
        else:
            tax_calculator = MarketDataRelationshipsTaxCalculator.from_dict(_tax_calculator)

        _customer_group = d.pop("customer_group", UNSET)
        customer_group: Union[Unset, MarketDataRelationshipsCustomerGroup]
        if isinstance(_customer_group, Unset):
            customer_group = UNSET
        else:
            customer_group = MarketDataRelationshipsCustomerGroup.from_dict(_customer_group)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, MarketDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = MarketDataRelationshipsAttachments.from_dict(_attachments)

        market_data_relationships = cls(
            merchant=merchant,
            price_list=price_list,
            inventory_model=inventory_model,
            tax_calculator=tax_calculator,
            customer_group=customer_group,
            attachments=attachments,
        )

        market_data_relationships.additional_properties = d
        return market_data_relationships

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
