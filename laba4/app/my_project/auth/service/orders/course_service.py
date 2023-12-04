from laba4.app.my_project.auth.dao import course_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class CourseService(GeneralService):
    _dao = course_dao

    def get_procedure(self, String_function):
        if String_function == "MAX" or String_function == "max":
            return course_dao.get_procedure(1)
        elif String_function == "MIN" or String_function == "min":
            return course_dao.get_procedure(2)
        elif String_function == "SUM" or String_function == "sum":
            return course_dao.get_procedure(3)
        else:
            return course_dao.get_procedure(4)

    def aff_insert(self, name, diff, id_author):
        course_dao.insert_with_aff(name, diff, id_author)
