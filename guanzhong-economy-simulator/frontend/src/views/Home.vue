<template>
  <div>
    <!-- 英雄区域 -->
    <section id="home" class="relative min-h-[90vh] flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0 z-0">
        <div class="absolute inset-0 bg-gradient-to-b from-dark/80 to-dark"></div>
        <video autoplay muted loop class="object-cover w-full h-full">
          <source src="https://assets.mixkit.co/videos/preview/mixkit-rain-falling-on-the-water-of-a-pond-or-lake-2101-large.mp4" type="video/mp4">
        </video>
      </div>

      <div class="container mx-auto px-4 z-10 text-center">
        <h2 class="text-[clamp(2rem,8vw,5rem)] font-bold mb-6 text-transparent bg-clip-text bg-gradient-to-r from-accent to-primary/80 animate-pulse">
          管仲思想 · AI新解
        </h2>
        <p class="text-[clamp(1rem,3vw,1.5rem)] text-light/80 max-w-3xl mx-auto mb-10">
          穿越千年时空，与管仲进行沉浸式对话，感受春秋第一相的治国智慧与哲学思想
        </p>
        <div class="flex flex-col sm:flex-row justify-center gap-4">
          <button @click="scrollToDialogue" class="bg-accent hover:bg-accent/90 text-dark font-bold py-3 px-8 rounded-full transition-all duration-300 transform hover:scale-105 hover:shadow-lg">
            <i class="fa fa-comments-o mr-2"></i>开始对话
          </button>
          <button class="bg-transparent border-2 border-primary hover:border-accent text-light hover:text-accent font-bold py-3 px-8 rounded-full transition-all duration-300">
            <i class="fa fa-book mr-2"></i>探索思想
          </button>
        </div>

        <div class="absolute bottom-10 left-1/2 transform -translate-x-1/2 animate-bounce">
          <a href="#dialogue" class="text-light/60 hover:text-accent">
            <i class="fa fa-angle-down text-3xl"></i>
          </a>
        </div>
      </div>
    </section>

    <!-- AI对话区域 -->
    <section id="dialogue" class="py-20 bg-gradient-to-b from-dark to-dark/95">
      <div class="container mx-auto px-4">
        <h2 class="text-[clamp(1.5rem,3vw,2.5rem)] font-bold mb-10 text-center text-light">
          <span class="inline-block border-b-2 border-accent pb-2">与管仲对话</span>
        </h2>

        <div class="max-w-4xl mx-auto bg-dark/60 rounded-2xl overflow-hidden border border-primary/20 shadow-xl">
          <!-- 对话头部 -->
          <div class="bg-primary/20 p-4 flex items-center border-b border-primary/30">
            <div class="w-12 h-12 rounded-full overflow-hidden border-2 border-accent">
              <img src="https://picsum.photos/id/1005/100/100" alt="管仲AI数字人形象" class="w-full h-full object-cover">
            </div>
            <div class="ml-4">
              <h3 class="font-bold text-light">管仲 · AI数字人</h3>
              <p class="text-sm text-light/60">正在线，思考中...</p>
            </div>
            <div class="ml-auto flex space-x-3">
              <button class="text-light/60 hover:text-accent transition-colors">
                <i class="fa fa-microphone"></i>
              </button>
              <button class="text-light/60 hover:text-accent transition-colors">
                <i class="fa fa-expand"></i>
              </button>
              <button class="text-light/60 hover:text-accent transition-colors">
                <i class="fa fa-cog"></i>
              </button>
            </div>
          </div>

          <!-- 对话内容 -->
          <div ref="chatContainer" class="h-[500px] overflow-y-auto scrollbar-hide p-6 space-y-6">
            <!-- 管仲消息 -->
            <div class="flex items-start">
              <div class="w-10 h-10 rounded-full overflow-hidden mr-3 flex-shrink-0">
                <img src="https://picsum.photos/id/1005/100/100" alt="管仲AI数字人形象" class="w-full h-full object-cover">
              </div>
              <div class="bg-primary/20 text-light p-4 rounded-lg rounded-tl-none max-w-[80%]">
                <p class="text-sm text-accent/80 mb-1">管仲 · AI</p>
                <p class="leading-relaxed">
                  吾乃管仲，承蒙召见。今日愿与尔探讨治国之道、经济之策，或论及人性、礼法，尔欲闻哪般？
                </p>
                <div class="flex justify-end mt-2">
                  <span class="text-xs text-light/40">10:01</span>
                </div>
              </div>
            </div>

            <!-- 用户消息 -->
            <div class="flex items-start justify-end">
              <div class="bg-secondary/20 text-light p-4 rounded-lg rounded-tr-none max-w-[80%]">
                <p class="text-sm text-accent/80 mb-1">阁下</p>
                <p class="leading-relaxed">
                  久仰仲父大名！今日请教，在当今时代，您认为什么是治国的首要任务？
                </p>
                <div class="flex justify-end mt-2">
                  <span class="text-xs text-light/40">10:02</span>
                </div>
              </div>
              <div class="w-10 h-10 rounded-full overflow-hidden ml-3 flex-shrink-0">
                <img src="https://picsum.photos/id/1027/100/100" alt="用户头像" class="w-full h-full object-cover">
              </div>
            </div>

            <!-- 管仲消息 -->
            <div class="flex items-start">
              <div class="w-10 h-10 rounded-full overflow-hidden mr-3 flex-shrink-0">
                <img src="https://picsum.photos/id/1005/100/100" alt="管仲AI数字人形象" class="w-full h-full object-cover">
              </div>
              <div class="bg-primary/20 text-light p-4 rounded-lg rounded-tl-none max-w-[80%]">
                <p class="text-sm text-accent/80 mb-1">管仲 · AI</p>
                <p class="leading-relaxed">
                  治国之要，首在富民。"仓廪实而知礼节，衣食足而知荣辱"。民富，则易治；民贫，则难治。故善为国者，必先富民，然后治之。
                </p>
                <div class="flex mt-3 space-x-2">
                  <button class="text-xs bg-accent/20 hover:bg-accent/30 text-accent px-3 py-1 rounded-full transition-colors">
                    相地而衰征
                  </button>
                  <button class="text-xs bg-accent/20 hover:bg-accent/30 text-accent px-3 py-1 rounded-full transition-colors">
                    轻重九府
                  </button>
                  <button class="text-xs bg-accent/20 hover:bg-accent/30 text-accent px-3 py-1 rounded-full transition-colors">
                    四民分业
                  </button>
                </div>
                <div class="flex justify-end mt-2">
                  <span class="text-xs text-light/40">10:05</span>
                </div>
              </div>
            </div>

            <!-- 正在输入 -->
            <div v-if="isTyping" class="flex items-start">
              <div class="w-10 h-10 rounded-full overflow-hidden mr-3 flex-shrink-0">
                <img src="https://picsum.photos/id/1005/100/100" alt="管仲AI数字人形象" class="w-full h-full object-cover">
              </div>
              <div class="bg-primary/10 text-light p-4 rounded-lg rounded-tl-none">
                <div class="flex space-x-1">
                  <div class="w-2 h-2 bg-accent rounded-full animate-bounce"></div>
                  <div class="w-2 h-2 bg-accent rounded-full animate-bounce" style="animation-delay: 0.2s"></div>
                  <div class="w-2 h-2 bg-accent rounded-full animate-bounce" style="animation-delay: 0.4s"></div>
                </div>
              </div>
            </div>

            <!-- 动态生成的消息 -->
            <div v-for="(msg, index) in chatMessages" :key="index" :class="msg.type === 'ai' ? 'flex items-start' : 'flex items-start justify-end'">
              <template v-if="msg.type === 'ai'">
                <div class="w-10 h-10 rounded-full overflow-hidden mr-3 flex-shrink-0">
                  <img src="https://picsum.photos/id/1005/100/100" alt="管仲AI数字人形象" class="w-full h-full object-cover">
                </div>
                <div class="bg-primary/20 text-light p-4 rounded-lg rounded-tl-none max-w-[80%]">
                  <p class="text-sm text-accent/80 mb-1">管仲 · AI</p>
                  <p class="leading-relaxed">{{ msg.content }}</p>
                  <div class="flex justify-end mt-2">
                    <span class="text-xs text-light/40">{{ msg.time }}</span>
                  </div>
                </div>
              </template>
              <template v-else>
                <div class="bg-secondary/20 text-light p-4 rounded-lg rounded-tr-none max-w-[80%]">
                  <p class="text-sm text-accent/80 mb-1">阁下</p>
                  <p class="leading-relaxed">{{ msg.content }}</p>
                  <div class="flex justify-end mt-2">
                    <span class="text-xs text-light/40">{{ msg.time }}</span>
                  </div>
                </div>
                <div class="w-10 h-10 rounded-full overflow-hidden ml-3 flex-shrink-0">
                  <img src="https://picsum.photos/id/1027/100/100" alt="用户头像" class="w-full h-full object-cover">
                </div>
              </template>
            </div>
          </div>

          <!-- 输入区域 -->
          <div class="p-4 border-t border-primary/30">
            <div class="relative">
              <input 
                v-model="userInput"
                type="text" 
                placeholder="请输入您的问题..." 
                class="w-full bg-dark/80 border border-primary/30 rounded-full py-3 px-5 pr-14 text-light focus:outline-none focus:border-accent transition-colors"
                @keyup.enter="sendMessage"
              >
              <button @click="sendMessage" class="absolute right-2 top-1/2 transform -translate-y-1/2 bg-accent hover:bg-accent/90 text-dark w-10 h-10 rounded-full flex items-center justify-center transition-colors">
                <i class="fa fa-paper-plane"></i>
              </button>
            </div>
            <div class="flex justify-between mt-3 text-xs text-light/40">
              <div>
                <span class="mr-3"><i class="fa fa-keyboard-o mr-1"></i> 文字输入</span>
                <span><i class="fa fa-microphone mr-1"></i> 语音输入</span>
              </div>
              <div>
                <button class="hover:text-accent transition-colors"><i class="fa fa-history mr-1"></i> 历史对话</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 管仲思想区域 -->
    <section id="knowledge" class="py-20 bg-ancient-paper relative">
      <div class="absolute inset-0 bg-dark/80"></div>
      <div class="container mx-auto px-4 relative z-10">
        <h2 class="text-[clamp(1.5rem,3vw,2.5rem)] font-bold mb-10 text-center text-light">
          <span class="inline-block border-b-2 border-accent pb-2">管仲思想体系</span>
        </h2>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- 思想卡片1 -->
          <div class="bg-dark/70 backdrop-blur-sm rounded-xl overflow-hidden border border-primary/20 hover:border-accent/50 transition-all duration-300 transform hover:-translate-y-2 hover:shadow-xl">
            <div class="h-48 overflow-hidden">
              <img src="https://picsum.photos/id/1015/600/400" alt="管仲经济思想" class="w-full h-full object-cover">
            </div>
            <div class="p-6">
              <div class="flex justify-between items-start mb-4">
                <h3 class="text-xl font-bold text-light">经济思想</h3>
                <span class="bg-accent/20 text-accent text-xs px-3 py-1 rounded-full">核心</span>
              </div>
              <p class="text-light/80 mb-4">
                管仲提出"仓廪实而知礼节，衣食足而知荣辱"，主张通过发展经济来稳定社会秩序，其"轻重九府"理论堪称古代宏观经济调控的典范。
              </p>
              <div class="flex flex-wrap gap-2 mb-4">
                <span class="bg-primary/30 text-xs px-3 py-1 rounded-full">相地而衰征</span>
                <span class="bg-primary/30 text-xs px-3 py-1 rounded-full">官山海</span>
                <span class="bg-primary/30 text-xs px-3 py-1 rounded-full">轻重理论</span>
              </div>
              <button class="w-full bg-accent/20 hover:bg-accent/30 text-accent py-2 rounded-lg transition-colors">
                深入了解
              </button>
            </div>
          </div>

          <!-- 思想卡片2 -->
          <div class="bg-dark/70 backdrop-blur-sm rounded-xl overflow-hidden border border-primary/20 hover:border-accent/50 transition-all duration-300 transform hover:-translate-y-2 hover:shadow-xl">
            <div class="h-48 overflow-hidden">
              <img src="https://picsum.photos/id/1016/600/400" alt="管仲政治思想" class="w-full h-full object-cover">
            </div>
            <div class="p-6">
              <div class="flex justify-between items-start mb-4">
                <h3 class="text-xl font-bold text-light">政治思想</h3>
                <span class="bg-primary/20 text-primary text-xs px-3 py-1 rounded-full">基础</span>
              </div>
              <p class="text-light/80 mb-4">
                管仲主张"以人为本"，提出"政之所兴，在顺民心；政之所废，在逆民心"，并创立了"三国五鄙"的行政区划和选拔人才的"三选制"。
              </p>
              <div class="flex flex-wrap gap-2 mb-4">
                <span class="bg-primary/30 text-xs px-3 py-1 rounded-full">三国五鄙</span>
                <span class="bg-primary/30 text-xs px-3 py-1 rounded-full">三选制</span>
                <span class="bg-primary/30 text-xs px-3 py-1 rounded-full">四维思想</span>
              </div>
              <button class="w-full bg-accent/20 hover:bg-accent/30 text-accent py-2 rounded-lg transition-colors">
                深入了解
              </button>
            </div>
          </div>

          <!-- 思想卡片3 -->
          <div class="bg-dark/70 backdrop-blur-sm rounded-xl overflow-hidden border border-primary/20 hover:border-accent/50 transition-all duration-300 transform hover:-translate-y-2 hover:shadow-xl">
            <div class="h-48 overflow-hidden">
              <img src="https://picsum.photos/id/1019/600/400" alt="管仲军事思想" class="w-full h-full object-cover">
            </div>
            <div class="p-6">
              <div class="flex justify-between items-start mb-4">
                <h3 class="text-xl font-bold text-light">军事思想</h3>
                <span class="bg-primary/20 text-primary text-xs px-3 py-1 rounded-full">特色</span>
              </div>
              <p class="text-light/80 mb-4">
                管仲提出"作内政而寄军令"，主张寓兵于农，兵民合一，实现了军事与行政的一体化管理，为齐国的霸业奠定了坚实基础。
              </p>
              <div class="flex flex-wrap gap-2 mb-4">
                <span class="bg-primary/30 text-xs px-3 py-1 rounded-full">作内政</span>
                <span class="bg-primary/30 text-xs px-3 py-1 rounded-full">寄军令</span>
                <span class="bg-primary/30 text-xs px-3 py-1 rounded-full">轻税足甲</span>
              </div>
              <button class="w-full bg-accent/20 hover:bg-accent/30 text-accent py-2 rounded-lg transition-colors">
                深入了解
              </button>
            </div>
          </div>
        </div>

        <!-- 思想图谱 -->
        <div class="mt-16 bg-dark/70 backdrop-blur-sm rounded-xl p-6 border border-primary/20">
          <h3 class="text-xl font-bold text-light mb-6 text-center">管仲思想知识图谱</h3>
          <div class="h-[400px] relative">
            <canvas ref="knowledgeGraph" id="knowledgeGraph"></canvas>
          </div>
        </div>
      </div>
    </section>

    <!-- 历史场景区域 -->
    <section id="scenarios" class="py-20 bg-dark">
      <div class="container mx-auto px-4">
        <h2 class="text-[clamp(1.5rem,3vw,2.5rem)] font-bold mb-10 text-center text-light">
          <span class="inline-block border-b-2 border-accent pb-2">历史场景模拟</span>
        </h2>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <!-- 场景卡片1 -->
          <div class="group relative h-[400px] rounded-xl overflow-hidden cursor-pointer">
            <img src="https://picsum.photos/id/1028/800/600" alt="九合诸侯场景" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
            <div class="absolute inset-0 bg-gradient-to-t from-dark/90 to-transparent"></div>
            <div class="absolute bottom-0 left-0 p-6 w-full">
              <h3 class="text-2xl font-bold text-light mb-2">九合诸侯</h3>
              <p class="text-light/80 mb-4">
                体验管仲辅佐齐桓公"九合诸侯，一匡天下"的历史场景，感受春秋第一相的外交智慧。
              </p>
              <div class="flex items-center justify-between">
                <span class="text-accent flex items-center">
                  <i class="fa fa-users mr-2"></i>多人互动
                </span>
                <button class="bg-accent/20 hover:bg-accent/30 text-accent px-4 py-2 rounded-lg transition-colors">
                  进入场景
                </button>
              </div>
            </div>
          </div>

          <!-- 场景卡片2 -->
          <div class="group relative h-[400px] rounded-xl overflow-hidden cursor-pointer">
            <img src="https://picsum.photos/id/1029/800/600" alt="相地而衰征场景" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
            <div class="absolute inset-0 bg-gradient-to-t from-dark/90 to-transparent"></div>
            <div class="absolute bottom-0 left-0 p-6 w-full">
              <h3 class="text-2xl font-bold text-light mb-2">相地而衰征</h3>
              <p class="text-light/80 mb-4">
                模拟管仲实施"相地而衰征"的土地改革政策，体验如何根据土地优劣征收赋税。
              </p>
              <div class="flex items-center justify-between">
                <span class="text-accent flex items-center">
                  <i class="fa fa-line-chart mr-2"></i>政策模拟
                </span>
                <button class="bg-accent/20 hover:bg-accent/30 text-accent px-4 py-2 rounded-lg transition-colors">
                  进入场景
                </button>
              </div>
            </div>
          </div>

          <!-- 场景卡片3 -->
          <div class="group relative h-[400px] rounded-xl overflow-hidden cursor-pointer">
            <img src="https://picsum.photos/id/1039/800/600" alt="管仲与鲍叔牙场景" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
            <div class="absolute inset-0 bg-gradient-to-t from-dark/90 to-transparent"></div>
            <div class="absolute bottom-0 left-0 p-6 w-full">
              <h3 class="text-2xl font-bold text-light mb-2">管鲍之交</h3>
              <p class="text-light/80 mb-4">
                重现管仲与鲍叔牙的深厚友谊，体验"生我者父母，知我者鲍子也"的千古佳话。
              </p>
              <div class="flex items-center justify-between">
                <span class="text-accent flex items-center">
                  <i class="fa fa-heart mr-2"></i>情感体验
                </span>
                <button class="bg-accent/20 hover:bg-accent/30 text-accent px-4 py-2 rounded-lg transition-colors">
                  进入场景
                </button>
              </div>
            </div>
          </div>

          <!-- 场景卡片4 -->
          <div class="group relative h-[400px] rounded-xl overflow-hidden cursor-pointer">
            <img src="https://picsum.photos/id/1040/800/600" alt="管仲论政场景" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
            <div class="absolute inset-0 bg-gradient-to-t from-dark/90 to-transparent"></div>
            <div class="absolute bottom-0 left-0 p-6 w-full">
              <h3 class="text-2xl font-bold text-light mb-2">管仲论政</h3>
              <p class="text-light/80 mb-4">
                参与管仲与齐桓公的治国讨论，体验如何运用"礼、义、廉、耻"四维思想治理国家。
              </p>
              <div class="flex items-center justify-between">
                <span class="text-accent flex items-center">
                  <i class="fa fa-comments-o mr-2"></i>思想辩论
                </span>
                <button class="bg-accent/20 hover:bg-accent/30 text-accent px-4 py-2 rounded-lg transition-colors">
                  进入场景
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 关于项目 -->
    <section id="about" class="py-20 bg-gradient-to-b from-dark/95 to-dark">
      <div class="container mx-auto px-4">
        <h2 class="text-[clamp(1.5rem,3vw,2.5rem)] font-bold mb-10 text-center text-light">
          <span class="inline-block border-b-2 border-accent pb-2">关于本项目</span>
        </h2>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
          <div>
            <h3 class="text-2xl font-bold text-light mb-6">项目背景与目标</h3>
            <p class="text-light/80 mb-6 leading-relaxed">
              "智管春秋：AI对话管仲体验平台"是一个融合管仲思想与现代AI技术的沉浸式互动项目。我们旨在通过前沿的人工智能技术，重新解读和传播春秋时期齐国名相管仲的治国思想与哲学理念。
            </p>
            <p class="text-light/80 mb-6 leading-relaxed">
              项目采用豆包大模型作为基础，结合管仲思想知识图谱，构建了具有深度和专业性的管仲AI数字人，使用户能够与之进行跨越千年的对话。
            </p>
            <div class="flex flex-wrap gap-4 mt-8">
              <div class="bg-primary/10 p-4 rounded-lg">
                <div class="text-accent text-3xl font-bold mb-1">100+</div>
                <div class="text-light/70">管仲思想核心观点</div>
              </div>
              <div class="bg-primary/10 p-4 rounded-lg">
                <div class="text-accent text-3xl font-bold mb-1">20+</div>
                <div class="text-light/70">历史场景模拟</div>
              </div>
              <div class="bg-primary/10 p-4 rounded-lg">
                <div class="text-accent text-3xl font-bold mb-1">50k+</div>
                <div class="text-light/70">知识库条目</div>
              </div>
            </div>
          </div>

          <div class="bg-dark/60 rounded-xl overflow-hidden border border-primary/20 shadow-xl p-6">
            <h3 class="text-xl font-bold text-light mb-6">技术架构</h3>
            <div class="space-y-6">
              <div>
                <div class="flex justify-between items-center mb-2">
                  <span class="text-light/80">AI对话引擎</span>
                  <span class="text-accent">95%</span>
                </div>
                <div class="w-full bg-primary/20 rounded-full h-2">
                  <div class="bg-accent h-2 rounded-full" style="width: 95%"></div>
                </div>
              </div>

              <div>
                <div class="flex justify-between items-center mb-2">
                  <span class="text-light/80">知识图谱构建</span>
                  <span class="text-accent">90%</span>
                </div>
                <div class="w-full bg-primary/20 rounded-full h-2">
                  <div class="bg-accent h-2 rounded-full" style="width: 90%"></div>
                </div>
              </div>

              <div>
                <div class="flex justify-between items-center mb-2">
                  <span class="text-light/80">沉浸式交互设计</span>
                  <span class="text-accent">85%</span>
                </div>
                <div class="w-full bg-primary/20 rounded-full h-2">
                  <div class="bg-accent h-2 rounded-full" style="width: 85%"></div>
                </div>
              </div>

              <div>
                <div class="flex justify-between items-center mb-2">
                  <span class="text-light/80">历史场景还原</span>
                  <span class="text-accent">80%</span>
                </div>
                <div class="w-full bg-primary/20 rounded-full h-2">
                  <div class="bg-accent h-2 rounded-full" style="width: 80%"></div>
                </div>
              </div>

              <div>
                <div class="flex justify-between items-center mb-2">
                  <span class="text-light/80">多模态交互</span>
                  <span class="text-accent">75%</span>
                </div>
                <div class="w-full bg-primary/20 rounded-full h-2">
                  <div class="bg-accent h-2 rounded-full" style="width: 75%"></div>
                </div>
              </div>
            </div>

            <div class="mt-8">
              <h4 class="text-lg font-bold text-light mb-4">技术栈</h4>
              <div class="flex flex-wrap gap-3">
                <span class="bg-primary/30 text-light px-4 py-2 rounded-full text-sm">豆包大模型</span>
                <span class="bg-primary/30 text-light px-4 py-2 rounded-full text-sm">知识图谱</span>
                <span class="bg-primary/30 text-light px-4 py-2 rounded-full text-sm">Vue 3</span>
                <span class="bg-primary/30 text-light px-4 py-2 rounded-full text-sm">Tailwind CSS</span>
                <span class="bg-primary/30 text-light px-4 py-2 rounded-full text-sm">Flask</span>
                <span class="bg-primary/30 text-light px-4 py-2 rounded-full text-sm">WebGL</span>
                <span class="bg-primary/30 text-light px-4 py-2 rounded-full text-sm">Three.js</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Chart from 'chart.js/auto'

