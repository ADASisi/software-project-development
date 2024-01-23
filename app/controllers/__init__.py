from flask import Blueprint, request, jsonify
from app.services import AuthService
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()

@auth_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    new_user = auth_service.register_user(data['username'], data['password'])
    return jsonify({'message': 'User registered successfully', 'user': {'id': new_user.id, 'username': new_user.username}}), 201

@auth_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = auth_service.authenticate_user(data['username'], data['password'])
    if user:
        access_token = create_access_token(indentity=user.id)
        return jsonify({'message': 'Login successful', 'token': 'your_jwt_token'})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    return jsonify(logged_in_as=current_user_id), 200
