from typing import Generic, TypeVar, Type, Optional

from .models import Node, Anchor
from .query_builder import QueryBuilder
from .ops import OrderByClause

NodeType = TypeVar("NodeType", bound=Node)


class NodeSet(Generic[NodeType]):
    def __init__(self) -> None:
        self.query_builder = QueryBuilder.clean()

    @classmethod
    def from_nodes(cls, *nodes: NodeType) -> "NodeSet[NodeType]":
        if len(nodes) == 0:
            raise ValueError("Cannot create a NodeSet from 0 nodes.")
        ids = (n.orm_id for n in nodes)
        return NodeSet.from_model(type(nodes[0])).filter(orm_id__in=ids)

    @classmethod
    def from_model(cls, model: Type[NodeType]) -> "NodeSet[NodeType]":
        raise NotImplementedError

    @classmethod
    def from_anchor(cls, model: Type[NodeType], anchor: Anchor) -> "NodeSet[NodeType]":
        raise NotImplementedError

    def filter(self, *args, **kwargs) -> "NodeSet[NodeType]":
        for arg in args:
            pass
        for field_and_op, value in kwargs.items():
            pass

    def order_by(self, *args: str) -> "NodeSet[NodeType]":
        for arg in args:
            builder = OrderByClause.from_operator_string(arg)
            self.query_builder.enqueue_order_by_clause(builder)

    def limit(self, number: int) -> "NodeSet[NodeType]":
        raise NotImplementedError

    def offset(self, number: int) -> "NodeSet[NodeType]":
        raise NotImplementedError

    async def first(self) -> Optional[NodeType]:
        raise NotImplementedError

    async def last(self) -> Optional[NodeType]:
        raise NotImplementedError

    async def get(self) -> NodeType:
        raise NotImplementedError

    async def count(self) -> int:
        raise NotImplementedError

    async def exists(self) -> bool:
        count = await self.count()
        return count > 0

    async def __aiter__(self):
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    # TODO: We need define a getattr function that checks if a relationship
    # is on the model. If the model has the relationship then we will create a connection set
    # anchored from this node set.
