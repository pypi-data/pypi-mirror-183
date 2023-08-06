from abc import ABC, abstractmethod

from .ops import OrderByClause


class QueryBuilder(ABC):
    @classmethod
    def clean(cls) -> "QueryBuilder":
        pass

    @abstractmethod
    def enqueue_order_by_clause(self, order_by: OrderByClause):
        pass
