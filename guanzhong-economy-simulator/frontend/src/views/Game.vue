<template>
  <div class="bg-scroll bg-primary/10 min-h-screen text-primary">
    <div class="container mx-auto px-4 py-6">
      <!-- 顶部信息栏 -->
      <div class="flex flex-col md:flex-row justify-between items-center mb-6 bg-card-bg p-4 rounded-lg border border-accent">
        <div>
          <h2 class="font-ancient text-2xl text-yellow-600">齐桓公<span>{{ gameData.year }}</span>年</h2>
          <p class="text-sm text-yellow-600">角色：<span>{{ role }}</span></p>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mt-4 md:mt-0">
          <!-- 统计小框：统一背景色 -->
          <div class="text-center bg-policy-btn-bg rounded-lg p-2">
            <i class="fa fa-cubes text-accent"></i>
            <p>粮仓：<span>{{ (gameData.grain / 10000).toFixed(0) }}</span>万石</p>
          </div>
          <div class="text-center bg-policy-btn-bg rounded-lg p-2">
            <i class="fa fa-money text-accent"></i>
            <p>国库：<span>{{ (gameData.treasury / 10000).toFixed(0) }}</span>万钱</p>
          </div>
          <div class="text-center bg-policy-btn-bg rounded-lg p-2">
            <i class="fa fa-users text-accent"></i>
            <p>民心：<span>{{ avgSatisfaction }}</span></p>
          </div>
          <div class="text-center bg-policy-btn-bg rounded-lg p-2">
            <i class="fa fa-calendar text-accent"></i>
            <p>剩余回合：<span>10</span></p>
          </div>
        </div>
      </div>

      <!-- 主要内容区 -->
      <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
        <!-- 左侧：政策面板 -->
        <div class="lg:col-span-1 bg-card-bg p-4 rounded-lg border border-accent">
          <!-- 政策决策标题：改为黄色 -->
          <h3 class="font-ancient text-xl text-center mb-4 text-yellow-600">政策决策</h3>
          <div class="space-y-3">
            <div class="policy-btn" @click="executePolicy('盐铁专营')">
              <h4 class="font-bold">盐铁专营</h4>
              <p class="text-sm">国家垄断盐铁生产销售</p>
            </div>
            <div class="policy-btn" @click="executePolicy('相地衰征')">
              <h4 class="font-bold">相地衰征</h4>
              <p class="text-sm">按土地质量征收赋税</p>
            </div>
            <div class="policy-btn" @click="executePolicy('铸币权集中')">
              <h4 class="font-bold">铸币权集中</h4>
              <p class="text-sm">由国家统一铸造货币</p>
            </div>
            <div class="policy-btn" @click="executePolicy('四民分业')">
              <h4 class="font-bold">四民分业</h4>
              <p class="text-sm">士农工商分类聚居</p>
            </div>
          </div>
        </div>

        <!-- 中间：场景与人物 -->
        <div class="lg:col-span-2 bg-card-bg p-4 rounded-lg border border-accent relative">
          <!-- 临淄朝堂标题：改为黄色 -->
          <h3 class="font-ancient text-xl text-center mb-4 text-yellow-600">临淄朝堂</h3>
          
          <!-- 场景图容器：统一背景色 -->
          <div class="bg-policy-btn-bg rounded-lg h-64 md:h-80 flex items-center justify-center overflow-hidden relative">
            <img src="https://picsum.photos/id/1076/800/500" alt="齐国朝堂场景" class="w-full h-full object-cover opacity-80">
            
            <!-- 互动人物：管仲 -->
            <div 
              class="absolute bottom-20 left-1/2 transform -translate-x-1/2 cursor-pointer transition-all hover:scale-110"
              @click="showGuanzhongDialog"
            >
              <img src="https://picsum.photos/id/1012/100/200" alt="管仲形象" class="w-20 h-40 object-cover rounded-full border-2 border-accent">
              <p class="text-center bg-policy-btn-bg px-2 rounded mt-1">管仲</p>
            </div>
          </div>
          
          <!-- 人物对话框：统一背景色 -->
          <div class="dialog-box mx-auto mt-4" v-show="showDialog">
            <p class="text-sm">{{ dialogText }}</p>
            <button @click="showDialog = false" class="mt-2 text-xs bg-primary text-textColor px-2 py-1 rounded "><p class="text-sm text-yellow-600">关闭</p></button>
          </div>
        </div>

        <!-- 右侧：消息与典籍 -->
        <div class="lg:col-span-1 bg-card-bg p-4 rounded-lg border border-accent">
          <!-- 典籍解读标题：改为黄色 -->
          <h3 class="font-ancient text-xl text-center mb-4 text-yellow-600">典籍解读</h3>
          <!-- 典籍内容框：统一背景色 -->
          <div class="bg-policy-btn-bg p-3 rounded-lg h-64 overflow-y-auto">
            <template v-if="classicContent">
              <h4 class="font-bold text-center">《管子·{{ classicContent.chapter }}》</h4>
              <p class="text-sm italic my-2">{{ classicContent.text }}</p>
              <p class="text-xs">{{ classicContent.explanation.substring(0, 100) }}...</p>
            </template>
            <template v-else>
              <p class="text-sm text-center text-primary/60">实施政策后将显示相关典籍...</p>
              <p class="text-sm text-center text-primary/60 mt-2">《管子》有云："通货积财，富国强兵"</p>
            </template>
          </div>
          
          <div class="mt-4">
            <button @click="nextYear" class="w-full bg-primary text-textColor py-2 rounded-lg hover:bg-primary/80 transition-all text-yellow-600">
              结束本年度
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- 典籍弹窗：统一背景色 -->
    <div class="fixed inset-0 bg-black/70 flex items-center justify-center" v-show="showClassicPopup">
      <div class="dialog-box">
        <h3 class="font-ancient text-xl text-center text-yellow-600 border-b border-yellow-600 pb-2">《管子·{{ classicContent?.chapter }}》</h3>
        <p class="my-4 text-center italic">{{ classicContent?.text }}</p>
        <p class="text-sm">{{ classicContent?.explanation }}</p>
        <button @click="showClassicPopup = false" class="mt-4 w-full bg-primary text-textColor py-2 rounded">了解了</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router' // 新增：导入路由，用于错误跳转

