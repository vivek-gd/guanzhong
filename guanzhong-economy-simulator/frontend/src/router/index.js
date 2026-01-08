import { createRouter, createWebHistory } from 'vue-router'
// 导入页面组件Home.vue（保留你原有导入路径和命名）
import Home from '../views/Home.vue'

import RoleSelect from '../views/RoleSelect.vue'
import Game from '../views/Game.vue'
import Login from '../views/Login.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home 
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
   // 新增：角色选择页
  {
    path: '/role-select',
    name: 'RoleSelect',
    component: RoleSelect
  },
  // 新增：游戏界面页
  {
    path: '/game',
    name: 'Game',
    component: Game,
    fullScreen: true
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  // ========== 新增：锚点平滑滚动配置（核心修改） ==========
  scrollBehavior(to, from, savedPosition) {
    // 1. 如果路由带锚点（如 #dialogue），平滑滚动到锚点位置
    if (to.hash) {
      return {
        el: to.hash,        // 匹配锚点元素
        behavior: 'smooth', // 平滑滚动
        top: 0              // 锚点位置偏移量（可根据需要调整）
      }
    }
    // 2. 如果是浏览器后退/前进，恢复之前的滚动位置
    else if (savedPosition) {
      return savedPosition
    }
    // 3. 其他情况默认滚动到页面顶部
    else {
      return { top: 0 }
    }
  }
})

export default router