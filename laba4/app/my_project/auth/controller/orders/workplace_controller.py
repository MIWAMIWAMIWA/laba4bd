from laba4.app.my_project.auth.service import workplace_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class WorkplaceController(GeneralController):

    _service = workplace_service