from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain import Affiliation


class AffiliationDAO(GeneralDAO):

    _domain_type = Affiliation
