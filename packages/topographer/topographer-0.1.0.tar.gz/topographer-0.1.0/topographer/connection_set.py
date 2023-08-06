from typing import Generic, TypeVar, Type, Optional, AsyncIterable

from .models import Relationship, Node, Anchor
from .node_set import NodeSet

T = TypeVar("T")
DestinationNode = TypeVar("DestinationNode", bound=Node)
TraversingRelationship = TypeVar("TraversingRelationship", bound=Relationship)


class ConnectionSet(Anchor, Generic[T, TraversingRelationship, DestinationNode]):
    def __init__(
        self,
        destination_node_type: Type[DestinationNode],
        traversing_relationship_type: Type[TraversingRelationship],
    ) -> None:
        self.destination_node_type = destination_node_type
        self.traversing_relationship_type = traversing_relationship_type

    async def triples(self):
        pass

    async def pairs(self):
        pass

    def follow(self) -> NodeSet[DestinationNode]:
        return NodeSet.from_anchor(self.destination_node_type, self)

    def filter(
        self, *args, **kwargs
    ) -> "ConnectionSet[T, TraversingRelationship, DestinationNode]":
        raise NotImplementedError

    def order_by(
        self, *args
    ) -> "ConnectionSet[T, TraversingRelationship, DestinationNode]":
        raise NotImplementedError

    def limit(
        self, number: int
    ) -> "ConnectionSet[T, TraversingRelationship, DestinationNode]":
        raise NotImplementedError

    def offset(
        self, number: int
    ) -> "ConnectionSet[T, TraversingRelationship, DestinationNode]":
        raise NotImplementedError

    async def first(self) -> Optional[TraversingRelationship]:
        raise NotImplementedError

    async def last(self) -> Optional[TraversingRelationship]:
        raise NotImplementedError

    async def get(self) -> TraversingRelationship:
        raise NotImplementedError

    async def first_with_node(self) -> Optional[TraversingRelationship]:
        raise NotImplementedError

    async def last_with_node(self) -> Optional[TraversingRelationship]:
        raise NotImplementedError

    async def get_with_node(self) -> TraversingRelationship:
        raise NotImplementedError

    async def count(self) -> int:
        raise NotImplementedError

    async def count_nodes(self) -> int:
        await self.follow().count()

    async def exists(self) -> bool:
        count = await self.count()
        return count > 0

    # TODO: We need define a getattr function that checks if a relationship
    # is on the destination ode model. If the model has the relationship then we will create a connection set
    # anchored from this node set.
