from sqlalchemy import Boolean, Column,  Integer, String, Text, DateTime, Numeric
from app.db.session import Base


class PaySalaryStructure(Base):
    __tablename__ = 'pay_salarystructure'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    forDepartment = Column(Boolean)
    dCode = Column(Integer)
    ePin = Column(String)
    effective_date = Column(DateTime, nullable=False)
    BasicSalary = Column(Numeric, nullable=False)

    def to_dict(self):
        return {
            'Id': self.Id,
            'forDepartment': self.forDepartment,
            'dCode': self.dCode,
            'ePin': self.ePin,
            'effective_date': self.effective_date,
            # Convert Numeric to float for JSON serialization
            'BasicSalary': float(self.BasicSalary)
        }

# CREATE TABLE pay_salarystructure (Id integer primary key autoincrement,
# forDepartment BOOL,
# dCode INT,
# ePin TEXT,
# effective_date DATETIME not null,
# BasicSalary NUMERIC not null);