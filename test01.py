from sqlalchemy import create_engine,  MetaData,   func
from sqlalchemy.orm import sessionmaker
from app.model import AttDaySummary, StatisticItem

DB_LOCAL = "sqlite:///./local.db"
# Create an engine
engine = create_engine(DB_LOCAL, echo=True)

# Define metadata
metadata = MetaData()
# Create a session
Session = sessionmaker(bind=engine)
session = Session()
# Perform the query
query = session.query(
    AttDaySummary.id,
    func.strftime('%Y-%m', AttDaySummary.att_date).label('att_month'),
    AttDaySummary.att_date,
    AttDaySummary.employee_id,
    StatisticItem.item_desc,
    AttDaySummary.item_results)\
    .join(StatisticItem, AttDaySummary.item_id == StatisticItem.id)\
    .filter(func.strftime('%Y-%m', AttDaySummary.att_date) == '2023-11')\
    .order_by(AttDaySummary.att_date.desc())
# Fetch the results
results = query.all()

# Output the results
for result in results:
    print(result)
session.close()
