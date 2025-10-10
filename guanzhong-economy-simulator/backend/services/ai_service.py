import requests
from backend.config import Config
from backend.models.economy import SocialClass

class AIService:
    def __init__(self):
        self.api_url = Config.DOUBAO_API_URL
        self.api_key = Config.DOUBAO_API_KEY
        self.policy_advice_cache = {}

    def get_policy_analysis(self, policy_id: str, state) -> dict:
        if policy_id in self.policy_advice_cache:
            return self.policy_advice_cache[policy_id]
        
        prompt = self._build_policy_prompt(policy_id, state)
        response = self._call_llm(prompt)
        
        analysis = {
            "historical_basis": self._extract_section(response, "历史依据"),
            "modern_analogy": self._extract_section(response, "现代类比"),
            "implementation_risk": float(self._extract_section(response, "实施风险"))
        }
        
        self.policy_advice_cache[policy_id] = analysis
        return analysis

    def _build_policy_prompt(self, policy_id: str, state) -> str:
        return f"""作为管仲的经济顾问，请分析以下政策：
        
政策名称：{policy_id}
当前国情：
- 国库：{state.treasury}钱
- 粮仓：{state.grain}石
- 民心稳定：{state.stability}
- 各阶层满意度：
  士：{state.class_satisfaction[SocialClass.SCHOLARS]} 
  农：{state.class_satisfaction[SocialClass.FARMERS]}
  工：{state.class_satisfaction[SocialClass.ARTISANS]}
  商：{state.class_satisfaction[SocialClass.MERCHANTS]}

请从以下角度分析：
### 历史依据
引用《管子》相关论述

### 现代类比
对应现代经济政策

### 实施风险
0-1的风险评分"""

    def _call_llm(self, prompt: str) -> str:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "model": "Doubao-Pro",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3  # 降低随机性
        }
        response = requests.post(self.api_url, headers=headers, json=payload)
        return response.json()["choices"][0]["message"]["content"]

    def _extract_section(self, response, section):
        start_index = response.find(f"### {section}")
        if start_index == -1:
            return ""
        start_index += len(f"### {section}")
        end_index = response.find("###", start_index)
        if end_index == -1:
            end_index = len(response)
        return response[start_index:end_index].strip()