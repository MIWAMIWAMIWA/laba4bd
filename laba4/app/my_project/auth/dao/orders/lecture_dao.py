from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.lecture import Lecture


class LectureDAO(GeneralDAO):

    _domain_type = Lecture