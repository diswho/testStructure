from fastapi import APIRouter
from sqlalchemy import text, insert
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.expression import func
from datetime import datetime, timedelta

from app.db.session import SesEXT, engEXT, SesLOC, engLOC, Base
from app.model.employee import HREmployee
from app.model import AttendanceTimetable,  EmployeeShift,  HREmployee,  ShiftDetails,  Shift, StatisticItem,  Punch, AttDaySummary, PaySalaryStructure, HRDepartment

router = APIRouter()


@router.get("/new_data/")
async def new_data():
    try:
        # Production use
        current_date = datetime.now()
        one_month_ago = current_date - timedelta(days=30)

        sesExt = SesEXT()
        sesLoc = SesLOC()
        Base.metadata.create_all(bind=engLOC)
        max_ids = {
            AttendanceTimetable: sesLoc.query(func.max(AttendanceTimetable.id)).scalar(),
            EmployeeShift: sesLoc.query(func.max(EmployeeShift.id)).scalar(),
            HREmployee: sesLoc.query(func.max(HREmployee.id)).scalar(),
            HRDepartment: sesLoc.query(func.max(HRDepartment.id)).scalar(),
            PaySalaryStructure: sesLoc.query(func.max(PaySalaryStructure.Id)).scalar(),
            ShiftDetails: sesLoc.query(func.max(ShiftDetails.id)).scalar(),
            Shift: sesLoc.query(func.max(Shift.id)).scalar(),
            StatisticItem: sesLoc.query(func.max(StatisticItem.id)).scalar(),
            AttDaySummary: sesLoc.query(func.max(AttDaySummary.id)).scalar(),
            Punch: sesLoc.query(func.max(Punch.id)).scalar(),
        }
        for table, max_id in max_ids.items():
            if max_id is None:
                max_id = 0
            if table == AttDaySummary and max_id == 0:
                max_id = sesExt.query(func.max(AttDaySummary.id).filter(
                    AttDaySummary.att_date <= '2023-06-01')).scalar()
                print(max_id)
            elif table == Punch and max_id == 0:
                max_id = sesExt.query(func.max(Punch.id).filter(
                    Punch.punch_time <= '2023-06-01')).scalar()
                print(max_id)
            if table == PaySalaryStructure:
                data_ext = sesExt.query(table).filter(table.Id > max_id).all()
            else:
                data_ext = sesExt.query(table).filter(table.id > max_id).all()
            for rec in data_ext:
                sesLoc.execute(insert(table).values(rec.to_dict()))
            sesLoc.commit()
        return {"message": "Raw SQL query executed successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        # Close sessions
        sesExt.close()
        sesLoc.close()


@router.get("/raw_sql_insert/")
async def raw_sql_insert():
    sesExt = SesEXT()
    sesLoc = SesLOC()
    Base.metadata.create_all(bind=engLOC)
    try:
        raw_sql_query = "SELECT * FROM hr_employee"
        result = sesExt.execute(text(raw_sql_query))
        # 2000-01-01 00:00:00.000000
        for row in result:
            # emp_hiredate = datetime.strptime("2000-01-01 00:00:00", '%Y-%m-%d %H:%M:%S')
            # emp_firedate = datetime.strptime("2000-01-01 00:00:00", '%Y-%m-%d %H:%M:%S')
            # emp_birthday = datetime.strptime("2000-01-01 00:00:00", '%Y-%m-%d %H:%M:%S')
            emp_hiredate = None
            emp_firedate = None
            emp_birthday = None
            if row[16]:
                emp_hiredate = datetime.strptime(row[16], '%Y-%m-%d %H:%M:%S')
            if row[19]:
                emp_firedate = datetime.strptime(row[19], '%Y-%m-%d %H:%M:%S')
            if row[39]:
                emp_birthday = datetime.strptime(row[39], '%Y-%m-%d %H:%M:%S')
            new_employee = HREmployee(
                id=row[0], emp_pin=row[1], emp_ssn=row[2], emp_role=row[3], emp_firstname=row[4], emp_lastname=row[5], emp_username=row[6],
                emp_pwd=row[7], emp_timezone=row[8], emp_phone=row[9], emp_payroll_id=row[10], emp_payroll_type=row[11], emp_pin2=row[12],
                emp_photo=row[13], emp_privilege=row[14], emp_group=row[15], emp_hiredate=emp_hiredate, emp_address=row[17], emp_active=row[18],
                emp_firedate=emp_firedate, emp_firereason=row[20], emp_emergencyphone1=row[21],
                emp_emergencyphone2=row[22], emp_emergencyname=row[23], emp_emergencyaddress=row[24],
                emp_cardNumber=row[25], emp_country=row[26], emp_city=row[27],
                emp_state=row[28], emp_postal=row[29], emp_fax=row[30], emp_email=row[31], emp_title=row[32], emp_hourlyrate1=row[33],
                emp_hourlyrate2=row[34], emp_hourlyrate3=row[35], emp_hourlyrate4=row[36], emp_hourlyrate5=row[37],
                emp_gender=row[38], emp_birthday=emp_birthday, emp_operationmode=row[40], emp_OtherName=row[41],
                emp_Line=row[42], emp_Passport=row[43], emp_MotobikeLicence=row[44], emp_CarLicence=row[45],
                emp_customName1=row[46], emp_customInfo1=row[47], emp_customName2=row[48],
                emp_customInfo2=row[49], IsSelect=row[50], middleware_id=row[51], nationalID=row[52], emp_Verify=row[53],
                emp_ViceCard=row[54], department_id=row[55], position_id=row[56])
            sesLoc.add(new_employee)
            sesLoc.commit()
            sesLoc.refresh(new_employee)
            print(row)
            # print(type(row).__name__)
        return {"message": "Raw SQL query executed successfully"}
    except SQLAlchemyError as e:
        return {"error": str(e)}
    finally:
        # Close session
        sesExt.close()
        sesLoc.close()

@router.get("/department_tree/")
async def department_tree():
    return {"message":"Success"}