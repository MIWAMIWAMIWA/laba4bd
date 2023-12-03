from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import test_controller
from laba4.app.my_project.auth.domain.orders.test import Test

test_bp = Blueprint('test', __name__, url_prefix='/test')


@test_bp.get('')
def get_all_tests() -> Response:
    return make_response(jsonify(test_controller.find_all()), HTTPStatus.OK)


@test_bp.post('')
def create_test() -> Response:
    content = request.get_json()
    item = Test.create_from_dto(content)
    test_controller.create(item)
    return make_response(jsonify(item.put_into_dto()), HTTPStatus.CREATED)


@test_bp.get('/<int:item_id>')
def get_test(item_id: int) -> Response:
    return make_response(jsonify(test_controller.find_by_id(item_id)), HTTPStatus.OK)


@test_bp.put('/<int:item_id>')
def update_test(item_id: int) -> Response:
    content = request.get_json()
    item = Test.create_from_dto(content)
    test_controller.update(item_id, item)
    return make_response("test updated", HTTPStatus.OK)


@test_bp.patch('/<int:item_id>')
def patch_test(item_id: int) -> Response:
    content = request.get_json()
    test_controller.patch(item_id, content)
    return make_response("test updated", HTTPStatus.OK)


@test_bp.delete('/<int:item_id>')
def delete_test(item_id: int) -> Response:
    test_controller.delete(item_id)
    return make_response("test deleted", HTTPStatus.OK)