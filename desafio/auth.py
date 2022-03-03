from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from desafio.constants.http_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from desafio.database import User, db
from flask_jwt_extended import create_access_token
from logging import getLogger

auth = Blueprint('auth', __name__, url_prefix='/auth')
log = getLogger(__name__)


@auth.post('/register')
def register():
    username = request.json['username']
    password = request.json['password']
    if User.query.filter_by(username=username).first() is not None:
        output = {'error': 'username is already taken'}
        log.info('{}\t{}'.format(HTTP_400_BAD_REQUEST, output))
        return jsonify(output), HTTP_400_BAD_REQUEST

    password_hash = generate_password_hash(password)
    user = User(username=username, password=password_hash)
    db.session.add(user)
    db.session.commit()

    output = {'message': 'User created', 'username': username}
    log.info('{}\t{}'.format(HTTP_200_OK, output))
    return jsonify(output), HTTP_200_OK


@auth.post('/login')
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
            log.info('{}\t{}'.format(HTTP_200_OK, output))
            return jsonify(output), HTTP_200_OK
    output = {'error': 'wrong credentials'}
    log.info('{}\t{}'.format(HTTP_401_UNAUTHORIZED, output))
    return jsonify(output), HTTP_401_UNAUTHORIZED
