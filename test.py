from sqlalchemy import cast, Integer, create_engine, MetaData, func, insert, text, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import case

from app.model import HRDepartment
from app.db.session import Base

import json

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
    descendant_id = []
    child_dept = []

    def get_tree(dept_code=0, indent=0):
        list = sesLOC.query(HRDepartment).filter_by(
            dept_parentcode=dept_code).all()
        for child_depart in list:
            print('  ---  ' * indent + f'{child_depart.dept_name}')
            get_tree(child_depart.dept_code, indent+1)

    def descendant_list(dept_code, indent=0):
        list = sesLOC.query(HRDepartment).filter_by(
            dept_parentcode=dept_code).all()
        for child_depart in list:
            descendant_id.append(child_depart.id)
            descendant_list(child_depart.dept_code, indent+1)

    def child_dept_code(dept_code):
        list = sesLOC.query(HRDepartment).filter_by(
            dept_parentcode=dept_code).all()
        for child_list in list:
            child_dept.append(child_list)
            # child_dept.append(child_list.dept_code)

    depart_code = 172
    # 1, 17, 19, 20, 21, 27, 33, 90, 124, 155, 172, 181
    prt = sesLOC.query(HRDepartment).filter_by(dept_code=depart_code).first()
    if prt:
        descendant_id.append(prt.id)
    get_tree()
    descendant_list(depart_code)
    child_dept_code(depart_code)
    print(f'descendant id: {descendant_id}')
    for chd in child_dept:
        print(
            f'child depart id: {chd.id}, \tcode: {chd.dept_code},\t name: {chd.dept_name}')

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
