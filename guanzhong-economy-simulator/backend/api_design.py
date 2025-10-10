# 管仲AI后端API设计规范
# 版本: v1.0
# 最后更新: 2025-01-20

"""
管仲AI后端API设计文档
基于OpenAPI 3.0规范，与实际代码保持同步
"""

# ========================
# 1. 用户认证模块
# ========================

"""
POST /api/auth/register
描述: 用户注册
请求体:
{
    "username": "string, 必需",
    "password": "string, 必需"
}
响应:
- 201: {"message": "注册成功"}
- 400: {"message": "用户名已存在"}
"""

"""
POST /api/auth/login
描述: 用户登录
请求体:
{
    "username": "string, 必需",
    "password": "string, 必需"
}
响应:
- 200: {"access_token": "JWT令牌"}
- 401: {"message": "认证失败"}
"""

"""
POST /api/auth/logout
描述: 用户登出（客户端清除token）
认证: 需要Bearer Token
响应:
- 200: {"message": "登出成功"}
"""

"""
GET /api/auth/user
描述: 获取当前用户信息
认证: 需要Bearer Token
响应:
- 200: {"id": 1, "username": "user123", "created_at": "2025-01-20T10:00:00"}
- 401: {"message": "未认证"}
"""

# ========================
# 2. 对话管理模块
# ========================

"""
POST /api/dialogues
描述: 创建新对话
认证: 需要Bearer Token
请求体:
{
    "title": "string, 可选，默认'新对话'",
    "tags": ["string", "可选标签"]
}
响应:
- 201: {"id": 1, "title": "对话标题", "created_at": "2025-01-20T10:00:00"}
"""

"""
GET /api/dialogues
描述: 获取对话列表（分页）
认证: 需要Bearer Token
查询参数:
- page: integer, 页码，默认1
- size: integer, 每页大小，默认10
响应:
- 200: {
    "dialogues": [
        {"id": 1, "title": "标题", "created_at": "2025-01-20T10:00:00", "message_count": 5}
    ],
    "total": 100,
    "page": 1,
    "size": 10
}
"""

"""
GET /api/dialogues/{id}
描述: 获取对话详情
认证: 需要Bearer Token
路径参数:
- id: integer, 对话ID
响应:
- 200: {
    "id": 1,
    "title": "标题",
    "created_at": "2025-01-20T10:00:00",
    "messages": [
        {"id": 1, "sender": "user", "content": "内容", "created_at": "2025-01-20T10:00:00"}
    ]
}
- 404: {"message": "对话不存在"}
"""

"""
GET /api/dialogues/{id}/messages
描述: 获取对话消息（分页）
认证: 需要Bearer Token
查询参数:
- page: integer, 页码，默认1
- size: integer, 每页大小，默认20
响应:
- 200: {
    "messages": [消息列表],
    "total": 50,
    "page": 1,
    "size": 20
}
"""

# ========================
# 3. 管仲AI核心模块
# ========================

"""
POST /api/guanzhong/chat
描述: 与管仲AI进行实时对话
认证: 可选（游客模式支持）
请求体:
{
    "message": "string, 必需，用户消息",
    "dialogue_id": "integer, 可选，关联对话ID"
}
响应:
- 200: {
    "ai_reply": "管仲AI的回复",
    "dialogue_id": "当前对话ID",
    "thought_process": {"economic": true, "political": false}
}
- 400: {"message": "请提供消息内容"}
- 500: {"message": "AI服务暂时不可用"}
"""

"""
POST /api/guanzhong/think
描述: 管仲AI深度思考（异步处理复杂问题）
认证: 需要Bearer Token
请求体:
{
    "question": "string, 必需，复杂问题",
    "background": "string, 可选，背景信息",
    "thinking_time": "integer, 可选，思考时间（秒）"
}
响应:
- 202: {"task_id": "uuid", "status": "processing", "estimated_time": 30}
"""

"""
GET /api/guanzhong/topics
描述: 获取管仲思想主题列表
响应:
- 200: [
    {"id": 1, "title": "经济思想", "description": "仓廪实而知礼节...", "icon": "💰"}
]
"""

"""
GET /api/guanzhong/topics/{id}
描述: 获取主题详情
路径参数:
- id: integer, 主题ID
响应:
- 200: {
    "id": 1,
    "title": "经济思想",
    "description": "详细描述...",
    "key_concepts": ["概念1", "概念2"],
    "related_topics": [2, 3]
}
- 404: {"message": "主题不存在"}
"""

# ========================
# 4. 知识图谱模块
# ========================

"""
GET /api/knowledge/graph
描述: 获取管仲思想知识图谱
查询参数:
- depth: integer, 图谱深度，默认2
- root: string, 根节点，默认"管仲"
响应:
- 200: {
    "nodes": [
        {"id": "gz", "label": "管仲", "category": "人物", "size": 30}
    ],
    "edges": [
        {"source": "gz", "target": "jj", "label": "提出"}
    ]
}
"""

"""
GET /api/knowledge/concepts
描述: 获取概念列表（支持搜索）
查询参数:
- q: string, 搜索关键词
- category: string, 分类过滤
- page: integer, 页码
响应:
- 200: {
    "concepts": [
        {"id": 1, "name": "相地而衰征", "category": "经济政策", "description": "..."}
    ],
    "total": 100
}
"""

"""
GET /api/knowledge/concepts/{id}
描述: 获取概念详情
响应:
- 200: 概念详细信息
- 404: {"message": "概念不存在"}
"""

"""
GET /api/knowledge/relations
描述: 获取关系列表
查询参数:
- source: string, 源概念
- target: string, 目标概念
- type: string, 关系类型
响应:
- 200: 关系列表
"""

# ========================
# 5. 历史场景模块
# ========================

"""
GET /api/scenarios
描述: 获取历史场景列表
响应:
- 200: [
    {
        "id": 1,
        "title": "九合诸侯",
        "description": "场景描述...",
        "image_url": "图片URL",
        "difficulty": "easy|medium|hard",
        "estimated_time": 30
    }
]
"""

"""
GET /api/scenarios/{id}
描述: 获取场景详情
响应:
- 200: 场景详细信息
- 404: {"message": "场景不存在"}
"""

"""
POST /api/scenarios/{id}/enter
描述: 进入历史场景
认证: 需要Bearer Token
响应:
- 200: {"session_id": "场景会话ID", "instructions": "场景说明"}
"""

"""
POST /api/scenarios/{id}/action
描述: 在场景中执行动作
认证: 需要Bearer Token
请求体:
{
    "session_id": "string, 必需，场景会话ID",
    "action": "string, 必需，执行的动作",
    "parameters": "object, 可选，动作参数"
}
响应:
- 200: {"result": "动作结果", "next_instructions": "下一步说明"}
"""

# ========================
# 6. 系统健康检查
# ========================

"""
GET /api/health
描述: 系统健康检查
响应:
- 200: {
    "status": "healthy",
    "timestamp": "2025-01-20T10:00:00",
    "version": "1.0.0",
    "services": {
        "database": "connected",
        "ai_service": "available"
    }
}
"""

"""
GET /api/version
描述: 获取API版本信息
响应:
- 200: {
    "name": "管仲AI后端API",
    "version": "1.0.0",
    "description": "管仲思想AI对话平台"
}
"""