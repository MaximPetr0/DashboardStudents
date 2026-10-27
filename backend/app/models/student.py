from sqlalchemy import Boolean, String
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Student(Base):
    __tablename__ = "students"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)  
    
