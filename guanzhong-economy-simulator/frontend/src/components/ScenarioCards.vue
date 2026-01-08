<template>
  <div class="py-12">
    <div class="container mx-auto px-6">
      <h2 class="text-3xl font-bold text-center mb-8">历史场景模拟</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div class="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300">
          <img src="@/assets/images/scenario-1.jpg" alt="Scenario 1" class="w-full h-48 object-cover">
          <div class="p-6">
            <h3 class="text-xl font-semibold mb-2">齐国盐政改革</h3>
            <p class="text-gray-700">体验管仲如何通过盐政改革增加国家收入。</p>
          </div>
        </div>
        <div class="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300">
          <img src="@/assets/images/scenario-2.jpg" alt="Scenario 2" class="w-full h-48 object-cover">
          <div class="p-6">
            <h3 class="text-xl font-semibold mb-2">轻重论实践</h3>
            <p class="text-gray-700">模拟轻重论在粮食市场中的应用。</p>
          </div>
        </div>
        <div class="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300">
          <img src="@/assets/images/scenario-3.jpg" alt="Scenario 3" class="w-full h-48 object-cover">
          <div class="p-6">
            <h3 class="text-xl font-semibold mb-2">平准法实施</h3>
            <p class="text-gray-700">体验平准法如何稳定物价。</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ScenarioCards',
};
</script>

<style scoped>
/* Add any scoped styles here if needed */
</style>