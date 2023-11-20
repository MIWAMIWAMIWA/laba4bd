from laba4.app.my_project.auth.dao import author_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class AuthorService(GeneralService):
    _dao = author_dao
