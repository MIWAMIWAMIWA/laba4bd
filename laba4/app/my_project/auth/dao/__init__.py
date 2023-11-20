from .orders.Afiliation_dao import AffiliationDAO
from .orders.attempt_answer_dao import AttemptAnswerDAO
from .orders.attempt_dao import AttemptDAO
from .orders.author_dao import AuthorDAO
from .orders.course_dao import CourseDAO
from .orders.lecture_dao import LectureDAO
from .orders.module_dao import ModuleDAO
from .orders.progress_dao import ProgressDAO
from .orders.student_dao import StudentDAO
from .orders.test_dao import TestDAO
from .orders.test_question_dao import TestQuestionDAO

affiliation_dao = AffiliationDAO()
attempt_dao = AttemptDAO()
author_dao = AuthorDAO()
course_dao = CourseDAO()
lecture_dao = LectureDAO()
module_dao = ModuleDAO()
progress_dao = ProgressDAO()
student_dao = StudentDAO()
test_dao = TestDAO()
test_question_dao = TestQuestionDAO()
attempt_answer_dao = AttemptAnswerDAO()
