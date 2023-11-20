from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class TestQuestion(db.Model, IDto):
    """
    Model declaration for the 'test_question' table.
    """
    __tablename__ = "test_question"

    id_question = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_text = db.Column(db.String(200), nullable=False)
    answers = db.Column(db.String(200), nullable=False)
    correct_answer = db.Column(db.String(200), nullable=False)
    test_idtest = db.Column(db.Integer, db.ForeignKey('test.idtest'), nullable=False)

    # Define relationship
    test = db.relationship("Test", backref="test_questions")

    def __repr__(self) -> str:
        return f"TestQuestion(id_question={self.id_question}, question_text='{self.question_text}', " \
               f"answers='{self.answers}', correct_answer='{self.correct_answer}', test_idtest={self.test_idtest})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "id_question": self.id_question,
            "question_text": self.question_text,
            "answers": self.answers,
            "correct_answer": self.correct_answer,
            "test_idtest": self.test_idtest,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TestQuestion:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = TestQuestion(
            question_text=dto_dict.get("question_text"),
            answers=dto_dict.get("answers"),
            correct_answer=dto_dict.get("correct_answer"),
            test_idtest=dto_dict.get("test_idtest"),
        )
        return obj
