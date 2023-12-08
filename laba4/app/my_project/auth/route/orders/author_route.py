from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import author_controller
from laba4.app.my_project.auth.domain.orders.authors import Author

author_bp = Blueprint('author', __name__, url_prefix='/author')


@author_bp.get('')
def get_all_authors() -> Response:
    return make_response(jsonify(author_controller.find_all()), HTTPStatus.OK)


@author_bp.post('')
def create_author() -> Response:
    content = request.get_json()
    item = Author.create_from_dto(content)
    author_controller.create(item)
    return make_response(jsonify(item.put_into_dto()), HTTPStatus.CREATED)


@author_bp.get('/<int:item_id>')
def get_author(item_id: int) -> Response:
    return make_response(jsonify(author_controller.find_by_id(item_id)), HTTPStatus.OK)


@author_bp.put('/<int:item_id>')
def update_author(item_id: int) -> Response:
    content = request.get_json()
    item = Author.create_from_dto(content)
    author_controller.update(item_id, item)
    return make_response("Author updated", HTTPStatus.OK)


@author_bp.patch('/<int:item_id>')
def patch_author(item_id: int) -> Response:
    content = request.get_json()
    author_controller.patch(item_id, content)
    return make_response("Author updated", HTTPStatus.OK)


@author_bp.delete('/<int:item_id>')
def delete_author(item_id: int) -> Response:
    author_controller.delete(item_id)
    return make_response("Author deleted", HTTPStatus.OK)


@author_bp.get('/insert-into-author/<string:name>/<string:title>/<string:email>')
def insert_into_author(name, title, email):
    author_controller.insert_author_par(name, title, email)
    return make_response("Author created", HTTPStatus.OK)


@author_bp.get('/insert-multiple-author/<string:name>')
def insert_multiple(name):
    author_controller.insert_multiple_author(name)
    return make_response("multiple authors created", HTTPStatus.OK)
