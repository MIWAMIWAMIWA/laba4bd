from laba4.app.my_project.auth.dao import  progress_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class ProgressService(GeneralService):
    _dao = progress_dao