from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import lecture_controller
from laba4.app.my_project.auth.domain.orders.lecture import Lecture

lecture_bp = Blueprint('lecture', __name__, url_prefix='/lecture')


@lecture_bp.get('')
def get_all_lectures() -> Response:
    return make_response(jsonify(lecture_controller.find_all()), HTTPStatus.OK)


@lecture_bp.post('')
def create_lecture() -> Response:
    content = request.get_json()
    item = Lecture.create_from_dto(content)
    lecture_controller.create(item)
    return make_response(jsonify(item.put_into_dto()), HTTPStatus.CREATED)


@lecture_bp.get('/<int:item_id>')
def get_lecture(item_id: int) -> Response:
    return make_response(jsonify(lecture_controller.find_by_id(item_id)), HTTPStatus.OK)


@lecture_bp.put('/<int:item_id>')
def update_lecture(item_id: int) -> Response:
    content = request.get_json()
    item = Lecture.create_from_dto(content)
    lecture_controller.update(item_id, item)
    return make_response("lecture updated", HTTPStatus.OK)


@lecture_bp.patch('/<int:item_id>')
def patch_lecture(item_id: int) -> Response:
    content = request.get_json()
    lecture_controller.patch(item_id, content)
    return make_response("lecture updated", HTTPStatus.OK)


@lecture_bp.delete('/<int:item_id>')
def delete_lecture(item_id: int) -> Response:
    lecture_controller.delete(item_id)
    return make_response("lecture deleted", HTTPStatus.OK)
