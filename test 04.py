from sqlalchemy import create_engine, MetaData, func, insert, text, select
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
    stmt = select(Shift).where(Shift.id == 1)
    result = sesLOC.scalars(stmt)
    for row in result:
        print(row)
except Exception as e:
    print(f"error {str(e)}")
finally:
    # Close sessions
    # sesEXT.close()
    sesLOC.close()
