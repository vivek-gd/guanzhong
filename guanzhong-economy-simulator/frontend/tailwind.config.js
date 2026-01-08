/** @type {import('tailwindcss').Config} */
export default {
  // 关键：指定要扫描的文件，让Tailwind生效
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#3B6E51',     // 春秋时期青铜色
        secondary: '#8C7851',   // 古代竹简色
        accent: '#D4AF37',      // 金色点缀
        dark: '#1A202C',        // 深色背景
        light: '#F7FAFC',       // 浅色背景
      },
      fontFamily: {
        sans: ['Noto Sans SC', 'sans-serif'],
        serif: ['SimSun', 'serif'],
      },
    },
  },
  plugins: [
    // 自定义工具类（对应目标HTML的@layer utilities）
    function ({ addUtilities }) {
      addUtilities({
        '.content-auto': {
          'content-visibility': 'auto',
        },
        '.scrollbar-hide': {
          '-ms-overflow-style': 'none',
          'scrollbar-width': 'none',
          '&::-webkit-scrollbar': {
            display: 'none',
          },
        },
        '.text-shadow': {
          'text-shadow': '0 2px 4px rgba(0,0,0,0.1)',
        },
        '.bg-ancient-paper': {
          'background-image': 'url("https://picsum.photos/id/106/1200/800")',
          'background-size': 'cover',
          'background-position': 'center',
        },
        '.animate-float': {
          'animation': 'float 6s ease-in-out infinite',
        },
        '@keyframes float': {
          '0%': { 'transform': 'translateY(0px)' },
          '50%': { 'transform': 'translateY(-15px)' },
          '100%': { 'transform': 'translateY(0px)' },
        },
      })
    }
  ],
}