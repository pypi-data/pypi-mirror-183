from pydantic.fields import FieldInfo


from typing import Optional


class PropertyFieldInfo(FieldInfo):
    def __init__(
        self,
        default,
        unique: bool = False,
        index: bool = False,
        db_name: Optional[str] = None,
        **kwargs
    ) -> None:
        super().__init__(default, **kwargs)
        self.unique = unique
        self.index = index
        self.db_name = db_name

    @property
    def is_aliased(self) -> bool:
        return self.db_name is not None
