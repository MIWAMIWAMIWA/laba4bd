from .orders.affiliation_controller import AffiliationController
from .orders.attempt_answer_controller import AttemptAnswerController
from .orders.attempt_controller import AttemptController
from .orders.author_controller import AuthorController

from .orders.course_controller import CourseController
from .orders.module_controller import ModuleController
from .orders.progress_controller import ProgressController
from .orders.student_controller import StudentController
from .orders.test_controller import TestController
from .orders.test_question_controller import TestQuestionController
from .orders.workplace_controller import WorkplaceController

affiliation_controller = AffiliationController()
attempt_answer_controller = AttemptAnswerController()
attempt_controller = AttemptController()
author_controller = AuthorController()
course_controller = CourseController()
module_controller = ModuleController()
progress_controller = ProgressController()
student_controller = StudentController()
test_question_controller = TestQuestionController()
test_controller = TestController()
workplace_controller = WorkplaceController()
