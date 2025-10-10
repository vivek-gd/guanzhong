from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from backend.models.user import User, db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/auth/register', methods=['POST'])
def register():
    """用户注册"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"message": "用户名和密码不能为空"}), 400
    
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "用户名已存在"}), 400
    
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({"message": "注册成功"}), 201

@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    """用户登录"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username, password=password).first()
    
    if user:
        access_token = create_access_token(identity=user.id)
        return jsonify({
            "access_token": access_token,
            "user_id": user.id,
            "username": user.username
        }), 200
    else:
        return jsonify({"message": "用户名或密码错误"}), 401

@auth_bp.route('/api/auth/user', methods=['GET'])
def get_user_info():
    """获取用户信息（示例）"""
    return jsonify({
        "message": "用户信息接口",
        "endpoint": "/api/auth/user"
    })