import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  root: path.resolve(__dirname, './'), // 强制根目录
  base: './', // 相对路径构建
  plugins: [vue()],
  server: {
    host: '0.0.0.0',
    port: 5173,
    cors: true,
    open: true,
    // 添加 API 代理配置
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        rewrite: (path) => path
      }
    }
  },
  // 新增build配置，明确入口和输出
  
  build: {
    outDir: 'dist',
    emptyOutDir: true
    // 移除rollupOptions.input配置
  },
  
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@assets': path.resolve(__dirname, './src/assets')
    }
  }
})