# 新增导入
import requests
import json
import os
import logging
import jwt
import bcrypt
from threading import Lock
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from enum import Enum, auto
from dataclasses import dataclass, asdict

# Flask 相关导入
from flask import Flask, request, jsonify, send_from_directory, make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# 游戏引擎模块（直接整合 game_engine.py 内容）
class SocialClass(Enum):
    SCHOLARS = "士"
    FARMERS = "农"
    ARTISANS = "工"
    MERCHANTS = "商"

class PolicyEffect:
    def __init__(self, 
                 treasury: float = 0,
                 grain: float = 0,
                 stability: float = 0,
                 class_effects: Dict[SocialClass, float] = None):
        self.treasury = treasury
        self.grain = grain
        self.stability = stability
        self.class_effects = class_effects or {}

@dataclass
class Policy:
    id: str
    name: str
    description: str
    cost: int
    effects: PolicyEffect
    prerequisites: List[str]
    historical_accuracy: float  # 0-1 历史契合度

@dataclass
class GameState:
    year: int
    treasury: float
    grain: float
    salt: float
    iron: float
    stability: float
    class_satisfaction: Dict[SocialClass, float]
    active_policies: List[str]
    historical_events: List[Dict]
    
    def apply_effect(self, effect: PolicyEffect):
        self.treasury += effect.treasury
        self.grain += effect.grain
        self.stability += effect.stability
        for cls, val in effect.class_effects.items():
            self.class_satisfaction[cls] = max(0, min(100, self.class_satisfaction[cls] + val))
    
    def to_dict(self):
        """转换为可序列化的字典"""
        data = asdict(self)
        # 处理 Enum 类型
        data['class_satisfaction'] = {k.value: v for k, v in self.class_satisfaction.items()}
        data['effects'] = asdict(self.effects) if hasattr(self, 'effects') else {}
        return data

# 初始化 Flask 应用
app = Flask(__name__)
CORS(app, supports_credentials=True)  # 允许跨域 + 携带Cookie

# 配置
app.config['SECRET_KEY'] = 'zhiguanchunqiu-2025-secret-key-keep-safe'  # 生产环境替换为环境变量
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'  # SQLite 数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_EXPIRATION_HOURS'] = 2  # Token 有效期2小时

# 豆包 API 配置
app.config['DOUBAO_API_KEY'] = '573ab249-3130-4926-be5f-da98998863ef'
app.config['DOUBAO_API_URL'] = 'https://ark.cn-beijing.volces.com/api/v3/chat/completions'

# 初始化数据库
db = SQLAlchemy(app)

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 线程安全锁
dialogue_lock = Lock()

# ======================== 数据库模型 ========================
class User(db.Model):
    """用户模型（符合 api_design.py 认证模块）"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    last_login = db.Column(db.DateTime, nullable=True)
    
    # 游戏相关字段
    selected_role = db.Column(db.String(20), default="国君")
    game_state = db.Column(db.JSON, nullable=True)  # 存储游戏状态

    def set_password(self, password):
        """加密存储密码"""
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    def check_password(self, password):
        """验证密码"""
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
    
    def generate_token(self):
        """生成JWT Token"""
        payload = {
            'user_id': self.id,
            'username': self.username,
            'exp': datetime.utcnow() + timedelta(hours=app.config['JWT_EXPIRATION_HOURS'])
        }
        return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    
    def to_dict(self):
        """转换为字典（隐藏敏感信息）"""
        return {
            'id': self.id,
            'username': self.username,
            'created_at': self.created_at.isoformat(),
            'last_login': self.last_login.isoformat() if self.last_login else None,
            'selected_role': self.selected_role
        }

class Dialogue(db.Model):
    """对话模型（符合 api_design.py 对话模块）"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(100), default="新对话")
    tags = db.Column(db.JSON, default=[])
    created_at = db.Column(db.DateTime, default=datetime.now)

class Message(db.Model):
    """消息模型"""
    id = db.Column(db.Integer, primary_key=True)
    dialogue_id = db.Column(db.Integer, db.ForeignKey('dialogue.id'))
    sender = db.Column(db.String(10), nullable=False)  # 'user' 或 'ai'
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

