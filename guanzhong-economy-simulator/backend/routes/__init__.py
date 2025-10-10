"""
路由模块初始化
"""

from .auth import auth_bp
from .dialogue import dialogue_bp
from .economy import economy_bp
from .game import game_bp

__all__ = ['auth_bp', 'dialogue_bp', 'economy_bp', 'game_bp']