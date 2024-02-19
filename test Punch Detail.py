from sqlalchemy import create_engine, MetaData, func, insert, text, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import case

from app.model import Punch,  Shift, AttDaySummary, StatisticItem, HREmployee, ShiftDetails, EmployeeShift, AttendanceTimetable
from app.db.session import Base

DB_LOCAL = "sqlite:///./local.db"
# DB_EXTRA = r"sqlite:///C:\\Users\\phuong\\OneDrive\\Private\\Xokthavi\\HR\\ZKTimeNet.db"
# Create an engine
engLOC = create_engine(DB_LOCAL, echo=True)

# Define metadata
metadata = MetaData()
# Create a session
SesLOC = sessionmaker(bind=engLOC)
# SesEXT = sessionmaker(bind=engEXT)
Base.metadata.create_all(bind=engLOC)

try:
    sesLOC = SesLOC()
    check_month = func.strftime('%Y-%m', Punch.punch_time)
    check_date = func.date(Punch.punch_time)
    punch_in = func.min(func.time(Punch.punch_time))
    punch_out = func.max(func.time(Punch.punch_time))

    sub_shift_detail = select(
        func.max(ShiftDetails.shift_date).label('max_shift'),
        ShiftDetails.shift_id,
        ShiftDetails.timetable_id)\
        .group_by(ShiftDetails.shift_id, ShiftDetails.timetable_id).subquery()

    att_shift = select(
        EmployeeShift.employee_id,
        AttendanceTimetable.timetable_start,
        AttendanceTimetable.timetable_end,
        sub_shift_detail.c.timetable_id)\
        .join(EmployeeShift, EmployeeShift.shift_id == sub_shift_detail.c.shift_id)\
        .join(AttendanceTimetable, AttendanceTimetable.id == sub_shift_detail.c.timetable_id)\
        .subquery()

    check_in = func.time(att_shift.c.timetable_start)
    check_out = func.time(att_shift.c.timetable_end)

    stmt = select(
        Punch.id,
        HREmployee.id.label('employee_id'),
        HREmployee.emp_firstname.label('firstname'),
        HREmployee.emp_lastname.label('lastname'),
        check_month, check_date, punch_in, punch_out
    ).join(Punch, Punch.employee_id == HREmployee.id)\
        .join(att_shift, att_shift.c.employee_id == HREmployee.id)\
        .where(func.strftime('%Y-%m', Punch.punch_time) == '2023-04', HREmployee.id == 5)\
        .group_by(HREmployee.id, Punch.punch_time).order_by(HREmployee.id, Punch.punch_time)

    result = sesLOC.execute(stmt)
    for row in result:
        print(row)
except Exception as e:
    print(f"error {str(e)}")
finally:
    # Close sessions
    # sesEXT.close()
    sesLOC.close()
