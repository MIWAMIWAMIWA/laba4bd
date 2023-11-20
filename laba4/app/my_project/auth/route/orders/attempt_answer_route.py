from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import attempt_answer_controller
from laba4.app.my_project.auth.domain.orders.Attempt_answer import AttemptAnswer

attempt_answer_bp = Blueprint('attempt_answer', __name__, url_prefix='/attempt_answer')


@attempt_answer_bp.get('')
def get_all_attempts() -> Response:
    return make_response(jsonify(attempt_answer_controller.find_all()), HTTPStatus.OK)


@attempt_answer_bp.post('')
def create_attempt() -> Response:
    content = request.get_json()
    attempt = AttemptAnswer.create_from_dto(content)
    attempt_answer_controller.create(attempt)
    return make_response(jsonify(attempt.put_into_dto()), HTTPStatus.CREATED)


@attempt_answer_bp.get('/<int:attempt_id>')
def get_attempt(attempt_id: int) -> Response:
    return make_response(jsonify(attempt_answer_controller.find_by_id(attempt_id)), HTTPStatus.OK)


@attempt_answer_bp.put('/<int:attempt_id>')
def update_attempt(attempt_id: int) -> Response:
    content = request.get_json()
    attempt = AttemptAnswer.create_from_dto(content)
    attempt_answer_controller.update(attempt_id, attempt)
    return make_response("Attempt ans updated", HTTPStatus.OK)


@attempt_answer_bp.patch('/<int:attempt_id>')
def patch_attempt(attempt_id: int) -> Response:
    content = request.get_json()
    attempt_answer_controller.patch(attempt_id, content)
    return make_response("Attempt ans  updated", HTTPStatus.OK)


@attempt_answer_bp.delete('/<int:attempt_id>')
def delete_attempt(attempt_id: int) -> Response:
    attempt_answer_controller.delete(attempt_id)
    return make_response("Attempt ans deleted", HTTPStatus.OK)
