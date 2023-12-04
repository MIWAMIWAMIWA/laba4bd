from laba4.app.my_project.auth.service import student_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class StudentController(GeneralController):

    _service = student_service

    def gen_databases(self):
        self._service.generate_databases()