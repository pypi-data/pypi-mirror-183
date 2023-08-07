from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_horder_subscriptionsorder_subscription_id_response_200_data_attributes_metadata import (
        PATCHorderSubscriptionsorderSubscriptionIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="PATCHorderSubscriptionsorderSubscriptionIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHorderSubscriptionsorderSubscriptionIdResponse200DataAttributes:
    """
    Attributes:
        expires_at (Union[Unset, str]): The expiration date/time of this subscription (must be after starts_at).
            Example: 2018-01-02T12:00:00.000Z.
        activate (Union[Unset, bool]): Send this attribute if you want to mark this subscription as active. Example:
            True.
        deactivate (Union[Unset, bool]): Send this attribute if you want to mark this subscription as inactive. Example:
            True.
        cancel (Union[Unset, bool]): Send this attribute if you want to mark this subscription as cancelled. Example:
            True.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHorderSubscriptionsorderSubscriptionIdResponse200DataAttributesMetadata]): Set of
            key-value pairs that you can attach to the resource. This can be useful for storing additional information about
            the resource in a structured format. Example: {'foo': 'bar'}.
    """

    expires_at: Union[Unset, str] = UNSET
    activate: Union[Unset, bool] = UNSET
    deactivate: Union[Unset, bool] = UNSET
    cancel: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHorderSubscriptionsorderSubscriptionIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expires_at = self.expires_at
        activate = self.activate
        deactivate = self.deactivate
        cancel = self.cancel
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if activate is not UNSET:
            field_dict["_activate"] = activate
        if deactivate is not UNSET:
            field_dict["_deactivate"] = deactivate
        if cancel is not UNSET:
            field_dict["_cancel"] = cancel
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_horder_subscriptionsorder_subscription_id_response_200_data_attributes_metadata import (
            PATCHorderSubscriptionsorderSubscriptionIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        expires_at = d.pop("expires_at", UNSET)

        activate = d.pop("_activate", UNSET)

        deactivate = d.pop("_deactivate", UNSET)

        cancel = d.pop("_cancel", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHorderSubscriptionsorderSubscriptionIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHorderSubscriptionsorderSubscriptionIdResponse200DataAttributesMetadata.from_dict(_metadata)

        patc_horder_subscriptionsorder_subscription_id_response_200_data_attributes = cls(
            expires_at=expires_at,
            activate=activate,
            deactivate=deactivate,
            cancel=cancel,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        patc_horder_subscriptionsorder_subscription_id_response_200_data_attributes.additional_properties = d
        return patc_horder_subscriptionsorder_subscription_id_response_200_data_attributes

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
