from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.models.user import db

dialogue_bp = Blueprint('dialogue', __name__)

# 临时对话存储（实际项目中使用数据库）
dialogues = {}

@dialogue_bp.route('/api/dialogues', methods=['POST'])
@jwt_required()
def create_dialogue():
    """创建新对话"""
    data = request.get_json() or {}
    user_id = get_jwt_identity()
    
    dialogue_id = len(dialogues) + 1
    dialogues[dialogue_id] = {
        'id': dialogue_id,
        'user_id': user_id,
        'title': data.get('title', '新对话'),
        'messages': [],
        'created_at': '2025-01-20T10:00:00'
    }
    
    return jsonify(dialogues[dialogue_id]), 201

@dialogue_bp.route('/api/dialogues', methods=['GET'])
@jwt_required()
def get_dialogues():
    """获取对话列表"""
    user_id = get_jwt_identity()
    user_dialogues = [d for d in dialogues.values() if d['user_id'] == user_id]
    
    return jsonify({
        'dialogues': user_dialogues,
        'total': len(user_dialogues)
    }), 200

@dialogue_bp.route('/api/dialogues/<int:dialogue_id>', methods=['GET'])
@jwt_required()
def get_dialogue(dialogue_id):
    """获取对话详情"""
    dialogue = dialogues.get(dialogue_id)
    if not dialogue:
        return jsonify({"message": "对话不存在"}), 404
    
    user_id = get_jwt_identity()
    if dialogue['user_id'] != user_id:
        return jsonify({"message": "无权访问此对话"}), 403
    
    return jsonify(dialogue), 200

@dialogue_bp.route('/api/dialogues/<int:dialogue_id>/messages', methods=['POST'])
@jwt_required()
def add_message(dialogue_id):
    """添加消息到对话"""
    data = request.get_json()
    message_content = data.get('message')
    
    if not message_content:
        return jsonify({"message": "消息内容不能为空"}), 400
    
    dialogue = dialogues.get(dialogue_id)
    if not dialogue:
        return jsonify({"message": "对话不存在"}), 404
    
    user_id = get_jwt_identity()
    if dialogue['user_id'] != user_id:
        return jsonify({"message": "无权访问此对话"}), 403
    
    # 添加用户消息
    dialogue['messages'].append({
        'sender': 'user',
        'content': message_content,
        'timestamp': '2025-01-20T10:00:00'
    })
    
    # 模拟AI回复
    dialogue['messages'].append({
        'sender': 'guanzhong',
        'content': f"收到您的消息: {message_content}。管仲正在思考中...",
        'timestamp': '2025-01-20T10:01:00'
    })
    
    return jsonify({
        'message': '消息添加成功',
        'dialogue_id': dialogue_id
    }), 200