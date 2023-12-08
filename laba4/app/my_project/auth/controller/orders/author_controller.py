from laba4.app.my_project.auth.service import author_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class AuthorController(GeneralController):
    _service = author_service

    def insert_author_par(self, name, title, email):
        self._service.insert_into_author(name, title, email)

    def insert_multiple_author(self, name):
        self._service.insert_into_multiple(name)
