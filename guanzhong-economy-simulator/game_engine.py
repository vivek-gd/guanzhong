from enum import Enum, auto
from dataclasses import dataclass
from typing import Dict, List

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