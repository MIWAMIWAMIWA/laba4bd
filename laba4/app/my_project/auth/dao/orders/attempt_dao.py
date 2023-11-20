from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.attempt import Attempt


class AttemptDAO(GeneralDAO):

    _domain_type = Attempt