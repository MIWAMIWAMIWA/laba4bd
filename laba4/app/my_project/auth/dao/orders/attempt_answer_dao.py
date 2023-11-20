from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.Attempt_answer import AttemptAnswer


class AttemptAnswerDAO(GeneralDAO):
    _domain_type = AttemptAnswer
