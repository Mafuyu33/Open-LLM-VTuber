# 声音二次处理详细教程

## 使用Audacity（免费开源）

### 1. 下载安装
- 官网：https://www.audacityteam.org/
- 选择Windows版本下载

### 2. 基础处理流程

#### 第一步：降噪
1. 选择一段纯噪音部分（1-2秒）
2. 效果 → 降噪 → 获取噪声配置
3. 选择全部音频 → 效果 → 降噪 → 确定

#### 第二步：音调调整（关键）
1. 选择全部音频
2. 效果 → 改变音高
3. 参数设置：
   - 半音：-2 到 -3（降低让声音更中性）
   - 百分比变化：会自动计算
   - 勾选"使用高质量拉伸"

#### 第三步：EQ均衡器
1. 效果 → 均衡器
2. 调整建议：
   - 200-400Hz：降低3-5dB（减少厚重感）
   - 1000-2000Hz：提升2-3dB（增加清晰度）
   - 4000Hz以上：略微降低（减少尖锐感）

#### 第四步：压缩器（让声音更稳定）
1. 效果 → 压缩器
2. 参数：
   - 阈值：-15dB
   - 比率：3:1
   - 起音时间：0.2秒
   - 释放时间：1.0秒

#### 第五步：混响（增加空间感）
1. 效果 → 混响
2. 选择预设："小房间"或"录音室"
3. 混响量：10-20%（不要太多）

### 3. 导出设置
- 文件 → 导出 → 导出音频
- 格式：WAV
- 采样率：16000Hz或48000Hz
- 位深度：16-bit

## 快速处理脚本（使用FFmpeg）

```bash
# 基础处理命令
ffmpeg -i input.wav -af "highpass=f=100,lowpass=f=8000,volume=1.5,asetrate=44100*0.95,atempo=1.05" output.wav

# 更复杂的处理（包含音调变化）
ffmpeg -i input.wav -af "asetrate=44100*0.92,atempo=1.087,equalizer=f=300:t=h:w=200:g=-3,equalizer=f=1500:t=h:w=200:g=2" output.wav
```

## 实时预览建议

在Audacity中处理时：
1. 先录一小段测试（10秒）
2. 应用各种效果
3. 反复调整参数直到满意
4. 再录制完整的30秒reference

## 注意事项

- 处理后音频时长会略微改变，确保还是30秒左右
- 保持音量适中，不要过载（看波形不要触顶）
- 每步处理后都试听效果
- 保存项目文件，方便后续调整