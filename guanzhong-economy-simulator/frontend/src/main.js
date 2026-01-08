import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
// 引入Tailwind样式
import './assets/tailwind.css'
// // 引入Font Awesome样式
// import '@fortawesome/font-awesome-free/css/all.min.css'

// 创建应用实例
const app = createApp(App)

// 安装Pinia状态管理
const pinia = createPinia()
app.use(pinia)

// 安装路由
app.use(router)

// 全局配置（可选）
app.config.globalProperties.$filters = {
  formatCurrency(value) {
    return new Intl.NumberFormat('zh-CN', {
      style: 'currency',
      currency: 'CNY'
    }).format(value)
  }
}

// 挂载应用
app.mount('#app')

// 开发环境日志
if (import.meta.env.DEV) {
  console.log('🚀 管仲经济模拟器已启动')
  console.log('📊 Vue版本:', app.version)
  console.log('🌐 环境:', import.meta.env.MODE)
}