// 响应式数据
const userInput = ref('')
const chatMessages = ref([])
const isTyping = ref(false)
const chatContainer = ref(null)
const knowledgeGraph = ref(null)
let currentDialogueId = null

// 滚动到对话区域
const scrollToDialogue = () => {
  document.getElementById('dialogue').scrollIntoView({ behavior: 'smooth' })
}

// API客户端类（完全迁移目标HTML的逻辑）
class DoubaoAPIClient {
  constructor() {
    // 自动检测运行环境
    this.baseUrl = this.getApiBaseUrl();
    console.log('API基础URL:', this.baseUrl);
  }

  getApiBaseUrl() {
    const { hostname, port } = window.location;

    // LiveServer环境 (5500端口)
    if (port === '5500') {
      return 'http://localhost:5000';
    }
    // 生产环境 (同源)
    else if (hostname === 'localhost' || hostname === '127.0.0.1') {
      return 'http://localhost:5000';
    }
    // 其他环境
    else {
      return '/api'; // 相对路径
    }
  }

  getHeaders() {
    const headers = {
      'Content-Type': 'application/json'
    };

    const token = localStorage.getItem('access_token');
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    return headers;
  }

  // 聊天接口
  async chatWithGuanZhong(message, dialogueId = null) {
    try {
      // 尝试POST方法
      let response = await fetch(`${this.baseUrl}/api/doubao/chat`, {
        method: 'POST',
        headers: this.getHeaders(),
        body: JSON.stringify({
          message: message,
          dialogue_id: dialogueId
        })
      });

      // 如果POST失败，尝试GET方法
      if (response.status === 405) {
        console.log('POST方法不被允许，尝试GET方法');
        const params = new URLSearchParams({
          message: message,
          dialogue_id: dialogueId || ''
        });

        response = await fetch(`${this.baseUrl}/api/doubao/chat?${params}`, {
          method: 'GET',
          headers: this.getHeaders()
        });
      }

      if (!response.ok) {
        throw new Error(`请求失败: ${response.status} ${response.statusText}`);
      }

      const data = await response.json();
      return {
        success: true,
        data: {
          ai_reply: data.ai_reply || data.reply,
          dialogue_id: data.dialogue_id
        }
      };

    } catch (error) {
      console.error('API调用错误:', error);
      return this.getFallbackResponse(message, error.message);
    }
  }

