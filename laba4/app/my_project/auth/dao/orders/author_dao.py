from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.authors import Author


class AuthorDAO(GeneralDAO):

    _domain_type = Author