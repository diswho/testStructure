from sqlalchemy import Boolean, Column,  Integer, String, Text, DateTime, Numeric, BigInteger
from typing import Dict
# from app.db.session import BasEXT, BasLOC
from app.db.session import Base


class Shift(Base):
    __tablename__ = 'att_shift'

    id = Column(Integer, primary_key=True, autoincrement=True)
    shift_name = Column(String, nullable=False)
    cycle_available = Column(Boolean, nullable=False)
    cycle_type = Column(Integer)
    cycle_parameter = Column(Integer)
    start_date = Column(DateTime)
    defaultShift = Column(Boolean)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "shift_name": self.shift_name,
            "cycle_available": self.cycle_available,
            "cycle_type": self.cycle_type,
            "cycle_parameter": self.cycle_parameter,
            "start_date": self.start_date,
            "defaultShift": self.defaultShift
        }

# class ShiftExt(BasEXT):
#     __tablename__ = 'att_shift'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     shift_name = Column(String, nullable=False)
#     cycle_available = Column(Boolean, nullable=False)
#     cycle_type = Column(Integer)
#     cycle_parameter = Column(Integer)
#     start_date = Column(DateTime)
#     defaultShift = Column(Boolean)

#     def to_dict(self) -> Dict:
#         """Converts Shift instance to dictionary."""
#         return {
#             "id": self.id,
#             "shift_name": self.shift_name,
#             "cycle_available": self.cycle_available,
#             "cycle_type": self.cycle_type,
#             "cycle_parameter": self.cycle_parameter,
#             "start_date": self.start_date,
#             "default_shift": self.default_shift
#         }
