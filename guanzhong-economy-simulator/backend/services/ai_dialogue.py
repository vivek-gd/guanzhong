import requests
import re
from enum import Enum

class QuestionType(Enum):
    ECONOMIC = "economic"
    HISTORICAL = "historical"
    GENERAL = "general"

class AIDialogueService:
    def __init__(self):
        self.llm_api = "https://api.doubao.com/v3/chat/completions"
        self.api_key = "your-api-key"
        
    def route_question(self, question: str, context: dict) -> dict:
        # 问题分类逻辑
        q_type = self._classify_question(question)
        
        if q_type == QuestionType.ECONOMIC:
            return self._handle_economic_question(question, context)
        elif q_type == QuestionType.HISTORICAL:
            return self._handle_historical_question(question)
        else:
            return self._handle_general_question(question)

    def _classify_question(self, question: str) -> QuestionType:
        economic_terms = ["税收", "财政", "粮食", "盐铁", "货币", "物价"]
        historical_terms = ["齐桓公", "鲍叔牙", "春秋", "诸侯"]
        
        if any(term in question for term in economic_terms):
            return QuestionType.ECONOMIC
        elif any(term in question for term in historical_terms):
            return QuestionType.HISTORICAL
        else:
            return QuestionType.GENERAL

    def _handle_economic_question(self, question: str, context: dict) -> dict:
        # 结合游戏状态生成专业回答
        prompt = f"""你扮演管仲（公元前725-前645年），当前是{context['game_year']}年。
        
        国家现状：
        - 国库: {context['current_state']['treasury']}钱
        - 粮仓: {context['current_state']['grain']}石
        - 稳定度: {context['current_state']['stability']}/100
        
        请用管仲的身份和语言风格回答关于经济政策的问题：
        {question}
        
        回答需包含：
        1. 简要分析问题本质
        2. 引用《管子》相关理论
        3. 提出具体政策建议
        4. 预测政策效果
        """
        
        llm_response = self._call_llm(prompt)
        
        # 提取建议政策
        suggested_actions = self._extract_policy_suggestions(llm_response)
        
        return {
            "answer": llm_response,
            "type": "economic",
            "actions": suggested_actions
        }

    def _call_llm(self, prompt: str) -> str:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        payload = {
            "model": "Doubao-Pro",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 500
        }
        
        response = requests.post(self.llm_api, json=payload, headers=headers)
        return response.json()['choices'][0]['message']['content']
    
    def _extract_policy_suggestions(self, text: str) -> list:
        # 使用正则提取政策建议
        pattern = r"建议实施(.*?)(?:，|。|$)"
        return re.findall(pattern, text)