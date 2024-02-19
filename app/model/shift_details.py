from sqlalchemy import Column,  Integer,   DateTime
from typing import Dict
# from app.db.session import BasEXT, BasLOC
from app.db.session import Base


class ShiftDetails(Base):
    __tablename__ = 'att_shift_details'

    id = Column(Integer, primary_key=True, autoincrement=True)
    shift_date = Column(DateTime, nullable=False)
    dayTypeCode = Column(Integer)
    timetable_paycode = Column(Integer)
    shift_id = Column(Integer,  nullable=False)
    timetable_id = Column(Integer)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "shift_date": self.shift_date,
            "dayTypeCode": self.dayTypeCode,
            "timetable_paycode": self.timetable_paycode,
            "shift_id": self.shift_id,
            "timetable_id": self.timetable_id
        }


# class ShiftDetailsEXT(BasEXT):
#     __tablename__ = 'att_shift_details'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     shift_date = Column(DateTime, nullable=False)
#     dayTypeCode = Column(Integer)
#     timetable_paycode = Column(Integer)
#     shift_id = Column(Integer,  nullable=False)
#     timetable_id = Column(Integer)

#     def to_dict(self) -> Dict:
#         return {
#             "id": self.id,
#             "shift_date": self.shift_date,
#             "dayTypeCode": self.dayTypeCode,
#             "timetable_paycode": self.timetable_paycode,
#             "shift_id": self.shift_id,
#             "timetable_id": self.timetable_id
#         }
