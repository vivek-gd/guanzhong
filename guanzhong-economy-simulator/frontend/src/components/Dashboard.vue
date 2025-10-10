<template>
  <div class="dashboard-container">
    <!-- 顶部状态栏 -->
    <div class="status-bar">
      <div class="status-item">
        <span class="label">年份:</span>
        <span class="value">{{ gameStore.state.year }}年</span>
      </div>
      <div class="status-item">
        <span class="label">国库:</span>
        <span class="value">{{ gameStore.state.treasury }}钱</span>
      </div>
      <div class="status-item">
        <span class="label">民心:</span>
        <span class="value">{{ gameStore.state.popularSupport }}%</span>
      </div>
      <div class="status-item class-support" v-for="cls in socialClasses" :key="cls">
        <span class="label">{{ cls }}支持:</span>
        <div class="support-bar">
          <div class="support-fill" :style="{ 
            width: `${gameStore.state.classSupport[cls]}%`,
            backgroundColor: socialClassColors[cls]
          }"></div>
          <span class="support-value">{{ gameStore.state.classSupport[cls] }}%</span>
        </div>
      </div>
    </div>

    <!-- 主内容区域 -->
    <div class="main-content">
      <!-- 左侧对话面板 -->
      <div class="left-panel">
        <DialogueContainer />
      </div>

      <!-- 右侧信息面板 -->
      <div class="right-panel">
        <!-- 政策列表 -->
        <div class="policy-list">
          <h3>可用政策</h3>
          <div class="policy-cards">
            <div v-for="policy in availablePolicies" 
                 :key="policy.id" 
                 class="policy-card"
                 @click="openPolicyModal(policy)">
              <h4>{{ policy.name }}</h4>
              <p class="policy-type">{{ policy.type }}</p>
              <p class="policy-cost">成本: {{ policy.cost }}钱</p>
              <div class="policy-effects">
                <span v-for="effect in policy.effects" 
                      :key="effect.name"
                      class="effect-tag">
                  {{ effect.name }}: {{ effect.value }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- 当前实施的政策 -->
        <div class="active-policies">
          <h3>已实施政策</h3>
          <div v-for="policy in activePolicies" 
               :key="policy.id" 
               class="active-policy">
            <span>{{ policy.name }}</span>
            <span class="policy-duration">已实施: {{ policy.duration }}年</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 政策模态框 -->
    <PolicyModal 
      v-if="selectedPolicy"
      :show="showPolicyModal"
      :policy="selectedPolicy"
      @close="closePolicyModal"
      @applied="onPolicyApplied" />

    <!-- 事件提醒 -->
    <EventAlert 
      v-if="gameStore.state.activeEvents.length > 0"
      :event="gameStore.state.activeEvents[0]" />

    <!-- 底部操作栏 -->
    <div class="action-bar">
      <button class="btn-next-turn" @click="nextTurn">
        结束回合 ({{ nextTurnTime }}s)
      </button>
      <div class="game-speed">
        <button v-for="speed in gameSpeeds" 
                :key="speed.value"
                :class="{ active: gameSpeed === speed.value }"
                @click="setGameSpeed(speed.value)">
          {{ speed.label }}
        </button>
      </div>
    </div>

    <!-- 政策分析面板 -->
    <div class="analysis-panel" v-if="analyzedPolicy">
      <PolicyAnalysis :policy="analyzedPolicy" />
      <button class="close-analysis" @click="analyzedPolicy = null">
        <i class="fas fa-times"></i>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useGameStore } from '@/stores/game'
import DialogueContainer from '@/components/DialogueContainer.vue'
import EventAlert from '@/components/EventAlert.vue'
import PolicyAnalysis from '@/components/PolicyAnalysis.vue'
import PolicyModal from '@/components/PolicyModal.vue'

const gameStore = useGameStore()

// 游戏状态
const showPolicyModal = ref(false)
const selectedPolicy = ref(null)
const analyzedPolicy = ref(null)
const gameSpeed = ref(1)
const nextTurnTime = ref(10)

// 社会阶级配置
const socialClasses = ['士', '农', '工', '商']
const socialClassColors = {
  '士': '#4C6EF5',
  '农': '#40C057', 
  '工': '#FD7E14',
  '商': '#E64980'
}

