from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from desafio.constants.http_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from desafio.database import User, db
from flask_jwt_extended import create_access_token
from desafio.custom_logger import log

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.post('/register')
@log
def register():
    username = request.json['username']
    password = request.json['password']
    if User.query.filter_by(username=username).first() is not None:
        output = {
            'error': {
                'reason': 'username is already taken'
            }
        }
        return jsonify(output), HTTP_400_BAD_REQUEST

    password_hash = generate_password_hash(password)
    user = User(username=username, password=password_hash)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created', 'username': username}), HTTP_200_OK


@auth.post('/login')
@log
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()

    if user:
        pwd_correct = check_password_hash(user.password, password)
        if pwd_correct:
            access = create_access_token(identity=user.id)
            output = {
                'user': {
                    'access': access,
                    'username': user.username
                }
            }
            return jsonify(output), HTTP_200_OK
    output = {
        'error': {
            'reason': 'wrong credentials'
        }
    }
    return jsonify(output), HTTP_401_UNAUTHORIZED
