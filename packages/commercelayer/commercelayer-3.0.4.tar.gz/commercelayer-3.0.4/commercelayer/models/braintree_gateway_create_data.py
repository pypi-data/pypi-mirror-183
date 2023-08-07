from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.braintree_gateway_create_data_type import BraintreeGatewayCreateDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.braintree_gateway_create_data_attributes import BraintreeGatewayCreateDataAttributes
    from ..models.braintree_gateway_create_data_relationships import BraintreeGatewayCreateDataRelationships


T = TypeVar("T", bound="BraintreeGatewayCreateData")


@attr.s(auto_attribs=True)
class BraintreeGatewayCreateData:
    """
    Attributes:
        type (BraintreeGatewayCreateDataType): The resource's type
        attributes (BraintreeGatewayCreateDataAttributes):
        relationships (Union[Unset, BraintreeGatewayCreateDataRelationships]):
    """

    type: BraintreeGatewayCreateDataType
    attributes: "BraintreeGatewayCreateDataAttributes"
    relationships: Union[Unset, "BraintreeGatewayCreateDataRelationships"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        attributes = self.attributes.to_dict()

        relationships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "attributes": attributes,
            }
        )
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.braintree_gateway_create_data_attributes import BraintreeGatewayCreateDataAttributes
        from ..models.braintree_gateway_create_data_relationships import BraintreeGatewayCreateDataRelationships

        d = src_dict.copy()
        type = BraintreeGatewayCreateDataType(d.pop("type"))

        attributes = BraintreeGatewayCreateDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, BraintreeGatewayCreateDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = BraintreeGatewayCreateDataRelationships.from_dict(_relationships)

        braintree_gateway_create_data = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        braintree_gateway_create_data.additional_properties = d
        return braintree_gateway_create_data

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
