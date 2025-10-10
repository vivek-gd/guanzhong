import random
from datetime import datetime
from backend.models.economy import SocialClass, PolicyEffect

class HistoricalEventSystem:
    EVENT_DATABASE = [
        {
            "id": "drought",
            "name": "大旱之年",
            "description": "齐国遭遇罕见旱灾，农田颗粒无收",
            "trigger_conditions": lambda state: state.grain > 500000,
            "effects": PolicyEffect(grain=-0.4, stability=-15),
            "solutions": [
                {
                    "name": "开仓放粮",
                    "effect": PolicyEffect(grain=-100000, stability=10),
                    "ai_advice": "《管子·轻重甲》曰：岁适凶，则市籴釜十繦"
                },
                {
                    "name": "加重赋税",
                    "effect": PolicyEffect(treasury=50000, stability=-20),
                    "ai_advice": "此非善策，恐伤民本"
                }
            ]
        },
        {
            "id": "merchant_revolt",
            "name": "盐商叛乱",
            "description": "因盐铁专卖政策，商人集团发动罢市",
            "trigger_conditions": lambda state: "salt_monopoly" in state.active_policies,
            "effects": PolicyEffect(treasury=-0.3, stability=-25),
            "solutions": [
                {
                    "name": "武力镇压",
                    "effect": PolicyEffect(stability=-10),
                    "ai_advice": "《管子·国蓄》云：利出于一孔者，其国无敌"
                },
                {
                    "name": "让步妥协",
                    "effect": PolicyEffect(treasury=-50000, stability=15),
                    "ai_advice": "暂时之策，非长久计"
                }
            ]
        }
    ]

    def get_current_events(self, state):
        active_events = []
        for event in self.EVENT_DATABASE:
            if event["trigger_conditions"](state):
                active_events.append({
                    "id": event["id"],
                    "name": event["name"],
                    "description": event["description"],
                    "solutions": event["solutions"],
                    "timestamp": datetime.now().isoformat()
                })
        return active_events[:3]  # 最多同时3个事件