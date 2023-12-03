from laba4.app.my_project.auth.service import  progress_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class ProgressController(GeneralController):

    _service = progress_service