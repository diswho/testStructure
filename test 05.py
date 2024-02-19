from sqlalchemy import create_engine, MetaData, func, insert, text, select
from sqlalchemy.orm import sessionmaker
from app.model import Punch,  Shift, AttDaySummary, StatisticItem

from app.db.session import Base

DB_LOCAL = "sqlite:///./local.db"
DB_EXTRA = r"sqlite:///C:\\Users\\phuong\\OneDrive\\Private\\Xokthavi\\HR\\ZKTimeNet.db"
# Create an engine
engLOC = create_engine(DB_LOCAL, echo=False)

# Define metadata
metadata = MetaData()
# Create a session
SesLOC = sessionmaker(bind=engLOC)
# SesEXT = sessionmaker(bind=engEXT)
Base.metadata.create_all(bind=engLOC)

try:
    sesLOC = SesLOC()
    stmt = select(AttDaySummary, StatisticItem).join(
        StatisticItem, AttDaySummary.item_id == StatisticItem.id)\
        .where(func.strftime('%Y-%m', AttDaySummary.att_date) == '2023-11')\
        .where(AttDaySummary.employee_id == 151)
    result = sesLOC.execute(stmt)
    for row in result:
        print(row.AttDaySummary, row.StatisticItem)
except Exception as e:
    print(f"error {str(e)}")
finally:
    # Close sessions
    # sesEXT.close()
    sesLOC.close()
