from laba4.app.my_project.auth.service import attempt_answer_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class AttemptAnswerController(GeneralController):

    _service = attempt_answer_service
