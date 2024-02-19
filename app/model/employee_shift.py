from sqlalchemy import Column,  Integer,  Text, DateTime, BigInteger, Boolean
# from app.db.session import BasEXT, BasLOC
from app.db.session import Base
from typing import Dict


class EmployeeShift(Base):
    __tablename__ = 'att_employee_shift'

    id = Column(Integer, primary_key=True, autoincrement=True)
    startDate = Column(DateTime)
    endDate = Column(DateTime)
    employee_id = Column(Integer, nullable=False)
    shift_id = Column(Integer,  nullable=False)
    modifyDate = Column(DateTime)
    NoEndDate = Column(Boolean)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "startDate": self.startDate,
            "endDate": self.endDate,
            "employee_id": self.employee_id,
            "shift_id": self.shift_id,
            "modifyDate": self.modifyDate,
            "NoEndDate": self.NoEndDate
        }


# class EmployeeShiftEXT(BasEXT):
#     __tablename__ = 'att_employee_shift'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     startDate = Column(DateTime)
#     endDate = Column(DateTime)
#     employee_id = Column(Integer, nullable=False)
#     shift_id = Column(Integer,  nullable=False)
#     modifyDate = Column(DateTime)
#     NoEndDate = Column(Boolean)

#     def to_dict(self) -> Dict:
#         return {
#             "id": self.id,
#             "startDate": self.startDate,
#             "endDate": self.endDate,
#             "employee_id": self.employee_id,
#             "shift_id": self.shift_id,
#             "modifyDate": self.modifyDate,
#             "NoEndDate": self.NoEndDate
#         }
