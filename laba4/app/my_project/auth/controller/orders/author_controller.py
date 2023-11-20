from laba4.app.my_project.auth.service import  author_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class AuthorController(GeneralController):

    _service = author_service
