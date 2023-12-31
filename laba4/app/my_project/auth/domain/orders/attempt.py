from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Attempt(db.Model , IDto):

    __tablename__ = "Attempt"

    idAttempt = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_of_attempt = db.Column(db.Date, nullable=True)
    score = db.Column(db.Integer, nullable=True)
    test_idtest = db.Column(db.Integer, db.ForeignKey('test.idtest'))
    students_id = db.Column(db.Integer, db.ForeignKey('students.id'))


    test = db.relationship("Test", backref="attempts")
    students = db.relationship("Student", backref="attempts")

    def __repr__(self) -> str:
        return f"Attempt(idAttempt={self.idAttempt}, date_of_attempt={self.date_of_attempt}, " \
               f"score={self.score}, test_idtest={self.test_idtest}, students_id={self.students_id})"

    def put_into_dto(self) -> Dict[str, Any]:

        from laba4.app.my_project.auth.controller import test_controller
        from laba4.app.my_project.auth.controller import student_controller
        from laba4.app.my_project.auth.dao import attempt_answer_dao
        return {
            "idAttempt": self.idAttempt,
            "date_of_attempt": self.date_of_attempt,
            "score": self.score,
            "test_idtest": test_controller.find_by_id_relation(self.test_idtest),
            "students_id": student_controller.find_by_id(self.students_id),
            "attempt_answers_in this attempt": list(map(lambda x: x.put_into_dto_relation(), attempt_answer_dao.find_objects_with_value('Attempt_idAttempt', self.idAttempt)))
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Attempt:

        obj = Attempt(
            date_of_attempt=dto_dict.get("date_of_attempt"),
            score=dto_dict.get("score"),
            test_idtest=dto_dict.get("test_idtest"),
            students_id=dto_dict.get("students_id"),
        )
        return obj
