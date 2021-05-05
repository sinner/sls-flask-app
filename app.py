from utils import LocalFlask
from http import HTTPStatus
from api.routes import routes
from traceback import format_exc

app = LocalFlask(__name__)
app.register_blueprint(routes)

# Error handlers #

@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(e):
    return {
        'error': {
            'type': 'NotFound',
            'message': str(e),
            'detail': format_exc()
        }
    }, HTTPStatus.NOT_FOUND

@app.errorhandler(HTTPStatus.FORBIDDEN)
def forbidden(e):
    return {
        'error': {
            'type': 'Forbidden',
            'message': str(e),
            'detail': format_exc()
        }
    }, HTTPStatus.FORBIDDEN

@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_server_error(e):
    return {
        'error': {
            'type': 'InternalServerError',
            'message': str(e),
            'detail': format_exc()
        }
    }, HTTPStatus.INTERNAL_SERVER_ERROR

if __name__ == "__main__":
    app.run(debug=True)
