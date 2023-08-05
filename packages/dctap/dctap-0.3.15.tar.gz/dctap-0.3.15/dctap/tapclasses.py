"""Classes for Python objects derived from CSV files."""

import re
from dataclasses import dataclass, field
from typing import List
from .utils import coerce_integer, coerce_numeric, is_uri_or_prefixed_uri


@dataclass
class TAPStatementTemplate:
    """Instances hold TAP/CSV elements related to statement templates."""

    # pylint: disable=too-many-instance-attributes # It's a dataclass, right?
    # pylint: disable=invalid-name # for elements not named in snake case.

    propertyID: str = ""
    propertyLabel: str = ""
    mandatory: str = ""
    repeatable: str = ""
    valueNodeType: str = ""
    valueDataType: str = ""
    valueConstraint: str = ""
    valueConstraintType: str = ""
    valueShape: str = ""
    note: str = ""
    state_warns: dict = field(default_factory=dict)
    state_extras: dict = field(default_factory=dict)

    def normalize(self, config_dict):
        """Normalizes specific fields."""
        # pylint: disable=attribute-defined-outside-init
        self._normalize_booleans()
        self._valueConstraintType_pattern_warn_if_valueConstraint_not_valid_regex()
        self._valueConstraintType_pattern_warn_if_used_with_value_shape()
        self._valueConstraintType_iristem_parse()
        self._valueConstraintType_iristem_warn_if_list_items_not_IRIs()
        self._valueConstraintType_languageTag_parse(config_dict)
        self._valueConstraintType_minmaxlength_warn_if_not_nonnegative_integer()
        self._valueConstraintType_minmaxinclusive_parse()
        self._valueConstraintType_minmaxinclusive_warn_if_value_not_numeric()
        self._valueConstraintType_warn_if_used_without_valueConstraint()
        self._valueDataType_warn_if_used_with_valueNodeType_IRI()
        self._valueDataType_warn_if_valueNodeType_literal_used_with_any_valueShape()
        self._valueConstraintType_picklist_parse(config_dict)
        self._valueNodeType_is_from_enumerated_list(config_dict)
        self._parse_elements_configured_as_picklist_elements(config_dict)
        return self

    def _warn_if_value_not_urilike(self):
        """Warns when values of given elements do not look like URIs."""
        elements_that_may_take_uris = {
            "propertyID": self.propertyID,
            "valueDataType": self.valueDataType,
        }
        for (elem, statefield) in elements_that_may_take_uris.items():
            if statefield:
                if not is_uri_or_prefixed_uri(statefield):
                    self.state_warns[elem] = f"{repr(elem)} is not IRI or Compact IRI."

    def _normalize_booleans(self):
        """Coerces supported Boolean values to 'true' or 'false' or leaves unchanged."""
        valid_values_for_true = ["true", "TRUE", "True", "1"]
        valid_values_for_false = ["false", "FALSE", "False", "0"]
        boolean_elements = ["mandatory", "repeatable"]
        for elem in boolean_elements:
            warning_message = f"{repr(elem)} is not a supported Boolean value."
            if getattr(self, elem):
                if getattr(self, elem) in valid_values_for_true:
                    setattr(self, elem, "true")
                elif getattr(self, elem) in valid_values_for_false:
                    setattr(self, elem, "false")
                else:
                    self.state_warns[elem] = warning_message
        return self

    def _valueConstraintType_iristem_parse(self):
        """If valueConstraintType is Iristem, split valueConstraint on whitespace."""
        self.valueConstraintType = self.valueConstraintType.lower()
        if self.valueConstraintType == "iristem":
            if self.valueConstraint:
                self.valueConstraint = self.valueConstraint.split()
        return self

    def _valueConstraintType_iristem_warn_if_list_items_not_IRIs(self):
        """If IRIStem, warn if valueConstraint list items do not look like IRIs."""
        self.valueConstraintType = self.valueConstraintType.lower()
        if self.valueConstraintType == "iristem":
            for list_item in self.valueConstraint:
                if not is_uri_or_prefixed_uri(list_item):
                    self.state_warns["valueConstraint"] = (
                        f"Value constraint type is {repr(self.valueConstraintType)}, "
                        f"but {repr(list_item)} does not look like an IRI or "
                        "Compact IRI."
                    )
        return self

    def _valueConstraintType_minmaxlength_warn_if_not_nonnegative_integer(self):
        """
        Tries to coerce valueConstraint to integer (or leaves string untouched).
        Warns if valueConstraint for minLength is not a nonnegative integer.
        """
        vctype = self.valueConstraintType.lower()
        vc = self.valueConstraint = coerce_integer(self.valueConstraint)
        bad_vc_warning = (
            f"Value constraint type is {repr(self.valueConstraintType)}, "
            f"but {repr(self.valueConstraint)} is not a positive integer."
        )
        if vctype in ("minlength", "maxlength"):
            if isinstance(vc, int):
                if vc < 0:
                    self.state_warns["valueConstraint"] = bad_vc_warning
            elif not isinstance(vc, int):
                self.state_warns["valueConstraint"] = bad_vc_warning

        return self

    def _valueConstraintType_minmaxinclusive_parse(self):
        """
        valueConstraintType minInclusive / maxInclusive
        - value of valueConstraint should be numeric (int or float)
        """
        self.valueConstraintType = self.valueConstraintType.lower()
        value_constraint = self.valueConstraint
        if self.valueConstraintType in ("mininclusive", "maxinclusive"):
            if value_constraint:
                self.valueConstraint = coerce_numeric(value_constraint)
        return self

    def _valueConstraintType_minmaxinclusive_warn_if_value_not_numeric(self):
        """Warns if valueConstraint for minInclusive not coercable to float."""
        self.valueConstraintType = self.valueConstraintType.lower()
        if self.valueConstraintType in ("mininclusive", "maxinclusive"):
            try:
                float(self.valueConstraint)
            except (ValueError, TypeError):
                self.state_warns["valueConstraint"] = (
                    f"Value constraint type is {repr(self.valueConstraintType)}, "
                    f"but {repr(self.valueConstraint)} is not numeric."
                )
        return self

    def _valueConstraintType_pattern_warn_if_valueConstraint_not_valid_regex(self):
        """If valueConstraintType Pattern, warn if valueConstraint not valid regex."""
        self.valueConstraintType = self.valueConstraintType.lower()
        if self.valueConstraintType == "pattern":
            try:
                re.compile(self.valueConstraint)
            except (re.error, TypeError):
                self.state_warns["valueConstraint"] = (
                    f"Value constraint type is {repr(self.valueConstraintType)}, but "
                    f"{repr(self.valueConstraint)} is not a valid regular expression."
                )
        return self

    def _valueConstraintType_pattern_warn_if_used_with_value_shape(self):
        """Regular expressions cannot conform to value shapes."""
        self.valueConstraintType = self.valueConstraintType.lower()
        if self.valueConstraintType == "pattern":
            if self.valueShape:
                self.state_warns["valueConstraintType"] = (
                    f"Value constraint type "
                    f"({repr(self.valueConstraintType)}) "
                    "cannot conform to a value shape."
                )

    def _valueConstraintType_languageTag_parse(self, config_dict):
        """For valueConstraintType languageTag, splits valueConstraint on whitespace."""
        self.valueConstraintType = self.valueConstraintType.lower()
        sep = config_dict.get("picklist_item_separator", " ")
        if self.valueConstraintType == "languagetag":
            if self.valueConstraint:
                self.valueConstraint = self.valueConstraint.split(sep)
                self.valueConstraint = [x.strip() for x in self.valueConstraint if x]
        return self

    def _valueConstraintType_warn_if_used_without_valueConstraint(self):
        """Warns if valueConstraintType used without valueConstraint."""
        if self.valueConstraintType:
            if not self.valueConstraint:
                self.state_warns["valueConstraint"] = (
                    f"Value constraint type "
                    f"({repr(self.valueConstraintType)}) "
                    "but no value constraint."
                )
        return self

    def _valueConstraintType_picklist_parse(self, config_dict):
        """If valueConstraintType is Picklist, split valueConstraint on whitespace."""
        self.valueConstraintType = self.valueConstraintType.lower()
        sep = config_dict.get("picklist_item_separator", " ")
        if self.valueConstraintType == "picklist":
            if self.valueConstraint:
                self.valueConstraint = self.valueConstraint.split(sep)
                self.valueConstraint = [x.strip() for x in self.valueConstraint if x]
        return self

    def _valueNodeType_is_from_enumerated_list(self, config_dict):
        """Take valueNodeType from configurable enumerated list, case-insensitive."""
        warning = f"{repr(self.valueNodeType)} is not a valid node type."
        valid_types = ["iri", "bnode", "literal"]
        if config_dict.get("value_node_types"):
            valid_types += [vnt.lower() for vnt in config_dict["value_node_types"]]
        if self.valueNodeType:
            self.valueNodeType = self.valueNodeType.lower()  # normalize to lowercase
            if self.valueNodeType not in valid_types:
                self.state_warns["valueNodeType"] = warning
        return self

    def _valueDataType_warn_if_valueNodeType_literal_used_with_any_valueShape(self):
        """Value with node type Literal cannot conform to a value shape."""
        warning = "Datatypes are only for values that are literals, not shapes."
        self.valueNodeType = self.valueNodeType.lower()
        if self.valueShape:
            if self.valueNodeType == "literal":
                self.state_warns["valueDataType"] = warning
        return self

    def _valueDataType_warn_if_used_with_valueShape(self):
        """Value with any datatype cannot conform to a value shape."""
        warning = "Datatypes are only for values that are literals, not shapes."
        if self.valueShape:
            if self.valueDataType:
                self.state_warns["valueDataType"] = warning
        return self

    def _valueDataType_warn_if_used_with_valueNodeType_IRI(self):
        """Value with datatype implies Literal and cannot be node type IRI."""
        warning = f"Datatypes do not apply to nodes of type {repr(self.valueNodeType)}."
        node_type = self.valueNodeType.lower()
        if node_type in ("iri", "uri", "bnode"):
            if self.valueDataType:
                self.state_warns["valueDataType"] = warning
        return self

    def _parse_elements_configured_as_picklist_elements(self, config_dict):
        """Parse elements configured as list elementss."""
        if config_dict.get("picklist_item_separator"):
            separator = config_dict.get("picklist_item_separator")
        else:
            separator = " "

        if config_dict.get("list_elements"):
            picklist_elements = config_dict.get("list_elements")
        elif config_dict.get("picklist_elements"):
            picklist_elements = config_dict.get("picklist_elements")
        else:
            picklist_elements = []

        for element in picklist_elements:
            if getattr(self, element):
                setattr(self, element, getattr(self, element).split(separator))

        return self

    def get_warnings(self):
        """Emit self.state_warns as populated by self.normalize()."""
        return dict(self.state_warns)


