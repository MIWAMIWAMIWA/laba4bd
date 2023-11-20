from laba4.app.my_project.auth.service import  lecture_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class LectureController(GeneralController):

    _service = lecture_service