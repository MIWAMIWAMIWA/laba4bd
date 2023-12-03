from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.student_workplace import StudentWorkplace


class WorkplaceDAO(GeneralDAO):
    _domain_type = StudentWorkplace