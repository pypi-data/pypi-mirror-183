from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_data_attributes_metadata import OrganizationDataAttributesMetadata


T = TypeVar("T", bound="OrganizationDataAttributes")


@attr.s(auto_attribs=True)
class OrganizationDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The organization's internal name. Example: The Blue Brand.
        slug (Union[Unset, str]): The organization's slug name. Example: the-blue-brand.
        domain (Union[Unset, str]): The organization's domain. Example: the-blue-brand.commercelayer.io.
        support_phone (Union[Unset, str]): The organization's support phone. Example: +01 30800857.
        support_email (Union[Unset, str]): The organization's support email. Example: support@bluebrand.com.
        logo_url (Union[Unset, str]): The URL to the organization's logo. Example: https://bluebrand.com/img/logo.svg.
        favicon_url (Union[Unset, str]): The URL to the organization's favicon. Example:
            https://bluebrand.com/img/favicon.ico.
        primary_color (Union[Unset, str]): The organization's primary color. Example: #C8984E.
        contrast_color (Union[Unset, str]): The organization's contrast color. Example: #FFFFCC.
        gtm_id (Union[Unset, str]): The organization's Google Tag Manager ID. Example: GTM-5FJXX6.
        gtm_id_test (Union[Unset, str]): The organization's Google Tag Manager ID for test. Example: GTM-5FJXX7.
        discount_disabled (Union[Unset, bool]): Indicates if organization has discount disabled.
        account_disabled (Union[Unset, bool]): Indicates if organization has account disabled.
        acceptance_disabled (Union[Unset, bool]): Indicates if organization has acceptance disabled.
        max_concurrent_promotions (Union[Unset, int]): The maximum number of active concurrent promotions allowed for
            your organization. Example: 10.
        max_concurrent_imports (Union[Unset, int]): The maximum number of concurrent imports allowed for your
            organization. Example: 30.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, OrganizationDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    domain: Union[Unset, str] = UNSET
    support_phone: Union[Unset, str] = UNSET
    support_email: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    favicon_url: Union[Unset, str] = UNSET
    primary_color: Union[Unset, str] = UNSET
    contrast_color: Union[Unset, str] = UNSET
    gtm_id: Union[Unset, str] = UNSET
    gtm_id_test: Union[Unset, str] = UNSET
    discount_disabled: Union[Unset, bool] = UNSET
    account_disabled: Union[Unset, bool] = UNSET
    acceptance_disabled: Union[Unset, bool] = UNSET
    max_concurrent_promotions: Union[Unset, int] = UNSET
    max_concurrent_imports: Union[Unset, int] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "OrganizationDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        slug = self.slug
        domain = self.domain
        support_phone = self.support_phone
        support_email = self.support_email
        logo_url = self.logo_url
        favicon_url = self.favicon_url
        primary_color = self.primary_color
        contrast_color = self.contrast_color
        gtm_id = self.gtm_id
        gtm_id_test = self.gtm_id_test
        discount_disabled = self.discount_disabled
        account_disabled = self.account_disabled
        acceptance_disabled = self.acceptance_disabled
        max_concurrent_promotions = self.max_concurrent_promotions
        max_concurrent_imports = self.max_concurrent_imports
        created_at = self.created_at
        updated_at = self.updated_at
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if domain is not UNSET:
            field_dict["domain"] = domain
        if support_phone is not UNSET:
            field_dict["support_phone"] = support_phone
        if support_email is not UNSET:
            field_dict["support_email"] = support_email
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if favicon_url is not UNSET:
            field_dict["favicon_url"] = favicon_url
        if primary_color is not UNSET:
            field_dict["primary_color"] = primary_color
        if contrast_color is not UNSET:
            field_dict["contrast_color"] = contrast_color
        if gtm_id is not UNSET:
            field_dict["gtm_id"] = gtm_id
        if gtm_id_test is not UNSET:
            field_dict["gtm_id_test"] = gtm_id_test
        if discount_disabled is not UNSET:
            field_dict["discount_disabled"] = discount_disabled
        if account_disabled is not UNSET:
            field_dict["account_disabled"] = account_disabled
        if acceptance_disabled is not UNSET:
            field_dict["acceptance_disabled"] = acceptance_disabled
        if max_concurrent_promotions is not UNSET:
            field_dict["max_concurrent_promotions"] = max_concurrent_promotions
        if max_concurrent_imports is not UNSET:
            field_dict["max_concurrent_imports"] = max_concurrent_imports
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization_data_attributes_metadata import OrganizationDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        domain = d.pop("domain", UNSET)

        support_phone = d.pop("support_phone", UNSET)

        support_email = d.pop("support_email", UNSET)

        logo_url = d.pop("logo_url", UNSET)

        favicon_url = d.pop("favicon_url", UNSET)

        primary_color = d.pop("primary_color", UNSET)

        contrast_color = d.pop("contrast_color", UNSET)

        gtm_id = d.pop("gtm_id", UNSET)

        gtm_id_test = d.pop("gtm_id_test", UNSET)

        discount_disabled = d.pop("discount_disabled", UNSET)

        account_disabled = d.pop("account_disabled", UNSET)

        acceptance_disabled = d.pop("acceptance_disabled", UNSET)

        max_concurrent_promotions = d.pop("max_concurrent_promotions", UNSET)

        max_concurrent_imports = d.pop("max_concurrent_imports", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OrganizationDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OrganizationDataAttributesMetadata.from_dict(_metadata)

        organization_data_attributes = cls(
            name=name,
            slug=slug,
            domain=domain,
            support_phone=support_phone,
            support_email=support_email,
            logo_url=logo_url,
            favicon_url=favicon_url,
            primary_color=primary_color,
            contrast_color=contrast_color,
            gtm_id=gtm_id,
            gtm_id_test=gtm_id_test,
            discount_disabled=discount_disabled,
            account_disabled=account_disabled,
            acceptance_disabled=acceptance_disabled,
            max_concurrent_promotions=max_concurrent_promotions,
            max_concurrent_imports=max_concurrent_imports,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        organization_data_attributes.additional_properties = d
        return organization_data_attributes

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
