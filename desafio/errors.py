from flask import Blueprint, jsonify
from desafio.constants.http_codes import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from desafio.custom_logger import log

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(HTTP_401_UNAUTHORIZED)
@log
def error_401(error):
    output = {'error': {
        'reason': 'something went wrong, check your credentials'
    }}
    return jsonify(output), HTTP_401_UNAUTHORIZED


@errors.app_errorhandler(HTTP_404_NOT_FOUND)
@log
def error_404(error):
    output = {'error': {
        'reason': 'page not found'
    }}
    return jsonify(output), HTTP_404_NOT_FOUND


@errors.app_errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
@log
def error_500(error):
    output = {'error': {
        'reason': 'something went wrong, please try again'
    }}
    return jsonify(output), HTTP_500_INTERNAL_SERVER_ERROR
