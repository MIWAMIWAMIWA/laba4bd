from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.student import Student


class StudentDAO(GeneralDAO):
    _domain_type = Student