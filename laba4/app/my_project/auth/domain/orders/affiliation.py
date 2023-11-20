from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Affiliation(db.Model,IDto):
    """
    Model declaration for the 'affiliation' table.
    """
    __tablename__ = "affiliation"

    courses_id1 = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)
    authors_id1 = db.Column(db.Integer, db.ForeignKey('authors.id'), primary_key=True)


    courses = db.relationship("Course", backref="affiliations")
    authors = db.relationship("Author", backref="affiliations")

    def __repr__(self) -> str:
        return f"Affiliation(courses_id1={self.courses_id1}, authors_id1={self.authors_id1})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "courses_id1": self.courses_id1,
            "authors_id1": self.authors_id1,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Affiliation:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Affiliation(
            courses_id1=dto_dict.get("courses_id1"),
            authors_id1=dto_dict.get("authors_id1"),
        )
        return obj
