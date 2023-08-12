from datetime import datetime
from sqlalchemy import DateTime, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Finance(Base):
    __tablename__ = "finances"
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(255))
    amount: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    date: Mapped[datetime] = mapped_column(DateTime)

    def __repr__(self) -> str:
        return f"Finance(category={self.category}, amount={self.amount}, date={self.date.strftime('%m/%d/%Y')})"


engine = create_engine("sqlite:///purchases.db", echo=True)

session = Session(engine)
