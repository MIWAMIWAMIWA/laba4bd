from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Student(db.Model,IDto):

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    students_name = db.Column(db.String(45), nullable=False)
    students_surname = db.Column(db.String(45), nullable=False)
    students_course = db.Column(db.Integer, nullable=True)

    def __repr__(self) -> str:
        return f"Student(id={self.id}, students_name='{self.students_name}', " \
               f"students_surname='{self.students_surname}', students_course={self.students_course})"

    def put_into_dto(self) -> Dict[str, Any]:

        return {
            "id": self.id,
            "students_name": self.students_name,
            "students_surname": self.students_surname,
            "students_course": self.students_course,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Student:

        obj = Student(
            students_name=dto_dict.get("students_name"),
            students_surname=dto_dict.get("students_surname"),
            students_course=dto_dict.get("students_course"),
        )
        return obj
