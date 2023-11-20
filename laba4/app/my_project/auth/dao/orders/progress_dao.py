from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.progress import Progress


class ProgressDAO(GeneralDAO):
    _domain_type = Progress
