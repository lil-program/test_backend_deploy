import uuid
from datetime import datetime

from db.base_class import Base
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship


class Closet(Base):
    __tablename__ = "closets"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(20), nullable=False)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="closets")
    clothes = relationship("Clothes", back_populates="closet")
