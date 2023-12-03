from laba4.app.my_project.auth.service import  module_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class ModuleController(GeneralController):

    _service = module_service