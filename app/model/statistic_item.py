from sqlalchemy import Boolean, Column,  Integer, String, Text, DateTime, Numeric, BigInteger
from sqlalchemy.orm import relationship
from typing import List, Dict, TYPE_CHECKING
# from app.db.session import BasEXT, BasLOC
from app.db.session import Base

# Define the StatisticItem class


class StatisticItem(Base):
    __tablename__ = 'att_StatisticItem'

    id = Column(Integer, primary_key=True, autoincrement=True)
    item_code = Column(Integer, nullable=False, unique=True)
    item_desc = Column(String)
    item_type = Column(Integer)
    export_code = Column(String)
    isDeleted = Column(Boolean)
    sign = Column(String)
    yearlyLimit = Column(Numeric)
    item_Mode = Column(Integer)
    ColorValue = Column(Integer)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "item_code": self.item_code,
            "item_desc": self.item_desc,
            "item_type": self.item_type,
            "export_code": self.export_code,
            "isDeleted": self.isDeleted,
            "sign": self.sign,
            "yearlyLimit": self.yearlyLimit,
            "item_Mode": self.item_Mode,
            "ColorValue": self.ColorValue
        }
