from laba4.app.my_project.auth.dao import workplace_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class WorkplaceService(GeneralService):
    _dao = workplace_dao
