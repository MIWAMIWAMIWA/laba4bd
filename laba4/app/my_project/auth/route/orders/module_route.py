from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import module_controller
from laba4.app.my_project.auth.domain.orders.module import Module

module_bp = Blueprint('module', __name__, url_prefix='/module')


@module_bp.get('')
def get_all_modules() -> Response:
    return make_response(jsonify(module_controller.find_all()), HTTPStatus.OK)


@module_bp.post('')
def create_modules() -> Response:
    content = request.get_json()
    item = Module.create_from_dto(content)
    module_controller.create(item)
    return make_response(jsonify(item.put_into_dto()), HTTPStatus.CREATED)


@module_bp.get('/<int:item_id>')
def get_module(item_id: int) -> Response:
    return make_response(jsonify(module_controller.find_by_id(item_id)), HTTPStatus.OK)


@module_bp.put('/<int:item_id>')
def update_module(item_id: int) -> Response:
    content = request.get_json()
    item = Module.create_from_dto(content)
    module_controller.update(item_id, item)
    return make_response("module updated", HTTPStatus.OK)


@module_bp.patch('/<int:item_id>')
def patch_module(item_id: int) -> Response:
    content = request.get_json()
    module_controller.patch(item_id, content)
    return make_response("module updated", HTTPStatus.OK)


@module_bp.delete('/<int:item_id>')
def delete_module(item_id: int) -> Response:
    module_controller.delete(item_id)
    return make_response("module deleted", HTTPStatus.OK)
