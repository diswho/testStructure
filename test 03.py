from sqlalchemy import create_engine, MetaData, func, insert, text
from sqlalchemy.orm import sessionmaker
from app.model import Punch,  Shift, AttDaySummary, StatisticItem

from app.db.session import Base

DB_LOCAL = "sqlite:///./local.db"
DB_EXTRA = r"sqlite:///C:\\Users\\phuong\\OneDrive\\Private\\Xokthavi\\HR\\ZKTimeNet.db"
# Create an engine
engLOC = create_engine(DB_LOCAL, echo=False)
# engEXT = create_engine(DB_EXTRA, echo=False)
# engLOC = create_engine(DB_LOCAL, echo=True)
# engEXT = create_engine(DB_EXTRA, echo=True)

# Define metadata
metadata = MetaData()
# Create a session
SesLOC = sessionmaker(bind=engLOC)
# SesEXT = sessionmaker(bind=engEXT)
Base.metadata.create_all(bind=engLOC)

try:
    sesLOC = SesLOC()
    # query = "SELECT id, shift_name ,start_date FROM att_shift "
    result = sesLOC.query(AttDaySummary)\
        .join(StatisticItem, AttDaySummary.item_id == StatisticItem.id)\
        .filter(func.strftime('%Y-%m', AttDaySummary.att_date) == '2023-11')
    # .join(StatisticItem, AttDaySummary.item_id)\
    for raw in result:
        print(raw)
except Exception as e:
    print(f"error {str(e)}")
finally:
    # Close sessions
    # sesEXT.close()
    sesLOC.close()
