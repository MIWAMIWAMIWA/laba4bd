from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import course_controller
from laba4.app.my_project.auth.domain.orders.courses import Course

course_bp = Blueprint('course', __name__, url_prefix='/course')


@course_bp.get('')
def get_all_courses() -> Response:
    return make_response(jsonify(course_controller.find_all()), HTTPStatus.OK)


@course_bp.post('')
def create_course() -> Response:
    content = request.get_json()
    item = Course.create_from_dto(content)
    course_controller.create(item)
    return make_response(jsonify(item.put_into_dto()), HTTPStatus.CREATED)


@course_bp.get('/<int:item_id>')
def get_course(item_id: int) -> Response:
    return make_response(jsonify(course_controller.find_by_id(item_id)), HTTPStatus.OK)


@course_bp.put('/<int:item_id>')
def update_course(item_id: int) -> Response:
    content = request.get_json()
    item = Course.create_from_dto(content)
    course_controller.update(item_id, item)
    return make_response("Course updated", HTTPStatus.OK)


@course_bp.patch('/<int:item_id>')
def patch_course(item_id: int) -> Response:
    content = request.get_json()
    course_controller.patch(item_id, content)
    return make_response("course updated", HTTPStatus.OK)


@course_bp.delete('/<int:item_id>')
def delete_course(item_id: int) -> Response:
    course_controller.delete(item_id)
    return make_response("course deleted", HTTPStatus.OK)
