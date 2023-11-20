from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Progress(db.Model, IDto):
    """
    Model declaration for the 'progress' table.
    """
    __tablename__ = "progress"

    date_of_start = db.Column(db.Date, nullable=False)
    current_deadline = db.Column(db.Date, nullable=True)
    students_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    modules_modules_id = db.Column(db.Integer, db.ForeignKey('modules.modules_id'), primary_key=True)

    # Define relationships
    students = db.relationship("Student", backref="progress")
    modules = db.relationship("Module", backref="progress")

    def __repr__(self) -> str:
        return f"Progress(date_of_start={self.date_of_start}, current_deadline={self.current_deadline}, " \
               f"students_id={self.students_id}, modules_modules_id={self.modules_modules_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "date_of_start": self.date_of_start,
            "current_deadline": self.current_deadline,
            "students_id": self.students_id,
            "modules_modules_id": self.modules_modules_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Progress:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Progress(
            date_of_start=dto_dict.get("date_of_start"),
            current_deadline=dto_dict.get("current_deadline"),
            students_id=dto_dict.get("students_id"),
            modules_modules_id=dto_dict.get("modules_modules_id"),
        )
        return obj
