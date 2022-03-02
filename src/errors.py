from flask import Blueprint, jsonify
from src.constants.http_codes import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(HTTP_401_UNAUTHORIZED)
def error_401(error):
    return jsonify({'error': {
        'reason': 'something went wrong, please try again'
    }}), HTTP_500_INTERNAL_SERVER_ERROR


@errors.app_errorhandler(HTTP_404_NOT_FOUND)
def error_404(error):
    return jsonify({'error': {
        'reason': 'page not found'
    }}), HTTP_404_NOT_FOUND


@errors.app_errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
def error_500(error):
    return jsonify({'error': {
        'reason': 'something went wrong, please try again'
    }}), HTTP_500_INTERNAL_SERVER_ERROR
