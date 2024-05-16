from pydantic import BaseModel, Field, field_validator
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from src.schemas.foo import Foo


class Bar(BaseModel):
    a: int = Field(...)
    b: "Foo" = Field(...)

    @field_validator("b", mode="before")
    @classmethod
    def validate_relationship(cls, v: Any):
        return Bar.model_validate(v)
