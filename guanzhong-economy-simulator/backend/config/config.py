import os
from enum import Enum

class Difficulty(Enum):
    EASY = {"income_multiplier": 1.2, "stability_impact": 0.8}
    NORMAL = {"income_multiplier": 1.0, "stability_impact": 1.0}
    HARD = {"income_multiplier": 0.8, "stability_impact": 1.2}

class Config:
    # 请替换为你自己的API密钥
    DOUBAO_API_KEY = os.getenv("DOUBAO_API_KEY", "573ab249-3130-4926-be5f-da98998863ef")
    DOUBAO_API_URL = os.getenv("DOUBAO_API_URL", "https://ark.cn-beijing.volces.com/api/v3/chat/completions")
    ECONOMY_SETTINGS = {
        "base_rates": {
            "tax_income": 0.05,
            "grain_yield": 0.15
        },
        "difficulty": Difficulty.NORMAL
    }
    HISTORICAL_EVENTS = {
        "enable": True,
        "frequency": 0.3  # 30%概率每年触发事件
    }