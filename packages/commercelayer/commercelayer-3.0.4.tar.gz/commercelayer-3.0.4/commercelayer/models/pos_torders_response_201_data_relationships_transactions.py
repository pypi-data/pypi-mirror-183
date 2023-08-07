from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_torders_response_201_data_relationships_transactions_data import (
        POSTordersResponse201DataRelationshipsTransactionsData,
    )
    from ..models.pos_torders_response_201_data_relationships_transactions_links import (
        POSTordersResponse201DataRelationshipsTransactionsLinks,
    )


T = TypeVar("T", bound="POSTordersResponse201DataRelationshipsTransactions")


@attr.s(auto_attribs=True)
class POSTordersResponse201DataRelationshipsTransactions:
    """
    Attributes:
        links (Union[Unset, POSTordersResponse201DataRelationshipsTransactionsLinks]):
        data (Union[Unset, POSTordersResponse201DataRelationshipsTransactionsData]):
    """

    links: Union[Unset, "POSTordersResponse201DataRelationshipsTransactionsLinks"] = UNSET
    data: Union[Unset, "POSTordersResponse201DataRelationshipsTransactionsData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_torders_response_201_data_relationships_transactions_data import (
            POSTordersResponse201DataRelationshipsTransactionsData,
        )
        from ..models.pos_torders_response_201_data_relationships_transactions_links import (
            POSTordersResponse201DataRelationshipsTransactionsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTordersResponse201DataRelationshipsTransactionsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTordersResponse201DataRelationshipsTransactionsLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTordersResponse201DataRelationshipsTransactionsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTordersResponse201DataRelationshipsTransactionsData.from_dict(_data)

        pos_torders_response_201_data_relationships_transactions = cls(
            links=links,
            data=data,
        )

        pos_torders_response_201_data_relationships_transactions.additional_properties = d
        return pos_torders_response_201_data_relationships_transactions

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
