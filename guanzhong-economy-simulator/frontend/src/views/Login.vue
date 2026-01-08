<template>
  <div class="min-h-screen flex items-center justify-center bg-paper bg-primary/20 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8 bg-secondary/80 p-8 rounded-lg border-2 border-accent shadow-lg">
      <!-- 登录标题 -->
      <div class="text-center">
        <h2 class="mt-6 text-3xl font-ancient font-bold text-primary">
          春秋富国策 · 登录
        </h2>
        <p class="mt-2 text-sm text-primary/70">
          请输入账号密码进入管仲经济模拟器
        </p>
      </div>

      <!-- 登录表单 -->
      <form class="mt-8 space-y-6" @submit.prevent="handleLogin">
        <!-- 用户名输入 -->
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="username" class="sr-only">用户名</label>
            <div class="relative">
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <i class="fa fa-user text-primary/50"></i>
              </div>
              <input
                id="username"
                name="username"
                type="text"
                v-model="form.username"
                required
                class="appearance-none rounded-none relative block w-full px-10 py-3 border border-accent placeholder-primary/50 text-primary bg-secondary/30 rounded-t-lg focus:outline-none focus:ring-accent focus:border-accent sm:text-sm"
                placeholder="请输入用户名"
              />
            </div>
            <!-- 用户名错误提示 -->
            <p v-if="errors.username" class="mt-1 text-xs text-red-600 pl-10">{{ errors.username }}</p>
          </div>

          <!-- 密码输入 -->
          <div>
            <label for="password" class="sr-only">密码</label>
            <div class="relative">
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <i class="fa fa-lock text-primary/50"></i>
              </div>
              <input
                id="password"
                name="password"
                type="password"
                v-model="form.password"
                required
                class="appearance-none rounded-none relative block w-full px-10 py-3 border border-accent placeholder-primary/50 text-primary bg-secondary/30 rounded-b-lg focus:outline-none focus:ring-accent focus:border-accent sm:text-sm"
                placeholder="请输入密码"
              />
              <!-- 显示/隐藏密码 -->
              <button
                type="button"
                class="absolute inset-y-0 right-0 pr-3 flex items-center text-primary/50 hover:text-primary"
                @click="showPassword = !showPassword"
              >
                <i class="fa" :class="showPassword ? 'fa-eye-slash' : 'fa-eye'"></i>
              </button>
            </div>
            <!-- 密码错误提示 -->
            <p v-if="errors.password" class="mt-1 text-xs text-red-600 pl-10">{{ errors.password }}</p>
          </div>
        </div>

        <!-- 登录错误提示 -->
        <div v-if="loginError" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded text-sm">
          {{ loginError }}
        </div>

        <!-- 登录按钮 -->
        <div>
          <button
            type="submit"
            class="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-textColor bg-primary hover:bg-primary/80 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-accent transition-all"
            :disabled="loading"
          >
            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
              <i class="fa fa-sign-in text-textColor/50 group-hover:text-textColor"></i>
            </span>
            <span v-if="!loading">登录</span>
            <span v-if="loading" class="flex items-center">
              <i class="fa fa-spinner fa-spin mr-2"></i>登录中...
            </span>
          </button>
        </div>

        <!-- 测试账号提示 -->
        <div class="text-center text-xs text-primary/60">
          <p>测试账号：admin / 密码：123456</p>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 表单数据
const form = ref({
  username: '',
  password: ''
})

// 状态管理
const errors = ref({}) // 表单校验错误
const loginError = ref('') // 登录错误提示
const loading = ref(false) // 登录加载状态
const showPassword = ref(false) // 显示/隐藏密码

// 表单校验
const validateForm = () => {
  const newErrors = {}
  // 用户名校验
  if (!form.value.username.trim()) {
    newErrors.username = '请输入用户名'
  }
  // 密码校验
  if (!form.value.password.trim()) {
    newErrors.password = '请输入密码'
  } else if (form.value.password.length < 6) {
    newErrors.password = '密码长度不能少于6位'
  }
  errors.value = newErrors
  // 无错误返回true
  return Object.keys(newErrors).length === 0
}

// 登录处理
const handleLogin = async () => {
  if (!validateForm()) return
  loading.value = true
  loginError.value = ''

  try {
    const response = await fetch('http://127.0.0.1:5000/api/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: form.value.username,
        password: form.value.password
      })
    })

    const data = await response.json()
    if (response.ok && data.access_token) {
      // 保存Token和用户信息
      localStorage.setItem('userInfo', JSON.stringify({
        username: data.user.username,
        token: data.access_token,
        id: data.user.id
      }))
      router.push('/role-select')
    } else {
      loginError.value = data.message || '登录失败'
    }
  } catch (error) {
    loginError.value = '无法连接后端，请检查服务是否运行'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
/* 复用项目古风样式 */
.bg-paper {
  background-image: url('https://picsum.photos/id/106/1200/800');
  background-size: cover;
  background-blend-mode: overlay;
}
.font-ancient {
  font-family: 'Ma Shan Zheng', cursive;
}
.text-primary {
  color: #8B4513;
}
.bg-primary {
  background-color: #8B4513;
}
.bg-secondary {
  background-color: #D2B48C;
}
.border-accent {
  border-color: #CD853F;
}
.text-textColor {
  color: #F5F5DC;
}
</style>