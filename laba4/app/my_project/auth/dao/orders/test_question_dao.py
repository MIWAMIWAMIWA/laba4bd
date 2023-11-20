from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.test_question import TestQuestion


class TestQuestionDAO(GeneralDAO):
    _domain_type = TestQuestion