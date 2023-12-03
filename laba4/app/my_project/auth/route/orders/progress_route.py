from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import progress_controller
from laba4.app.my_project.auth.domain.orders.progress import Progress

progress_bp = Blueprint('progress', __name__, url_prefix='/progress')


@progress_bp.get('')
def get_all_progresses() -> Response:
    return make_response(jsonify(progress_controller.find_all()), HTTPStatus.OK)


@progress_bp.post('')
def create_progress() -> Response:
    content = request.get_json()
    item = Progress.create_from_dto(content)
    progress_controller.create(item)
    return make_response(jsonify(item.put_into_dto()), HTTPStatus.CREATED)


@progress_bp.get('/<int:item_id>')
def get_progress(item_id: int) -> Response:
    return make_response(jsonify(progress_controller.find_by_id(item_id)), HTTPStatus.OK)


@progress_bp.put('/<int:item_id>')
def update_progress(item_id: int) -> Response:
    content = request.get_json()
    item = Progress.create_from_dto(content)
    progress_controller.update(item_id, item)
    return make_response("progress updated", HTTPStatus.OK)


@progress_bp.patch('/<int:item_id>')
def patch_progress(item_id: int) -> Response:
    content = request.get_json()
    progress_controller.patch(item_id, content)
    return make_response("progress updated", HTTPStatus.OK)


@progress_bp.delete('/<int:item_id>')
def delete_progress(item_id: int) -> Response:
    progress_controller.delete(item_id)
    return make_response("progress deleted", HTTPStatus.OK)