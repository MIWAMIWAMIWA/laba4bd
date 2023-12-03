from laba4.app.my_project.auth.dao import attempt_answer_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class AttemptAnswerService(GeneralService):
    _dao = attempt_answer_dao
