import { useGameStore } from '../stores/game'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api'

class ApiService {
  constructor() {
    this.baseURL = API_BASE_URL
  }

  // 通用请求方法
  async request(endpoint, options = {}) {
    const url = `${this.baseURL}${endpoint}`
    const config = {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    }

    try {
      const response = await fetch(url, config)
      
      if (!response.ok) {
        throw new Error(`HTTP错误: ${response.status}`)
      }

      return await response.json()
    } catch (error) {
      console.error('API请求失败:', error)
      throw error
    }
  }

  // ==================== 对话API ====================
  async chatWithGuanZhong(message, dialogueId = null) {
    return this.request('/guanzhong/chat', {
      method: 'POST',
      body: JSON.stringify({ 
        message, 
        dialogue_id: dialogueId 
      })
    })
  }

  // ==================== 经济API ====================
  async simulateEconomy(policyId, parameters) {
    return this.request('/economy/simulate', {
      method: 'POST',
      body: JSON.stringify({
        policy_id: policyId,
        parameters: parameters
      })
    })
  }

  async getEconomicData() {
    return this.request('/economy/data')
  }

  // ==================== 游戏API ====================
  async getGameState() {
    return this.request('/game/state')
  }

  async nextTurn() {
    return this.request('/game/next-turn', {
      method: 'POST'
    })
  }

  async applyPolicy(policyId) {
    return this.request('/policies/apply', {
      method: 'POST',
      body: JSON.stringify({ policy_id: policyId })
    })
  }

  // ==================== 系统API ====================
  async healthCheck() {
    return this.request('/health')
  }

  async getVersion() {
    return this.request('/version')
  }
}

export const apiService = new ApiService()