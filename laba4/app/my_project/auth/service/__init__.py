from .orders.affiliation_service import AffiliationService
from .orders.attempt_answer_service import AttemptAnswerService
from .orders.attempt_service import AttemptService
from .orders.author_service import AuthorService
from .orders.course_service import CourseService

from .orders.module_service import ModuleService
from .orders.progress_service import ProgressService
from .orders.student_service import StudentService
from .orders.test_question_service import TestQuestionService
from .orders.test_service import TestService
from .orders.workplace_service import WorkplaceService

affiliation_service = AffiliationService()
attempt_answer_service = AttemptAnswerService()
attempt_service = AttemptService()
author_service = AuthorService()
course_service = CourseService()

module_service = ModuleService()
progress_service = ProgressService()
student_service = StudentService()
test_question_service = TestQuestionService()
test_service = TestService()
workplace_service = WorkplaceService()
