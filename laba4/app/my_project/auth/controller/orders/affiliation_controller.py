from laba4.app.my_project.auth.service import affiliation_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class AffiliationController(GeneralController):

    _service = affiliation_service
