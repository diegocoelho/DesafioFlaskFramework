from flask import Blueprint, jsonify
import requests
from flask_jwt_extended import jwt_required
from src.constants.http_codes import HTTP_200_OK

DATA_URL = 'https://jsonplaceholder.typicode.com/todos'
NUMBER_OF_RECORDS = 5

api = Blueprint('api', __name__, url_prefix='/api')


@api.get('/')
def root():
    return {'message': 'Desafio Flask - Framework'}


@api.get('/first_five')
@jwt_required()
def first_five():
    response = requests.get(DATA_URL)
    data = response.json()[:NUMBER_OF_RECORDS]
    for element in data:
        del element['userId']
        del element['completed']
    return jsonify(data), HTTP_200_OK
