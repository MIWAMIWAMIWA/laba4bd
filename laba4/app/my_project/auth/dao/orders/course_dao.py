import sqlalchemy
from flask import jsonify

from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.courses import Course


class CourseDAO(GeneralDAO):
    _domain_type = Course

    def get_procedure(self, option):
        result = self._session.execute(sqlalchemy.text(f"CALL StoredMiwa({option}, @miwa)"))
        result = result.scalar()
        if option == 1:
            return jsonify({'MAX': result})
        elif option == 2:
            return jsonify({'MIN': result})
        elif option == 3:
            return jsonify({'SUM': result})
        else:
            return jsonify({'AVG': result})
