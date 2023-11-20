from laba4.app.my_project.auth.dao import attempt_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class AttemptService(GeneralService):
    _dao = attempt_dao