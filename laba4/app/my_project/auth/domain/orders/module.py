from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db


class Module(db.Model):

    __tablename__ = "modules"

    modules_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modules_name = db.Column(db.String(45), nullable=False)
    modules_position = db.Column(db.Integer, nullable=False)
    time_to_deadline = db.Column(db.Integer, nullable=True, default=None)
    courses_id = db.Column(db.Integer, db.ForeignKey('courses.id'))


    courses = db.relationship("Course", backref="modules")

    def __repr__(self) -> str:
        return f"Module(modules_id={self.modules_id}, modules_name='{self.modules_name}', " \
               f"modules_position={self.modules_position}, time_to_deadline={self.time_to_deadline}, " \
               f"courses_id={self.courses_id})"

    def put_into_dto_relation(self) -> Dict[str, Any]:
        return {
            "modules_id": self.modules_id,
            "modules_name": self.modules_name,
            "modules_position": self.modules_position,
            "time_to_deadline": self.time_to_deadline,
        }

    def put_into_dto(self) -> Dict[str, Any]:

        from laba4.app.my_project.auth.controller import course_controller
        from laba4.app.my_project.auth.dao import test_dao
        return {
            "modules_id": self.modules_id,
            "modules_name": self.modules_name,
            "modules_position": self.modules_position,
            "time_to_deadline": self.time_to_deadline,
            "courses_id": self.courses_id,
            "tests in this module": list(map(lambda x: x.put_into_dto_relation(), test_dao.find_objects_with_value('modules_modules_id', self.modules_id)))
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Module:

        obj = Module(
            modules_name=dto_dict.get("modules_name"),
            modules_position=dto_dict.get("modules_position"),
            time_to_deadline=dto_dict.get("time_to_deadline"),
            courses_id=dto_dict.get("courses_id"),
        )
        return obj
