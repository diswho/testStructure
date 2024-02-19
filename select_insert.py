from sqlalchemy import create_engine,  MetaData,   func, insert
from sqlalchemy.orm import sessionmaker
from app.model import Punch, AttDaySummary
from app.db.session import Base

DB_LOCAL = "sqlite:///./local.db"
DB_EXTRA = r"sqlite:///C:\\Users\\phuong\\OneDrive\\Private\\Xokthavi\\HR\\ZKTimeNet.db"
# Create an engine
engLOC = create_engine(DB_LOCAL, echo=False)
engEXT = create_engine(DB_EXTRA, echo=False)
# engLOC = create_engine(DB_LOCAL, echo=True)
# engEXT = create_engine(DB_EXTRA, echo=True)

# Define metadata
metadata = MetaData()
# Create a session
SesLOC = sessionmaker(bind=engLOC)
SesEXT = sessionmaker(bind=engEXT)
Base.metadata.create_all(bind=engLOC)

try:
    sesLOC = SesLOC()
    sesEXT = SesEXT()
    query = sesEXT.query(AttDaySummary)\
        .filter(func.strftime('%Y', AttDaySummary.att_date) == '2023')
    # .filter(Punch.punch_time >= '2023-06-01')
    # .filter(func.strftime('%Y-%m', Punch.punch_time) >= '2023-05-01')

    results = query.all()

    # Output the results
    for result in results:
        sesLOC.execute(insert(AttDaySummary).values(result.to_dict()))
        print(result.att_date)
    sesLOC.commit()
except Exception as e:
    print(f"error {str(e)}")
finally:
    # Close sessions
    sesEXT.close()
    sesLOC.close()
