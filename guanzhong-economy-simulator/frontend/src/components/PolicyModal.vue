<template>
  <div class="policy-modal" v-if="show">
    <div class="modal-content">
      <h3>{{ policy.name }}</h3>
      <div class="policy-details">
        <p><strong>类型：</strong>{{ policy.type }}</p>
        <p><strong>实施成本：</strong>{{ policy.cost }}钱</p>
        <div class="effects">
          <h4>政策效果：</h4>
          <ul>
            <li v-for="(effect, idx) in policy.effects" :key="idx">
              {{ effect.name }}: {{ effect.value }}
            </li>
          </ul>
        </div>
      </div>
      <div class="modal-actions">
        <button 
          @click="applyPolicy"
          :disabled="!canApply"
          :class="{ disabled: !canApply }">
          实施政策
        </button>
        <button @click="$emit('close')">取消</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useGameStore } from '@/stores/game'

const props = defineProps({
  show: Boolean,
  policy: Object
})

const emit = defineEmits(['close', 'applied'])

const gameStore = useGameStore()

const canApply = computed(() => {
  return gameStore.canApplyPolicy(props.policy.id)
})

async function applyPolicy() {
  const result = await gameStore.applyPolicy(props.policy.id)
  if (result.status === 'success') {
    emit('applied', props.policy)
  }
  emit('close')
}
</script>

<style scoped>
.policy-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: #3B6E51;
  padding: 2rem;
  border-radius: 8px;
  width: 80%;
  max-width: 500px;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 1.5rem;
}

button.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>