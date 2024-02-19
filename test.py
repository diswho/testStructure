from sqlalchemy import cast, Integer, create_engine, MetaData, func, insert, text, select
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
    totals = func.sum(AttDaySummary.item_results)

    sub_shift_detail = select(
        AttDaySummary.employee_id,
        StatisticItem.item_desc,
        cast(totals, Integer).label('totals'))\
        .join(StatisticItem, AttDaySummary.item_id == StatisticItem.id)\
        .where(func.strftime('%Y-%m', AttDaySummary.att_date) == '2023-01', AttDaySummary.employee_id == 5)\
        .group_by(AttDaySummary.employee_id,
                  AttDaySummary.item_id,
                  StatisticItem.item_desc)\
        .order_by(AttDaySummary.employee_id,
                  AttDaySummary.item_id,
                  StatisticItem.item_desc)

    result = sesLOC.execute(sub_shift_detail)
    for row in result:
        print(row)
except Exception as e:
    print(f"error {str(e)}")
finally:
    # Close sessions
    # sesEXT.close()
    sesLOC.close()
