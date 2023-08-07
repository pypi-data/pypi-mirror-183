from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_info_validation_rule import BillingInfoValidationRule
    from ..models.bundle import Bundle
    from ..models.carrier_account import CarrierAccount
    from ..models.customer import Customer
    from ..models.customer_group import CustomerGroup
    from ..models.delivery_lead_time import DeliveryLeadTime
    from ..models.geocoder import Geocoder
    from ..models.gift_card import GiftCard
    from ..models.gift_card_recipient import GiftCardRecipient
    from ..models.inventory_model import InventoryModel
    from ..models.market import Market
    from ..models.merchant import Merchant
    from ..models.order import Order
    from ..models.package import Package
    from ..models.parcel import Parcel
    from ..models.payment_method import PaymentMethod
    from ..models.price import Price
    from ..models.price_list import PriceList
    from ..models.promotion import Promotion
    from ..models.return_ import Return
    from ..models.shipment import Shipment
    from ..models.shipping_category import ShippingCategory
    from ..models.shipping_method import ShippingMethod
    from ..models.shipping_zone import ShippingZone
    from ..models.sku import Sku
    from ..models.sku_option import SkuOption
    from ..models.stock_item import StockItem
    from ..models.stock_location import StockLocation
    from ..models.tax_calculator import TaxCalculator
    from ..models.tax_category import TaxCategory


T = TypeVar("T", bound="AttachmentUpdateDataRelationships")


