from . import routes
from .config import API_PREFIX

@routes.route(f'{API_PREFIX}', methods=['GET'])
def healthCheck():
    return {
        'username': 'testuser',
        'email': 'test@mail.com',
        'description': 'healthCheck',
        'process': __name__
    }
