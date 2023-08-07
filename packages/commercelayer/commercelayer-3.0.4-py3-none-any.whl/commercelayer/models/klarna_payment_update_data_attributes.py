from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.klarna_payment_update_data_attributes_metadata import KlarnaPaymentUpdateDataAttributesMetadata


T = TypeVar("T", bound="KlarnaPaymentUpdateDataAttributes")


@attr.s(auto_attribs=True)
class KlarnaPaymentUpdateDataAttributes:
    """
    Attributes:
        auth_token (Union[Unset, str]): The token returned by a successful client authorization, mandatory to place the
            order. Example: xxxx-yyyy-zzzz.
        update (Union[Unset, bool]): Send this attribute if you want to update the payment session with fresh order
            data. Example: True.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, KlarnaPaymentUpdateDataAttributesMetadata]): Set of key-value pairs that you can attach
            to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    auth_token: Union[Unset, str] = UNSET
    update: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "KlarnaPaymentUpdateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auth_token = self.auth_token
        update = self.update
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_token is not UNSET:
            field_dict["auth_token"] = auth_token
        if update is not UNSET:
            field_dict["_update"] = update
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.klarna_payment_update_data_attributes_metadata import KlarnaPaymentUpdateDataAttributesMetadata

        d = src_dict.copy()
        auth_token = d.pop("auth_token", UNSET)

        update = d.pop("_update", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, KlarnaPaymentUpdateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = KlarnaPaymentUpdateDataAttributesMetadata.from_dict(_metadata)

        klarna_payment_update_data_attributes = cls(
            auth_token=auth_token,
            update=update,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        klarna_payment_update_data_attributes.additional_properties = d
        return klarna_payment_update_data_attributes

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
