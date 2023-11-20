from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Course(db.Model, IDto):
    """
    Model declaration for the 'courses' table.
    """
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    courses_name = db.Column(db.String(45), nullable=False)
    courses_description = db.Column(db.String(300), nullable=True, default=None)
    courses_diffc = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Course({self.id}, '{self.courses_name}', '{self.courses_description}', {self.courses_diffc})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "courses_name": self.courses_name,
            "courses_description": self.courses_description,
            "courses_diffc": self.courses_diffc,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Course:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Course(
            courses_name=dto_dict.get("courses_name"),
            courses_description=dto_dict.get("courses_description"),
            courses_diffc=dto_dict.get("courses_diffc"),
        )
        return obj
