from datetime import datetime

from db.base_class import Base
from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    name = Column(String(20), nullable=False, default="default_name")
    created_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    closets = relationship("Closet", back_populates="user")
