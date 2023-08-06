from dataclasses import dataclass
from enum import Enum
from typing import Any


class FilterOperation(Enum):
    EQUAL = "eq"
    NOT_EQUAL = "ne"
    GREATER_THAN = "gt"
    LESS_THAN = "lt"
    GREATER_THAN_EQUAL_TO = "gte"
    LESS_THAN_EQUAL_TO = "lte"
    IN = "in"

    EXACT = "exact"
    CONTAINS = "contains"
    STARTS_WITH = "startswith"
    ENDS_WITH = "endswith"
    REGEX = "regex"

    CASE_INSENSITIVE_EXACT = "iexact"
    CASE_INSENSITIVE_CONTAINS = "icontains"
    CASE_INSENSITIVE_STARTS_WITH = "istartswith"
    CASE_INSENSITIVE_ENDS_WITH = "iendswith"
    CASE_INSENSITIVE_REGEX = "iregex"


class Ordering(Enum):
    ASCENDING = "+"
    DESCENDING = "-"


@dataclass
class OrderByClause:
    ordering: Ordering
    field_name: str

    @classmethod
    def from_operator_string(cls, operator_string: str) -> "OrderByClause":
        starts_with_operator = any(o.value == operator_string[0] for o in  Ordering)
        if starts_with_operator:
            ordering, field_name = Ordering(operator_string[0]), operator_string[1:]
        else:
            ordering, field_name = Ordering.ASCENDING, operator_string

        return OrderByClause(ordering, field_name)


@dataclass
class FilterClause:
    filter_operation: FilterOperation
    field_name: str
    filter_value: Any
