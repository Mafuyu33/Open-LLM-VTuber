# GPT-SoVITS 设置指南

## 1. 安装GPT-SoVITS
```bash
# 克隆项目
git clone https://github.com/RVC-Boss/GPT-SoVITS.git
cd GPT-SoVITS

# 安装依赖
pip install -r requirements.txt
```

## 2. 下载预训练模型
- 访问 https://github.com/RVC-Boss/GPT-SoVITS/releases
- 下载预训练模型

## 3. 准备参考音频
- 录制3-10秒的目标声音
- 保存为wav格式

## 4. 在Open-LLM-VTuber中配置
```yaml
tts_config:
  tts_model: 'gpt_sovits_tts'
  gpt_sovits_tts:
    api_url: 'http://127.0.0.1:9880/tts'
    ref_audio_path: '/path/to/your/reference.wav'
    prompt_text: '这是一段参考文本'
```

这样可以实现类似Neuro-sama的独特音色。