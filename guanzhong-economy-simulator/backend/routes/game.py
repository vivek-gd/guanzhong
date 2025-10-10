from flask import Blueprint, request, jsonify

game_bp = Blueprint('game', __name__)

@game_bp.route('/api/game/scenarios', methods=['GET'])
def get_game_scenarios():
    """获取历史场景列表"""
    scenarios = [
        {
            "id": 1,
            "title": "九合诸侯",
            "description": "体验管仲辅佐齐桓公'九合诸侯，一匡天下'的历史场景",
            "difficulty": "中等",
            "estimated_time": 45,
            "image": "/static/images/scenario1.jpg"
        },
        {
            "id": 2,
            "title": "相地而衰征",
            "description": "模拟管仲实施土地改革政策的历史场景",
            "difficulty": "简单",
            "estimated_time": 30,
            "image": "/static/images/scenario2.jpg"
        },
        {
            "id": 3,
            "title": "管鲍之交",
            "description": "重现管仲与鲍叔牙深厚友谊的历史场景",
            "difficulty": "简单",
            "estimated_time": 25,
            "image": "/static/images/scenario3.jpg"
        }
    ]
    return jsonify(scenarios), 200

@game_bp.route('/api/game/scenarios/<int:scenario_id>', methods=['GET'])
def get_scenario_detail(scenario_id):
    """获取场景详情"""
    scenarios_data = {
        1: {
            "id": 1,
            "title": "九合诸侯",
            "description": "详细描述...",
            "objectives": ["达成外交协议", "维护齐国霸权"],
            "characters": ["管仲", "齐桓公", "诸侯"],
            "duration": "45分钟"
        },
        2: {
            "id": 2,
            "title": "相地而衰征",
            "description": "详细描述...",
            "objectives": ["实施土地改革", "平衡赋税"],
            "characters": ["管仲", "土地官员", "农民"],
            "duration": "30分钟"
        },
        3: {
            "id": 3,
            "title": "管鲍之交",
            "description": "详细描述...",
            "objectives": ["建立信任关系", "展现才能"],
            "characters": ["管仲", "鲍叔牙", "齐桓公"],
            "duration": "25分钟"
        }
    }
    
    scenario = scenarios_data.get(scenario_id)
    if not scenario:
        return jsonify({"message": "场景不存在"}), 404
    
    return jsonify(scenario), 200

@game_bp.route('/api/game/start/<int:scenario_id>', methods=['POST'])
def start_scenario(scenario_id):
    """开始游戏场景"""
    return jsonify({
        "scenario_id": scenario_id,
        "status": "started",
        "message": "场景已开始，请按照指引进行操作",
        "first_step": "了解当前局势和任务目标"
    }), 200

@game_bp.route('/api/game/action', methods=['POST'])
def game_action():
    """执行游戏动作"""
    data = request.get_json()
    action = data.get('action')
    scenario_id = data.get('scenario_id')
    
    # 模拟动作结果
    results = {
        "diplomacy": "外交成功，诸侯信服",
        "economic_reform": "经济改革初见成效",
        "military": "军事部署完成",
        "advice": "建议被采纳"
    }
    
    result = results.get(action, "动作执行中...")
    
    return jsonify({
        "action": action,
        "result": result,
        "next_step": "请继续下一步操作",
        "score_change": +10
    }), 200