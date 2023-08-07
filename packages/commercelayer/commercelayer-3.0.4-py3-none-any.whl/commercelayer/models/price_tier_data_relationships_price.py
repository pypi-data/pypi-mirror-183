from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_tier_data_relationships_price_data import PriceTierDataRelationshipsPriceData


T = TypeVar("T", bound="PriceTierDataRelationshipsPrice")


@attr.s(auto_attribs=True)
class PriceTierDataRelationshipsPrice:
    """
    Attributes:
        data (Union[Unset, PriceTierDataRelationshipsPriceData]):
    """

    data: Union[Unset, "PriceTierDataRelationshipsPriceData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.price_tier_data_relationships_price_data import PriceTierDataRelationshipsPriceData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, PriceTierDataRelationshipsPriceData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PriceTierDataRelationshipsPriceData.from_dict(_data)

        price_tier_data_relationships_price = cls(
            data=data,
        )

        price_tier_data_relationships_price.additional_properties = d
        return price_tier_data_relationships_price

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
