from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Test(db.Model, IDto):
    """
    Model declaration for the 'test' table.
    """
    __tablename__ = "test"

    idtest = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modules_modules_id = db.Column(db.Integer, db.ForeignKey('modules.modules_id'), primary_key=True)

    # Define relationship
    modules = db.relationship("Module", backref="test")

    def __repr__(self) -> str:
        return f"Test(idtest={self.idtest}, modules_modules_id={self.modules_modules_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "idtest": self.idtest,
            "modules_modules_id": self.modules_modules_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Test:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Test(
            idtest=dto_dict.get("idtest"),
            modules_modules_id=dto_dict.get("modules_modules_id"),
        )
        return obj
