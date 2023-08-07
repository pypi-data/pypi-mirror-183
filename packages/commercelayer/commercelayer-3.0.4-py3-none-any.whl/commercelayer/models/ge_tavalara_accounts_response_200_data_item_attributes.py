from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tavalara_accounts_response_200_data_item_attributes_metadata import (
        GETavalaraAccountsResponse200DataItemAttributesMetadata,
    )


T = TypeVar("T", bound="GETavalaraAccountsResponse200DataItemAttributes")


@attr.s(auto_attribs=True)
class GETavalaraAccountsResponse200DataItemAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The tax calculator's internal name. Example: Personal tax calculator.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETavalaraAccountsResponse200DataItemAttributesMetadata]): Set of key-value pairs that
            you can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
        username (Union[Unset, str]): The Avalara account username. Example: user@mydomain.com.
        company_code (Union[Unset, str]): The Avalara company code. Example: MYCOMPANY.
        commit_invoice (Union[Unset, str]): Indicates if the transaction will be recorded and visible on the Avalara
            website. Example: true.
        ddp (Union[Unset, str]): Indicates if the seller is responsible for paying/remitting the customs duty & import
            tax to the customs authorities. Example: true.
    """

    name: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETavalaraAccountsResponse200DataItemAttributesMetadata"] = UNSET
    username: Union[Unset, str] = UNSET
    company_code: Union[Unset, str] = UNSET
    commit_invoice: Union[Unset, str] = UNSET
    ddp: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        created_at = self.created_at
        updated_at = self.updated_at
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        username = self.username
        company_code = self.company_code
        commit_invoice = self.commit_invoice
        ddp = self.ddp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
        if username is not UNSET:
            field_dict["username"] = username
        if company_code is not UNSET:
            field_dict["company_code"] = company_code
        if commit_invoice is not UNSET:
            field_dict["commit_invoice"] = commit_invoice
        if ddp is not UNSET:
            field_dict["ddp"] = ddp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tavalara_accounts_response_200_data_item_attributes_metadata import (
            GETavalaraAccountsResponse200DataItemAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETavalaraAccountsResponse200DataItemAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETavalaraAccountsResponse200DataItemAttributesMetadata.from_dict(_metadata)

        username = d.pop("username", UNSET)

        company_code = d.pop("company_code", UNSET)

        commit_invoice = d.pop("commit_invoice", UNSET)

        ddp = d.pop("ddp", UNSET)

        ge_tavalara_accounts_response_200_data_item_attributes = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
            username=username,
            company_code=company_code,
            commit_invoice=commit_invoice,
            ddp=ddp,
        )

        ge_tavalara_accounts_response_200_data_item_attributes.additional_properties = d
        return ge_tavalara_accounts_response_200_data_item_attributes

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
