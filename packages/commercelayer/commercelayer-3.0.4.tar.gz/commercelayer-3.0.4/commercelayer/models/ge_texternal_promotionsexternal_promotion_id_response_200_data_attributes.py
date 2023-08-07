from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_texternal_promotionsexternal_promotion_id_response_200_data_attributes_metadata import (
        GETexternalPromotionsexternalPromotionIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="GETexternalPromotionsexternalPromotionIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class GETexternalPromotionsexternalPromotionIdResponse200DataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The promotion's internal name. Example: Personal promotion.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard.
            Example: EUR.
        starts_at (Union[Unset, str]): The activation date/time of this promotion. Example: 2018-01-01T12:00:00.000Z.
        expires_at (Union[Unset, str]): The expiration date/time of this promotion (must be after starts_at). Example:
            2018-01-02T12:00:00.000Z.
        total_usage_limit (Union[Unset, int]): The total number of times this promotion can be applied. Example: 5.
        total_usage_count (Union[Unset, int]): The number of times this promotion has been applied. Example: 2.
        active (Union[Unset, bool]): Indicates if the promotion is active. Example: True.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETexternalPromotionsexternalPromotionIdResponse200DataAttributesMetadata]): Set of key-
            value pairs that you can attach to the resource. This can be useful for storing additional information about the
            resource in a structured format. Example: {'foo': 'bar'}.
        promotion_url (Union[Unset, str]): The URL to the service that will compute the discount. Example:
            https://external_promotion.yourbrand.com.
        shared_secret (Union[Unset, str]): The shared secret used to sign the external request payload. Example: xxxx-
            yyyy-zzzz.
    """

    name: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    starts_at: Union[Unset, str] = UNSET
    expires_at: Union[Unset, str] = UNSET
    total_usage_limit: Union[Unset, int] = UNSET
    total_usage_count: Union[Unset, int] = UNSET
    active: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETexternalPromotionsexternalPromotionIdResponse200DataAttributesMetadata"] = UNSET
    promotion_url: Union[Unset, str] = UNSET
    shared_secret: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        currency_code = self.currency_code
        starts_at = self.starts_at
        expires_at = self.expires_at
        total_usage_limit = self.total_usage_limit
        total_usage_count = self.total_usage_count
        active = self.active
        created_at = self.created_at
        updated_at = self.updated_at
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        promotion_url = self.promotion_url
        shared_secret = self.shared_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if starts_at is not UNSET:
            field_dict["starts_at"] = starts_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if total_usage_limit is not UNSET:
            field_dict["total_usage_limit"] = total_usage_limit
        if total_usage_count is not UNSET:
            field_dict["total_usage_count"] = total_usage_count
        if active is not UNSET:
            field_dict["active"] = active
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
        if promotion_url is not UNSET:
            field_dict["promotion_url"] = promotion_url
        if shared_secret is not UNSET:
            field_dict["shared_secret"] = shared_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_texternal_promotionsexternal_promotion_id_response_200_data_attributes_metadata import (
            GETexternalPromotionsexternalPromotionIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        starts_at = d.pop("starts_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        total_usage_limit = d.pop("total_usage_limit", UNSET)

        total_usage_count = d.pop("total_usage_count", UNSET)

        active = d.pop("active", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETexternalPromotionsexternalPromotionIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETexternalPromotionsexternalPromotionIdResponse200DataAttributesMetadata.from_dict(_metadata)

        promotion_url = d.pop("promotion_url", UNSET)

        shared_secret = d.pop("shared_secret", UNSET)

        ge_texternal_promotionsexternal_promotion_id_response_200_data_attributes = cls(
            name=name,
            currency_code=currency_code,
            starts_at=starts_at,
            expires_at=expires_at,
            total_usage_limit=total_usage_limit,
            total_usage_count=total_usage_count,
            active=active,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
            promotion_url=promotion_url,
            shared_secret=shared_secret,
        )

        ge_texternal_promotionsexternal_promotion_id_response_200_data_attributes.additional_properties = d
        return ge_texternal_promotionsexternal_promotion_id_response_200_data_attributes

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
