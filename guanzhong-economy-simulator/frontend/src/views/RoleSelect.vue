<template>
  <div class="bg-paper bg-primary/20 min-h-screen">
    <div class="container mx-auto px-4 py-8">
      <!-- 标题 -->
      <div class="text-center mb-12">
        <h1 class="text-[clamp(2rem,5vw,4rem)] font-ancient text-primary text-shadow">春秋富国策</h1>
        <p class="text-[clamp(1rem,2vw,1.5rem)] text-primary/80 mt-2">管仲经济模拟器</p>
      </div>

      <!-- 角色选择 -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">
        <!-- 国君 -->
        <div 
          class="role-card-hover bg-secondary/70 rounded-lg p-5 border-2 cursor-pointer"
          :class="selectedRole === '国君' ? 'border-red-500' : 'border-accent'"
          @click="selectRole('国君')"
        >
          <div class="w-32 h-32 mx-auto bg-primary/10 rounded-full flex items-center justify-center">
            <i class="fa fa-university text-5xl text-primary"></i>
          </div>
          <h3 class="text-center text-primary text-xl mt-4">国君</h3>
          <p class="text-center text-primary/80 text-sm mt-2">政策最终决策权</p>
        </div>

        <!-- 大司农 -->
        <div 
          class="role-card-hover bg-secondary/70 rounded-lg p-5 border-2 cursor-pointer"
          :class="selectedRole === '大司农' ? 'border-red-500' : 'border-accent'"
          @click="selectRole('大司农')"
        >
          <div class="w-32 h-32 mx-auto bg-primary/10 rounded-full flex items-center justify-center">
            <i class="fa fa-line-chart text-5xl text-primary"></i>
          </div>
          <h3 class="text-center text-primary text-xl mt-4">大司农</h3>
          <p class="text-center text-primary/80 text-sm mt-2">经济数据可视化</p>
        </div>

        <!-- 盐铁使 -->
        <div 
          class="role-card-hover bg-secondary/70 rounded-lg p-5 border-2 cursor-pointer"
          :class="selectedRole === '盐铁使' ? 'border-red-500' : 'border-accent'"
          @click="selectRole('盐铁使')"
        >
          <div class="w-32 h-32 mx-auto bg-primary/10 rounded-full flex items-center justify-center">
            <i class="fa fa-balance-scale text-5xl text-primary"></i>
          </div>
          <h3 class="text-center text-primary text-xl mt-4">盐铁使</h3>
          <p class="text-center text-primary/80 text-sm mt-2">专营商品定价权</p>
        </div>

        <!-- 民间商人 -->
        <div 
          class="role-card-hover bg-secondary/70 rounded-lg p-5 border-2 cursor-pointer"
          :class="selectedRole === '民间商人' ? 'border-red-500' : 'border-accent'"
          @click="selectRole('民间商人')"
        >
          <div class="w-32 h-32 mx-auto bg-primary/10 rounded-full flex items-center justify-center">
            <i class="fa fa-shopping-cart text-5xl text-primary"></i>
          </div>
          <h3 class="text-center text-primary text-xl mt-4">民间商人</h3>
          <p class="text-center text-primary/80 text-sm mt-2">跨区域贸易特权</p>
        </div>
      </div>

      <!-- 开始按钮 -->
      <div class="text-center">
        <button 
          class="bg-primary hover:bg-primary/80 text-textColor px-8 py-3 rounded-lg text-lg font-ancient border-2 border-accent disabled:opacity-50 disabled:cursor-not-allowed"
          :disabled="!selectedRole"
          @click="startGame"
        >
          开始治国
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const selectedRole = ref(null)

// 选择角色
const selectRole = (role) => {
  selectedRole.value = role
  localStorage.setItem('selectedRole', role)
}

// 开始游戏
const startGame = async () => {
  try {
    // 获取本地存储的Token
    const userInfo = JSON.parse(localStorage.getItem('userInfo'))
    const response = await fetch('http://127.0.0.1:5000/api/game/select-role', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${userInfo.token}`  // 携带Token认证
      },
      body: JSON.stringify({
        role: selectedRole.value
      })
    })

    const data = await response.json()
    if (response.ok) {
      // 保存游戏状态
      localStorage.setItem('gameData', JSON.stringify(data.game_state))
      router.push('/game')
    } else {
      alert(data.message || '选择角色失败')
    }
  } catch (error) {
    alert('无法连接游戏服务器')
  }
}

// 页面挂载时读取本地存储的角色（可选）
onMounted(() => {
  const savedRole = localStorage.getItem('selectedRole')
  if (savedRole) {
    selectedRole.value = savedRole
  }
})
</script>

<style scoped>
/* 保留原自定义样式，适配Vue scoped */
.bg-paper {
  background-image: url('https://picsum.photos/id/106/1200/800');
  background-size: cover;
  background-blend-mode: overlay;
}
.text-shadow {
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}
.role-card-hover {
  transition: all 0.3s ease;
}
.role-card-hover:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
}
</style>