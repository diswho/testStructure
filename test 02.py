from sqlalchemy import create_engine, MetaData, func, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from app.model import AttDaySummary, StatisticItem

DB_LOCAL = "sqlite:///./local.db"
# Create an engine
engine = create_engine(DB_LOCAL)

# Define metadata
metadata = MetaData()
# Create a session
Session = sessionmaker(bind=engine)


def init():
    sesExt = Session()
    # Perform the query
    try:
        raw_sql_query = "SELECT	* FROM hr_employee WHERE 1 = 1 LIMIT 10"
        result = sesExt.execute(text(raw_sql_query))
        for row in result:
            print(
                f'emp_pin: \t{row.emp_pin},\temp_firstname: \t{row.emp_firstname},\t\temp_lastname: \t{row.emp_lastname}')
        return {"message": "Success"}
    except SQLAlchemyError as e:
        return {"error": str(e)}
    finally:
        # Close session
        sesExt.close()


init()