// 游戏速度选项
const gameSpeeds = [
  { label: '慢速', value: 0.5 },
  { label: '正常', value: 1 },
  { label: '快速', value: 2 }
]

// 计算属性
const availablePolicies = computed(() => gameStore.getAvailablePolicies())
const activePolicies = computed(() => gameStore.getActivePolicies())

// 政策操作
const openPolicyModal = (policy) => {
  selectedPolicy.value = policy
  showPolicyModal.value = true
}

const closePolicyModal = () => {
  showPolicyModal.value = false
  selectedPolicy.value = null
}

const onPolicyApplied = (policy) => {
  // 政策应用后的处理
  analyzedPolicy.value = policy
}

// 游戏流程控制
const nextTurn = () => {
  gameStore.nextTurn()
  // 重置倒计时
  nextTurnTime.value = 10
}

const setGameSpeed = (speed) => {
  gameSpeed.value = speed
  // 更新游戏计时器
}

// 自动回合计时
let turnTimer = null
onMounted(() => {
  turnTimer = setInterval(() => {
    if (nextTurnTime.value > 0) {
      nextTurnTime.value -= 1
    } else {
      nextTurn()
    }
  }, 1000)
})

onUnmounted(() => {
  if (turnTimer) {
    clearInterval(turnTimer)
  }
})
</script>

<style scoped>
.dashboard-container {
  height: 100vh;
  background: linear-gradient(135deg, #1A202C 0%, #2D3748 100%);
  color: white;
  display: flex;
  flex-direction: column;
  font-family: 'SimSun', serif;
}

.status-bar {
  display: flex;
  align-items: center;
  padding: 1rem;
  background: rgba(59, 110, 81, 0.3);
  border-bottom: 2px solid #3B6E51;
  gap: 2rem;
  flex-wrap: wrap;
}

.status-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.label {
  font-weight: bold;
  color: #D4AF37;
}

.support-bar {
  position: relative;
  width: 80px;
  height: 16px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  overflow: hidden;
}

.support-fill {
  height: 100%;
  transition: width 0.3s ease;
}

.support-value {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 0.7rem;
  color: white;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
}

.main-content {
  flex: 1;
  display: flex;
  gap: 1rem;
  padding: 1rem;
  overflow: hidden;
}

.left-panel {
  flex: 2;
  min-width: 0;
}

.right-panel {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  min-width: 300px;
}

.policy-list, .active-policies {
  background: rgba(59, 110, 81, 0.2);
  border: 1px solid #3B6E51;
  border-radius: 8px;
  padding: 1rem;
}

.policy-cards {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.policy-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid #3B6E51;
  border-radius: 6px;
  padding: 0.8rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.policy-card:hover {
  background: rgba(59, 110, 81, 0.3);
  transform: translateY(-2px);
}

.policy-type {
  font-size: 0.8rem;
  color: #D4AF37;
  margin: 0.2rem 0;
}

.policy-cost {
  font-size: 0.8rem;
  color: #FF6B6B;
  margin: 0.2rem 0;
}

.effect-tag {
  display: inline-block;
  background: rgba(59, 110, 81, 0.3);
  padding: 0.2rem 0.5rem;
  border-radius: 12px;
  font-size: 0.7rem;
  margin: 0.2rem;
}

.active-policy {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem;
  background: rgba(59, 110, 81, 0.1);
  border-radius: 4px;
  margin: 0.2rem 0;
}

.policy-duration {
  font-size: 0.8rem;
  color: #868E96;
}

.action-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background: rgba(59, 110, 81, 0.3);
  border-top: 2px solid #3B6E51;
}

.btn-next-turn {
  background: linear-gradient(135deg, #D4AF37 0%, #BF9520 100%);
  color: #1A202C;
  border: none;
  padding: 0.8rem 2rem;
  border-radius: 6px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-next-turn:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(212, 175, 55, 0.3);
}

.game-speed {
  display: flex;
  gap: 0.5rem;
}

.game-speed button {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid #3B6E51;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
}

.game-speed button.active {
  background: #3B6E51;
  color: white;
}

.analysis-panel {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #1A202C;
  border: 2px solid #D4AF37;
  border-radius: 8px;
  padding: 2rem;
  z-index: 1001;
  max-width: 600px;
  width: 90%;
}

.close-analysis {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  color: white;
  cursor: pointer;
  font-size: 1.2rem;
}
</style>