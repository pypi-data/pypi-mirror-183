from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tsku_list_promotion_rulessku_list_promotion_rule_id_response_200_data_attributes_metadata import (
        GETskuListPromotionRulesskuListPromotionRuleIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="GETskuListPromotionRulesskuListPromotionRuleIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class GETskuListPromotionRulesskuListPromotionRuleIdResponse200DataAttributes:
    """
    Attributes:
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETskuListPromotionRulesskuListPromotionRuleIdResponse200DataAttributesMetadata]): Set of
            key-value pairs that you can attach to the resource. This can be useful for storing additional information about
            the resource in a structured format. Example: {'foo': 'bar'}.
        all_skus (Union[Unset, bool]): Indicates if the rule is activated only when all of the SKUs of the list is also
            part of the order. Example: True.
        min_quantity (Union[Unset, int]): The min quantity of SKUs of the list that must be also part of the order. If
            positive, overwrites the 'all_skus' option. When the SKU list is manual, its items quantities are honoured.
            Example: 3.
    """

    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETskuListPromotionRulesskuListPromotionRuleIdResponse200DataAttributesMetadata"] = UNSET
    all_skus: Union[Unset, bool] = UNSET
    min_quantity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at
        updated_at = self.updated_at
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        all_skus = self.all_skus
        min_quantity = self.min_quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if all_skus is not UNSET:
            field_dict["all_skus"] = all_skus
        if min_quantity is not UNSET:
            field_dict["min_quantity"] = min_quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tsku_list_promotion_rulessku_list_promotion_rule_id_response_200_data_attributes_metadata import (
            GETskuListPromotionRulesskuListPromotionRuleIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETskuListPromotionRulesskuListPromotionRuleIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETskuListPromotionRulesskuListPromotionRuleIdResponse200DataAttributesMetadata.from_dict(
                _metadata
            )

        all_skus = d.pop("all_skus", UNSET)

        min_quantity = d.pop("min_quantity", UNSET)

        ge_tsku_list_promotion_rulessku_list_promotion_rule_id_response_200_data_attributes = cls(
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
            all_skus=all_skus,
            min_quantity=min_quantity,
        )

        ge_tsku_list_promotion_rulessku_list_promotion_rule_id_response_200_data_attributes.additional_properties = d
        return ge_tsku_list_promotion_rulessku_list_promotion_rule_id_response_200_data_attributes

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
