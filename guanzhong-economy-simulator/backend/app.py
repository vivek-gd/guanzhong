# 新增导入
import requests
import json
import os
import logging
from threading import Lock
from datetime import datetime
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# 正确初始化Flask应用
app = Flask(__name__)
CORS(app)  # 允许跨域请求



# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 豆包API配置（使用您提供的API Key）
app.config['DOUBAO_API_KEY'] = '573ab249-3130-4926-be5f-da98998863ef'
app.config['DOUBAO_API_URL'] = 'https://ark.cn-beijing.volces.com/api/v3/chat/completions'

# 线程安全锁
dialogue_lock = Lock()

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
                    "model": "doubao-seed-1-6-250615",  # 根据实际模型调整
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

# 豆包对话API路由
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

# 豆包API健康检查
@app.route('/api/doubao/health', methods=['GET'])
def doubao_health():
    """检查豆包API状态"""
    try:
        # 简单的测试请求
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

# 静态文件服务
@app.route('/')
def serve_index():
    """提供前端主页面"""
    return send_from_directory('../frontend/public', 'guanzhong_ai.html')

@app.route('/<path:path>')
def serve_static(path):
    """提供静态文件"""
    return send_from_directory('../frontend/public', path)

# 应用启动
if __name__ == '__main__':
    # 检查前端目录是否存在
    frontend_path = os.path.abspath('../frontend/public')
    if not os.path.exists(frontend_path):
        logger.warning(f"前端目录不存在: {frontend_path}")
    
    # 启动Flask应用
    app.run(
        debug=True,
        port=5000,
        host='0.0.0.0',
        threaded=True
    )