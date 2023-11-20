from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class AttemptAnswer(db.Model, IDto):
    """
    Model declaration for the 'Attempt_answer' table.
    """
    __tablename__ = "Attempt_answer"

    user_answer = db.Column(db.String(200), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    Attempt_idAttempt = db.Column(db.Integer, db.ForeignKey('Attempt.idAttempt'), primary_key=True)
    test_question_id_question = db.Column(db.Integer, db.ForeignKey('test_question.id_question'), primary_key=True)

    # Define relationships
    attempt = db.relationship("Attempt", backref="attempt_answers")
    test_question = db.relationship("TestQuestion", backref="attempt_answers")

    def __repr__(self) -> str:
        return f"AttemptAnswer(user_answer='{self.user_answer}', is_correct={self.is_correct}, " \
               f"Attempt_idAttempt={self.Attempt_idAttempt}, test_question_id_question={self.test_question_id_question})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "user_answer": self.user_answer,
            "is_correct": self.is_correct,
            "Attempt_idAttempt": self.Attempt_idAttempt,
            "test_question_id_question": self.test_question_id_question,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AttemptAnswer:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = AttemptAnswer(
            user_answer=dto_dict.get("user_answer"),
            is_correct=dto_dict.get("is_correct"),
            Attempt_idAttempt=dto_dict.get("Attempt_idAttempt"),
            test_question_id_question=dto_dict.get("test_question_id_question"),
        )
        return obj
