from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Affiliation(db.Model, IDto):
    __tablename__ = "affiliation"
    idaff = db.Column(db.Integer, primary_key=True, autoincrement=True)
    courses_id1 = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    authors_id1 = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    courses = db.relationship("Course", backref="affiliations")
    authors = db.relationship("Author", backref="affiliations")

    def __repr__(self) -> str:
        return f"Affiliation(idAff={self.idaff},courses_id1={self.courses_id1}, authors_id1={self.authors_id1})"

    def put_into_dto(self) -> Dict[str, Any]:
        from laba4.app.my_project.auth.controller import course_controller
        from laba4.app.my_project.auth.controller import author_controller
        return {
            "id":self.idaff,
            "courses_id1": course_controller.find_by_id(self.courses_id1),
            "authors_id1": author_controller.find_by_id(self.authors_id1)
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Affiliation:
        obj = Affiliation(
            idaff= dto_dict.get("id"),
            courses_id1=dto_dict.get("courses_id1"),
            authors_id1=dto_dict.get("authors_id1"),
        )
        return obj
