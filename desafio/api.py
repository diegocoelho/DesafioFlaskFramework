from flask import Blueprint, jsonify, request
import requests
from flask_jwt_extended import jwt_required
from desafio.constants.http_codes import HTTP_200_OK
from desafio.custom_logger import log

DATA_URL = 'https://jsonplaceholder.typicode.com/todos'
ITEMS_PER_PAGE = 5
DEFAULT_PAGE = 1

api = Blueprint('api', __name__, url_prefix='/api')


@api.get('/')
@log
def root():
    return jsonify({'message': 'Desafio Flask - Framework'}), HTTP_200_OK


@api.get('/records')
@jwt_required()
@log
def records():
    response = requests.get(DATA_URL)
    page = request.args.get('page', DEFAULT_PAGE, type=int)
    limit = request.args.get('limit', ITEMS_PER_PAGE, type=int)
    data = response.json()[limit*page-limit:limit*page]
    for element in data:
        del element['userId']
        del element['completed']
    return jsonify(data), HTTP_200_OK
