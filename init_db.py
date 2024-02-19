from app.db.session import BasLOC, engLOC, SesLOC
from app.model.employee import HREmployee
# from ap


def init_db() -> None:
    sess = SesLOC()
    BasLOC.metadata.create_all(bind=engLOC)
    new_employee = HREmployee(emp_pin="001",
                              emp_firstname="test",
                              emp_active=1)
    sess.add(new_employee)
    sess.commit()
    sess.refresh(new_employee)


def main() -> None:
    # logger.info("====== Creating initial data")
    init_db()
    # logger.info("====== Initial data created")


if __name__ == "__main__":
    main()

# python init_db.py
