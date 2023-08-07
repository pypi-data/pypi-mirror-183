from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.adyen_gateway_update_data_type import AdyenGatewayUpdateDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adyen_gateway_update_data_attributes import AdyenGatewayUpdateDataAttributes
    from ..models.adyen_gateway_update_data_relationships import AdyenGatewayUpdateDataRelationships


T = TypeVar("T", bound="AdyenGatewayUpdateData")


@attr.s(auto_attribs=True)
class AdyenGatewayUpdateData:
    """
    Attributes:
        type (AdyenGatewayUpdateDataType): The resource's type
        id (str): The resource's id Example: XGZwpOSrWL.
        attributes (AdyenGatewayUpdateDataAttributes):
        relationships (Union[Unset, AdyenGatewayUpdateDataRelationships]):
    """

    type: AdyenGatewayUpdateDataType
    id: str
    attributes: "AdyenGatewayUpdateDataAttributes"
    relationships: Union[Unset, "AdyenGatewayUpdateDataRelationships"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id
        attributes = self.attributes.to_dict()

        relationships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "id": id,
                "attributes": attributes,
            }
        )
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adyen_gateway_update_data_attributes import AdyenGatewayUpdateDataAttributes
        from ..models.adyen_gateway_update_data_relationships import AdyenGatewayUpdateDataRelationships

        d = src_dict.copy()
        type = AdyenGatewayUpdateDataType(d.pop("type"))

        id = d.pop("id")

        attributes = AdyenGatewayUpdateDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, AdyenGatewayUpdateDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = AdyenGatewayUpdateDataRelationships.from_dict(_relationships)

        adyen_gateway_update_data = cls(
            type=type,
            id=id,
            attributes=attributes,
            relationships=relationships,
        )

        adyen_gateway_update_data.additional_properties = d
        return adyen_gateway_update_data

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
