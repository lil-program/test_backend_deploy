import uuid
from datetime import datetime

from db.base_class import Base
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship


class Clothes(Base):
    __tablename__ = "clothes"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=True)
    shop_url = Column(String, nullable=False)
    img_path = Column(String, nullable=False)
    description = Column(String, nullable=True)
    closet_id = Column(String, ForeignKey("closets.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    closet = relationship("Closet", back_populates="clothes")
