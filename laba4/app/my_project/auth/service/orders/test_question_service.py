from laba4.app.my_project.auth.dao import test_question_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class TestQuestionService(GeneralService):
    _dao = test_question_dao