@dataclass
class TAPShape:
    """An instance holds TAP/CSV row elements related to one given, named shape."""

    # pylint: disable=invalid-name
    # True that propertyID, etc, do not conform to snake-case naming style.

    shapeID: str = ""
    shapeLabel: str = ""
    state_list: List[TAPStatementTemplate] = field(default_factory=list)
    shape_warns: dict = field(default_factory=dict)
    shape_extras: dict = field(default_factory=dict)

    def normalize(self, config_dict):
        """Normalize values where required."""
        self._normalize_default_shapeID(config_dict)
        self._warn_if_value_not_urilike()
        return True

    def _normalize_default_shapeID(self, config_dict):
        """If shapeID not specified, looks first in config, else sets "default"."""
        if not self.shapeID:
            self.shapeID = config_dict.get("default_shape_identifier", "default")
        return self

    def _warn_if_value_not_urilike(self):
        """Warns when values of given elements do not look like URIs."""
        elements_that_may_take_uris = {"shapeID": self.shapeID}
        for (elem, shapefield) in elements_that_may_take_uris.items():
            if shapefield:
                if not is_uri_or_prefixed_uri(shapefield):
                    self.shape_warns[elem] = f"{repr(elem)} is not IRI or Compact IRI."

    def get_warnings(self):
        """Emit warnings dictionary self.shape_warns, populated by normalize() method."""
        return dict(self.shape_warns)
