from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tax_calculator_data_relationships_attachments import TaxCalculatorDataRelationshipsAttachments
    from ..models.tax_calculator_data_relationships_markets import TaxCalculatorDataRelationshipsMarkets


T = TypeVar("T", bound="TaxCalculatorDataRelationships")


@attr.s(auto_attribs=True)
class TaxCalculatorDataRelationships:
    """
    Attributes:
        markets (Union[Unset, TaxCalculatorDataRelationshipsMarkets]):
        attachments (Union[Unset, TaxCalculatorDataRelationshipsAttachments]):
    """

    markets: Union[Unset, "TaxCalculatorDataRelationshipsMarkets"] = UNSET
    attachments: Union[Unset, "TaxCalculatorDataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        markets: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.markets, Unset):
            markets = self.markets.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if markets is not UNSET:
            field_dict["markets"] = markets
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tax_calculator_data_relationships_attachments import TaxCalculatorDataRelationshipsAttachments
        from ..models.tax_calculator_data_relationships_markets import TaxCalculatorDataRelationshipsMarkets

        d = src_dict.copy()
        _markets = d.pop("markets", UNSET)
        markets: Union[Unset, TaxCalculatorDataRelationshipsMarkets]
        if isinstance(_markets, Unset):
            markets = UNSET
        else:
            markets = TaxCalculatorDataRelationshipsMarkets.from_dict(_markets)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, TaxCalculatorDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = TaxCalculatorDataRelationshipsAttachments.from_dict(_attachments)

        tax_calculator_data_relationships = cls(
            markets=markets,
            attachments=attachments,
        )

        tax_calculator_data_relationships.additional_properties = d
        return tax_calculator_data_relationships

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