# ======================== 认证装饰器 ========================
def token_required(f):
    """JWT Token 认证装饰器（符合 api_design.py 认证规范）"""
    def wrapper(*args, **kwargs):
        token = None
        # 从请求头获取 Token（Bearer Token 格式）
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            token = auth_header.split(" ")[1] if " " in auth_header else None
        
        if not token:
            return jsonify({"message": "未认证", "error": "token_missing"}), 401
        
        try:
            # 验证 Token
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = payload['user_id']
            user = User.query.get(user_id)
            
            if not user:
                return jsonify({"message": "用户不存在", "error": "user_not_found"}), 401
            
            # 将用户对象传给视图函数
            return f(user, *args, **kwargs)
        
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token 已过期", "error": "token_expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "无效的 Token", "error": "invalid_token"}), 401
    
    wrapper.__name__ = f.__name__
    return wrapper

# ======================== 豆包 AI 客户端（保留原有功能） ========================
class DoubaoAIClient:
    @staticmethod
    def generate_reply(user_message):
        """调用豆包大模型生成管仲风格回复"""
        system_prompt = """
        你正在扮演春秋时期齐国名相管仲。请严格遵循以下角色设定：

        角色背景：
        - 春秋时期齐国名相，辅佐齐桓公成为春秋五霸之首
        - 思想核心：富民强国、礼义廉耻、尊王攘夷
        - 著名主张："仓廪实而知礼节，衣食足而知荣辱"
        - 政策：相地而衰征、官山海、轻重九府、四民分业

        回答要求：
        1. 使用文言文与现代汉语结合的风格（70%文言+30%现代）
        2. 体现管仲的治国智慧和哲学思想
        3. 适当引用《管子》中的经典语句
        4. 保持谦逊但权威的语气
        5. 回答要精炼，控制在100-200字
        6. 以"善哉！"、"吾闻之"等春秋时期用语开头

        示例回答：
        "善哉！治国之道，首在富民。仓廪实而知礼节，衣食足而知荣辱。民富则易治，民贫则难安。"
        """
        
        try:
            with dialogue_lock:
                headers = {
                    'Authorization': f'Bearer {app.config["DOUBAO_API_KEY"]}',
                    'Content-Type': 'application/json'
                }
                
                payload = {
                    "model": "doubao-seed-1-6-250615",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_message}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 500,
                    "stream": False
                }
                
                logger.info(f"发送请求到豆包API: {payload['messages'][1]['content'][:50]}...")
                
                response = requests.post(
                    app.config['DOUBAO_API_URL'],
                    headers=headers,
                    json=payload,
                    timeout=30
                )
                
                if response.status_code != 200:
                    error_msg = f"API请求失败: {response.status_code} - {response.text}"
                    logger.error(error_msg)
                    raise Exception(error_msg)
                
                result = response.json()
                logger.info("豆包API响应成功")
                return result['choices'][0]['message']['content']
                
        except Exception as e:
            logger.error(f"豆包API调用失败: {e}")
            return f"吾思有所阻，请稍后再试。错误：{str(e)}"

# ======================== 认证接口（符合 api_design.py /api/auth 规范） ========================
@app.route('/api/auth/register', methods=['POST'])
def register():
    """用户注册"""
    try:
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()
        
        # 校验参数
        if not username or not password:
            return jsonify({"message": "用户名和密码不能为空"}), 400
        if len(username) < 3 or len(password) < 6:
            return jsonify({"message": "用户名至少3位，密码至少6位"}), 400
        
        # 检查用户名是否已存在
        if User.query.filter_by(username=username).first():
            return jsonify({"message": "用户名已存在"}), 400
        
        # 创建新用户
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        logger.info(f"用户注册成功: {username}")
        return jsonify({"message": "注册成功", "user": new_user.to_dict()}), 201
    
    except Exception as e:
        logger.error(f"注册失败: {e}")
        return jsonify({"message": "注册失败", "error": str(e)}), 500

@app.route('/api/auth/login', methods=['POST'])
def login():
    """用户登录（返回JWT Token）"""
    try:
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()
        
        # 校验参数
        if not username or not password:
            return jsonify({"message": "用户名和密码不能为空"}), 400
        
        # 查找用户
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return jsonify({"message": "认证失败，用户名或密码错误"}), 401
        
        # 更新最后登录时间
        user.last_login = datetime.now()
        db.session.commit()
        
        # 生成 Token
        token = user.generate_token()
        
        logger.info(f"用户登录成功: {username}")
        return jsonify({
            "message": "登录成功",
            "access_token": token,
            "user": user.to_dict()
        }), 200
    
    except Exception as e:
        logger.error(f"登录失败: {e}")
        return jsonify({"message": "登录失败", "error": str(e)}), 500

