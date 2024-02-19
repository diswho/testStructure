from sqlalchemy import Boolean, Column,  Integer, String,  DateTime
from typing import Dict
# from app.db.session import BasLOC
from app.db.session import Base


class AttendanceTimetable(Base):
    __tablename__ = 'att_timetable'

    id = Column(Integer, primary_key=True, autoincrement=True)
    timetableType = Column(Integer)
    timetable_color = Column(Integer)
    timetable_name = Column(String)
    timetable_start = Column(DateTime)
    timetable_end = Column(DateTime)
    timetable_checkin_begin = Column(DateTime)
    timetable_checkout_end = Column(DateTime)
    usedForSmartShift = Column(Boolean)
    timetable_checkin_end = Column(DateTime)
    timetable_checkout_begin = Column(DateTime)
    requireWork = Column(Integer)
    timetable_late = Column(Boolean)
    timetable_latecome = Column(Integer)
    timetable_early = Column(Boolean)
    timetable_earlyout = Column(Integer)
    countAbsentLateExceed = Column(Boolean)
    countAbsentLateExceedMins = Column(Integer)
    withoutInAsLateAllDay = Column(Boolean)
    countAbsentEarlyExceed = Column(Boolean)
    countAbsentEarlyExceedMins = Column(Integer)
    withoutOutAsEarlyAllDay = Column(Boolean)
    enableOT = Column(Boolean)
    earlyComeAsWork = Column(Boolean)
    lateOutAsWork = Column(Boolean)
    firstInLastOut = Column(Boolean)
    isDefault = Column(Boolean)
    timetable_lateincluderelatives = Column(Boolean)
    countEarlyComeExceedMins = Column(Integer)
    countLateOutExceedMins = Column(Integer)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "timetableType": self.timetableType,
            "timetable_color": self.timetable_color,
            "timetable_name": self.timetable_name,
            "timetable_start": self.timetable_start,
            "timetable_end": self.timetable_end,
            "timetable_checkin_begin": self.timetable_checkin_begin,
            "timetable_checkout_end": self.timetable_checkout_end,
            "usedForSmartShift": self.usedForSmartShift,
            "timetable_checkin_end": self.timetable_checkin_end,
            "timetable_checkout_begin": self.timetable_checkout_begin,
            "requireWork": self.requireWork,
            "timetable_late": self.timetable_late,
            "timetable_latecome": self.timetable_latecome,
            "timetable_early": self.timetable_early,
            "timetable_earlyout": self.timetable_earlyout,
            "countAbsentLateExceed": self.countAbsentLateExceed,
            "countAbsentLateExceedMins": self.countAbsentLateExceedMins,
            "withoutInAsLateAllDay": self.withoutInAsLateAllDay,
            "countAbsentEarlyExceed": self.countAbsentEarlyExceed,
            "countAbsentEarlyExceedMins": self.countAbsentEarlyExceedMins,
            "withoutOutAsEarlyAllDay": self.withoutOutAsEarlyAllDay,
            "enableOT": self.enableOT,
            "earlyComeAsWork": self.earlyComeAsWork,
            "lateOutAsWork": self.lateOutAsWork,
            "firstInLastOut": self.firstInLastOut,
            "isDefault": self.isDefault,
            "timetable_lateincluderelatives": self.timetable_lateincluderelatives,
            "countEarlyComeExceedMins": self.countEarlyComeExceedMins,
            "countLateOutExceedMins": self.countLateOutExceedMins
        }


# class AttendanceTimetableEXT(BasEXT):
#     __tablename__ = 'att_timetable'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     timetableType = Column(Integer)
#     timetable_color = Column(Integer)
#     timetable_name = Column(String)
#     timetable_start = Column(DateTime)
#     timetable_end = Column(DateTime)
#     timetable_checkin_begin = Column(DateTime)
#     timetable_checkout_end = Column(DateTime)
#     usedForSmartShift = Column(Boolean)
#     timetable_checkin_end = Column(DateTime)
#     timetable_checkout_begin = Column(DateTime)
#     requireWork = Column(Integer)
#     timetable_late = Column(Boolean)
#     timetable_latecome = Column(Integer)
#     timetable_early = Column(Boolean)
#     timetable_earlyout = Column(Integer)
#     countAbsentLateExceed = Column(Boolean)
#     countAbsentLateExceedMins = Column(Integer)
#     withoutInAsLateAllDay = Column(Boolean)
#     countAbsentEarlyExceed = Column(Boolean)
#     countAbsentEarlyExceedMins = Column(Integer)
#     withoutOutAsEarlyAllDay = Column(Boolean)
#     enableOT = Column(Boolean)
#     earlyComeAsWork = Column(Boolean)
#     lateOutAsWork = Column(Boolean)
#     firstInLastOut = Column(Boolean)
#     isDefault = Column(Boolean)
#     timetable_lateincluderelatives = Column(Boolean)
#     countEarlyComeExceedMins = Column(Integer)
#     countLateOutExceedMins = Column(Integer)
#     def to_dict(self) -> Dict:
#         return {
#             "id": self.id,
#             "timetableType": self.timetableType,
#             "timetable_color": self.timetable_color,
#             "timetable_name": self.timetable_name,
#             "timetable_start": self.timetable_start,
#             "timetable_end": self.timetable_end,
#             "timetable_checkin_begin": self.timetable_checkin_begin,
#             "timetable_checkout_end": self.timetable_checkout_end,
#             "usedForSmartShift": self.usedForSmartShift,
#             "timetable_checkin_end": self.timetable_checkin_end,
#             "timetable_checkout_begin": self.timetable_checkout_begin,
#             "requireWork": self.requireWork,
#             "timetable_late": self.timetable_late,
#             "timetable_latecome": self.timetable_latecome,
#             "timetable_early": self.timetable_early,
#             "timetable_earlyout": self.timetable_earlyout,
#             "countAbsentLateExceed": self.countAbsentLateExceed,
#             "countAbsentLateExceedMins": self.countAbsentLateExceedMins,
#             "withoutInAsLateAllDay": self.withoutInAsLateAllDay,
#             "countAbsentEarlyExceed": self.countAbsentEarlyExceed,
#             "countAbsentEarlyExceedMins": self.countAbsentEarlyExceedMins,
#             "withoutOutAsEarlyAllDay": self.withoutOutAsEarlyAllDay,
#             "enableOT": self.enableOT,
#             "earlyComeAsWork": self.earlyComeAsWork,
#             "lateOutAsWork": self.lateOutAsWork,
#             "firstInLastOut": self.firstInLastOut,
#             "isDefault": self.isDefault,
#             "timetable_lateincluderelatives": self.timetable_lateincluderelatives,
#             "countEarlyComeExceedMins": self.countEarlyComeExceedMins,
#             "countLateOutExceedMins": self.countLateOutExceedMins
#         }
