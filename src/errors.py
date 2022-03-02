from flask import Blueprint, jsonify
from src.constants.http_codes import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from logging import getLogger

errors = Blueprint('errors', __name__)
log = getLogger(__name__)


@errors.app_errorhandler(HTTP_401_UNAUTHORIZED)
def error_401(error):
    output = {'error': {
        'reason': 'something went wrong, please try again'
    }}
    log.info('{}\t{}'.format(HTTP_401_UNAUTHORIZED, output))
    return jsonify(output), HTTP_401_UNAUTHORIZED


@errors.app_errorhandler(HTTP_404_NOT_FOUND)
def error_404(error):
    output = {'error': {
        'reason': 'page not found'
    }}
    log.info('{}\t{}'.format(HTTP_404_NOT_FOUND, output))
    return jsonify(output), HTTP_404_NOT_FOUND


@errors.app_errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
def error_500(error):
    output = {'error': {
        'reason': 'something went wrong, please try again'
    }}
    log.info('{}\t{}'.format(HTTP_500_INTERNAL_SERVER_ERROR, output))
    return jsonify(output), HTTP_500_INTERNAL_SERVER_ERROR
