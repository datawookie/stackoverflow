from pydantic import BaseModel, Field, field_validator
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from src.schemas.bar import Bar


class Foo(BaseModel):
    x: int = Field(...)
    y: "Bar" = Field(...)

    @field_validator("y", mode="before")
    @classmethod
    def validate_relationship(cls, v: Any):
        return Bar.model_validate(v)
