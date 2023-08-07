from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gift_card_data_attributes_balance_log_item import GiftCardDataAttributesBalanceLogItem
    from ..models.gift_card_data_attributes_metadata import GiftCardDataAttributesMetadata


T = TypeVar("T", bound="GiftCardDataAttributes")


@attr.s(auto_attribs=True)
class GiftCardDataAttributes:
    """
    Attributes:
        status (Union[Unset, str]): The gift card status, one of 'draft', 'inactive', 'active', or 'redeemed'. Example:
            draft.
        code (Union[Unset, str]): The gift card code UUID. If not set, it's automatically generated. Example:
            32db311a-75d9-4c17-9e34-2be220137ad6.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard.
            Example: EUR.
        initial_balance_cents (Union[Unset, int]): The gift card initial balance, in cents. Example: 15000.
        initial_balance_float (Union[Unset, float]): The gift card initial balance, float. Example: 150.0.
        formatted_initial_balance (Union[Unset, str]): The gift card initial balance, formatted. Example: €150,00.
        balance_cents (Union[Unset, int]): The gift card balance, in cents. Example: 15000.
        balance_float (Union[Unset, float]): The gift card balance, float. Example: 150.0.
        formatted_balance (Union[Unset, str]): The gift card balance, formatted. Example: €150,00.
        balance_max_cents (Union[Unset, str]): The gift card balance max, in cents. Example: 100000.
        balance_max_float (Union[Unset, float]): The gift card balance max, float. Example: 1000.0.
        formatted_balance_max (Union[Unset, str]): The gift card balance max, formatted. Example: €1000,00.
        balance_log (Union[Unset, List['GiftCardDataAttributesBalanceLogItem']]): The gift card balance log. Tracks all
            the gift card transactions. Example: [{'date': '2019-12-23T12:00:00.000Z', 'amount_cents': -10000}, {'date':
            '2020-02-01T12:00:00.000Z', 'amount_cents': 5000}].
        single_use (Union[Unset, bool]): Indicates if the gift card can be used only one.
        rechargeable (Union[Unset, bool]): Indicates if the gift card can be recharged. Example: True.
        image_url (Union[Unset, str]): The URL of an image that represents the gift card. Example:
            https://img.yourdomain.com/gift_cards/32db311a.png.
        expires_at (Union[Unset, str]): Time at which the gift card will expire. Example: 2018-01-01T12:00:00.000Z.
        recipient_email (Union[Unset, str]): The email address of the associated recipient. When creating or updating a
            gift card, this is a shortcut to find or create the associated recipient by email. Example: john@example.com.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GiftCardDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    status: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    initial_balance_cents: Union[Unset, int] = UNSET
    initial_balance_float: Union[Unset, float] = UNSET
    formatted_initial_balance: Union[Unset, str] = UNSET
    balance_cents: Union[Unset, int] = UNSET
    balance_float: Union[Unset, float] = UNSET
    formatted_balance: Union[Unset, str] = UNSET
    balance_max_cents: Union[Unset, str] = UNSET
    balance_max_float: Union[Unset, float] = UNSET
    formatted_balance_max: Union[Unset, str] = UNSET
    balance_log: Union[Unset, List["GiftCardDataAttributesBalanceLogItem"]] = UNSET
    single_use: Union[Unset, bool] = UNSET
    rechargeable: Union[Unset, bool] = UNSET
    image_url: Union[Unset, str] = UNSET
    expires_at: Union[Unset, str] = UNSET
    recipient_email: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GiftCardDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        code = self.code
        currency_code = self.currency_code
        initial_balance_cents = self.initial_balance_cents
        initial_balance_float = self.initial_balance_float
        formatted_initial_balance = self.formatted_initial_balance
        balance_cents = self.balance_cents
        balance_float = self.balance_float
        formatted_balance = self.formatted_balance
        balance_max_cents = self.balance_max_cents
        balance_max_float = self.balance_max_float
        formatted_balance_max = self.formatted_balance_max
        balance_log: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.balance_log, Unset):
            balance_log = []
            for balance_log_item_data in self.balance_log:
                balance_log_item = balance_log_item_data.to_dict()

                balance_log.append(balance_log_item)

        single_use = self.single_use
        rechargeable = self.rechargeable
        image_url = self.image_url
        expires_at = self.expires_at
        recipient_email = self.recipient_email
        created_at = self.created_at
        updated_at = self.updated_at
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if code is not UNSET:
            field_dict["code"] = code
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if initial_balance_cents is not UNSET:
            field_dict["initial_balance_cents"] = initial_balance_cents
        if initial_balance_float is not UNSET:
            field_dict["initial_balance_float"] = initial_balance_float
        if formatted_initial_balance is not UNSET:
            field_dict["formatted_initial_balance"] = formatted_initial_balance
        if balance_cents is not UNSET:
            field_dict["balance_cents"] = balance_cents
        if balance_float is not UNSET:
            field_dict["balance_float"] = balance_float
        if formatted_balance is not UNSET:
            field_dict["formatted_balance"] = formatted_balance
        if balance_max_cents is not UNSET:
            field_dict["balance_max_cents"] = balance_max_cents
        if balance_max_float is not UNSET:
            field_dict["balance_max_float"] = balance_max_float
        if formatted_balance_max is not UNSET:
            field_dict["formatted_balance_max"] = formatted_balance_max
        if balance_log is not UNSET:
            field_dict["balance_log"] = balance_log
        if single_use is not UNSET:
            field_dict["single_use"] = single_use
        if rechargeable is not UNSET:
            field_dict["rechargeable"] = rechargeable
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if recipient_email is not UNSET:
            field_dict["recipient_email"] = recipient_email
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gift_card_data_attributes_balance_log_item import GiftCardDataAttributesBalanceLogItem
        from ..models.gift_card_data_attributes_metadata import GiftCardDataAttributesMetadata

        d = src_dict.copy()
        status = d.pop("status", UNSET)

        code = d.pop("code", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        initial_balance_cents = d.pop("initial_balance_cents", UNSET)

        initial_balance_float = d.pop("initial_balance_float", UNSET)

        formatted_initial_balance = d.pop("formatted_initial_balance", UNSET)

        balance_cents = d.pop("balance_cents", UNSET)

        balance_float = d.pop("balance_float", UNSET)

        formatted_balance = d.pop("formatted_balance", UNSET)

        balance_max_cents = d.pop("balance_max_cents", UNSET)

        balance_max_float = d.pop("balance_max_float", UNSET)

        formatted_balance_max = d.pop("formatted_balance_max", UNSET)

        balance_log = []
        _balance_log = d.pop("balance_log", UNSET)
        for balance_log_item_data in _balance_log or []:
            balance_log_item = GiftCardDataAttributesBalanceLogItem.from_dict(balance_log_item_data)

            balance_log.append(balance_log_item)

        single_use = d.pop("single_use", UNSET)

        rechargeable = d.pop("rechargeable", UNSET)

        image_url = d.pop("image_url", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        recipient_email = d.pop("recipient_email", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GiftCardDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GiftCardDataAttributesMetadata.from_dict(_metadata)

        gift_card_data_attributes = cls(
            status=status,
            code=code,
            currency_code=currency_code,
            initial_balance_cents=initial_balance_cents,
            initial_balance_float=initial_balance_float,
            formatted_initial_balance=formatted_initial_balance,
            balance_cents=balance_cents,
            balance_float=balance_float,
            formatted_balance=formatted_balance,
            balance_max_cents=balance_max_cents,
            balance_max_float=balance_max_float,
            formatted_balance_max=formatted_balance_max,
            balance_log=balance_log,
            single_use=single_use,
            rechargeable=rechargeable,
            image_url=image_url,
            expires_at=expires_at,
            recipient_email=recipient_email,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        gift_card_data_attributes.additional_properties = d
        return gift_card_data_attributes

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
