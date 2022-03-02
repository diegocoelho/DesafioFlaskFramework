from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from src.constants.http_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from src.database import User, db
from flask_jwt_extended import jwt_required, create_refresh_token, create_access_token, get_jwt_identity
auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.post('/register')
def register():
    username = request.json['username']
    password = request.json['password']
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'error': 'username is already taken'}), HTTP_400_BAD_REQUEST

    password_hash = generate_password_hash(password)
    user = User(username=username, password=password_hash)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created',
                    'username': username}), HTTP_200_OK


@auth.post('/login')
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()

    if user:
        pwd_correct = check_password_hash(user.password, password)
        print(pwd_correct)
        if pwd_correct:
            refresh = create_refresh_token(identity=user.id)
            access = create_access_token(identity=user.id)
            return jsonify({
                'user': {
                    'refresh': refresh,
                    'access': access,
                    'username': user.username
                }
            }), HTTP_200_OK
    return jsonify({'error': 'wrong credentials'}), HTTP_401_UNAUTHORIZED


@auth.post('/refresh_token')
@jwt_required(refresh=True)
def refresh_token():
    user_id = get_jwt_identity()
    access = create_access_token(identity=user_id)
    return jsonify({'access': access})
