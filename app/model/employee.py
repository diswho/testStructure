from sqlalchemy import Boolean, Column,  Integer, String, Text, DateTime, Numeric, BigInteger
from sqlalchemy.orm import relationship
from typing import List, Dict, TYPE_CHECKING
# from app.db.session import BasEXT, BasLOC
from app.db.session import Base


class HREmployee(Base):
    __tablename__ = "hr_employee"

    id = Column(Integer, primary_key=True, autoincrement=True)
    emp_pin = Column(Text, nullable=False)
    emp_ssn = Column(Text)
    emp_role = Column(Text)
    emp_firstname = Column(Text, nullable=False)
    emp_lastname = Column(Text)
    emp_username = Column(Text)
    emp_pwd = Column(Text)
    emp_timezone = Column(Text)
    emp_phone = Column(Text)
    emp_payroll_id = Column(Text)
    emp_payroll_type = Column(Text)
    emp_pin2 = Column(Text)
    # Assuming BLOB is stored as Text (base64 encoded)
    emp_photo = Column(Text)
    emp_privilege = Column(Text)
    emp_group = Column(Text)
    emp_hiredate = Column(DateTime)
    emp_address = Column(Text)
    emp_active = Column(Integer, nullable=False)
    emp_firedate = Column(DateTime)
    emp_firereason = Column(Text)
    emp_emergencyphone1 = Column(Text)
    emp_emergencyphone2 = Column(Text)
    emp_emergencyname = Column(Text)
    emp_emergencyaddress = Column(Text)
    emp_cardNumber = Column(Text)
    emp_country = Column(Text)
    emp_city = Column(Text)
    emp_state = Column(Text)
    emp_postal = Column(Text)
    emp_fax = Column(Text)
    emp_email = Column(Text)
    emp_title = Column(Text)
    emp_hourlyrate1 = Column(Numeric)
    emp_hourlyrate2 = Column(Numeric)
    emp_hourlyrate3 = Column(Numeric)
    emp_hourlyrate4 = Column(Numeric)
    emp_hourlyrate5 = Column(Numeric)
    emp_gender = Column(Integer)
    emp_birthday = Column(DateTime)
    emp_operationmode = Column(Integer)
    emp_OtherName = Column(Text)
    emp_Line = Column(Text)
    emp_Passport = Column(Text)
    emp_MotobikeLicence = Column(Text)
    emp_CarLicence = Column(Text)
    emp_customName1 = Column(Text)
    emp_customInfo1 = Column(Text)
    emp_customName2 = Column(Text)
    emp_customInfo2 = Column(Text)
    IsSelect = Column(Integer)
    middleware_id = Column(BigInteger)
    nationalID = Column(Text)
    emp_Verify = Column(Text)
    emp_ViceCard = Column(Text)
    department_id = Column(Integer)
    position_id = Column(Integer)

    def to_dict(self) -> Dict:
        """Converts HREmployeeExt instance to dictionary."""
        return {
            "id": self.id,
            "emp_pin": self.emp_pin,
            "emp_ssn": self.emp_ssn,
            "emp_role": self.emp_role,
            "emp_firstname": self.emp_firstname,
            "emp_lastname": self.emp_lastname,
            "emp_username": self.emp_username,
            "emp_pwd": self.emp_pwd,
            "emp_timezone": self.emp_timezone,
            "emp_phone": self.emp_phone,
            "emp_payroll_id": self.emp_payroll_id,
            "emp_payroll_type": self.emp_payroll_type,
            "emp_pin2": self.emp_pin2,
            "emp_photo": self.emp_photo,
            "emp_privilege": self.emp_privilege,
            "emp_group": self.emp_group,
            "emp_hiredate": self.emp_hiredate,
            "emp_address": self.emp_address,
            "emp_active": self.emp_active,
            "emp_firedate": self.emp_firedate,
            "emp_firereason": self.emp_firereason,
            "emp_emergencyphone1": self.emp_emergencyphone1,
            "emp_emergencyphone2": self.emp_emergencyphone2,
            "emp_emergencyname": self.emp_emergencyname,
            "emp_emergencyaddress": self.emp_emergencyaddress,
            "emp_cardNumber": self.emp_cardNumber,
            "emp_country": self.emp_country,
            "emp_city": self.emp_city,
            "emp_state": self.emp_state,
            "emp_postal": self.emp_postal,
            "emp_fax": self.emp_fax,
            "emp_email": self.emp_email,
            "emp_title": self.emp_title,
            "emp_hourlyrate1": self.emp_hourlyrate1,
            "emp_hourlyrate2": self.emp_hourlyrate2,
            "emp_hourlyrate3": self.emp_hourlyrate3,
            "emp_hourlyrate4": self.emp_hourlyrate4,
            "emp_hourlyrate5": self.emp_hourlyrate5,
            "emp_gender": self.emp_gender,
            "emp_birthday": self.emp_birthday,
            "emp_operationmode": self.emp_operationmode,
            "emp_OtherName": self.emp_OtherName,
            "emp_Line": self.emp_Line,
            "emp_Passport": self.emp_Passport,
            "emp_MotobikeLicence": self.emp_MotobikeLicence,
            "emp_CarLicence": self.emp_CarLicence,
            "emp_customName1": self.emp_customName1,
            "emp_customInfo1": self.emp_customInfo1,
            "emp_customName2": self.emp_customName2,
            "emp_customInfo2": self.emp_customInfo2,
            "IsSelect": self.IsSelect,
            "middleware_id": self.middleware_id,
            "nationalID": self.nationalID,
            "emp_Verify": self.emp_Verify,
            "emp_ViceCard": self.emp_ViceCard,
            "department_id": self.department_id,
            "position_id": self.position_id
        }

