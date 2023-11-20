from laba4.app.my_project.auth.dao import  test_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class TestService(GeneralService):
    _dao = test_dao