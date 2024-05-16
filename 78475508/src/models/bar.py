from typing import TYPE_CHECKING

# if TYPE_CHECKING:
from src.models.foo import Foo


class Bar(Base):
    a: Mapped[int] = mapped_column(Integer)
    b: Mapped["Foo"] = relationship("Foo", back_populates="y")
