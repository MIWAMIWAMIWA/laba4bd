from laba4.app.my_project.auth.service import course_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class CourseController(GeneralController):
    _service = course_service

    def get_statistics(self, Option):
        return course_service.get_procedure(Option)
