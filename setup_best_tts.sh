#!/bin/bash
# GPT-SoVITS快速部署脚本

echo "=== 部署最佳中文TTS - GPT-SoVITS ==="

# 1. 下载GPT-SoVITS
cd /mnt/h/AI/main/
git clone https://github.com/RVC-Boss/GPT-SoVITS.git
cd GPT-SoVITS

# 2. 下载预训练模型
echo "请手动下载以下模型："
echo "1. 访问 https://github.com/RVC-Boss/GPT-SoVITS/releases"
echo "2. 下载最新的预训练模型包"
echo "3. 解压到 GPT-SoVITS 目录"

# 3. 安装依赖
pip install -r requirements.txt

# 4. 启动API服务
echo "启动命令：python api_v2.py"