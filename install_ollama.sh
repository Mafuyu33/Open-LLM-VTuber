#!/bin/bash
echo "准备安装Ollama..."
curl -fsSL https://ollama.com/install.sh | sh

echo "启动Ollama服务..."
ollama serve &

echo "等待服务启动..."
sleep 5

echo "下载中文模型..."
ollama pull qwen2.5:latest

echo "Ollama安装完成！"