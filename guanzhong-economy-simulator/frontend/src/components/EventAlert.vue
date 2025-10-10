<template>
  <div v-if="event" class="event-alert">
    <div class="event-header">
      <h3>{{ event.name }}</h3>
      <span class="year">{{ store.state.year }}年</span>
    </div>
    
    <p class="description">{{ event.description }}</p>
    
    <div class="solutions">
      <div v-for="(solution, idx) in event.solutions" 
           :key="idx" 
           class="solution">
        <h4>{{ solution.name }}</h4>
        <p class="ai-advice">管仲建议：{{ solution.ai_advice }}</p>
        <button @click="resolve(idx)">
          选择此方案
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useGameStore } from '@/stores/game'

const store = useGameStore()
const event = computed(() => store.state.activeEvents[0])

const resolve = (solutionIndex) => {
  store.resolveEvent(event.value.id, solutionIndex)
}
</script>

<style scoped>
.event-alert {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #1A202C;
  border: 2px solid #D4AF37;
  border-radius: 8px;
  padding: 2rem;
  z-index: 1000;
  max-width: 600px;
}

.event-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.solutions {
  margin-top: 1.5rem;
}

.solution {
  background: rgba(59, 110, 81, 0.2);
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 4px;
}

.ai-advice {
  font-style: italic;
  color: #D4AF37;
  margin: 0.5rem 0;
}

button {
  background: #D4AF37;
  color: #1A202C;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
}
</style>