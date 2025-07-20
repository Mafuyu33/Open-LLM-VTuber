# 快速部署最佳中文TTS

## 方案1：Bert-VITS2（最简单）

### 下载地址
- 整合包：https://github.com/YYuX-1145/Bert-VITS2-Integration-Package
- 包含预训练模型和多个角色音色

### 配置Open-LLM-VTuber
```yaml
tts_config:
  tts_model: 'x_tts'
  x_tts:
    api_url: 'http://127.0.0.1:5000/tts'  # Bert-VITS2的API地址
    speaker_wav: 'male'  # 选择男声
    language: 'zh'
```

## 方案2：GPT-SoVITS（效果最好）

### 整合包下载
- B站UP主整合包：搜索"GPT-SoVITS整合包"
- 包含模型和一键启动

### 录制参考音频
1. 录制3-10秒的男声音频
2. 内容："你好，我是晓风，很高兴认识大家。今天天气真不错。"
3. 保存为 reference.wav

### 配置
```yaml
tts_config:
  tts_model: 'gpt_sovits_tts'
  gpt_sovits_tts:
    api_url: 'http://127.0.0.1:9880/tts'
    ref_audio_path: './reference.wav'
    prompt_text: '你好，我是晓风'
```

## 方案3：使用现成的VITS模型

### 下载中文男声模型
- https://huggingface.co/spaces/zomehwh/vits-models/tree/main
- 选择中文男声模型下载

### 通过Sherpa-ONNX使用
已集成在项目中，配置即可使用