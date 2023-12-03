from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.module import Module


class ModuleDAO(GeneralDAO):

    _domain_type = Module