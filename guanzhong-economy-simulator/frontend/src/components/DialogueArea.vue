<template>
  <div class="container mx-auto px-6 py-12">
    <div class="bg-white rounded-lg shadow-lg p-6">
      <h2 class="text-2xl font-bold mb-4">与管仲 AI 对话</h2>
      <div class="mb-4 h-64 overflow-y-auto border border-gray-200 rounded-lg p-4">
        <!-- Messages will be rendered here -->
      </div>
      <div class="flex">
        <input type="text" class="flex-grow border border-gray-300 rounded-l-lg p-2" placeholder="输入你的问题...">
        <button class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-r-lg">发送</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DialogueArea',
};
</script>

<style scoped>
/* Add any scoped styles here if needed */
</style>