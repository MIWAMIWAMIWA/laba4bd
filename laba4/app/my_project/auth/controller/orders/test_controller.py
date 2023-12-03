from laba4.app.my_project.auth.service import test_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class TestController(GeneralController):

    _service = test_service