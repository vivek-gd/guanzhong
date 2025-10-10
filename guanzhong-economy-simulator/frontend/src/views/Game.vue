<template>
  <div class="game-container">
    <div class="header">
      <h1>春秋富国策 · {{ state.year }}年</h1>
      <div class="stats">
        <div class="stat">
          <span class="label">国库：</span>
          <span class="value">{{ state.treasury }}钱</span>
        </div>
        <div class="stat">
          <span class="label">粮仓：</span>
          <span class="value">{{ state.grain }}石</span>
        </div>
        <div class="stat">
          <span class="label">稳定度：</span>
          <span class="value">{{ state.stability }}/100</span>
        </div>
      </div>
    </div>

    <div class="main-content">
      <PolicyModal 
        v-if="showPolicyModal"
        :policy="selectedPolicy"
        @close="showPolicyModal = false"
        @applied="onPolicyApplied" />
      
      <EventAlert 
        v-if="state.activeEvent"
        :event="state.activeEvent"
        @resolve="resolveEvent" />
      
      <PolicyList 
        :policies="state.policies"
        @select="openPolicyModal" />
      
      <button class="next-round" @click="advanceRound">
        进入下一年
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useGameStore } from '@/stores/game'
import PolicyModal from '@/components/PolicyModal.vue'
import EventAlert from '@/components/EventAlert.vue'
import PolicyList from '@/components/PolicyList.vue'

const gameStore = useGameStore()
const state = gameStore.state
const showPolicyModal = ref(false)
const selectedPolicy = ref(null)

onMounted(async () => {
  await gameStore.fetchGameState()
})

function openPolicyModal(policy) {
  selectedPolicy.value = policy
  showPolicyModal.value = true
}

function onPolicyApplied(policy) {
  // 可添加政策应用后的特殊效果
}

async function advanceRound() {
  state.year++
  await gameStore.checkForEvent()
}

async function resolveEvent(solution) {
  // 处理事件解决方案
  state.activeEvent = null
}
</script>

<style scoped>
.game-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  color: #F7FAFC;
}

.header {
  background: rgba(59, 110, 81, 0.8);
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 2rem;
}

.stats {
  display: flex;
  gap: 2rem;
  margin-top: 1rem;
}

.stat {
  background: rgba(140, 120, 81, 0.3);
  padding: 0.5rem 1rem;
  border-radius: 4px;
}

.next-round {
  background: #D4AF37;
  color: #1A202C;
  padding: 0.8rem 1.5rem;
  border: none;
  border-radius: 4px;
  font-weight: bold;
  margin-top: 2rem;
  cursor: pointer;
}
</style>