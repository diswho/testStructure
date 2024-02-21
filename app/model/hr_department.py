from sqlalchemy import Boolean, Column,  Integer, String, Text,BigInteger
from app.db.session import Base

class HRDepartment(Base):
    __tablename__ = 'hr_department'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dept_code = Column(Integer, nullable=False)
    dept_name = Column(String, nullable=False)
    dept_parentcode = Column(Integer, nullable=False)
    useCode = Column(Boolean)
    dept_operationmode = Column(Integer)
    middleware_id = Column(BigInteger)
    defaultDepartment = Column(Integer)
    company_id = Column(Integer, nullable=False)
    lineToken = Column(Text)
    description = Column(Text)

    def to_dict(self):
        return {
            'id': self.id,
            'dept_code': self.dept_code,
            'dept_name': self.dept_name,
            'dept_parentcode': self.dept_parentcode,
            'useCode': self.useCode,
            'dept_operationmode': self.dept_operationmode,
            'middleware_id': self.middleware_id,
            'defaultDepartment': self.defaultDepartment,
            'company_id': self.company_id,
            'lineToken': self.lineToken,
            'description': self.description
        }