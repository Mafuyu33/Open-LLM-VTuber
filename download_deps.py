import urllib.request
import json
import os
import sys

# 核心依赖列表
deps = [
    "click",
    "fastapi", 
    "uvicorn",
    "h11",  # uvicorn依赖
    "httptools",  # uvicorn依赖
    "loguru",
    "pydantic",
    "pydantic-core",  # pydantic依赖
    "typing-extensions",
    "starlette",  # fastapi依赖
    "anyio",  # starlette依赖
    "idna",
    "sniffio",
    "numpy",
    "requests",
    "aiofiles",
    "websocket-client",
    "httpx",
    "certifi",
    "charset-normalizer",
    "urllib3",
]

def download_package(package_name, download_dir="H:/AI/pip_packages"):
    """下载包的最新版本"""
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    try:
        # 从清华镜像获取包信息
        url = f"https://pypi.tuna.tsinghua.edu.cn/pypi/{package_name}/json"
        print(f"获取 {package_name} 信息...")
        
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
        
        # 获取最新版本
        latest_version = data["info"]["version"]
        
        # 查找适合Python 3.10的wheel文件
        releases = data["releases"][latest_version]
        wheel_url = None
        
        for release in releases:
            filename = release["filename"]
            # 优先选择py3-none-any或cp310
            if filename.endswith(".whl") and ("py3-none-any" in filename or "cp310" in filename):
                # 使用清华镜像下载地址
                wheel_url = f"https://pypi.tuna.tsinghua.edu.cn/packages/{release['url'].split('/packages/')[-1]}"
                wheel_filename = filename
                break
        
        if not wheel_url:
            # 如果没有wheel，下载tar.gz
            for release in releases:
                if release["filename"].endswith(".tar.gz"):
                    wheel_url = f"https://pypi.tuna.tsinghua.edu.cn/packages/{release['url'].split('/packages/')[-1]}"
                    wheel_filename = release["filename"]
                    break
        
        if wheel_url:
            output_path = os.path.join(download_dir, wheel_filename)
            if os.path.exists(output_path):
                print(f"{wheel_filename} 已存在，跳过")
                return output_path
                
            print(f"下载 {wheel_filename}...")
            urllib.request.urlretrieve(wheel_url, output_path)
            print(f"✓ 下载完成: {output_path}")
            return output_path
        else:
            print(f"✗ 找不到合适的文件: {package_name}")
            return None
            
    except Exception as e:
        print(f"✗ 下载 {package_name} 失败: {e}")
        return None

def main():
    download_dir = "H:/AI/pip_packages"
    downloaded_files = []
    
    print(f"开始下载依赖包到 {download_dir}")
    print("="*50)
    
    for dep in deps:
        result = download_package(dep, download_dir)
        if result:
            downloaded_files.append(result)
    
    print("="*50)
    print(f"\n下载完成！共下载 {len(downloaded_files)} 个包")
    print("\n现在可以运行以下命令安装：")
    print(f"cd {download_dir}")
    print("pip install --no-deps *.whl")
    
    # 创建安装脚本
    with open(os.path.join(download_dir, "install_all.bat"), "w") as f:
        f.write("@echo off\n")
        f.write("echo Installing all packages...\n")
        f.write("pip install --no-deps *.whl\n")
        f.write("echo Done!\n")
        f.write("pause\n")
    
    print(f"\n或者运行: {download_dir}\\install_all.bat")

if __name__ == "__main__":
    main()