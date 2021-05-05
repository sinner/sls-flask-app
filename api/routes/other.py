from flask import abort
from http import HTTPStatus
from . import routes
from .config import API_PREFIX

@routes.route(f'{API_PREFIX}/bad-request', methods=['GET'])
def badRequest():
    return {
        'username': 'testuser',
        'email': 'test@mail.com',
        'description': 'badRequest',
        'process': __name__
    }, HTTPStatus.BAD_REQUEST

@routes.route(f'{API_PREFIX}/not-found', methods=['GET'])
def notFound():
    abort(HTTPStatus.NOT_FOUND, description='Resource not found')

@routes.route(f'{API_PREFIX}/internal-server-error', methods=['GET'])
def internalServerError():
    abort(HTTPStatus.INTERNAL_SERVER_ERROR, description='Internal Server Error using the abort flask function')