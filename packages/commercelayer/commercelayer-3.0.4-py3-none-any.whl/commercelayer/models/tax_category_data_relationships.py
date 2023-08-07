from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.avalara_account import AvalaraAccount
    from ..models.external_tax_calculator import ExternalTaxCalculator
    from ..models.manual_tax_calculator import ManualTaxCalculator
    from ..models.tax_category_data_relationships_attachments import TaxCategoryDataRelationshipsAttachments
    from ..models.tax_category_data_relationships_sku import TaxCategoryDataRelationshipsSku
    from ..models.taxjar_account import TaxjarAccount


T = TypeVar("T", bound="TaxCategoryDataRelationships")


@attr.s(auto_attribs=True)
class TaxCategoryDataRelationships:
    """
    Attributes:
        sku (Union[Unset, TaxCategoryDataRelationshipsSku]):
        tax_calculator (Union['AvalaraAccount', 'ExternalTaxCalculator', 'ManualTaxCalculator', 'TaxjarAccount',
            Unset]):
        attachments (Union[Unset, TaxCategoryDataRelationshipsAttachments]):
    """

    sku: Union[Unset, "TaxCategoryDataRelationshipsSku"] = UNSET
    tax_calculator: Union[
        "AvalaraAccount", "ExternalTaxCalculator", "ManualTaxCalculator", "TaxjarAccount", Unset
    ] = UNSET
    attachments: Union[Unset, "TaxCategoryDataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.avalara_account import AvalaraAccount
        from ..models.manual_tax_calculator import ManualTaxCalculator
        from ..models.taxjar_account import TaxjarAccount

        sku: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku, Unset):
            sku = self.sku.to_dict()

        tax_calculator: Union[Dict[str, Any], Unset]
        if isinstance(self.tax_calculator, Unset):
            tax_calculator = UNSET

        elif isinstance(self.tax_calculator, AvalaraAccount):
            tax_calculator = UNSET
            if not isinstance(self.tax_calculator, Unset):
                tax_calculator = self.tax_calculator.to_dict()

        elif isinstance(self.tax_calculator, TaxjarAccount):
            tax_calculator = UNSET
            if not isinstance(self.tax_calculator, Unset):
                tax_calculator = self.tax_calculator.to_dict()

        elif isinstance(self.tax_calculator, ManualTaxCalculator):
            tax_calculator = UNSET
            if not isinstance(self.tax_calculator, Unset):
                tax_calculator = self.tax_calculator.to_dict()

        else:
            tax_calculator = UNSET
            if not isinstance(self.tax_calculator, Unset):
                tax_calculator = self.tax_calculator.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku is not UNSET:
            field_dict["sku"] = sku
        if tax_calculator is not UNSET:
            field_dict["tax_calculator"] = tax_calculator
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.avalara_account import AvalaraAccount
        from ..models.external_tax_calculator import ExternalTaxCalculator
        from ..models.manual_tax_calculator import ManualTaxCalculator
        from ..models.tax_category_data_relationships_attachments import TaxCategoryDataRelationshipsAttachments
        from ..models.tax_category_data_relationships_sku import TaxCategoryDataRelationshipsSku
        from ..models.taxjar_account import TaxjarAccount

        d = src_dict.copy()
        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, TaxCategoryDataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = TaxCategoryDataRelationshipsSku.from_dict(_sku)

        def _parse_tax_calculator(
            data: object,
        ) -> Union["AvalaraAccount", "ExternalTaxCalculator", "ManualTaxCalculator", "TaxjarAccount", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _tax_calculator_type_0 = data
                tax_calculator_type_0: Union[Unset, AvalaraAccount]
                if isinstance(_tax_calculator_type_0, Unset):
                    tax_calculator_type_0 = UNSET
                else:
                    tax_calculator_type_0 = AvalaraAccount.from_dict(_tax_calculator_type_0)

                return tax_calculator_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _tax_calculator_type_1 = data
                tax_calculator_type_1: Union[Unset, TaxjarAccount]
                if isinstance(_tax_calculator_type_1, Unset):
                    tax_calculator_type_1 = UNSET
                else:
                    tax_calculator_type_1 = TaxjarAccount.from_dict(_tax_calculator_type_1)

                return tax_calculator_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _tax_calculator_type_2 = data
                tax_calculator_type_2: Union[Unset, ManualTaxCalculator]
                if isinstance(_tax_calculator_type_2, Unset):
                    tax_calculator_type_2 = UNSET
                else:
                    tax_calculator_type_2 = ManualTaxCalculator.from_dict(_tax_calculator_type_2)

                return tax_calculator_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _tax_calculator_type_3 = data
            tax_calculator_type_3: Union[Unset, ExternalTaxCalculator]
            if isinstance(_tax_calculator_type_3, Unset):
                tax_calculator_type_3 = UNSET
            else:
                tax_calculator_type_3 = ExternalTaxCalculator.from_dict(_tax_calculator_type_3)

            return tax_calculator_type_3

        tax_calculator = _parse_tax_calculator(d.pop("tax_calculator", UNSET))

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, TaxCategoryDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = TaxCategoryDataRelationshipsAttachments.from_dict(_attachments)

        tax_category_data_relationships = cls(
            sku=sku,
            tax_calculator=tax_calculator,
            attachments=attachments,
        )

        tax_category_data_relationships.additional_properties = d
        return tax_category_data_relationships

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
