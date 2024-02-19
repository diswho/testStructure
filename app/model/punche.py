from sqlalchemy import Column,  Integer,  Text, DateTime, BigInteger
from typing import Dict
# from app.db.session import BasEXT, BasLOC
from app.db.session import Base


class Punch(Base):
    __tablename__ = "att_punches"

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, nullable=False)
    punch_time = Column(DateTime, nullable=False)
    workcode = Column(Integer)
    workstate = Column(Integer)
    verifycode = Column(Text)
    terminal_id = Column(Integer)
    punch_type = Column(Text)
    operator = Column(Text)
    operator_reason = Column(Text)
    operator_time = Column(DateTime)
    IsSelect = Column(Integer)
    reserved1 = Column(Text)
    reserved2 = Column(Text)
    middleware_id = Column(BigInteger)
    attendance_event = Column(Text)
    login_combination = Column(Integer)
    status = Column(Integer)
    annotation = Column(Text)
    processed = Column(Integer)

    def to_dict(self) -> Dict:
        """Converts HREmployeeExt instance to dictionary."""
        return {
            "employee_id": self.employee_id,
            "punch_time": self.punch_time,
            "workcode": self.workcode,
            "workstate": self.workstate,
            "verifycode": self.verifycode,
            "terminal_id": self.terminal_id,
            "punch_type": self.punch_type,
            "operator": self.operator,
            "operator_reason": self.operator_reason,
            "operator_time": self.operator_time,
            "IsSelect": self.IsSelect,
            "reserved1": self.reserved1,
            "reserved2": self.reserved2,
            "middleware_id": self.middleware_id,
            "attendance_event": self.attendance_event,
            "login_combination": self.login_combination,
            "status": self.status,
            "annotation": self.annotation,
            "processed": self.processed
        }


# class PunchExt(BasEXT):
#     __tablename__ = "att_punches"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     employee_id = Column(Integer, nullable=False)
#     punch_time = Column(DateTime, nullable=False)
#     workcode = Column(Integer)
#     workstate = Column(Integer)
#     verifycode = Column(Text)
#     terminal_id = Column(Integer)
#     punch_type = Column(Text)
#     operator = Column(Text)
#     operator_reason = Column(Text)
#     operator_time = Column(DateTime)
#     IsSelect = Column(Integer)
#     reserved1 = Column(Text)
#     reserved2 = Column(Text)
#     middleware_id = Column(BigInteger)
#     attendance_event = Column(Text)
#     login_combination = Column(Integer)
#     status = Column(Integer)
#     annotation = Column(Text)
#     processed = Column(Integer)

#     def to_dict(self) -> Dict:
#         """Converts HREmployeeExt instance to dictionary."""
#         return {
#             "employee_id": self.employee_id,
#             "punch_time": self.punch_time,
#             "workcode": self.workcode,
#             "workstate": self.workstate,
#             "verifycode": self.verifycode,
#             "terminal_id": self.terminal_id,
#             "punch_type": self.punch_type,
#             "operator": self.operator,
#             "operator_reason": self.operator_reason,
#             "operator_time": self.operator_time,
#             "IsSelect": self.IsSelect,
#             "reserved1": self.reserved1,
#             "reserved2": self.reserved2,
#             "middleware_id": self.middleware_id,
#             "attendance_event": self.attendance_event,
#             "login_combination": self.login_combination,
#             "status": self.status,
#             "annotation": self.annotation,
#             "processed": self.processed
#         }
