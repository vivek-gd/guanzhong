import { defineStore } from 'pinia'
import { reactive, computed } from 'vue'

export const useGameStore = defineStore('game', () => {
  const state = reactive({
    year: -685,
    treasury: 200000,
    grain: 600000,
    stability: 50,
    classSatisfaction: {
      [SocialClass.SCHOLARS]: 60,
      [SocialClass.FARMERS]: 50,
      [SocialClass.ARTISANS]: 40,
      [SocialClass.MERCHANTS]: 30
    },
    activePolicies: [],
    activeEvents: [],
    policyAnalysis: {}
  })

  const socialClassColors = {
    [SocialClass.SCHOLARS]: '#3B6E51',
    [SocialClass.FARMERS]: '#8C7851',
    [SocialClass.ARTISANS]: '#D4AF37',
    [SocialClass.MERCHANTS]: '#A23B72'
  }

  const getPolicyAnalysis = async (policyId) => {
    if (!state.policyAnalysis[policyId]) {
      const res = await fetch(`/api/policies/${policyId}/analysis`)
      state.policyAnalysis[policyId] = await res.json()
    }
    return state.policyAnalysis[policyId]
  }

  const resolveEvent = async (eventId, solutionIndex) => {
    const res = await fetch(`/api/events/${eventId}/resolve`, {
      method: 'POST',
      body: JSON.stringify({ solution_index: solutionIndex })
    })
    Object.assign(state, await res.json())
  }

  return { 
    state,
    socialClassColors,
    getPolicyAnalysis,
    resolveEvent
  }
})