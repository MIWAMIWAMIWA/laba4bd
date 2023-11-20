from laba4.app.my_project.auth.service import attempt_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class AttemptController(GeneralController):

    _service = attempt_service