@attr.s(auto_attribs=True)
class AttachmentUpdateDataRelationships:
    """
    Attributes:
        attachable (Union['BillingInfoValidationRule', 'Bundle', 'CarrierAccount', 'Customer', 'CustomerGroup',
            'DeliveryLeadTime', 'Geocoder', 'GiftCard', 'GiftCardRecipient', 'InventoryModel', 'Market', 'Merchant',
            'Order', 'Package', 'Parcel', 'PaymentMethod', 'Price', 'PriceList', 'Promotion', 'Return', 'Shipment',
            'ShippingCategory', 'ShippingMethod', 'ShippingZone', 'Sku', 'SkuOption', 'StockItem', 'StockLocation',
            'TaxCalculator', 'TaxCategory', Unset]):
    """

    attachable: Union[
        "BillingInfoValidationRule",
        "Bundle",
        "CarrierAccount",
        "Customer",
        "CustomerGroup",
        "DeliveryLeadTime",
        "Geocoder",
        "GiftCard",
        "GiftCardRecipient",
        "InventoryModel",
        "Market",
        "Merchant",
        "Order",
        "Package",
        "Parcel",
        "PaymentMethod",
        "Price",
        "PriceList",
        "Promotion",
        "Return",
        "Shipment",
        "ShippingCategory",
        "ShippingMethod",
        "ShippingZone",
        "Sku",
        "SkuOption",
        "StockItem",
        "StockLocation",
        "TaxCalculator",
        "TaxCategory",
        Unset,
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.billing_info_validation_rule import BillingInfoValidationRule
        from ..models.bundle import Bundle
        from ..models.carrier_account import CarrierAccount
        from ..models.customer import Customer
        from ..models.customer_group import CustomerGroup
        from ..models.delivery_lead_time import DeliveryLeadTime
        from ..models.geocoder import Geocoder
        from ..models.gift_card import GiftCard
        from ..models.gift_card_recipient import GiftCardRecipient
        from ..models.inventory_model import InventoryModel
        from ..models.market import Market
        from ..models.merchant import Merchant
        from ..models.order import Order
        from ..models.package import Package
        from ..models.parcel import Parcel
        from ..models.payment_method import PaymentMethod
        from ..models.price import Price
        from ..models.price_list import PriceList
        from ..models.promotion import Promotion
        from ..models.return_ import Return
        from ..models.shipment import Shipment
        from ..models.shipping_category import ShippingCategory
        from ..models.shipping_method import ShippingMethod
        from ..models.shipping_zone import ShippingZone
        from ..models.sku import Sku
        from ..models.sku_option import SkuOption
        from ..models.stock_item import StockItem
        from ..models.stock_location import StockLocation
        from ..models.tax_calculator import TaxCalculator

        attachable: Union[Dict[str, Any], Unset]
        if isinstance(self.attachable, Unset):
            attachable = UNSET

        elif isinstance(self.attachable, Bundle):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, CarrierAccount):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, CustomerGroup):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Customer):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, DeliveryLeadTime):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Geocoder):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, GiftCardRecipient):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, GiftCard):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, InventoryModel):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Market):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Merchant):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, BillingInfoValidationRule):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Order):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Package):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Parcel):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, PaymentMethod):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, PriceList):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Price):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Promotion):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Return):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Shipment):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, ShippingCategory):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, ShippingMethod):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, ShippingZone):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, SkuOption):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Sku):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, StockItem):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, StockLocation):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, TaxCalculator):
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        else:
            attachable = UNSET
            if not isinstance(self.attachable, Unset):
                attachable = self.attachable.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachable is not UNSET:
            field_dict["attachable"] = attachable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.billing_info_validation_rule import BillingInfoValidationRule
        from ..models.bundle import Bundle
        from ..models.carrier_account import CarrierAccount
        from ..models.customer import Customer
        from ..models.customer_group import CustomerGroup
        from ..models.delivery_lead_time import DeliveryLeadTime
        from ..models.geocoder import Geocoder
        from ..models.gift_card import GiftCard
        from ..models.gift_card_recipient import GiftCardRecipient
        from ..models.inventory_model import InventoryModel
        from ..models.market import Market
        from ..models.merchant import Merchant
        from ..models.order import Order
        from ..models.package import Package
        from ..models.parcel import Parcel
        from ..models.payment_method import PaymentMethod
        from ..models.price import Price
        from ..models.price_list import PriceList
        from ..models.promotion import Promotion
        from ..models.return_ import Return
        from ..models.shipment import Shipment
        from ..models.shipping_category import ShippingCategory
        from ..models.shipping_method import ShippingMethod
        from ..models.shipping_zone import ShippingZone
        from ..models.sku import Sku
        from ..models.sku_option import SkuOption
        from ..models.stock_item import StockItem
        from ..models.stock_location import StockLocation
        from ..models.tax_calculator import TaxCalculator
        from ..models.tax_category import TaxCategory

        d = src_dict.copy()

        def _parse_attachable(
            data: object,
        ) -> Union[
            "BillingInfoValidationRule",
            "Bundle",
            "CarrierAccount",
            "Customer",
            "CustomerGroup",
            "DeliveryLeadTime",
            "Geocoder",
            "GiftCard",
            "GiftCardRecipient",
            "InventoryModel",
            "Market",
            "Merchant",
            "Order",
            "Package",
            "Parcel",
            "PaymentMethod",
            "Price",
            "PriceList",
            "Promotion",
            "Return",
            "Shipment",
            "ShippingCategory",
            "ShippingMethod",
            "ShippingZone",
            "Sku",
            "SkuOption",
            "StockItem",
            "StockLocation",
            "TaxCalculator",
            "TaxCategory",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_0 = data
                attachable_type_0: Union[Unset, Bundle]
                if isinstance(_attachable_type_0, Unset):
                    attachable_type_0 = UNSET
                else:
                    attachable_type_0 = Bundle.from_dict(_attachable_type_0)

                return attachable_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_1 = data
                attachable_type_1: Union[Unset, CarrierAccount]
                if isinstance(_attachable_type_1, Unset):
                    attachable_type_1 = UNSET
                else:
                    attachable_type_1 = CarrierAccount.from_dict(_attachable_type_1)

                return attachable_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_2 = data
                attachable_type_2: Union[Unset, CustomerGroup]
                if isinstance(_attachable_type_2, Unset):
                    attachable_type_2 = UNSET
                else:
                    attachable_type_2 = CustomerGroup.from_dict(_attachable_type_2)

                return attachable_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_3 = data
                attachable_type_3: Union[Unset, Customer]
                if isinstance(_attachable_type_3, Unset):
                    attachable_type_3 = UNSET
                else:
                    attachable_type_3 = Customer.from_dict(_attachable_type_3)

                return attachable_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_4 = data
                attachable_type_4: Union[Unset, DeliveryLeadTime]
                if isinstance(_attachable_type_4, Unset):
                    attachable_type_4 = UNSET
                else:
                    attachable_type_4 = DeliveryLeadTime.from_dict(_attachable_type_4)

                return attachable_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_5 = data
                attachable_type_5: Union[Unset, Geocoder]
                if isinstance(_attachable_type_5, Unset):
                    attachable_type_5 = UNSET
                else:
                    attachable_type_5 = Geocoder.from_dict(_attachable_type_5)

                return attachable_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_6 = data
                attachable_type_6: Union[Unset, GiftCardRecipient]
                if isinstance(_attachable_type_6, Unset):
                    attachable_type_6 = UNSET
                else:
                    attachable_type_6 = GiftCardRecipient.from_dict(_attachable_type_6)

                return attachable_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_7 = data
                attachable_type_7: Union[Unset, GiftCard]
                if isinstance(_attachable_type_7, Unset):
                    attachable_type_7 = UNSET
                else:
                    attachable_type_7 = GiftCard.from_dict(_attachable_type_7)

                return attachable_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_8 = data
                attachable_type_8: Union[Unset, InventoryModel]
                if isinstance(_attachable_type_8, Unset):
                    attachable_type_8 = UNSET
                else:
                    attachable_type_8 = InventoryModel.from_dict(_attachable_type_8)

                return attachable_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_9 = data
                attachable_type_9: Union[Unset, Market]
                if isinstance(_attachable_type_9, Unset):
                    attachable_type_9 = UNSET
                else:
                    attachable_type_9 = Market.from_dict(_attachable_type_9)

                return attachable_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_10 = data
                attachable_type_10: Union[Unset, Merchant]
                if isinstance(_attachable_type_10, Unset):
                    attachable_type_10 = UNSET
                else:
                    attachable_type_10 = Merchant.from_dict(_attachable_type_10)

                return attachable_type_10
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_11 = data
                attachable_type_11: Union[Unset, BillingInfoValidationRule]
                if isinstance(_attachable_type_11, Unset):
                    attachable_type_11 = UNSET
                else:
                    attachable_type_11 = BillingInfoValidationRule.from_dict(_attachable_type_11)

                return attachable_type_11
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_12 = data
                attachable_type_12: Union[Unset, Order]
                if isinstance(_attachable_type_12, Unset):
                    attachable_type_12 = UNSET
                else:
                    attachable_type_12 = Order.from_dict(_attachable_type_12)

                return attachable_type_12
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_13 = data
                attachable_type_13: Union[Unset, Package]
                if isinstance(_attachable_type_13, Unset):
                    attachable_type_13 = UNSET
                else:
                    attachable_type_13 = Package.from_dict(_attachable_type_13)

                return attachable_type_13
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_14 = data
                attachable_type_14: Union[Unset, Parcel]
                if isinstance(_attachable_type_14, Unset):
                    attachable_type_14 = UNSET
                else:
                    attachable_type_14 = Parcel.from_dict(_attachable_type_14)

                return attachable_type_14
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_15 = data
                attachable_type_15: Union[Unset, PaymentMethod]
                if isinstance(_attachable_type_15, Unset):
                    attachable_type_15 = UNSET
                else:
                    attachable_type_15 = PaymentMethod.from_dict(_attachable_type_15)

                return attachable_type_15
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_16 = data
                attachable_type_16: Union[Unset, PriceList]
                if isinstance(_attachable_type_16, Unset):
                    attachable_type_16 = UNSET
                else:
                    attachable_type_16 = PriceList.from_dict(_attachable_type_16)

                return attachable_type_16
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_17 = data
                attachable_type_17: Union[Unset, Price]
                if isinstance(_attachable_type_17, Unset):
                    attachable_type_17 = UNSET
                else:
                    attachable_type_17 = Price.from_dict(_attachable_type_17)

                return attachable_type_17
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_18 = data
                attachable_type_18: Union[Unset, Promotion]
                if isinstance(_attachable_type_18, Unset):
                    attachable_type_18 = UNSET
                else:
                    attachable_type_18 = Promotion.from_dict(_attachable_type_18)

                return attachable_type_18
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_19 = data
                attachable_type_19: Union[Unset, Return]
                if isinstance(_attachable_type_19, Unset):
                    attachable_type_19 = UNSET
                else:
                    attachable_type_19 = Return.from_dict(_attachable_type_19)

                return attachable_type_19
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_20 = data
                attachable_type_20: Union[Unset, Shipment]
                if isinstance(_attachable_type_20, Unset):
                    attachable_type_20 = UNSET
                else:
                    attachable_type_20 = Shipment.from_dict(_attachable_type_20)

                return attachable_type_20
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_21 = data
                attachable_type_21: Union[Unset, ShippingCategory]
                if isinstance(_attachable_type_21, Unset):
                    attachable_type_21 = UNSET
                else:
                    attachable_type_21 = ShippingCategory.from_dict(_attachable_type_21)

                return attachable_type_21
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_22 = data
                attachable_type_22: Union[Unset, ShippingMethod]
                if isinstance(_attachable_type_22, Unset):
                    attachable_type_22 = UNSET
                else:
                    attachable_type_22 = ShippingMethod.from_dict(_attachable_type_22)

                return attachable_type_22
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_23 = data
                attachable_type_23: Union[Unset, ShippingZone]
                if isinstance(_attachable_type_23, Unset):
                    attachable_type_23 = UNSET
                else:
                    attachable_type_23 = ShippingZone.from_dict(_attachable_type_23)

                return attachable_type_23
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_24 = data
                attachable_type_24: Union[Unset, SkuOption]
                if isinstance(_attachable_type_24, Unset):
                    attachable_type_24 = UNSET
                else:
                    attachable_type_24 = SkuOption.from_dict(_attachable_type_24)

                return attachable_type_24
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_25 = data
                attachable_type_25: Union[Unset, Sku]
                if isinstance(_attachable_type_25, Unset):
                    attachable_type_25 = UNSET
                else:
                    attachable_type_25 = Sku.from_dict(_attachable_type_25)

                return attachable_type_25
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_26 = data
                attachable_type_26: Union[Unset, StockItem]
                if isinstance(_attachable_type_26, Unset):
                    attachable_type_26 = UNSET
                else:
                    attachable_type_26 = StockItem.from_dict(_attachable_type_26)

                return attachable_type_26
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_27 = data
                attachable_type_27: Union[Unset, StockLocation]
                if isinstance(_attachable_type_27, Unset):
                    attachable_type_27 = UNSET
                else:
                    attachable_type_27 = StockLocation.from_dict(_attachable_type_27)

                return attachable_type_27
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attachable_type_28 = data
                attachable_type_28: Union[Unset, TaxCalculator]
                if isinstance(_attachable_type_28, Unset):
                    attachable_type_28 = UNSET
                else:
                    attachable_type_28 = TaxCalculator.from_dict(_attachable_type_28)

                return attachable_type_28
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _attachable_type_29 = data
            attachable_type_29: Union[Unset, TaxCategory]
            if isinstance(_attachable_type_29, Unset):
                attachable_type_29 = UNSET
            else:
                attachable_type_29 = TaxCategory.from_dict(_attachable_type_29)

            return attachable_type_29

        attachable = _parse_attachable(d.pop("attachable", UNSET))

        attachment_update_data_relationships = cls(
            attachable=attachable,
        )

        attachment_update_data_relationships.additional_properties = d
        return attachment_update_data_relationships

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
