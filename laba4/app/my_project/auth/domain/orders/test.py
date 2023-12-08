from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Test(db.Model, IDto):
    __tablename__ = "test"

    idtest = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modules_modules_id = db.Column(db.Integer, db.ForeignKey('modules.modules_id'), nullable=True)

    # Define relationship
    modules = db.relationship("Module", backref="test")

    def __repr__(self) -> str:
        return f"Test(idtest={self.idtest}, modules_modules_id={self.modules_modules_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        from laba4.app.my_project.auth.controller import module_controller
        from laba4.app.my_project.auth.dao import test_question_dao
        return {
            "idtest": self.idtest,
            "modules_modules_id": module_controller.find_by_id_relation(self.modules_modules_id),
            "test_questions in this test": list(map(lambda x: x.put_into_dto_relation(),
                                                    test_question_dao.find_objects_with_value('test_idtest',
                                                                                              self.idtest)))
        }

    def put_into_dto_relation(self) -> Dict[str, Any]:
        from laba4.app.my_project.auth.dao import test_question_dao
        return {
            "idtest": self.idtest,
            "test_questions in this test": list(map(lambda x: x.put_into_dto_relation(),
                                                    test_question_dao.find_objects_with_value('test_idtest',
                                                                                              self.idtest)))
        }
    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Test:
        obj = Test(
            idtest=dto_dict.get("idtest"),
            modules_modules_id=dto_dict.get("modules_modules_id"),
        )
        return obj
