from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import student_controller
from laba4.app.my_project.auth.dao import student_dao
from laba4.app.my_project.auth.domain.orders.student import Student

student_bp = Blueprint('student', __name__, url_prefix='/student')


@student_bp.get('')
def get_all_students() -> Response:
    return make_response(jsonify(student_controller.find_all()), HTTPStatus.OK)


@student_bp.post('')
def create_student() -> Response:
    content = request.get_json()
    item = Student.create_from_dto(content)
    student_controller.create(item)
    return make_response(jsonify(item.put_into_dto()), HTTPStatus.CREATED)


@student_bp.get('/<int:item_id>')
def get_student(item_id: int) -> Response:
    return make_response(jsonify(student_controller.find_by_id(item_id)), HTTPStatus.OK)


@student_bp.put('/<int:item_id>')
def update_student(item_id: int) -> Response:
    content = request.get_json()
    item = Student.create_from_dto(content)
    student_controller.update(item_id, item)
    return make_response("student updated", HTTPStatus.OK)


@student_bp.patch('/<int:item_id>')
def patch_student(item_id: int) -> Response:
    content = request.get_json()
    student_controller.patch(item_id, content)
    return make_response("student updated", HTTPStatus.OK)


@student_bp.delete('/<int:item_id>')
def delete_student(item_id: int) -> Response:
    student_controller.delete(item_id)
    return make_response("progress deleted", HTTPStatus.OK)


@student_bp.get('/generate_dbs')
def generate_tables():
    student_controller.gen_databases()
    return make_response("Databases created", HTTPStatus.OK)
