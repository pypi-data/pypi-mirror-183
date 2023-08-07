from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pos_tcheckout_com_gateways_response_201_data_type import POSTcheckoutComGatewaysResponse201DataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tcheckout_com_gateways_response_201_data_attributes import (
        POSTcheckoutComGatewaysResponse201DataAttributes,
    )
    from ..models.pos_tcheckout_com_gateways_response_201_data_links import POSTcheckoutComGatewaysResponse201DataLinks
    from ..models.pos_tcheckout_com_gateways_response_201_data_relationships import (
        POSTcheckoutComGatewaysResponse201DataRelationships,
    )


T = TypeVar("T", bound="POSTcheckoutComGatewaysResponse201Data")


@attr.s(auto_attribs=True)
class POSTcheckoutComGatewaysResponse201Data:
    """
    Attributes:
        id (Union[Unset, str]): The resource's id Example: XGZwpOSrWL.
        type (Union[Unset, POSTcheckoutComGatewaysResponse201DataType]): The resource's type
        links (Union[Unset, POSTcheckoutComGatewaysResponse201DataLinks]):
        attributes (Union[Unset, POSTcheckoutComGatewaysResponse201DataAttributes]):
        relationships (Union[Unset, POSTcheckoutComGatewaysResponse201DataRelationships]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, POSTcheckoutComGatewaysResponse201DataType] = UNSET
    links: Union[Unset, "POSTcheckoutComGatewaysResponse201DataLinks"] = UNSET
    attributes: Union[Unset, "POSTcheckoutComGatewaysResponse201DataAttributes"] = UNSET
    relationships: Union[Unset, "POSTcheckoutComGatewaysResponse201DataRelationships"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if links is not UNSET:
            field_dict["links"] = links
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tcheckout_com_gateways_response_201_data_attributes import (
            POSTcheckoutComGatewaysResponse201DataAttributes,
        )
        from ..models.pos_tcheckout_com_gateways_response_201_data_links import (
            POSTcheckoutComGatewaysResponse201DataLinks,
        )
        from ..models.pos_tcheckout_com_gateways_response_201_data_relationships import (
            POSTcheckoutComGatewaysResponse201DataRelationships,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, POSTcheckoutComGatewaysResponse201DataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = POSTcheckoutComGatewaysResponse201DataType(_type)

        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTcheckoutComGatewaysResponse201DataLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTcheckoutComGatewaysResponse201DataLinks.from_dict(_links)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, POSTcheckoutComGatewaysResponse201DataAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = POSTcheckoutComGatewaysResponse201DataAttributes.from_dict(_attributes)

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, POSTcheckoutComGatewaysResponse201DataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = POSTcheckoutComGatewaysResponse201DataRelationships.from_dict(_relationships)

        pos_tcheckout_com_gateways_response_201_data = cls(
            id=id,
            type=type,
            links=links,
            attributes=attributes,
            relationships=relationships,
        )

        pos_tcheckout_com_gateways_response_201_data.additional_properties = d
        return pos_tcheckout_com_gateways_response_201_data

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
