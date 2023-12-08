from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class StudentWorkplace(db.Model, IDto):
    __tablename__ = "workplace_student"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link = db.Column(db.String(100))
    id_student = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"WorkplaceStudent({self.id}, '{self.link}', {self.id_student})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "link": self.link,
            "student_id": self.id_student,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> StudentWorkplace:
        obj = StudentWorkplace(
            id=dto_dict.get("id"),
            link=dto_dict.get("link"),
            id_student=dto_dict.get("student"),
        )
        return obj
