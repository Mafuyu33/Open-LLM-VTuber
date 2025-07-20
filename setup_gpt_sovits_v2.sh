#!/bin/bash
# GPT-SoVITS v2 快速部署脚本

echo "=== 部署 GPT-SoVITS v2 ==="

# 1. 克隆项目
cd /mnt/h/AI/main/
git clone https://github.com/RVC-Boss/GPT-SoVITS.git
cd GPT-SoVITS

# 2. 安装依赖
pip install -r requirements.txt

# 3. 下载预训练模型
echo "下载预训练模型..."
# 从ModelScope下载（国内更快）
wget https://modelscope.cn/models/iic/GPT-SoVITS/resolve/master/pretrained_models.zip

echo "配置完成！"
echo "使用方法："
echo "1. 录制3-10秒的参考音频"
echo "2. 运行 python webui.py"
echo "3. 在Open-LLM-VTuber中配置API"