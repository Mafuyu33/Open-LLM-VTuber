#!/bin/bash
# 启动脚本 - 自动配置代理

# 获取Windows主机IP
export WIN_HOST=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}')

# 设置代理（请根据您的代理软件端口调整）
export http_proxy="http://${WIN_HOST}:7890"
export https_proxy="http://${WIN_HOST}:7890"
export all_proxy="socks5://${WIN_HOST}:7890"

echo "设置代理为: $http_proxy"

# 测试连接
echo "测试Google连接..."
curl -I -m 5 https://www.google.com

echo "启动Open-LLM-VTuber..."
uv run run_server.py