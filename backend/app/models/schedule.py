from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import String
from app.db.base import Base
from sqlalchemy import Boolean, String, Integer, ForeignKey, Numeric


class Schedule(Base):
    __tablename__ = "schedules"

    student_id: Mapped[int] = mapped_column(Integer, nullable=False, index=True)    
    day_of_week: Mapped[str] = mapped_column(String(3), nullable=False)
    time_start: Mapped[str] = mapped_column(String(5), nullable=False)
    duration_minutes: Mapped[int] = mapped_column(Integer, default=60, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    notes: Mapped[str] = mapped_column(String(255), nullable=True)    
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)    
    
    