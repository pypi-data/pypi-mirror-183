from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tmarketsmarket_id_response_200_data_relationships_attachments import (
        GETmarketsmarketIdResponse200DataRelationshipsAttachments,
    )
    from ..models.ge_tmarketsmarket_id_response_200_data_relationships_customer_group import (
        GETmarketsmarketIdResponse200DataRelationshipsCustomerGroup,
    )
    from ..models.ge_tmarketsmarket_id_response_200_data_relationships_inventory_model import (
        GETmarketsmarketIdResponse200DataRelationshipsInventoryModel,
    )
    from ..models.ge_tmarketsmarket_id_response_200_data_relationships_merchant import (
        GETmarketsmarketIdResponse200DataRelationshipsMerchant,
    )
    from ..models.ge_tmarketsmarket_id_response_200_data_relationships_price_list import (
        GETmarketsmarketIdResponse200DataRelationshipsPriceList,
    )
    from ..models.ge_tmarketsmarket_id_response_200_data_relationships_tax_calculator import (
        GETmarketsmarketIdResponse200DataRelationshipsTaxCalculator,
    )


T = TypeVar("T", bound="GETmarketsmarketIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETmarketsmarketIdResponse200DataRelationships:
    """
    Attributes:
        merchant (Union[Unset, GETmarketsmarketIdResponse200DataRelationshipsMerchant]):
        price_list (Union[Unset, GETmarketsmarketIdResponse200DataRelationshipsPriceList]):
        inventory_model (Union[Unset, GETmarketsmarketIdResponse200DataRelationshipsInventoryModel]):
        tax_calculator (Union[Unset, GETmarketsmarketIdResponse200DataRelationshipsTaxCalculator]):
        customer_group (Union[Unset, GETmarketsmarketIdResponse200DataRelationshipsCustomerGroup]):
        attachments (Union[Unset, GETmarketsmarketIdResponse200DataRelationshipsAttachments]):
    """

    merchant: Union[Unset, "GETmarketsmarketIdResponse200DataRelationshipsMerchant"] = UNSET
    price_list: Union[Unset, "GETmarketsmarketIdResponse200DataRelationshipsPriceList"] = UNSET
    inventory_model: Union[Unset, "GETmarketsmarketIdResponse200DataRelationshipsInventoryModel"] = UNSET
    tax_calculator: Union[Unset, "GETmarketsmarketIdResponse200DataRelationshipsTaxCalculator"] = UNSET
    customer_group: Union[Unset, "GETmarketsmarketIdResponse200DataRelationshipsCustomerGroup"] = UNSET
    attachments: Union[Unset, "GETmarketsmarketIdResponse200DataRelationshipsAttachments"] = UNSET
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
        from ..models.ge_tmarketsmarket_id_response_200_data_relationships_attachments import (
            GETmarketsmarketIdResponse200DataRelationshipsAttachments,
        )
        from ..models.ge_tmarketsmarket_id_response_200_data_relationships_customer_group import (
            GETmarketsmarketIdResponse200DataRelationshipsCustomerGroup,
        )
        from ..models.ge_tmarketsmarket_id_response_200_data_relationships_inventory_model import (
            GETmarketsmarketIdResponse200DataRelationshipsInventoryModel,
        )
        from ..models.ge_tmarketsmarket_id_response_200_data_relationships_merchant import (
            GETmarketsmarketIdResponse200DataRelationshipsMerchant,
        )
        from ..models.ge_tmarketsmarket_id_response_200_data_relationships_price_list import (
            GETmarketsmarketIdResponse200DataRelationshipsPriceList,
        )
        from ..models.ge_tmarketsmarket_id_response_200_data_relationships_tax_calculator import (
            GETmarketsmarketIdResponse200DataRelationshipsTaxCalculator,
        )

        d = src_dict.copy()
        _merchant = d.pop("merchant", UNSET)
        merchant: Union[Unset, GETmarketsmarketIdResponse200DataRelationshipsMerchant]
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = GETmarketsmarketIdResponse200DataRelationshipsMerchant.from_dict(_merchant)

        _price_list = d.pop("price_list", UNSET)
        price_list: Union[Unset, GETmarketsmarketIdResponse200DataRelationshipsPriceList]
        if isinstance(_price_list, Unset):
            price_list = UNSET
        else:
            price_list = GETmarketsmarketIdResponse200DataRelationshipsPriceList.from_dict(_price_list)

        _inventory_model = d.pop("inventory_model", UNSET)
        inventory_model: Union[Unset, GETmarketsmarketIdResponse200DataRelationshipsInventoryModel]
        if isinstance(_inventory_model, Unset):
            inventory_model = UNSET
        else:
            inventory_model = GETmarketsmarketIdResponse200DataRelationshipsInventoryModel.from_dict(_inventory_model)

        _tax_calculator = d.pop("tax_calculator", UNSET)
        tax_calculator: Union[Unset, GETmarketsmarketIdResponse200DataRelationshipsTaxCalculator]
        if isinstance(_tax_calculator, Unset):
            tax_calculator = UNSET
        else:
            tax_calculator = GETmarketsmarketIdResponse200DataRelationshipsTaxCalculator.from_dict(_tax_calculator)

        _customer_group = d.pop("customer_group", UNSET)
        customer_group: Union[Unset, GETmarketsmarketIdResponse200DataRelationshipsCustomerGroup]
        if isinstance(_customer_group, Unset):
            customer_group = UNSET
        else:
            customer_group = GETmarketsmarketIdResponse200DataRelationshipsCustomerGroup.from_dict(_customer_group)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETmarketsmarketIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETmarketsmarketIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        ge_tmarketsmarket_id_response_200_data_relationships = cls(
            merchant=merchant,
            price_list=price_list,
            inventory_model=inventory_model,
            tax_calculator=tax_calculator,
            customer_group=customer_group,
            attachments=attachments,
        )

        ge_tmarketsmarket_id_response_200_data_relationships.additional_properties = d
        return ge_tmarketsmarket_id_response_200_data_relationships

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
