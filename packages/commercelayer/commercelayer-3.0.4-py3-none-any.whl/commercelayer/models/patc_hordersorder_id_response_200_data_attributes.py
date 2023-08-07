from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hordersorder_id_response_200_data_attributes_metadata import (
        PATCHordersorderIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="PATCHordersorderIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHordersorderIdResponse200DataAttributes:
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
        archive (Union[Unset, bool]): Send this attribute if you want to archive the order. Example: True.
        unarchive (Union[Unset, bool]): Send this attribute if you want to unarchive the order. Example: True.
        place (Union[Unset, bool]): Send this attribute if you want to place the order. Example: True.
        cancel (Union[Unset, bool]): Send this attribute if you want to cancel a placed order. The order's authorization
            will be automatically voided. Example: True.
        approve (Union[Unset, bool]): Send this attribute if you want to approve a placed order. Example: True.
        approve_and_capture (Union[Unset, bool]): Send this attribute if you want to approve and capture a placed order.
            Example: True.
        authorize (Union[Unset, bool]): Send this attribute if you want to authorize the order's payment source.
            Example: True.
        authorization_amount_cents (Union[Unset, int]): The authorization amount, in cents. Example: 500.
        capture (Union[Unset, bool]): Send this attribute if you want to capture an authorized order. Example: True.
        refund (Union[Unset, bool]): Send this attribute if you want to refund a captured order. Example: True.
        update_taxes (Union[Unset, bool]): Send this attribute if you want to force tax calculation for this order (a
            tax calculator must be associated to the order's market). Example: True.
        nullify_payment_source (Union[Unset, bool]): Send this attribute if you want to nullify the payment source for
            this order.
        billing_address_clone_id (Union[Unset, str]): The id of the address that you want to clone to create the order's
            billing address. Example: 1234.
        shipping_address_clone_id (Union[Unset, str]): The id of the address that you want to clone to create the
            order's shipping address. Example: 1234.
        customer_payment_source_id (Union[Unset, str]): The id of the customer payment source (i.e. credit card) that
            you want to use as the order's payment source. Example: 1234.
        shipping_address_same_as_billing (Union[Unset, bool]): Send this attribute if you want the shipping address to
            be cloned from the order's billing address. Example: True.
        billing_address_same_as_shipping (Union[Unset, bool]): Send this attribute if you want the billing address to be
            cloned from the order's shipping address. Example: True.
        commit_invoice (Union[Unset, bool]): Send this attribute if you want commit the sales tax invoice to the
            associated tax calculator (currently supported by Avalara). Example: True.
        refund_invoice (Union[Unset, bool]): Send this attribute if you want refund the sales tax invoice to the
            associated tax calculator (currently supported by Avalara). Example: True.
        save_payment_source_to_customer_wallet (Union[Unset, bool]): Send this attribute if you want the order's payment
            source to be saved in the customer's wallet as a customer payment source. Example: True.
        save_shipping_address_to_customer_address_book (Union[Unset, bool]): Send this attribute if you want the order's
            shipping address to be saved in the customer's address book as a customer address. Example: True.
        save_billing_address_to_customer_address_book (Union[Unset, bool]): Send this attribute if you want the order's
            billing address to be saved in the customer's address book as a customer address. Example: True.
        refresh (Union[Unset, bool]): Send this attribute if you want to manually refresh the order. Example: True.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHordersorderIdResponse200DataAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
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
    archive: Union[Unset, bool] = UNSET
    unarchive: Union[Unset, bool] = UNSET
    place: Union[Unset, bool] = UNSET
    cancel: Union[Unset, bool] = UNSET
    approve: Union[Unset, bool] = UNSET
    approve_and_capture: Union[Unset, bool] = UNSET
    authorize: Union[Unset, bool] = UNSET
    authorization_amount_cents: Union[Unset, int] = UNSET
    capture: Union[Unset, bool] = UNSET
    refund: Union[Unset, bool] = UNSET
    update_taxes: Union[Unset, bool] = UNSET
    nullify_payment_source: Union[Unset, bool] = UNSET
    billing_address_clone_id: Union[Unset, str] = UNSET
    shipping_address_clone_id: Union[Unset, str] = UNSET
    customer_payment_source_id: Union[Unset, str] = UNSET
    shipping_address_same_as_billing: Union[Unset, bool] = UNSET
    billing_address_same_as_shipping: Union[Unset, bool] = UNSET
    commit_invoice: Union[Unset, bool] = UNSET
    refund_invoice: Union[Unset, bool] = UNSET
    save_payment_source_to_customer_wallet: Union[Unset, bool] = UNSET
    save_shipping_address_to_customer_address_book: Union[Unset, bool] = UNSET
    save_billing_address_to_customer_address_book: Union[Unset, bool] = UNSET
    refresh: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHordersorderIdResponse200DataAttributesMetadata"] = UNSET
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
        archive = self.archive
        unarchive = self.unarchive
        place = self.place
        cancel = self.cancel
        approve = self.approve
        approve_and_capture = self.approve_and_capture
        authorize = self.authorize
        authorization_amount_cents = self.authorization_amount_cents
        capture = self.capture
        refund = self.refund
        update_taxes = self.update_taxes
        nullify_payment_source = self.nullify_payment_source
        billing_address_clone_id = self.billing_address_clone_id
        shipping_address_clone_id = self.shipping_address_clone_id
        customer_payment_source_id = self.customer_payment_source_id
        shipping_address_same_as_billing = self.shipping_address_same_as_billing
        billing_address_same_as_shipping = self.billing_address_same_as_shipping
        commit_invoice = self.commit_invoice
        refund_invoice = self.refund_invoice
        save_payment_source_to_customer_wallet = self.save_payment_source_to_customer_wallet
        save_shipping_address_to_customer_address_book = self.save_shipping_address_to_customer_address_book
        save_billing_address_to_customer_address_book = self.save_billing_address_to_customer_address_book
        refresh = self.refresh
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
        if archive is not UNSET:
            field_dict["_archive"] = archive
        if unarchive is not UNSET:
            field_dict["_unarchive"] = unarchive
        if place is not UNSET:
            field_dict["_place"] = place
        if cancel is not UNSET:
            field_dict["_cancel"] = cancel
        if approve is not UNSET:
            field_dict["_approve"] = approve
        if approve_and_capture is not UNSET:
            field_dict["_approve_and_capture"] = approve_and_capture
        if authorize is not UNSET:
            field_dict["_authorize"] = authorize
        if authorization_amount_cents is not UNSET:
            field_dict["_authorization_amount_cents"] = authorization_amount_cents
        if capture is not UNSET:
            field_dict["_capture"] = capture
        if refund is not UNSET:
            field_dict["_refund"] = refund
        if update_taxes is not UNSET:
            field_dict["_update_taxes"] = update_taxes
        if nullify_payment_source is not UNSET:
            field_dict["_nullify_payment_source"] = nullify_payment_source
        if billing_address_clone_id is not UNSET:
            field_dict["_billing_address_clone_id"] = billing_address_clone_id
        if shipping_address_clone_id is not UNSET:
            field_dict["_shipping_address_clone_id"] = shipping_address_clone_id
        if customer_payment_source_id is not UNSET:
            field_dict["_customer_payment_source_id"] = customer_payment_source_id
        if shipping_address_same_as_billing is not UNSET:
            field_dict["_shipping_address_same_as_billing"] = shipping_address_same_as_billing
        if billing_address_same_as_shipping is not UNSET:
            field_dict["_billing_address_same_as_shipping"] = billing_address_same_as_shipping
        if commit_invoice is not UNSET:
            field_dict["_commit_invoice"] = commit_invoice
        if refund_invoice is not UNSET:
            field_dict["_refund_invoice"] = refund_invoice
        if save_payment_source_to_customer_wallet is not UNSET:
            field_dict["_save_payment_source_to_customer_wallet"] = save_payment_source_to_customer_wallet
        if save_shipping_address_to_customer_address_book is not UNSET:
            field_dict[
                "_save_shipping_address_to_customer_address_book"
            ] = save_shipping_address_to_customer_address_book
        if save_billing_address_to_customer_address_book is not UNSET:
            field_dict["_save_billing_address_to_customer_address_book"] = save_billing_address_to_customer_address_book
        if refresh is not UNSET:
            field_dict["_refresh"] = refresh
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hordersorder_id_response_200_data_attributes_metadata import (
            PATCHordersorderIdResponse200DataAttributesMetadata,
        )

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

        archive = d.pop("_archive", UNSET)

        unarchive = d.pop("_unarchive", UNSET)

        place = d.pop("_place", UNSET)

        cancel = d.pop("_cancel", UNSET)

        approve = d.pop("_approve", UNSET)

        approve_and_capture = d.pop("_approve_and_capture", UNSET)

        authorize = d.pop("_authorize", UNSET)

        authorization_amount_cents = d.pop("_authorization_amount_cents", UNSET)

        capture = d.pop("_capture", UNSET)

        refund = d.pop("_refund", UNSET)

        update_taxes = d.pop("_update_taxes", UNSET)

        nullify_payment_source = d.pop("_nullify_payment_source", UNSET)

        billing_address_clone_id = d.pop("_billing_address_clone_id", UNSET)

        shipping_address_clone_id = d.pop("_shipping_address_clone_id", UNSET)

        customer_payment_source_id = d.pop("_customer_payment_source_id", UNSET)

        shipping_address_same_as_billing = d.pop("_shipping_address_same_as_billing", UNSET)

        billing_address_same_as_shipping = d.pop("_billing_address_same_as_shipping", UNSET)

        commit_invoice = d.pop("_commit_invoice", UNSET)

        refund_invoice = d.pop("_refund_invoice", UNSET)

        save_payment_source_to_customer_wallet = d.pop("_save_payment_source_to_customer_wallet", UNSET)

        save_shipping_address_to_customer_address_book = d.pop("_save_shipping_address_to_customer_address_book", UNSET)

        save_billing_address_to_customer_address_book = d.pop("_save_billing_address_to_customer_address_book", UNSET)

        refresh = d.pop("_refresh", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHordersorderIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHordersorderIdResponse200DataAttributesMetadata.from_dict(_metadata)

        patc_hordersorder_id_response_200_data_attributes = cls(
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
            archive=archive,
            unarchive=unarchive,
            place=place,
            cancel=cancel,
            approve=approve,
            approve_and_capture=approve_and_capture,
            authorize=authorize,
            authorization_amount_cents=authorization_amount_cents,
            capture=capture,
            refund=refund,
            update_taxes=update_taxes,
            nullify_payment_source=nullify_payment_source,
            billing_address_clone_id=billing_address_clone_id,
            shipping_address_clone_id=shipping_address_clone_id,
            customer_payment_source_id=customer_payment_source_id,
            shipping_address_same_as_billing=shipping_address_same_as_billing,
            billing_address_same_as_shipping=billing_address_same_as_shipping,
            commit_invoice=commit_invoice,
            refund_invoice=refund_invoice,
            save_payment_source_to_customer_wallet=save_payment_source_to_customer_wallet,
            save_shipping_address_to_customer_address_book=save_shipping_address_to_customer_address_book,
            save_billing_address_to_customer_address_book=save_billing_address_to_customer_address_book,
            refresh=refresh,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        patc_hordersorder_id_response_200_data_attributes.additional_properties = d
        return patc_hordersorder_id_response_200_data_attributes

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