const router = useRouter() // 新增：初始化路由
// 政策与典籍映射（保留原逻辑）
const policies = {
  "盐铁专营": {
    treasury: 50000,
    satisfaction: { 士: 0, 农: 5, 工: 0, 商: -10 },
    classic: {
      chapter: "海王",
      text: "唯官山海为可耳。十口之家十人食盐，百口之家百人食盐。",
      explanation: "白话解读：只有由国家垄断山海资源（盐铁）才是可行的办法。十口人的家庭有十个人吃盐，百口人的家庭有一百个人吃盐。这体现了管仲通过垄断战略资源增加财政收入的思想。"
    }
  },
  "相地衰征": {
    grain: 100000,
    satisfaction: { 士: 5, 农: 15, 工: 0, 商: 0 },
    classic: {
      chapter: "乘马",
      text: "相地而衰征，则民不移。政不旅旧，则民不偷。",
      explanation: "白话解读：根据土地的好坏征收不同的赋税，百姓就不会迁移。政令不沉迷于旧习，百姓就不会苟且偷安。这体现了管仲的公平税收思想。"
    }
  },
  "铸币权集中": {
    treasury: 30000,
    satisfaction: { 士: 10, 农: 0, 工: 0, 商: -5 },
    classic: {
      chapter: "轻重乙",
      text: "币重则万物轻，币轻则万物重。",
      explanation: "白话解读：货币价值高则万物价格低，货币价值低则万物价格高。管仲认识到货币流通对经济的重要性，主张国家控制铸币权以调节经济。"
    }
  },
  "四民分业": {
    satisfaction: { 士: 5, 农: -5, 工: 10, 商: 10 },
    classic: {
      chapter: "小匡",
      text: "士农工商四民者，国之石民也，不可使杂处。",
      explanation: "白话解读：士农工商这四种民众，是国家的基石，不能让他们混杂居住。管仲主张职业分工和聚居，以提高生产效率和专业技能。"
    }
  }
};

