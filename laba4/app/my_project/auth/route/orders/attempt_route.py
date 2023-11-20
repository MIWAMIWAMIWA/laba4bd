from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import attempt_controller
from laba4.app.my_project.auth.domain.orders.attempt import Attempt

attempt_bp = Blueprint('attempt', __name__, url_prefix='/attempt')


@attempt_bp.get('')
def get_all_attempt_answers() -> Response:

    return make_response(jsonify(attempt_controller.find_all()), HTTPStatus.OK)


@attempt_bp.post('')
def create_attempt_answer() -> Response:
    content = request.get_json()
    attempt = Attempt.create_from_dto(content)
    attempt_controller.create(attempt)
    return make_response(jsonify(attempt.put_into_dto()), HTTPStatus.CREATED)


@attempt_bp.get('/<int:attempt_id>')
def get_attempt_answer(attempt_id: int) -> Response:

    return make_response(jsonify(attempt_controller.find_by_id(attempt_id)), HTTPStatus.OK)


@attempt_bp.put('/<int:attempt_id>')
def update_attempt_answer(attempt_id: int) -> Response:

    content = request.get_json()
    attempt = Attempt.create_from_dto(content)
    attempt_controller.update(attempt_id, attempt)
    return make_response("Attempt updated", HTTPStatus.OK)


@attempt_bp.patch('/<int:attempt_id>')
def patch_attempt_answer(attempt_id: int) -> Response:

    content = request.get_json()
    attempt_controller.patch(attempt_id, content)
    return make_response("Attempt updated", HTTPStatus.OK)


@attempt_bp.delete('/<int:attempt_id>')
def delete_attempt_answer(attempt_id: int) -> Response:

    attempt_controller.delete(attempt_id)
    return make_response("Attempt deleted", HTTPStatus.OK)