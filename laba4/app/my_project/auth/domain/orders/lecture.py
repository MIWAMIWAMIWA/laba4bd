from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Lecture(db.Model, IDto):
    """
    Model declaration for the 'lectures' table.
    """
    __tablename__ = "lectures"

    position_in_module = db.Column(db.Integer, nullable=False)
    lectures_name = db.Column(db.String(45), nullable=False)
    link_to_video = db.Column(db.String(200), nullable=False)
    modules_modules_id = db.Column(db.Integer, db.ForeignKey('modules.modules_id'), primary_key=True)

    # Define relationship
    modules = db.relationship("Module", backref="lectures")

    def __repr__(self) -> str:
        return f"Lecture(position_in_module={self.position_in_module}, lectures_name='{self.lectures_name}', " \
               f"link_to_video='{self.link_to_video}', modules_modules_id={self.modules_modules_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "position_in_module": self.position_in_module,
            "lectures_name": self.lectures_name,
            "link_to_video": self.link_to_video,
            "modules_modules_id": self.modules_modules_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Lecture:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Lecture(
            position_in_module=dto_dict.get("position_in_module"),
            lectures_name=dto_dict.get("lectures_name"),
            link_to_video=dto_dict.get("link_to_video"),
            modules_modules_id=dto_dict.get("modules_modules_id"),
        )
        return obj
