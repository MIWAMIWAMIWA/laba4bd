from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import test_question_controller
from laba4.app.my_project.auth.domain.orders.test_question import TestQuestion

test_question_bp = Blueprint('test_question', __name__, url_prefix='/test_question')


@test_question_bp.get('')
def get_all_tests_questions() -> Response:
    return make_response(jsonify(test_question_controller.find_all()), HTTPStatus.OK)


@test_question_bp.post('')
def create_test_question() -> Response:
    content = request.get_json()
    item = TestQuestion.create_from_dto(content)
    test_question_controller.create(item)
    return make_response(jsonify(item.put_into_dto()), HTTPStatus.CREATED)


@test_question_bp.get('/<int:item_id>')
def get_test_question(item_id: int) -> Response:
    return make_response(jsonify(test_question_controller.find_by_id(item_id)), HTTPStatus.OK)


@test_question_bp.put('/<int:item_id>')
def update_test_question(item_id: int) -> Response:
    content = request.get_json()
    item = TestQuestion.create_from_dto(content)
    test_question_controller.update(item_id, item)
    return make_response("test question updated", HTTPStatus.OK)


@test_question_bp.patch('/<int:item_id>')
def patch_test_question(item_id: int) -> Response:
    content = request.get_json()
    test_question_controller.patch(item_id, content)
    return make_response("test question updated", HTTPStatus.OK)


@test_question_bp.delete('/<int:item_id>')
def delete_test_question(item_id: int) -> Response:
    test_question_controller.delete(item_id)
    return make_response("test question deleted", HTTPStatus.OK)