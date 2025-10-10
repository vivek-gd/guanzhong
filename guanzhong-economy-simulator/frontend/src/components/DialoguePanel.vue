<template>
  <div class="dialogue-container">
    <div class="messages">
      <div v-for="(msg, idx) in messages" :key="idx" 
           :class="['message', msg.role]">
        <div class="avatar">
          
          
        </div>
        <div class="content">
          <div class="text">{{ msg.content }}</div>
          <div v-if="msg.actions && msg.role === 'assistant'" 
               class="actions">
            <button v-for="(action, i) in msg.actions" 
                    :key="i" @click="applyAction(action)">
              {{ action }}
            </button>
          </div>
        </div>
      </div>
    </div>
    
    <div class="input-area">
      <input v-model="inputMessage" 
             @keyup.enter="sendMessage"
             placeholder="向管仲请教治国之道...">
      <button @click="sendMessage">
        <i class="fas fa-paper-plane"></i>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useGameStore } from '@/stores/game'

const gameStore = useGameStore()
const messages = ref([
  {
    role: 'assistant',
    content: '老夫管仲，见过阁下。治国之道，首在富民。有何疑问，但说无妨。',
    actions: []
  }
])
const inputMessage = ref('')

async function sendMessage() {
  if (!inputMessage.value.trim()) return
  
  // 添加用户消息
  messages.value.push({
    role: 'user',
    content: inputMessage.value,
    actions: []
  })
  
  const userQuestion = inputMessage.value
  inputMessage.value = ''
  
  // 调用API获取回答
  const response = await fetch('/api/dialogue/ask', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question: userQuestion })
  })
  
  const data = await response.json()
  
  // 添加AI回复
  messages.value.push({
    role: 'assistant',
    content: data.data.answer,
    actions: data.data.suggested_actions || []
  })
}

function applyAction(action) {
  // 在游戏状态中应用建议政策
  gameStore.applyPolicySuggestion(action)
}
</script>

<style scoped>
.dialogue-container {
  border: 1px solid #3B6E51;
  border-radius: 8px;
  height: 500px;
  display: flex;
  flex-direction: column;
}

.messages {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
}

.message {
  display: flex;
  margin-bottom: 1rem;
}

.message.user {
  justify-content: flex-end;
}

.avatar img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
}

.content {
  max-width: 70%;
  margin: 0 10px;
}

.actions {
  margin-top: 10px;
}

.actions button {
  background: rgba(59, 110, 81, 0.3);
  border: none;
  padding: 5px 10px;
  margin-right: 5px;
  border-radius: 4px;
  cursor: pointer;
}

.input-area {
  display: flex;
  padding: 10px;
  border-top: 1px solid #3B6E51;
}

.input-area input {
  flex: 1;
  padding: 8px;
  border: 1px solid #3B6E51;
  border-radius: 4px;
  background: rgba(255,255,255,0.1);
  color: white;
}
</style>