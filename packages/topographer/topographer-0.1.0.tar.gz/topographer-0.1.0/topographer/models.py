from pydantic import BaseModel, Field

from typing import Generic, TypeVar
from uuid import UUID, uuid4

T = TypeVar("T")


class Anchor(Generic[T]):
    pass


class Node(BaseModel):
    orm_id: UUID = Field(default_factory=uuid4)


class Relationship(BaseModel):
    orm_id: UUID = Field(default_factory=uuid4)