# if TYPE_CHECKING:
#     from .item import Item
#     from .role import Role


# class HREmployeeExt(BasEXT):
#     __tablename__ = "hr_employee"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     emp_pin = Column(Text, nullable=False)
#     emp_ssn = Column(Text)
#     emp_role = Column(Text)
#     emp_firstname = Column(Text, nullable=False)
#     emp_lastname = Column(Text)
#     emp_username = Column(Text)
#     emp_pwd = Column(Text)
#     emp_timezone = Column(Text)
#     emp_phone = Column(Text)
#     emp_payroll_id = Column(Text)
#     emp_payroll_type = Column(Text)
#     emp_pin2 = Column(Text)
#     # Assuming BLOB is stored as Text (base64 encoded)
#     emp_photo = Column(Text)
#     emp_privilege = Column(Text)
#     emp_group = Column(Text)
#     emp_hiredate = Column(DateTime)
#     emp_address = Column(Text)
#     emp_active = Column(Integer, nullable=False)
#     emp_firedate = Column(DateTime)
#     emp_firereason = Column(Text)
#     emp_emergencyphone1 = Column(Text)
#     emp_emergencyphone2 = Column(Text)
#     emp_emergencyname = Column(Text)
#     emp_emergencyaddress = Column(Text)
#     emp_cardNumber = Column(Text)
#     emp_country = Column(Text)
#     emp_city = Column(Text)
#     emp_state = Column(Text)
#     emp_postal = Column(Text)
#     emp_fax = Column(Text)
#     emp_email = Column(Text)
#     emp_title = Column(Text)
#     emp_hourlyrate1 = Column(Numeric)
#     emp_hourlyrate2 = Column(Numeric)
#     emp_hourlyrate3 = Column(Numeric)
#     emp_hourlyrate4 = Column(Numeric)
#     emp_hourlyrate5 = Column(Numeric)
#     emp_gender = Column(Integer)
#     emp_birthday = Column(DateTime)
#     emp_operationmode = Column(Integer)
#     emp_OtherName = Column(Text)
#     emp_Line = Column(Text)
#     emp_Passport = Column(Text)
#     emp_MotobikeLicence = Column(Text)
#     emp_CarLicence = Column(Text)
#     emp_customName1 = Column(Text)
#     emp_customInfo1 = Column(Text)
#     emp_customName2 = Column(Text)
#     emp_customInfo2 = Column(Text)
#     IsSelect = Column(Integer)
#     middleware_id = Column(BigInteger)
#     nationalID = Column(Text)
#     emp_Verify = Column(Text)
#     emp_ViceCard = Column(Text)
#     department_id = Column(Integer)
#     position_id = Column(Integer)

#     def to_dict(self) -> Dict:
#         """Converts HREmployeeExt instance to dictionary."""
#         return {
#             "id": self.id,
#             "emp_pin": self.emp_pin,
#             "emp_ssn": self.emp_ssn,
#             "emp_role": self.emp_role,
#             "emp_firstname": self.emp_firstname,
#             "emp_lastname": self.emp_lastname,
#             "emp_username": self.emp_username,
#             "emp_pwd": self.emp_pwd,
#             "emp_timezone": self.emp_timezone,
#             "emp_phone": self.emp_phone,
#             "emp_payroll_id": self.emp_payroll_id,
#             "emp_payroll_type": self.emp_payroll_type,
#             "emp_pin2": self.emp_pin2,
#             "emp_photo": self.emp_photo,
#             "emp_privilege": self.emp_privilege,
#             "emp_group": self.emp_group,
#             "emp_hiredate": self.emp_hiredate,
#             "emp_address": self.emp_address,
#             "emp_active": self.emp_active,
#             "emp_firedate": self.emp_firedate,
#             "emp_firereason": self.emp_firereason,
#             "emp_emergencyphone1": self.emp_emergencyphone1,
#             "emp_emergencyphone2": self.emp_emergencyphone2,
#             "emp_emergencyname": self.emp_emergencyname,
#             "emp_emergencyaddress": self.emp_emergencyaddress,
#             "emp_cardNumber": self.emp_cardNumber,
#             "emp_country": self.emp_country,
#             "emp_city": self.emp_city,
#             "emp_state": self.emp_state,
#             "emp_postal": self.emp_postal,
#             "emp_fax": self.emp_fax,
#             "emp_email": self.emp_email,
#             "emp_title": self.emp_title,
#             "emp_hourlyrate1": self.emp_hourlyrate1,
#             "emp_hourlyrate2": self.emp_hourlyrate2,
#             "emp_hourlyrate3": self.emp_hourlyrate3,
#             "emp_hourlyrate4": self.emp_hourlyrate4,
#             "emp_hourlyrate5": self.emp_hourlyrate5,
#             "emp_gender": self.emp_gender,
#             "emp_birthday": self.emp_birthday,
#             "emp_operationmode": self.emp_operationmode,
#             "emp_OtherName": self.emp_OtherName,
#             "emp_Line": self.emp_Line,
#             "emp_Passport": self.emp_Passport,
#             "emp_MotobikeLicence": self.emp_MotobikeLicence,
#             "emp_CarLicence": self.emp_CarLicence,
#             "emp_customName1": self.emp_customName1,
#             "emp_customInfo1": self.emp_customInfo1,
#             "emp_customName2": self.emp_customName2,
#             "emp_customInfo2": self.emp_customInfo2,
#             "IsSelect": self.IsSelect,
#             "middleware_id": self.middleware_id,
#             "nationalID": self.nationalID,
#             "emp_Verify": self.emp_Verify,
#             "emp_ViceCard": self.emp_ViceCard,
#             "department_id": self.department_id,
#             "position_id": self.position_id
#         }
