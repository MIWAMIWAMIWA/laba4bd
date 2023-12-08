from laba4.app.my_project.auth.dao import  student_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class StudentService(GeneralService):
    _dao = student_dao

    def generate_databases(self):
        self._dao.generate_tables()