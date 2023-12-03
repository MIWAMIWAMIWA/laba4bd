from laba4.app.my_project.auth.service import test_question_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class TestQuestionController(GeneralController):

    _service = test_question_service