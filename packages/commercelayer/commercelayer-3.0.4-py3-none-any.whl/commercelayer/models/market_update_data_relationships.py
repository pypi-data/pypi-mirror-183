from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.market_update_data_relationships_customer_group import MarketUpdateDataRelationshipsCustomerGroup
    from ..models.market_update_data_relationships_inventory_model import MarketUpdateDataRelationshipsInventoryModel
    from ..models.market_update_data_relationships_merchant import MarketUpdateDataRelationshipsMerchant
    from ..models.market_update_data_relationships_price_list import MarketUpdateDataRelationshipsPriceList
    from ..models.market_update_data_relationships_tax_calculator import MarketUpdateDataRelationshipsTaxCalculator


T = TypeVar("T", bound="MarketUpdateDataRelationships")


@attr.s(auto_attribs=True)
class MarketUpdateDataRelationships:
    """
    Attributes:
        merchant (Union[Unset, MarketUpdateDataRelationshipsMerchant]):
        price_list (Union[Unset, MarketUpdateDataRelationshipsPriceList]):
        inventory_model (Union[Unset, MarketUpdateDataRelationshipsInventoryModel]):
        tax_calculator (Union[Unset, MarketUpdateDataRelationshipsTaxCalculator]):
        customer_group (Union[Unset, MarketUpdateDataRelationshipsCustomerGroup]):
    """

    merchant: Union[Unset, "MarketUpdateDataRelationshipsMerchant"] = UNSET
    price_list: Union[Unset, "MarketUpdateDataRelationshipsPriceList"] = UNSET
    inventory_model: Union[Unset, "MarketUpdateDataRelationshipsInventoryModel"] = UNSET
    tax_calculator: Union[Unset, "MarketUpdateDataRelationshipsTaxCalculator"] = UNSET
    customer_group: Union[Unset, "MarketUpdateDataRelationshipsCustomerGroup"] = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.market_update_data_relationships_customer_group import MarketUpdateDataRelationshipsCustomerGroup
        from ..models.market_update_data_relationships_inventory_model import (
            MarketUpdateDataRelationshipsInventoryModel,
        )
        from ..models.market_update_data_relationships_merchant import MarketUpdateDataRelationshipsMerchant
        from ..models.market_update_data_relationships_price_list import MarketUpdateDataRelationshipsPriceList
        from ..models.market_update_data_relationships_tax_calculator import MarketUpdateDataRelationshipsTaxCalculator

        d = src_dict.copy()
        _merchant = d.pop("merchant", UNSET)
        merchant: Union[Unset, MarketUpdateDataRelationshipsMerchant]
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = MarketUpdateDataRelationshipsMerchant.from_dict(_merchant)

        _price_list = d.pop("price_list", UNSET)
        price_list: Union[Unset, MarketUpdateDataRelationshipsPriceList]
        if isinstance(_price_list, Unset):
            price_list = UNSET
        else:
            price_list = MarketUpdateDataRelationshipsPriceList.from_dict(_price_list)

        _inventory_model = d.pop("inventory_model", UNSET)
        inventory_model: Union[Unset, MarketUpdateDataRelationshipsInventoryModel]
        if isinstance(_inventory_model, Unset):
            inventory_model = UNSET
        else:
            inventory_model = MarketUpdateDataRelationshipsInventoryModel.from_dict(_inventory_model)

        _tax_calculator = d.pop("tax_calculator", UNSET)
        tax_calculator: Union[Unset, MarketUpdateDataRelationshipsTaxCalculator]
        if isinstance(_tax_calculator, Unset):
            tax_calculator = UNSET
        else:
            tax_calculator = MarketUpdateDataRelationshipsTaxCalculator.from_dict(_tax_calculator)

        _customer_group = d.pop("customer_group", UNSET)
        customer_group: Union[Unset, MarketUpdateDataRelationshipsCustomerGroup]
        if isinstance(_customer_group, Unset):
            customer_group = UNSET
        else:
            customer_group = MarketUpdateDataRelationshipsCustomerGroup.from_dict(_customer_group)

        market_update_data_relationships = cls(
            merchant=merchant,
            price_list=price_list,
            inventory_model=inventory_model,
            tax_calculator=tax_calculator,
            customer_group=customer_group,
        )

        market_update_data_relationships.additional_properties = d
        return market_update_data_relationships

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