@app.route('/api/auth/logout', methods=['POST'])
@token_required
def logout(user):
    """用户登出（客户端清除Token即可，服务端无需操作）"""
    logger.info(f"用户登出: {user.username}")
    return jsonify({"message": "登出成功"}), 200

@app.route('/api/auth/user', methods=['GET'])
@token_required
def get_user_info(user):
    """获取当前用户信息"""
    return jsonify({"user": user.to_dict()}), 200

# ======================== 游戏接口 ========================
@app.route('/api/game/select-role', methods=['POST'])
@token_required
def select_role(user):
    """选择游戏角色"""
    try:
        data = request.get_json()
        role = data.get('role', '国君')
        
        # 校验角色
        valid_roles = ["国君", "大司农", "盐铁使", "民间商人"]
        if role not in valid_roles:
            return jsonify({"message": f"无效角色，可选：{valid_roles}"}), 400
        
        # 更新用户角色
        user.selected_role = role
        db.session.commit()
        
        # 初始化游戏状态
        initial_game_state = GameState(
            year=1,
            treasury=200000.0,
            grain=600000.0,
            salt=10000.0,
            iron=5000.0,
            stability=50.0,
            class_satisfaction={
                SocialClass.SCHOLARS: 50.0,
                SocialClass.FARMERS: 45.0,
                SocialClass.ARTISANS: 40.0,
                SocialClass.MERCHANTS: 35.0
            },
            active_policies=[],
            historical_events=[]
        )
        
        # 保存游戏状态到用户表
        user.game_state = initial_game_state.to_dict()
        db.session.commit()
        
        logger.info(f"用户 {user.username} 选择角色: {role}，初始化游戏状态")
        return jsonify({
            "message": "角色选择成功",
            "role": role,
            "game_state": initial_game_state.to_dict()
        }), 200
    
    except Exception as e:
        logger.error(f"选择角色失败: {e}")
        return jsonify({"message": "选择角色失败", "error": str(e)}), 500

@app.route('/api/game/state', methods=['GET'])
@token_required
def get_game_state(user):
    """获取当前游戏状态"""
    try:
        if not user.game_state:
            return jsonify({"message": "未初始化游戏状态，请先选择角色"}), 400
        
        return jsonify({
            "game_state": user.game_state,
            "role": user.selected_role
        }), 200
    
    except Exception as e:
        logger.error(f"获取游戏状态失败: {e}")
        return jsonify({"message": "获取游戏状态失败", "error": str(e)}), 500

@app.route('/api/game/apply-policy', methods=['POST'])
@token_required
def apply_policy(user):
    """执行游戏政策"""
    try:
        # 校验游戏状态
        if not user.game_state:
            return jsonify({"message": "未初始化游戏状态，请先选择角色"}), 400
        
        data = request.get_json()
        policy_id = data.get('policy_id', '')
        
        # 预设政策列表（可扩展）
        policies = {
            "salt_iron_monopoly": Policy(
                id="salt_iron_monopoly",
                name="盐铁专营",
                description="国家垄断盐铁生产销售",
                cost=10000,
                effects=PolicyEffect(
                    treasury=50000,
                    class_effects={SocialClass.MERCHANTS: -10, SocialClass.FARMERS: 5}
                ),
                prerequisites=[],
                historical_accuracy=0.95
            ),
            "land_tax": Policy(
                id="land_tax",
                name="相地而衰征",
                description="按土地质量征收赋税",
                cost=5000,
                effects=PolicyEffect(
                    grain=100000,
                    class_effects={SocialClass.FARMERS: 15, SocialClass.SCHOLARS: 5}
                ),
                prerequisites=[],
                historical_accuracy=0.98
            )
        }
        
        # 校验政策
        if policy_id not in policies:
            return jsonify({"message": "无效政策ID"}), 400
        policy = policies[policy_id]
        
        # 检查国库是否足够
        game_state_dict = user.game_state
        if game_state_dict['treasury'] < policy.cost:
            return jsonify({"message": "国库不足，无法执行该政策"}), 400
        
        # 应用政策效果
        game_state = GameState(
            year=game_state_dict['year'],
            treasury=game_state_dict['treasury'],
            grain=game_state_dict['grain'],
            salt=game_state_dict['salt'],
            iron=game_state_dict['iron'],
            stability=game_state_dict['stability'],
            class_satisfaction={SocialClass(k): v for k, v in game_state_dict['class_satisfaction'].items()},
            active_policies=game_state_dict['active_policies'],
            historical_events=game_state_dict['historical_events']
        )
        
        # 扣除政策成本
        game_state.treasury -= policy.cost
        # 应用政策效果
        game_state.apply_effect(policy.effects)
        # 添加到已执行政策
        if policy.id not in game_state.active_policies:
            game_state.active_policies.append(policy.id)
        
        # 保存更新后的游戏状态
        user.game_state = game_state.to_dict()
        db.session.commit()
        
        logger.info(f"用户 {user.username} 执行政策: {policy.name}")
        return jsonify({
            "message": f"成功执行 {policy.name}",
            "policy": {
                "id": policy.id,
                "name": policy.name,
                "description": policy.description
            },
            "game_state": game_state.to_dict()
        }), 200
    
    except Exception as e:
        logger.error(f"执行政策失败: {e}")
        return jsonify({"message": "执行政策失败", "error": str(e)}), 500
    
    
