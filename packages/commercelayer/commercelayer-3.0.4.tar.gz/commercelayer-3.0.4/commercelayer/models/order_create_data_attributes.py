from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_create_data_attributes_metadata import OrderCreateDataAttributesMetadata


T = TypeVar("T", bound="OrderCreateDataAttributes")


@attr.s(auto_attribs=True)
class OrderCreateDataAttributes:
    """
    Attributes:
        autorefresh (Union[Unset, bool]): Save this attribute as 'false' if you want prevent the order to be refreshed
            automatically at each change (much faster). Example: True.
        guest (Union[Unset, bool]): Indicates if the order has been placed as guest. Example: True.
        customer_email (Union[Unset, str]): The email address of the associated customer. When creating or updating an
            order, this is a shortcut to find or create the associated customer by email. Example: john@example.com.
        customer_password (Union[Unset, str]): The password of the associated customer. When creating or updating an
            order, this is a shortcut to sign up the associated customer. Example: secret.
        language_code (Union[Unset, str]): The preferred language code (ISO 639-1) to be used when communicating with
            the customer. This can be useful when sending the order to 3rd party marketing tools and CRMs. If the language
            is supported, the hosted checkout will be localized accordingly. Example: it.
        shipping_country_code_lock (Union[Unset, str]): The country code that you want the shipping address to be locked
            to. This can be useful to make sure the shipping address belongs to a given shipping country, e.g. the one
            selected in a country selector page. Example: IT.
        coupon_code (Union[Unset, str]): The coupon code to be used for the order. If valid, it triggers a promotion
            adding a discount line item to the order. Example: SUMMERDISCOUNT.
        gift_card_code (Union[Unset, str]): The gift card code (at least the first 8 characters) to be used for the
            order. If valid, it uses the gift card balance to pay for the order. Example:
            cc92c23e-967e-48b2-a323-59add603301f.
        gift_card_or_coupon_code (Union[Unset, str]): The gift card or coupon code (at least the first 8 characters) to
            be used for the order. If a gift card mathes, it uses the gift card balance to pay for the order. Otherwise it
            tries to find a valid coupon code and applies the associated discount. Example:
            cc92c23e-967e-48b2-a323-59add603301f.
        cart_url (Union[Unset, str]): The cart url on your site. If present, it will be used on our hosted checkout
            application. Example: https://yourdomain.com/cart.
        return_url (Union[Unset, str]): The return url on your site. If present, it will be used on our hosted checkout
            application. Example: https://yourdomain.com/.
        terms_url (Union[Unset, str]): The terms and conditions url on your site. If present, it will be used on our
            hosted checkout application. Example: https://yourdomain.com/terms.
        privacy_url (Union[Unset, str]): The privacy policy url on your site. If present, it will be used on our hosted
            checkout application. Example: https://yourdomain.com/privacy.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, OrderCreateDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    autorefresh: Union[Unset, bool] = UNSET
    guest: Union[Unset, bool] = UNSET
    customer_email: Union[Unset, str] = UNSET
    customer_password: Union[Unset, str] = UNSET
    language_code: Union[Unset, str] = UNSET
    shipping_country_code_lock: Union[Unset, str] = UNSET
    coupon_code: Union[Unset, str] = UNSET
    gift_card_code: Union[Unset, str] = UNSET
    gift_card_or_coupon_code: Union[Unset, str] = UNSET
    cart_url: Union[Unset, str] = UNSET
    return_url: Union[Unset, str] = UNSET
    terms_url: Union[Unset, str] = UNSET
    privacy_url: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "OrderCreateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        autorefresh = self.autorefresh
        guest = self.guest
        customer_email = self.customer_email
        customer_password = self.customer_password
        language_code = self.language_code
        shipping_country_code_lock = self.shipping_country_code_lock
        coupon_code = self.coupon_code
        gift_card_code = self.gift_card_code
        gift_card_or_coupon_code = self.gift_card_or_coupon_code
        cart_url = self.cart_url
        return_url = self.return_url
        terms_url = self.terms_url
        privacy_url = self.privacy_url
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if autorefresh is not UNSET:
            field_dict["autorefresh"] = autorefresh
        if guest is not UNSET:
            field_dict["guest"] = guest
        if customer_email is not UNSET:
            field_dict["customer_email"] = customer_email
        if customer_password is not UNSET:
            field_dict["customer_password"] = customer_password
        if language_code is not UNSET:
            field_dict["language_code"] = language_code
        if shipping_country_code_lock is not UNSET:
            field_dict["shipping_country_code_lock"] = shipping_country_code_lock
        if coupon_code is not UNSET:
            field_dict["coupon_code"] = coupon_code
        if gift_card_code is not UNSET:
            field_dict["gift_card_code"] = gift_card_code
        if gift_card_or_coupon_code is not UNSET:
            field_dict["gift_card_or_coupon_code"] = gift_card_or_coupon_code
        if cart_url is not UNSET:
            field_dict["cart_url"] = cart_url
        if return_url is not UNSET:
            field_dict["return_url"] = return_url
        if terms_url is not UNSET:
            field_dict["terms_url"] = terms_url
        if privacy_url is not UNSET:
            field_dict["privacy_url"] = privacy_url
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_create_data_attributes_metadata import OrderCreateDataAttributesMetadata

        d = src_dict.copy()
        autorefresh = d.pop("autorefresh", UNSET)

        guest = d.pop("guest", UNSET)

        customer_email = d.pop("customer_email", UNSET)

        customer_password = d.pop("customer_password", UNSET)

        language_code = d.pop("language_code", UNSET)

        shipping_country_code_lock = d.pop("shipping_country_code_lock", UNSET)

        coupon_code = d.pop("coupon_code", UNSET)

        gift_card_code = d.pop("gift_card_code", UNSET)

        gift_card_or_coupon_code = d.pop("gift_card_or_coupon_code", UNSET)

        cart_url = d.pop("cart_url", UNSET)

        return_url = d.pop("return_url", UNSET)

        terms_url = d.pop("terms_url", UNSET)

        privacy_url = d.pop("privacy_url", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OrderCreateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OrderCreateDataAttributesMetadata.from_dict(_metadata)

        order_create_data_attributes = cls(
            autorefresh=autorefresh,
            guest=guest,
            customer_email=customer_email,
            customer_password=customer_password,
            language_code=language_code,
            shipping_country_code_lock=shipping_country_code_lock,
            coupon_code=coupon_code,
            gift_card_code=gift_card_code,
            gift_card_or_coupon_code=gift_card_or_coupon_code,
            cart_url=cart_url,
            return_url=return_url,
            terms_url=terms_url,
            privacy_url=privacy_url,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        order_create_data_attributes.additional_properties = d
        return order_create_data_attributes

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
