from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.merchant_create_data_relationships_address import MerchantCreateDataRelationshipsAddress


T = TypeVar("T", bound="MerchantCreateDataRelationships")


@attr.s(auto_attribs=True)
class MerchantCreateDataRelationships:
    """
    Attributes:
        address (MerchantCreateDataRelationshipsAddress):
    """

    address: "MerchantCreateDataRelationshipsAddress"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.merchant_create_data_relationships_address import MerchantCreateDataRelationshipsAddress

        d = src_dict.copy()
        address = MerchantCreateDataRelationshipsAddress.from_dict(d.pop("address"))

        merchant_create_data_relationships = cls(
            address=address,
        )

        merchant_create_data_relationships.additional_properties = d
        return merchant_create_data_relationships

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
