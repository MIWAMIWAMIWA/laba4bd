from laba4.app.my_project.auth.dao import  course_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class CourseService(GeneralService):
    _dao = course_dao