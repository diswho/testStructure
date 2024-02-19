
from sqlalchemy import Boolean, Column,  Integer, String, Text, DateTime, Numeric, BigInteger
from sqlalchemy.orm import relationship
from typing import List, Dict, TYPE_CHECKING
from app.db.session import Base
# from app.db.session import BasEXT, BasLOC,Base


class AttDaySummary(Base):
    __tablename__ = 'att_day_summary'
    id = Column(Integer, primary_key=True, autoincrement=True)
    att_date = Column(DateTime, nullable=False)
    item_results = Column(Numeric)
    recordsFrom = Column(DateTime, nullable=False)
    recordsTo = Column(DateTime, nullable=False)
    iuser1 = Column(Integer)
    iuser2 = Column(Integer)
    iuser3 = Column(Integer)
    cuser1 = Column(String)
    cuser2 = Column(String)
    cuser3 = Column(String)
    remark = Column(String)
    dt_id = Column(Integer, nullable=False)
    item_id = Column(Integer, nullable=False)
    employee_id = Column(Integer, nullable=False)
    timetable_id = Column(Integer)
    paycode_id = Column(Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'att_date': self.att_date,
            'item_results': self.item_results,
            'recordsFrom': self.recordsFrom,
            'recordsTo': self.recordsTo,
            'iuser1': self.iuser1,
            'iuser2': self.iuser2,
            'iuser3': self.iuser3,
            'cuser1': self.cuser1,
            'cuser2': self.cuser2,
            'cuser3': self.cuser3,
            'remark': self.remark,
            'dt_id': self.dt_id,
            'item_id': self.item_id,
            'employee_id': self.employee_id,
            'timetable_id': self.timetable_id,
            'paycode_id': self.paycode_id
        }
    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'att_date': self.att_date.strftime('%Y-%m-%d %H:%M:%S'),
    #         'item_results': float(self.item_results) if self.item_results is not None else None,
    #         'recordsFrom': self.recordsFrom.strftime('%Y-%m-%d %H:%M:%S'),
    #         'recordsTo': self.recordsTo.strftime('%Y-%m-%d %H:%M:%S'),
    #         'iuser1': self.iuser1,
    #         'iuser2': self.iuser2,
    #         'iuser3': self.iuser3,
    #         'cuser1': self.cuser1,
    #         'cuser2': self.cuser2,
    #         'cuser3': self.cuser3,
    #         'remark': self.remark,
    #         'dt_id': self.dt_id,
    #         'item_id': self.item_id,
    #         'employee_id': self.employee_id,
    #         'timetable_id': self.timetable_id,
    #         'paycode_id': self.paycode_id
    #     }
