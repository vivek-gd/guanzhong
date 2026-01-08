<template>
  <div class="relative bg-gray-900 text-white">
    <video autoplay muted loop class="w-full h-screen object-cover opacity-50">
      <source src="@/assets/videos/hero-background.mp4" type="video/mp4">
    </video>
    <div class="absolute inset-0 flex items-center justify-center">
      <div class="text-center">
        <h1 class="text-5xl font-bold mb-4">探索管仲的经济智慧</h1>
        <p class="text-xl mb-8">与 AI 管仲对话，体验古代经济思想在现代的应用</p>
        <button class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-6 rounded-lg">开始对话</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HeroSection',
};
</script>

<style scoped>
/* Add any scoped styles here if needed */
</style>