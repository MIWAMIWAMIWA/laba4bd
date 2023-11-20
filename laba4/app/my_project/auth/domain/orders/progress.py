from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Progress(db.Model, IDto):

    __tablename__ = "progress"
    idPr = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_of_start = db.Column(db.Date, nullable=False)
    current_deadline = db.Column(db.Date, nullable=True)
    students_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=True)
    modules_modules_id = db.Column(db.Integer, db.ForeignKey('modules.modules_id'), nullable=True)


    students = db.relationship("Student", backref="progress")
    modules = db.relationship("Module", backref="progress")

    def __repr__(self) -> str:
        return f"Progress(idPr={self.idPr},date_of_start={self.date_of_start}, current_deadline={self.current_deadline}, " \
               f"students_id={self.students_id}, modules_modules_id={self.modules_modules_id})"

    def put_into_dto(self) -> Dict[str, Any]:

        from laba4.app.my_project.auth.controller import student_controller
        from laba4.app.my_project.auth.controller import module_controller
        return {
            "id":self.idPr,
            "date_of_start": self.date_of_start,
            "current_deadline": self.current_deadline,
            "students_id": student_controller.find_by_id(self.students_id),
            "modules_modules_id": module_controller.find_by_id(self.modules_modules_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Progress:

        obj = Progress(
            idPr=dto_dict.get("id"),
            date_of_start=dto_dict.get("date_of_start"),
            current_deadline=dto_dict.get("current_deadline"),
            students_id=dto_dict.get("students_id"),
            modules_modules_id=dto_dict.get("modules_modules_id"),
        )
        return obj
