<template>
  <div class="policy-analysis">
    <div class="header">
      <h3>{{ policy.name }}</h3>
      <div class="risk-meter">
        实施风险: 
        <div class="risk-bar" :style="{ width: `${analysis.implementation_risk * 100}%` }"></div>
      </div>
    </div>
    
    <div class="tabs">
      <button v-for="tab in tabs" 
              :key="tab"
              @click="activeTab = tab"
              :class="{ active: activeTab === tab }">
        {{ tab }}
      </button>
    </div>
    
    <div class="tab-content">
      <div v-if="activeTab === '历史依据'" class="historical-basis">
        {{ analysis.historical_basis }}
      </div>
      <div v-if="activeTab === '现代类比'" class="modern-analogy">
        {{ analysis.modern_analogy }}
      </div>
    </div>
    
    <div class="class-effects">
      <div v-for="cls in socialClasses" 
           :key="cls" 
           class="class-effect"
           :style="{ backgroundColor: socialClassColors[cls] }">
        {{ cls }}: {{ policy.effects.class_effects[cls] || 0 }}%
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useGameStore } from '@/stores/game'

const props = defineProps({
  policy: Object
})

const store = useGameStore()
const activeTab = ref('历史依据')
const tabs = ['历史依据', '现代类比']

const analysis = computed(() => 
  store.getPolicyAnalysis(props.policy.id)
)

const socialClasses = Object.values(SocialClass)
const socialClassColors = store.socialClassColors
</script>

<style scoped>
.policy-analysis {
  border: 1px solid #3B6E51;
  border-radius: 8px;
  padding: 1rem;
}

.risk-meter {
  display: flex;
  align-items: center;
  margin: 0.5rem 0;
}

.risk-bar {
  height: 10px;
  background: linear-gradient(to right, #3B6E51, #D4AF37);
  margin-left: 10px;
  border-radius: 5px;
}

.tabs {
  display: flex;
  margin: 1rem 0;
}

.tabs button {
  padding: 0.5rem 1rem;
  background: none;
  border: none;
  cursor: pointer;
}

.tabs button.active {
  border-bottom: 2px solid #D4AF37;
}

.class-effects {
  display: flex;
  gap: 0.5rem;
  margin-top: 1rem;
}

.class-effect {
  padding: 0.3rem 0.6rem;
  border-radius: 4px;
  color: white;
  font-size: 0.8rem;
}
</style>