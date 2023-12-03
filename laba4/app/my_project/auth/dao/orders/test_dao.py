from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.test import Test


class TestDAO(GeneralDAO):
    _domain_type = Test
