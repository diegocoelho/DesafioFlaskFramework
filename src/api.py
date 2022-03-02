from flask import Blueprint, jsonify
import requests
from flask_jwt_extended import jwt_required
from src.constants.http_codes import HTTP_200_OK
from logging import getLogger

DATA_URL = 'https://jsonplaceholder.typicode.com/todos'
NUMBER_OF_RECORDS = 5

api = Blueprint('api', __name__, url_prefix='/api')
log = getLogger(__name__)


@api.get('/')
def root():
    output = {'message': 'Desafio Flask - Framework'}
    log.info('{}\t{}'.format(HTTP_200_OK, output))
    return jsonify(output), HTTP_200_OK


@api.get('/first_five')
@jwt_required()
def first_five():
    response = requests.get(DATA_URL)
    data = response.json()[:NUMBER_OF_RECORDS]
    for element in data:
        del element['userId']
        del element['completed']
    log.info('{}\t{}'.format(HTTP_200_OK, data))
    return jsonify(data), HTTP_200_OK
