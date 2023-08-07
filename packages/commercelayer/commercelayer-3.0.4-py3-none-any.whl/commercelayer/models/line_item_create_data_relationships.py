from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adjustment import Adjustment
    from ..models.bundle import Bundle
    from ..models.external_promotion import ExternalPromotion
    from ..models.fixed_amount_promotion import FixedAmountPromotion
    from ..models.free_shipping_promotion import FreeShippingPromotion
    from ..models.gift_card import GiftCard
    from ..models.line_item_create_data_relationships_order import LineItemCreateDataRelationshipsOrder
    from ..models.payment_method import PaymentMethod
    from ..models.percentage_discount_promotion import PercentageDiscountPromotion
    from ..models.shipment import Shipment
    from ..models.sku import Sku


T = TypeVar("T", bound="LineItemCreateDataRelationships")


@attr.s(auto_attribs=True)
class LineItemCreateDataRelationships:
    """
    Attributes:
        order (LineItemCreateDataRelationshipsOrder):
        item (Union['Adjustment', 'Bundle', 'ExternalPromotion', 'FixedAmountPromotion', 'FreeShippingPromotion',
            'GiftCard', 'PaymentMethod', 'PercentageDiscountPromotion', 'Shipment', 'Sku', Unset]):
    """

    order: "LineItemCreateDataRelationshipsOrder"
    item: Union[
        "Adjustment",
        "Bundle",
        "ExternalPromotion",
        "FixedAmountPromotion",
        "FreeShippingPromotion",
        "GiftCard",
        "PaymentMethod",
        "PercentageDiscountPromotion",
        "Shipment",
        "Sku",
        Unset,
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.adjustment import Adjustment
        from ..models.bundle import Bundle
        from ..models.external_promotion import ExternalPromotion
        from ..models.fixed_amount_promotion import FixedAmountPromotion
        from ..models.free_shipping_promotion import FreeShippingPromotion
        from ..models.gift_card import GiftCard
        from ..models.payment_method import PaymentMethod
        from ..models.percentage_discount_promotion import PercentageDiscountPromotion
        from ..models.shipment import Shipment

        order = self.order.to_dict()

        item: Union[Dict[str, Any], Unset]
        if isinstance(self.item, Unset):
            item = UNSET

        elif isinstance(self.item, Adjustment):
            item = UNSET
            if not isinstance(self.item, Unset):
                item = self.item.to_dict()

        elif isinstance(self.item, Bundle):
            item = UNSET
            if not isinstance(self.item, Unset):
                item = self.item.to_dict()

        elif isinstance(self.item, ExternalPromotion):
            item = UNSET
            if not isinstance(self.item, Unset):
                item = self.item.to_dict()

        elif isinstance(self.item, FixedAmountPromotion):
            item = UNSET
            if not isinstance(self.item, Unset):
                item = self.item.to_dict()

        elif isinstance(self.item, FreeShippingPromotion):
            item = UNSET
            if not isinstance(self.item, Unset):
                item = self.item.to_dict()

        elif isinstance(self.item, GiftCard):
            item = UNSET
            if not isinstance(self.item, Unset):
                item = self.item.to_dict()

        elif isinstance(self.item, PaymentMethod):
            item = UNSET
            if not isinstance(self.item, Unset):
                item = self.item.to_dict()

        elif isinstance(self.item, PercentageDiscountPromotion):
            item = UNSET
            if not isinstance(self.item, Unset):
                item = self.item.to_dict()

        elif isinstance(self.item, Shipment):
            item = UNSET
            if not isinstance(self.item, Unset):
                item = self.item.to_dict()

        else:
            item = UNSET
            if not isinstance(self.item, Unset):
                item = self.item.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order": order,
            }
        )
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adjustment import Adjustment
        from ..models.bundle import Bundle
        from ..models.external_promotion import ExternalPromotion
        from ..models.fixed_amount_promotion import FixedAmountPromotion
        from ..models.free_shipping_promotion import FreeShippingPromotion
        from ..models.gift_card import GiftCard
        from ..models.line_item_create_data_relationships_order import LineItemCreateDataRelationshipsOrder
        from ..models.payment_method import PaymentMethod
        from ..models.percentage_discount_promotion import PercentageDiscountPromotion
        from ..models.shipment import Shipment
        from ..models.sku import Sku

        d = src_dict.copy()
        order = LineItemCreateDataRelationshipsOrder.from_dict(d.pop("order"))

        def _parse_item(
            data: object,
        ) -> Union[
            "Adjustment",
            "Bundle",
            "ExternalPromotion",
            "FixedAmountPromotion",
            "FreeShippingPromotion",
            "GiftCard",
            "PaymentMethod",
            "PercentageDiscountPromotion",
            "Shipment",
            "Sku",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _item_type_0 = data
                item_type_0: Union[Unset, Adjustment]
                if isinstance(_item_type_0, Unset):
                    item_type_0 = UNSET
                else:
                    item_type_0 = Adjustment.from_dict(_item_type_0)

                return item_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _item_type_1 = data
                item_type_1: Union[Unset, Bundle]
                if isinstance(_item_type_1, Unset):
                    item_type_1 = UNSET
                else:
                    item_type_1 = Bundle.from_dict(_item_type_1)

                return item_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _item_type_2 = data
                item_type_2: Union[Unset, ExternalPromotion]
                if isinstance(_item_type_2, Unset):
                    item_type_2 = UNSET
                else:
                    item_type_2 = ExternalPromotion.from_dict(_item_type_2)

                return item_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _item_type_3 = data
                item_type_3: Union[Unset, FixedAmountPromotion]
                if isinstance(_item_type_3, Unset):
                    item_type_3 = UNSET
                else:
                    item_type_3 = FixedAmountPromotion.from_dict(_item_type_3)

                return item_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _item_type_4 = data
                item_type_4: Union[Unset, FreeShippingPromotion]
                if isinstance(_item_type_4, Unset):
                    item_type_4 = UNSET
                else:
                    item_type_4 = FreeShippingPromotion.from_dict(_item_type_4)

                return item_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _item_type_5 = data
                item_type_5: Union[Unset, GiftCard]
                if isinstance(_item_type_5, Unset):
                    item_type_5 = UNSET
                else:
                    item_type_5 = GiftCard.from_dict(_item_type_5)

                return item_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _item_type_6 = data
                item_type_6: Union[Unset, PaymentMethod]
                if isinstance(_item_type_6, Unset):
                    item_type_6 = UNSET
                else:
                    item_type_6 = PaymentMethod.from_dict(_item_type_6)

                return item_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _item_type_7 = data
                item_type_7: Union[Unset, PercentageDiscountPromotion]
                if isinstance(_item_type_7, Unset):
                    item_type_7 = UNSET
                else:
                    item_type_7 = PercentageDiscountPromotion.from_dict(_item_type_7)

                return item_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _item_type_8 = data
                item_type_8: Union[Unset, Shipment]
                if isinstance(_item_type_8, Unset):
                    item_type_8 = UNSET
                else:
                    item_type_8 = Shipment.from_dict(_item_type_8)

                return item_type_8
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _item_type_9 = data
            item_type_9: Union[Unset, Sku]
            if isinstance(_item_type_9, Unset):
                item_type_9 = UNSET
            else:
                item_type_9 = Sku.from_dict(_item_type_9)

            return item_type_9

        item = _parse_item(d.pop("item", UNSET))

        line_item_create_data_relationships = cls(
            order=order,
            item=item,
        )

        line_item_create_data_relationships.additional_properties = d
        return line_item_create_data_relationships

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