@app.route('/api/game/sync-state', methods=['POST'])
@token_required
def sync_game_state(user):
    """同步游戏状态到后端"""
    try:
        data = request.get_json()
        game_state = data.get('game_state', {})
        
        # 更新用户的游戏状态
        user.game_state = game_state
        db.session.commit()
        
        return jsonify({
            "message": "游戏状态同步成功",
            "game_state": game_state
        }), 200
    
    except Exception as e:
        logger.error(f"同步游戏状态失败: {e}")
        return jsonify({"message": "同步失败", "error": str(e)}), 500

# ======================== 原有豆包 AI 接口 ========================
@app.route('/api/doubao/chat', methods=['POST'])
def doubao_chat():
    """豆包大模型对话接口"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({"error": "消息内容不能为空"}), 400
        
        logger.info(f"收到用户消息: {user_message}")
        
        # 调用豆包API
        ai_reply = DoubaoAIClient.generate_reply(user_message)
        
        return jsonify({
            "success": True,
            "ai_reply": ai_reply,
            "model": "doubao",
            "api_key": app.config['DOUBAO_API_KEY'][:8] + "..." + app.config['DOUBAO_API_KEY'][-4:],
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"对话处理错误: {e}")
        return jsonify({
            "success": False,
            "error": str(e),
            "ai_reply": "管仲沉思中，请稍候再试"
        }), 500

@app.route('/api/doubao/health', methods=['GET'])
def doubao_health():
    """检查豆包API状态"""
    try:
        test_reply = DoubaoAIClient.generate_reply("你好")
        return jsonify({
            "status": "healthy",
            "model": "doubao",
            "api_key_status": "有效",
            "response_time": "正常",
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e),
            "api_key_status": "无效",
            "timestamp": datetime.now().isoformat()
        }), 503

# ======================== 静态文件服务 ========================
@app.route('/')
def serve_index():
    """提供前端主页面"""
    frontend_path = os.path.abspath('../frontend/public')
    if os.path.exists(frontend_path):
        return send_from_directory(frontend_path, 'guanzhong_ai.html')
    return "前端页面未找到，请检查路径", 404

@app.route('/<path:path>')
def serve_static(path):
    """提供静态文件"""
    frontend_path = os.path.abspath('../frontend/public')
    if os.path.exists(frontend_path):
        return send_from_directory(frontend_path, path)
    return f"文件 {path} 未找到", 404

# ======================== 应用启动 ========================
if __name__ == '__main__':
    # 创建数据库表
    with app.app_context():
        db.create_all()
        logger.info("数据库表创建成功")
    
    # 检查前端目录
    frontend_path = os.path.abspath('../frontend/public')
    if not os.path.exists(frontend_path):
        logger.warning(f"前端目录不存在: {frontend_path}")
    
    # 启动应用
    app.run(
        debug=False,  # 生产环境关闭debug
        port=5000,
        host='0.0.0.0',
        threaded=True
    )