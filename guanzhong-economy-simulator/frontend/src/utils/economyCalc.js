// 经济计算工具 - 纯计算逻辑，不涉及网络请求
export class EconomyCalculator {
  // 政策效果计算
  static calculatePolicyEffects(policy, currentState) {
    const effects = {
      treasury: 0,
      grain: 0,
      stability: 0,
      classEffects: {}
    }

    // 基于政策类型进行计算
    switch (policy.type) {
      case 'taxation':
        effects.treasury = policy.rate * currentState.gdp * 0.1
        effects.stability = -policy.rate * 5
        break
      case 'infrastructure':
        effects.treasury = -policy.cost
        effects.grain = policy.efficiency * 100
        effects.stability = 10
        break
      // 更多政策类型...
    }

    return effects
  }

  // 经济指标预测
  static forecastEconomy(currentState, policies, years = 1) {
    const forecast = []
    let state = { ...currentState }

    for (let year = 0; year < years; year++) {
      // 应用所有政策效果
      policies.forEach(policy => {
        const effects = this.calculatePolicyEffects(policy, state)
        Object.keys(effects).forEach(key => {
          if (typeof state[key] === 'number') {
            state[key] += effects[key]
          }
        })
      })

      forecast.push({
        year: state.year + year,
        ...state
      })
    }

    return forecast
  }

  // 风险评估
  static assessRisk(state, policies) {
    let riskScore = 0
    
    // 国库风险
    if (state.treasury < 0) riskScore += 30
    if (state.treasury < state.expenses * 3) riskScore += 20
    
    // 民心风险
    if (state.stability < 30) riskScore += 40
    if (state.stability < 50) riskScore += 20
    
    // 政策风险
    policies.forEach(policy => {
      riskScore += policy.riskLevel * 10
    })

    return Math.min(riskScore, 100)
  }
}

// 导出工具函数
export const formatCurrency = (amount) => {
  return new Intl.NumberFormat('zh-CN', {
    style: 'currency',
    currency: 'CNY'
  }).format(amount)
}

export const calculateGrowthRate = (current, previous) => {
  if (previous === 0) return 0
  return ((current - previous) / previous * 100).toFixed(2)
}