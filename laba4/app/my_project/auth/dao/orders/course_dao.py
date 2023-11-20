from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.courses import Course


class CourseDAO(GeneralDAO):

    _domain_type = Course
