from laba4.app.my_project.auth.dao import  module_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class ModuleService(GeneralService):
    _dao = module_dao