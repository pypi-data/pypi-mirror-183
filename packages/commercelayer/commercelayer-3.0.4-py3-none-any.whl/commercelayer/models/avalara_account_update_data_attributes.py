from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.avalara_account_update_data_attributes_metadata import AvalaraAccountUpdateDataAttributesMetadata


T = TypeVar("T", bound="AvalaraAccountUpdateDataAttributes")


@attr.s(auto_attribs=True)
class AvalaraAccountUpdateDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The tax calculator's internal name. Example: Personal tax calculator.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, AvalaraAccountUpdateDataAttributesMetadata]): Set of key-value pairs that you can attach
            to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
        username (Union[Unset, str]): The Avalara account username. Example: user@mydomain.com.
        password (Union[Unset, str]): The Avalara account password. Example: secret.
        company_code (Union[Unset, str]): The Avalara company code. Example: MYCOMPANY.
        commit_invoice (Union[Unset, str]): Indicates if the transaction will be recorded and visible on the Avalara
            website. Example: true.
        ddp (Union[Unset, str]): Indicates if the seller is responsible for paying/remitting the customs duty & import
            tax to the customs authorities. Example: true.
    """

    name: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "AvalaraAccountUpdateDataAttributesMetadata"] = UNSET
    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    company_code: Union[Unset, str] = UNSET
    commit_invoice: Union[Unset, str] = UNSET
    ddp: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        username = self.username
        password = self.password
        company_code = self.company_code
        commit_invoice = self.commit_invoice
        ddp = self.ddp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if company_code is not UNSET:
            field_dict["company_code"] = company_code
        if commit_invoice is not UNSET:
            field_dict["commit_invoice"] = commit_invoice
        if ddp is not UNSET:
            field_dict["ddp"] = ddp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.avalara_account_update_data_attributes_metadata import AvalaraAccountUpdateDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, AvalaraAccountUpdateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AvalaraAccountUpdateDataAttributesMetadata.from_dict(_metadata)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        company_code = d.pop("company_code", UNSET)

        commit_invoice = d.pop("commit_invoice", UNSET)

        ddp = d.pop("ddp", UNSET)

        avalara_account_update_data_attributes = cls(
            name=name,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
            username=username,
            password=password,
            company_code=company_code,
            commit_invoice=commit_invoice,
            ddp=ddp,
        )

        avalara_account_update_data_attributes.additional_properties = d
        return avalara_account_update_data_attributes

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
