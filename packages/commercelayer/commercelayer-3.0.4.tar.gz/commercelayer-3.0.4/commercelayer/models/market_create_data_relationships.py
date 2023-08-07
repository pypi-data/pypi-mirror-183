from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.market_create_data_relationships_customer_group import MarketCreateDataRelationshipsCustomerGroup
    from ..models.market_create_data_relationships_inventory_model import MarketCreateDataRelationshipsInventoryModel
    from ..models.market_create_data_relationships_merchant import MarketCreateDataRelationshipsMerchant
    from ..models.market_create_data_relationships_price_list import MarketCreateDataRelationshipsPriceList
    from ..models.market_create_data_relationships_tax_calculator import MarketCreateDataRelationshipsTaxCalculator


T = TypeVar("T", bound="MarketCreateDataRelationships")


@attr.s(auto_attribs=True)
class MarketCreateDataRelationships:
    """
    Attributes:
        merchant (MarketCreateDataRelationshipsMerchant):
        price_list (MarketCreateDataRelationshipsPriceList):
        inventory_model (MarketCreateDataRelationshipsInventoryModel):
        tax_calculator (Union[Unset, MarketCreateDataRelationshipsTaxCalculator]):
        customer_group (Union[Unset, MarketCreateDataRelationshipsCustomerGroup]):
    """

    merchant: "MarketCreateDataRelationshipsMerchant"
    price_list: "MarketCreateDataRelationshipsPriceList"
    inventory_model: "MarketCreateDataRelationshipsInventoryModel"
    tax_calculator: Union[Unset, "MarketCreateDataRelationshipsTaxCalculator"] = UNSET
    customer_group: Union[Unset, "MarketCreateDataRelationshipsCustomerGroup"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        merchant = self.merchant.to_dict()

        price_list = self.price_list.to_dict()

        inventory_model = self.inventory_model.to_dict()

        tax_calculator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_calculator, Unset):
            tax_calculator = self.tax_calculator.to_dict()

        customer_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_group, Unset):
            customer_group = self.customer_group.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "merchant": merchant,
                "price_list": price_list,
                "inventory_model": inventory_model,
            }
        )
        if tax_calculator is not UNSET:
            field_dict["tax_calculator"] = tax_calculator
        if customer_group is not UNSET:
            field_dict["customer_group"] = customer_group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.market_create_data_relationships_customer_group import MarketCreateDataRelationshipsCustomerGroup
        from ..models.market_create_data_relationships_inventory_model import (
            MarketCreateDataRelationshipsInventoryModel,
        )
        from ..models.market_create_data_relationships_merchant import MarketCreateDataRelationshipsMerchant
        from ..models.market_create_data_relationships_price_list import MarketCreateDataRelationshipsPriceList
        from ..models.market_create_data_relationships_tax_calculator import MarketCreateDataRelationshipsTaxCalculator

        d = src_dict.copy()
        merchant = MarketCreateDataRelationshipsMerchant.from_dict(d.pop("merchant"))

        price_list = MarketCreateDataRelationshipsPriceList.from_dict(d.pop("price_list"))

        inventory_model = MarketCreateDataRelationshipsInventoryModel.from_dict(d.pop("inventory_model"))

        _tax_calculator = d.pop("tax_calculator", UNSET)
        tax_calculator: Union[Unset, MarketCreateDataRelationshipsTaxCalculator]
        if isinstance(_tax_calculator, Unset):
            tax_calculator = UNSET
        else:
            tax_calculator = MarketCreateDataRelationshipsTaxCalculator.from_dict(_tax_calculator)

        _customer_group = d.pop("customer_group", UNSET)
        customer_group: Union[Unset, MarketCreateDataRelationshipsCustomerGroup]
        if isinstance(_customer_group, Unset):
            customer_group = UNSET
        else:
            customer_group = MarketCreateDataRelationshipsCustomerGroup.from_dict(_customer_group)

        market_create_data_relationships = cls(
            merchant=merchant,
            price_list=price_list,
            inventory_model=inventory_model,
            tax_calculator=tax_calculator,
            customer_group=customer_group,
        )

        market_create_data_relationships.additional_properties = d
        return market_create_data_relationships

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
