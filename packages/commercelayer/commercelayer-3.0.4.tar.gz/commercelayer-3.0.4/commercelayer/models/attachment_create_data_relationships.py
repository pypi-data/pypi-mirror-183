from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

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


T = TypeVar("T", bound="AttachmentCreateDataRelationships")


@attr.s(auto_attribs=True)
class AttachmentCreateDataRelationships:
    """
    Attributes:
        attachable (Union['BillingInfoValidationRule', 'Bundle', 'CarrierAccount', 'Customer', 'CustomerGroup',
            'DeliveryLeadTime', 'Geocoder', 'GiftCard', 'GiftCardRecipient', 'InventoryModel', 'Market', 'Merchant',
            'Order', 'Package', 'Parcel', 'PaymentMethod', 'Price', 'PriceList', 'Promotion', 'Return', 'Shipment',
            'ShippingCategory', 'ShippingMethod', 'ShippingZone', 'Sku', 'SkuOption', 'StockItem', 'StockLocation',
            'TaxCalculator', 'TaxCategory']):
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
    ]
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

        attachable: Dict[str, Any]

        if isinstance(self.attachable, Bundle):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, CarrierAccount):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, CustomerGroup):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Customer):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, DeliveryLeadTime):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Geocoder):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, GiftCardRecipient):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, GiftCard):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, InventoryModel):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Market):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Merchant):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, BillingInfoValidationRule):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Order):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Package):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Parcel):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, PaymentMethod):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, PriceList):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Price):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Promotion):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Return):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Shipment):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, ShippingCategory):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, ShippingMethod):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, ShippingZone):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, SkuOption):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, Sku):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, StockItem):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, StockLocation):
            attachable = self.attachable.to_dict()

        elif isinstance(self.attachable, TaxCalculator):
            attachable = self.attachable.to_dict()

        else:
            attachable = self.attachable.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attachable": attachable,
            }
        )

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
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_0 = Bundle.from_dict(data)

                return attachable_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_1 = CarrierAccount.from_dict(data)

                return attachable_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_2 = CustomerGroup.from_dict(data)

                return attachable_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_3 = Customer.from_dict(data)

                return attachable_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_4 = DeliveryLeadTime.from_dict(data)

                return attachable_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_5 = Geocoder.from_dict(data)

                return attachable_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_6 = GiftCardRecipient.from_dict(data)

                return attachable_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_7 = GiftCard.from_dict(data)

                return attachable_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_8 = InventoryModel.from_dict(data)

                return attachable_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_9 = Market.from_dict(data)

                return attachable_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_10 = Merchant.from_dict(data)

                return attachable_type_10
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_11 = BillingInfoValidationRule.from_dict(data)

                return attachable_type_11
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_12 = Order.from_dict(data)

                return attachable_type_12
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_13 = Package.from_dict(data)

                return attachable_type_13
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_14 = Parcel.from_dict(data)

                return attachable_type_14
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_15 = PaymentMethod.from_dict(data)

                return attachable_type_15
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_16 = PriceList.from_dict(data)

                return attachable_type_16
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_17 = Price.from_dict(data)

                return attachable_type_17
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_18 = Promotion.from_dict(data)

                return attachable_type_18
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_19 = Return.from_dict(data)

                return attachable_type_19
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_20 = Shipment.from_dict(data)

                return attachable_type_20
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_21 = ShippingCategory.from_dict(data)

                return attachable_type_21
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_22 = ShippingMethod.from_dict(data)

                return attachable_type_22
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_23 = ShippingZone.from_dict(data)

                return attachable_type_23
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_24 = SkuOption.from_dict(data)

                return attachable_type_24
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_25 = Sku.from_dict(data)

                return attachable_type_25
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_26 = StockItem.from_dict(data)

                return attachable_type_26
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_27 = StockLocation.from_dict(data)

                return attachable_type_27
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachable_type_28 = TaxCalculator.from_dict(data)

                return attachable_type_28
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            attachable_type_29 = TaxCategory.from_dict(data)

            return attachable_type_29

        attachable = _parse_attachable(d.pop("attachable"))

        attachment_create_data_relationships = cls(
            attachable=attachable,
        )

        attachment_create_data_relationships.additional_properties = d
        return attachment_create_data_relationships

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
