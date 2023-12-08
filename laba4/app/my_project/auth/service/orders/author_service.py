from laba4.app.my_project.auth.dao import author_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class AuthorService(GeneralService):
    _dao = author_dao

    def insert_into_author(self, name, title, email):
        self._dao.insert_author(name, title, email)

    def insert_into_multiple(self, name):
        self._dao.insert_multiple_authors(name)