  // 降级响应
  getFallbackResponse(message, error) {
    const fallbackReplies = [
      "仓廪实而知礼节，衣食足而知荣辱。君之所问，实乃治国之根本也。",
      "夫民，别而听之则愚，合而听之则圣。君之问，当合天下之智而答之。",
      "政之所兴，在顺民心；政之所废，在逆民心。君之所思，正合此道。",
      "善为国者，必先富民，然后治之。此乃吾一生之悟也。"
    ];
    const randomReply = fallbackReplies[Math.floor(Math.random() * fallbackReplies.length)];
    
    return {
      success: false,
      error: error,
      data: {
        ai_reply: `${randomReply}（注：AI服务暂时不可用，此为离线回复）`,
        dialogue_id: Date.now().toString()
      }
    };
  }
}

// 初始化API客户端
const apiClient = new DoubaoAPIClient()

// 发送消息
const sendMessage = async () => {
  const message = userInput.value.trim()
  if (!message) return

  // 添加用户消息
  const now = new Date()
  const timeStr = `${now.getHours()}:${now.getMinutes().toString().padStart(2, '0')}`
  chatMessages.value.push({
    type: 'user',
    content: message,
    time: timeStr
  })
  
  // 清空输入框
  userInput.value = ''
  
  // 滚动到底部
  chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  
  // 显示正在输入
  isTyping.value = true
  
  try {
    // 调用API
    const result = await apiClient.chatWithGuanZhong(message, currentDialogueId)
    
    // 更新对话ID
    if (result.data.dialogue_id) {
      currentDialogueId = result.data.dialogue_id
    }
    
    // 添加AI回复
    const aiTimeStr = `${new Date().getHours()}:${new Date().getMinutes().toString().padStart(2, '0')}`
    chatMessages.value.push({
      type: 'ai',
      content: result.data.ai_reply,
      time: aiTimeStr
    })
    
  } catch (error) {
    // 错误处理
    chatMessages.value.push({
      type: 'ai',
      content: `抱歉，暂时无法回答您的问题：${error.message}`,
      time: timeStr
    })
  } finally {
    // 隐藏正在输入
    isTyping.value = false
    // 滚动到底部
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  }
}

