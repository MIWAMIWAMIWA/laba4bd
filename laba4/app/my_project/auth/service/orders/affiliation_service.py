from laba4.app.my_project.auth.dao import affiliation_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class AffiliationService(GeneralService):
    _dao = affiliation_dao
