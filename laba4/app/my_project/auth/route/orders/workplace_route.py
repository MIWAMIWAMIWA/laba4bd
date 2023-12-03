from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import workplace_controller
from laba4.app.my_project.auth.domain.orders.student_workplace import StudentWorkplace

workplace_bp = Blueprint('workplace', __name__, url_prefix='/workplace')


@workplace_bp.get('')
def get_all_tests() -> Response:
    return make_response(jsonify(workplace_controller.find_all()), HTTPStatus.OK)


@workplace_bp.post('')
def create_test() -> Response:
    content = request.get_json()
    item = StudentWorkplace.create_from_dto(content)
    workplace_controller.create(item)
    return make_response(jsonify(item.put_into_dto()), HTTPStatus.CREATED)


@workplace_bp.get('/<int:item_id>')
def get_test(item_id: int) -> Response:
    return make_response(jsonify(workplace_controller.find_by_id(item_id)), HTTPStatus.OK)


@workplace_bp.put('/<int:item_id>')
def update_test(item_id: int) -> Response:
    content = request.get_json()
    item = StudentWorkplace.create_from_dto(content)
    workplace_controller.update(item_id, item)
    return make_response("test updated", HTTPStatus.OK)


@workplace_bp.patch('/<int:item_id>')
def patch_test(item_id: int) -> Response:
    content = request.get_json()
    workplace_controller.patch(item_id, content)
    return make_response("test updated", HTTPStatus.OK)


@workplace_bp.delete('/<int:item_id>')
def delete_test(item_id: int) -> Response:
    workplace_controller.delete(item_id)
    return make_response("test deleted", HTTPStatus.OK)