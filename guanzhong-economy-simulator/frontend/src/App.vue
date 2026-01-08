<template>
  <!-- 顶部导航栏（完全匹配目标HTML） -->
  <header class="bg-dark/80 backdrop-blur-md sticky top-0 z-50 border-b border-primary/30">
    <div class="container mx-auto px-4 py-3 flex justify-between items-center">
      <div class="flex items-center space-x-2">
        <div class="w-10 h-10 rounded-full bg-primary flex items-center justify-center">
          <i class="fa fa-lightbulb-o text-accent text-xl"></i>
        </div>
        <h1 class="text-xl font-bold text-light">智管春秋</h1>
      </div>

      <nav class="hidden md:flex items-center space-x-6">
        <router-link to="#home" class="text-light hover:text-accent transition-colors duration-300">首页</router-link>
        <router-link to="#dialogue" class="text-light hover:text-accent transition-colors duration-300">AI对话</router-link>
        <router-link to="#knowledge" class="text-light hover:text-accent transition-colors duration-300">管仲思想</router-link>
        <router-link to="#scenarios" class="text-light hover:text-accent transition-colors duration-300">历史场景</router-link>
        <router-link to="#about" class="text-light hover:text-accent transition-colors duration-300">关于项目</router-link>

        <!-- 游戏入口：登录后才可点击 -->
        <router-link 
          to="/role-select" 
          class="bg-primary text-textColor px-6 py-3 rounded-lg hover:bg-primary/80 transition-all"
          :class="{ 'opacity-50 cursor-not-allowed pointer-events-none': !userInfo }"
        >
          <i class="fa fa-gamepad mr-2"></i>登录后进入管仲经济模拟器
        </router-link>
      </nav>

      <div class="flex items-center space-x-4">
        <!-- 登录/退出区域：根据登录状态切换 -->
        <template v-if="!userInfo">
          <router-link 
            to="/login" 
            class="bg-primary/20 hover:bg-primary/30 text-accent px-4 py-2 rounded-full transition-all duration-300 flex items-center"
          >
            <i class="fa fa-user-circle-o mr-2"></i>
            <span class="hidden md:inline">登录</span>
          </router-link>
        </template>
        <template v-else>
          <!-- 已登录：显示用户名 + 退出按钮 -->
          <div class="bg-primary/20 text-accent px-4 py-2 rounded-full flex items-center">
            <i class="fa fa-user mr-2"></i>
            <span class="hidden md:inline">{{ userInfo.username }}</span>
          </div>
          <button 
            @click="handleLogout"
            class="bg-red-600/80 hover:bg-red-600 text-light px-4 py-2 rounded-full transition-all duration-300 flex items-center"
          >
            <i class="fa fa-sign-out mr-2"></i>
            <span class="hidden md:inline">退出</span>
          </button>
        </template>

        <button class="md:hidden text-light">
          <i class="fa fa-bars text-xl"></i>
        </button>
      </div>
    </div>
  </header>

  <!-- 路由出口：匹配目标HTML的main区域 -->
  <main class="flex-grow">
    <router-view></router-view>
  </main>

  <!-- 页脚（完全匹配目标HTML） -->
  <footer class="bg-dark border-t border-primary/30 py-10">
    <div class="container mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <div>
          <div class="flex items-center space-x-2 mb-6">
            <div class="w-10 h-10 rounded-full bg-primary flex items-center justify-center">
              <i class="fa fa-lightbulb-o text-accent text-xl"></i>
            </div>
            <h2 class="text-xl font-bold text-light">智管春秋</h2>
          </div>
          <p class="text-light/60 mb-6">
            让管仲思想在AI时代焕发新生，感受春秋智慧的现代启示。
          </p>
          <div class="flex space-x-4">
            <a href="#" class="text-light/60 hover:text-accent transition-colors">
              <i class="fa fa-weibo"></i>
            </a>
            <a href="#" class="text-light/60 hover:text-accent transition-colors">
              <i class="fa fa-wechat"></i>
            </a>
            <a href="#" class="text-light/60 hover:text-accent transition-colors">
              <i class="fa fa-twitter"></i>
            </a>
            <a href="#" class="text-light/60 hover:text-accent transition-colors">
              <i class="fa fa-github"></i>
            </a>
          </div>
        </div>

        <div>
          <h3 class="text-lg font-bold text-light mb-6">快速链接</h3>
          <ul class="space-y-3">
            <li><a href="#home" class="text-light/60 hover:text-accent transition-colors">首页</a></li>
            <li><a href="#dialogue" class="text-light/60 hover:text-accent transition-colors">AI对话</a></li>
            <li><a href="#knowledge" class="text-light/60 hover:text-accent transition-colors">管仲思想</a></li>
            <li><a href="#scenarios" class="text-light/60 hover:text-accent transition-colors">历史场景</a></li>
            <li><a href="#about" class="text-light/60 hover:text-accent transition-colors">关于项目</a></li>
          </ul>
        </div>

        <div>
          <h3 class="text-lg font-bold text-light mb-6">管仲思想</h3>
          <ul class="space-y-3">
            <li><a href="#" class="text-light/60 hover:text-accent transition-colors">经济思想</a></li>
            <li><a href="#" class="text-light/60 hover:text-accent transition-colors">政治思想</a></li>
            <li><a href="#" class="text-light/60 hover:text-accent transition-colors">军事思想</a></li>
            <li><a href="#" class="text-light/60 hover:text-accent transition-colors">哲学思想</a></li>
            <li><a href="#" class="text-light/60 hover:text-accent transition-colors">教育思想</a></li>
          </ul>
        </div>

        <div>
          <h3 class="text-lg font-bold text-light mb-6">联系我们</h3>
          <ul class="space-y-3">
            <li class="flex items-start">
              <i class="fa fa-envelope-o text-accent mt-1 mr-3"></i>
              <span class="text-light/60">contact@zhiguanchunqiu.com</span>
            </li>
            <li class="flex items-start">
              <i class="fa fa-phone text-accent mt-1 mr-3"></i>
              <span class="text-light/60">+86 123 4567 8901</span>
            </li>
            <li class="flex items-start">
              <i class="fa fa-map-marker text-accent mt-1 mr-3"></i>
              <span class="text-light/60">北京市海淀区中关村大街1号</span>
            </li>
          </ul>
        </div>
      </div>

      <div class="border-t border-primary/20 mt-10 pt-6 flex flex-col md:flex-row justify-between items-center">
        <p class="text-light/40 text-sm mb-4 md:mb-0">
          © 2025 智管春秋 AI对话管仲体验平台. 保留所有权利.
        </p>
        <div class="flex space-x-6">
          <a href="#" class="text-light/40 hover:text-accent text-sm transition-colors">隐私政策</a>
          <a href="#" class="text-light/40 hover:text-accent text-sm transition-colors">使用条款</a>
          <a href="#" class="text-light/40 hover:text-accent text-sm transition-colors">Cookie政策</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

// 初始化路由实例
const router = useRouter()

// 响应式数据：存储用户登录信息
const userInfo = ref(null)

// 页面挂载时：读取本地存储的登录状态
onMounted(() => {
  const savedUser = localStorage.getItem('userInfo')
  if (savedUser) {
    userInfo.value = JSON.parse(savedUser)
  }
})

// 退出登录逻辑
const handleLogout = () => {
  // 1. 清除本地存储的用户信息
  localStorage.removeItem('userInfo')
  // 2. 重置登录状态
  userInfo.value = null
  // 3. 可选：跳转到首页（提升用户体验）
  router.push('/')
  // 4. 可选：提示退出成功（可根据需要添加）
  alert('已成功退出登录')
}
</script>

<style scoped>
/* 补充禁用状态的样式（确保游戏入口禁用时不可点击） */
.pointer-events-none {
  pointer-events: none;
}
</style>