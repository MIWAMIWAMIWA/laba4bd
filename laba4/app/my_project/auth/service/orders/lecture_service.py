from laba4.app.my_project.auth.dao import lecture_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class LectureService(GeneralService):
    _dao = lecture_dao