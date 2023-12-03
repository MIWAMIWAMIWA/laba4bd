from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class AttemptAnswer(db.Model, IDto):

    __tablename__ = "Attempt_answer"
    idAttemptAns = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_answer = db.Column(db.String(200), nullable=True)
    is_correct = db.Column(db.Boolean, nullable=True)
    Attempt_idAttempt = db.Column(db.Integer, db.ForeignKey('Attempt.idAttempt'))
    test_question_id_question = db.Column(db.Integer, db.ForeignKey('test_question.id_question'))


    attempt = db.relationship("Attempt", backref="attempt_answers")
    test_question = db.relationship("TestQuestion", backref="attempt_answers")

    def __repr__(self) -> str:
        return f"AttemptAnswer(idAttemptAns={self.idAttemptAns},user_answer='{self.user_answer}', is_correct={self.is_correct}, " \
               f"Attempt_idAttempt={self.Attempt_idAttempt}, test_question_id_question={self.test_question_id_question})"

    def put_into_dto(self) -> Dict[str, Any]:

        from laba4.app.my_project.auth.controller import attempt_controller
        from laba4.app.my_project.auth.controller import test_question_controller
        return {
            "id":self.idAttemptAns,
            "user_answer": self.user_answer,
            "is_correct": self.is_correct,
            "Attempt_idAttempt": attempt_controller.find_by_id(self.Attempt_idAttempt),
            "test_question_id_question": test_question_controller.find_by_id(self.test_question_id_question),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AttemptAnswer:

        obj = AttemptAnswer(
            idAttemptAns=dto_dict.get("id"),
            user_answer=dto_dict.get("user_answer"),
            is_correct=dto_dict.get("is_correct"),
            Attempt_idAttempt=dto_dict.get("Attempt_idAttempt"),
            test_question_id_question=dto_dict.get("test_question_id_question"),
        )
        return obj
