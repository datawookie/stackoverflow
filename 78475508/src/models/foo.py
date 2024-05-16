from typing import TYPE_CHECKING
from src.models.bar import Bar


class Foo(Base):
    x: Mapped[int] = mapped_column(Integer)
    y: Mapped["Bar"] = relationship("Bar", back_populates="b")
