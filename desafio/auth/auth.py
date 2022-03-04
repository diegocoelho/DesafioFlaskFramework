from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from desafio.constants.http_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from desafio.util.errors import error_output
from desafio.database import db
from desafio.models.user import User
from flask_jwt_extended import create_access_token
from desafio.util.custom_logger import log

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.post('/register')
@log
def register():
    username = request.json['username']
    password = request.json['password']
    if User.query.filter_by(username=username).first() is not None:
        return error_output(code=HTTP_400_BAD_REQUEST, reason='username is already taken')

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

    return error_output(code=HTTP_401_UNAUTHORIZED, reason='wrong credentials')
