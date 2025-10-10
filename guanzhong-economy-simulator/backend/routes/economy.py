from flask import Blueprint, request, jsonify
from backend.models.economy import EconomyModel, db

economy_bp = Blueprint('economy', __name__)

@economy_bp.route('/api/economy/concepts', methods=['GET'])
def get_economy_concepts():
    """获取管仲经济思想概念"""
    concepts = [
        {
            "id": 1,
            "name": "相地而衰征",
            "category": "土地政策",
            "description": "根据土地优劣征收不同赋税的土地改革政策",
            "importance": 95
        },
        {
            "id": 2,
            "name": "轻重九府",
            "category": "经济调控",
            "description": "国家调控市场、平衡物价的经济管理方法",
            "importance": 90
        },
        {
            "id": 3,
            "name": "官山海",
            "category": "资源管理",
            "description": "国家垄断盐铁等重要资源的管理政策",
            "importance": 85
        }
    ]
    return jsonify(concepts), 200

@economy_bp.route('/api/economy/graph', methods=['GET'])
def get_economy_graph():
    """获取经济思想知识图谱"""
    graph_data = {
        "nodes": [
            {"id": "gz", "label": "管仲", "category": "人物", "size": 30},
            {"id": "jj", "label": "经济思想", "category": "思想", "size": 25},
            {"id": "xd", "label": "相地而衰征", "category": "政策", "size": 20},
            {"id": "qz", "label": "轻重九府", "category": "政策", "size": 20},
            {"id": "gsh", "label": "官山海", "category": "政策", "size": 20}
        ],
        "edges": [
            {"source": "gz", "target": "jj", "label": "提出"},
            {"source": "jj", "target": "xd", "label": "包含"},
            {"source": "jj", "target": "qz", "label": "包含"},
            {"source": "jj", "target": "gsh", "label": "包含"}
        ]
    }
    return jsonify(graph_data), 200

@economy_bp.route('/api/economy/simulate', methods=['POST'])
def simulate_economy():
    """经济政策模拟"""
    data = request.get_json()
    policy = data.get('policy')
    parameters = data.get('parameters', {})
    
    # 模拟不同政策的效果
    simulations = {
        "相地而衰征": {
            "effect": "财政收入增加20%",
            "stability": "社会稳定性提高",
            "duration": "长期有效"
        },
        "轻重九府": {
            "effect": "市场物价稳定",
            "stability": "经济波动减少",
            "duration": "中期调控"
        },
        "官山海": {
            "effect": "国家资源收入大幅增加",
            "stability": "资源分配更合理",
            "duration": "长期政策"
        }
    }
    
    result = simulations.get(policy, {
        "effect": "政策效果待评估",
        "stability": "未知",
        "duration": "需要更多数据"
    })
    
    return jsonify({
        "policy": policy,
        "parameters": parameters,
        "simulation_result": result
    }), 200