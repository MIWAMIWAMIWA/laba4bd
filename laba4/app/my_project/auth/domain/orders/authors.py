from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Author(db.Model, IDto):
    """
    Model declaration for the 'authors' table.
    """
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    authors_name = db.Column(db.String(45), nullable=False)
    authors_title = db.Column(db.String(45), nullable=False)
    authors_email = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Author({self.id}, '{self.authors_name}', '{self.authors_title}', '{self.authors_email}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "authors_name": self.authors_name,
            "authors_title": self.authors_title,
            "authors_email": self.authors_email,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Author:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Author(
            authors_name=dto_dict.get("authors_name"),
            authors_title=dto_dict.get("authors_title"),
            authors_email=dto_dict.get("authors_email"),
        )
        return obj
