from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

if TYPE_CHECKING:
    from ..models.avalara_account import AvalaraAccount
    from ..models.external_tax_calculator import ExternalTaxCalculator
    from ..models.manual_tax_calculator import ManualTaxCalculator
    from ..models.tax_category_create_data_relationships_sku import TaxCategoryCreateDataRelationshipsSku
    from ..models.taxjar_account import TaxjarAccount


T = TypeVar("T", bound="TaxCategoryCreateDataRelationships")


@attr.s(auto_attribs=True)
class TaxCategoryCreateDataRelationships:
    """
    Attributes:
        sku (TaxCategoryCreateDataRelationshipsSku):
        tax_calculator (Union['AvalaraAccount', 'ExternalTaxCalculator', 'ManualTaxCalculator', 'TaxjarAccount']):
    """

    sku: "TaxCategoryCreateDataRelationshipsSku"
    tax_calculator: Union["AvalaraAccount", "ExternalTaxCalculator", "ManualTaxCalculator", "TaxjarAccount"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.avalara_account import AvalaraAccount
        from ..models.manual_tax_calculator import ManualTaxCalculator
        from ..models.taxjar_account import TaxjarAccount

        sku = self.sku.to_dict()

        tax_calculator: Dict[str, Any]

        if isinstance(self.tax_calculator, AvalaraAccount):
            tax_calculator = self.tax_calculator.to_dict()

        elif isinstance(self.tax_calculator, TaxjarAccount):
            tax_calculator = self.tax_calculator.to_dict()

        elif isinstance(self.tax_calculator, ManualTaxCalculator):
            tax_calculator = self.tax_calculator.to_dict()

        else:
            tax_calculator = self.tax_calculator.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sku": sku,
                "tax_calculator": tax_calculator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.avalara_account import AvalaraAccount
        from ..models.external_tax_calculator import ExternalTaxCalculator
        from ..models.manual_tax_calculator import ManualTaxCalculator
        from ..models.tax_category_create_data_relationships_sku import TaxCategoryCreateDataRelationshipsSku
        from ..models.taxjar_account import TaxjarAccount

        d = src_dict.copy()
        sku = TaxCategoryCreateDataRelationshipsSku.from_dict(d.pop("sku"))

        def _parse_tax_calculator(
            data: object,
        ) -> Union["AvalaraAccount", "ExternalTaxCalculator", "ManualTaxCalculator", "TaxjarAccount"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tax_calculator_type_0 = AvalaraAccount.from_dict(data)

                return tax_calculator_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tax_calculator_type_1 = TaxjarAccount.from_dict(data)

                return tax_calculator_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tax_calculator_type_2 = ManualTaxCalculator.from_dict(data)

                return tax_calculator_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            tax_calculator_type_3 = ExternalTaxCalculator.from_dict(data)

            return tax_calculator_type_3

        tax_calculator = _parse_tax_calculator(d.pop("tax_calculator"))

        tax_category_create_data_relationships = cls(
            sku=sku,
            tax_calculator=tax_calculator,
        )

        tax_category_create_data_relationships.additional_properties = d
        return tax_category_create_data_relationships

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
