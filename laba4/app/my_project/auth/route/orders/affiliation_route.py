from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import affiliation_controller
from laba4.app.my_project.auth.domain.orders.affiliation import Affiliation

affiliation_bp = Blueprint('affiliation', __name__, url_prefix='/affiliation')


@affiliation_bp.get('')
def get_all_aff() -> Response:
    return make_response(jsonify(affiliation_controller.find_all()), HTTPStatus.OK)


@affiliation_bp.post('')
def create_aff() -> Response:
    content = request.get_json()
    affiliation = Affiliation.create_from_dto(content)
    affiliation_controller.create(affiliation)
    return make_response(jsonify(affiliation.put_into_dto()), HTTPStatus.CREATED)


@affiliation_bp.get('/<int:affiliation_id>')
def get_aff(affiliation_id: int) -> Response:
    return make_response(jsonify(affiliation_controller.find_by_id(affiliation_id)), HTTPStatus.OK)


@affiliation_bp.put('/<int:affiliation_id>')
def update_aff(affiliation_id: int) -> Response:
    content = request.get_json()
    affiliation = Affiliation.create_from_dto(content)
    affiliation_controller.update(affiliation_id, affiliation)
    return make_response("Affiliation updated", HTTPStatus.OK)


@affiliation_bp.patch('/<int:affiliation_id>')
def patch_aff(affiliation_id: int) -> Response:
    content = request.get_json()
    affiliation_controller.patch(affiliation_id, content)
    return make_response("Affiliation updated", HTTPStatus.OK)


@affiliation_bp.delete('/<int:affiliation_id>')
def delete_aff(affiliation_id: int) -> Response:
    affiliation_controller.delete(affiliation_id)
    return make_response("Affiliation deleted", HTTPStatus.OK)