// 初始化知识图谱
const initKnowledgeGraph = () => {
  if (knowledgeGraph.value) {
    const ctx = knowledgeGraph.value.getContext('2d')
    new Chart(ctx, {
      type: 'radar',
      data: {
        labels: ['经济思想', '政治思想', '军事思想', '外交策略', '伦理观'],
        datasets: [{
          label: '管仲思想体系',
          data: [90, 85, 80, 95, 75],
          backgroundColor: 'rgba(212, 175, 55, 0.2)',
          borderColor: 'rgba(212, 175, 55, 1)',
          borderWidth: 2
        }]
      },
      options: {
        scales: {
          r: {
            angleLines: {
              color: 'rgba(255, 255, 255, 0.1)'
            },
            grid: {
              color: 'rgba(255, 255, 255, 0.1)'
            },
            pointLabels: {
              color: '#F7FAFC'
            },
            ticks: {
              color: 'rgba(255, 255, 255, 0.7)',
              backdropColor: 'transparent'
            }
          }
        },
        plugins: {
          legend: {
            labels: {
              color: '#F7FAFC'
            }
          }
        }
      }
    })
  }
}

// 组件挂载后初始化
onMounted(() => {
  // 初始化知识图谱
  initKnowledgeGraph()
  
  // 欢迎消息
  setTimeout(() => {
    chatMessages.value.push({
      type: 'ai',
      content: "善哉！君来问政于管仲，实乃苍生之幸也。有何治国之道，富民之策，尽管道来，管仲当以平生所学为君解惑。",
      time: `${new Date().getHours()}:${new Date().getMinutes().toString().padStart(2, '0')}`
    })
  }, 500)
})
</script>

<style scoped>
/* 补充少量样式（Tailwind未覆盖的） */
video {
  object-fit: cover;
}
</style>