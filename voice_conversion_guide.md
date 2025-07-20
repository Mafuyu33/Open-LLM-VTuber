# 音色转换指南 - 制作中性AI声音

## 方案1：RVC-WebUI（最简单）
1. 下载RVC整合包：https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI
2. 录制您的声音（正常说话）
3. 选择目标音色模型（中性声音）
4. 转换后作为GPT-SoVITS的参考音频

## 方案2：使用音频编辑软件
### Audacity（免费）：
- 音调变换：效果 → 改变音调 → 降低2-4个半音
- 共振峰移位：让声音更中性
- 均衡器：调整频率特征

### Adobe Audition（专业）：
- 音调转换器：更精确的控制
- 声音变形效果

## 方案3：在线工具
- https://voicechanger.io/
- https://www.voicemod.net/

## 推荐参数（制作中性声音）：
- 音调：降低2-3个半音
- 共振峰：略微降低
- 混响：添加少量房间混响
- EQ：减少高频，略增中低频

## GPT-SoVITS使用流程：
1. 录制原始音频："大家好，我是晓风，一个AI虚拟主播。"
2. 使用上述方法转换音色
3. 保存为 reference.wav
4. 在GPT-SoVITS中使用转换后的音频