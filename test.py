from sqlalchemy import cast, Integer, create_engine, MetaData, func, insert, text, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import case

from app.model import HRDepartment
from app.db.session import Base

DB_LOCAL = "sqlite:///./local.db"
# DB_EXTRA = r"sqlite:///C:\\Users\\phuong\\OneDrive\\Private\\Xokthavi\\HR\\ZKTimeNet.db"
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

    def department_list(dept_code, indent=0):
        list = sesLOC.query(HRDepartment).filter_by(
            dept_parentcode=dept_code).all()
        for child_depart in list:
            print('\t' * indent + f'i:{child_depart.id} \tc:{child_depart.dept_code} \tn:{child_depart.dept_name}')
            department_list(child_depart.dept_code, indent+1)
    department_list(0)
    # def print_department_tree(department, indent=0):
    #     print('-' * indent + str(department.id) + '=' +
    #           str(department.dept_code) + '-' + department.dept_name)
    #     for child_department in department.children:
    #         print_department_tree(child_department, indent + 1)

    # root_departments = sesLOC.query(
    #     HRDepartment).filter_by(dept_parentcode=0).all()
    # for root_department in root_departments:
    #     print_department_tree(root_department)

except Exception as e:
    print(f"error {str(e)}")
finally:
    # Close sessions
    # sesEXT.close()
    sesLOC.close()