// 响应式数据（替换原原生JS变量）
const role = ref(localStorage.getItem('selectedRole') || '国君')
const gameData = ref({
  year: 1,
  grain: 600000,
  treasury: 200000,
  satisfaction: { 士: 50, 农: 45, 工: 40, 商: 35 }
})
const showDialog = ref(false)
const dialogText = ref('')
const showClassicPopup = ref(false)
const classicContent = ref(null)

// 修复计算平均民心：关键修改点1 - 改用gameData，添加完整空值判断
const avgSatisfaction = computed(() => {
  // 兜底空对象，避免undefined/null
  const satisfactionObj = gameData.value.satisfaction || {}
  const satisfactionArr = Object.values(satisfactionObj)
  // 避免除以0（当数组为空时返回0）
  return satisfactionArr.length > 0 
    ? Math.round(satisfactionArr.reduce((a, b) => a + b, 0) / satisfactionArr.length)
    : 0
})

// 页面挂载时：优先从后端获取游戏状态，本地存储兜底
onMounted(async () => {
  try {
    // 获取本地存储的用户Token
    const userInfo = JSON.parse(localStorage.getItem('userInfo'))
    if (userInfo?.token) {
      // 调用后端接口获取最新游戏状态
      const response = await fetch('http://127.0.0.1:5000/api/game/state', {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${userInfo.token}`
        }
      })
      const data = await response.json()
      if (response.ok && data.game_state) {
        // 转换后端数据结构（class_satisfaction → satisfaction）
        const backendState = data.game_state
        gameData.value = {
          year: backendState.year || 1,
          grain: backendState.grain || 600000,
          treasury: backendState.treasury || 200000,
          // 后端返回的是{"士":50...}，直接复用
          satisfaction: backendState.class_satisfaction || { 士: 50, 农: 45, 工: 40, 商: 35 }
        }
        // 同步到本地存储
        localStorage.setItem('gameData', JSON.stringify(gameData.value))
      }
    }
  } catch (error) {
    console.log('获取后端游戏状态失败，使用本地存储:', error)
    // 读取本地存储的游戏数据
    const savedGameData = localStorage.getItem('gameData')
    if (savedGameData) {
      gameData.value = JSON.parse(savedGameData)
    }
  }
})

// 显示管仲对话
const showGuanzhongDialog = () => {
  const dialogs = [
    "国君，如今国库空虚，当推行盐铁专营以充实府库。",
    "仓廪实而知礼节，衣食足而知荣辱，治国当以富民为先。",
    "轻重之术，在于调控物价，平衡供需，此乃治国要道。",
    "四民分业，各司其职，国家才能井然有序，富强可期。"
  ];
  dialogText.value = dialogs[Math.floor(Math.random() * dialogs.length)]
  showDialog.value = true
}

// 显示典籍弹窗
const showClassicPopupFn = (policy) => {
  classicContent.value = policies[policy].classic
  showClassicPopup.value = true
}

// 执行政策
const executePolicy = (policy) => {
  const effects = policies[policy]
  
  // 更新经济数据
  if (effects.treasury) gameData.value.treasury += effects.treasury
  if (effects.grain) gameData.value.grain += effects.grain
  
  // 更新满意度（限制0-100）
  if (effects.satisfaction) {
    for (const [group, change] of Object.entries(effects.satisfaction)) {
      // 关键修改点2 - 兜底默认值，避免undefined
      const currentValue = gameData.value.satisfaction[group] || 50
      gameData.value.satisfaction[group] = Math.max(0, Math.min(100, currentValue + change))
    }
  }
  
  // 保存数据到本地存储
  localStorage.setItem('gameData', JSON.stringify(gameData.value))
  
  // 同步到后端（新增：可选，确保后端数据最新）
  syncGameStateToBackend()
  
  // 显示典籍
  showClassicPopupFn(policy)
}

// 结束本年度
const nextYear = () => {
  gameData.value.year++
  // 每年粮食自然损耗5%
  gameData.value.grain = Math.round(gameData.value.grain * 0.95)
  localStorage.setItem('gameData', JSON.stringify(gameData.value))
  
  // 同步到后端
  syncGameStateToBackend()
  
  // 随机事件
  const events = [
    "今年风调雨顺，农业略有丰收，粮食+5万石。",
    "商人囤积居奇，民心略有下降。",
    "邻国遣使来朝，带来贡品，国库+3万钱。"
  ];
  const randomEvent = events[Math.floor(Math.random() * events.length)]
  
  // 临时显示事件（可优化为UI展示）
  classicContent.value = {
    chapter: "年度事件",
    text: randomEvent,
    explanation: ""
  }
  
  // 事件对应的数值变化（可选）
  if (randomEvent.includes('粮食+5万石')) {
    gameData.value.grain += 50000
  } else if (randomEvent.includes('国库+3万钱')) {
    gameData.value.treasury += 30000
  } else if (randomEvent.includes('民心略有下降')) {
    for (const group in gameData.value.satisfaction) {
      // 关键修改点3 - 兜底默认值
      const currentValue = gameData.value.satisfaction[group] || 50
      gameData.value.satisfaction[group] = Math.max(0, currentValue - 2)
    }
  }
  localStorage.setItem('gameData', JSON.stringify(gameData.value))
  syncGameStateToBackend()
}

// 新增：同步游戏状态到后端（确保数据持久化）
const syncGameStateToBackend = async () => {
  try {
    const userInfo = JSON.parse(localStorage.getItem('userInfo'))
    if (!userInfo?.token) return
    
    // 转换为后端需要的格式
    const backendState = {
      year: gameData.value.year,
      treasury: gameData.value.treasury,
      grain: gameData.value.grain,
      salt: 10000, // 兜底默认值
      iron: 5000,  // 兜底默认值
      stability: avgSatisfaction.value,
      class_satisfaction: gameData.value.satisfaction,
      active_policies: [],
      historical_events: []
    }
    
    await fetch('http://127.0.0.1:5000/api/game/sync-state', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${userInfo.token}`
      },
      body: JSON.stringify({ game_state: backendState })
    })
  } catch (error) {
    console.log('同步游戏状态到后端失败:', error)
  }
}
</script>

<style scoped>
/* 保留原自定义样式 */
.bg-scroll {
  background-image: url('https://picsum.photos/id/152/1200/800');
  background-size: cover;
  background-blend-mode: overlay;
}

/* 统一政策按钮背景色（基准色） */
.policy-btn {
  background-color: rgba(210, 180, 140, 0.8); /* 基准黄色系背景 */
  border: 2px solid #CD853F;
  border-radius: 0.5rem;
  padding: 0.75rem;
  cursor: pointer;
  transition: all 0.3s;
}
.policy-btn:hover {
  transform: scale(1.05);
  background-color: #D2B48C;
}

/* 新增：统一小框背景色（和政策按钮一致） */
.bg-policy-btn-bg {
  background-color: rgba(210, 180, 140, 0.8);
}

/* 新增：统一卡片背景色（稍浅的同色系） */
.bg-card-bg {
  background-color: rgba(210, 180, 140, 0.3);
}

/* 对话框样式（保持和政策按钮一致） */
.dialog-box {
  background-color: rgba(210, 180, 140, 0.9);
  border: 2px solid #8B4513;
  border-radius: 0.5rem;
  padding: 1rem;
  max-width: 24rem;
}

/* 古风黄色（标题色） */
.text-yellow-600 {
  color: #CA8A04; /* 适配古风的暗黄色，比纯黄更协调 */
}
.border-yellow-600 {
  border-color: #CA8A04;
}
</style>