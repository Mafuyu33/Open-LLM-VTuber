import urllib.request
import json
import os
import platform

# 需要的额外依赖
deps = [
    "win32-setctime",  # loguru在Windows上需要
    "colorama",  # Windows颜色支持
    "charset-normalizer",  # 重新下载Windows版本
    "numpy",  # 重新下载Windows版本
    "pydantic-core",  # 重新下载Windows版本
    "httptools",  # 重新下载Windows版本
    "watchfiles",  # uvicorn的可选依赖
    "python-multipart",  # fastapi的表单支持
    "scipy",  # 音频处理
    "soundfile",  # 音频文件读写
    "librosa",  # 音频处理
    "numba",  # librosa依赖
    "httpcore",  # httpx依赖
]

def download_package(package_name, download_dir="H:/AI/pip_packages"):
    """下载适合Windows的包"""
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    try:
        url = f"https://pypi.tuna.tsinghua.edu.cn/pypi/{package_name}/json"
        print(f"获取 {package_name} 信息...")
        
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
        
        latest_version = data["info"]["version"]
        releases = data["releases"][latest_version]
        
        # 查找适合的文件
        wheel_url = None
        wheel_filename = None
        
        # 优先级：win_amd64 > py3-none-any > cp310-none-win_amd64
        for release in releases:
            filename = release["filename"]
            if filename.endswith(".whl"):
                if "py3-none-any" in filename:
                    wheel_url = f"https://pypi.tuna.tsinghua.edu.cn/packages/{release['url'].split('/packages/')[-1]}"
                    wheel_filename = filename
                    break
                elif "cp310" in filename and "win_amd64" in filename:
                    wheel_url = f"https://pypi.tuna.tsinghua.edu.cn/packages/{release['url'].split('/packages/')[-1]}"
                    wheel_filename = filename
                    break
                elif "cp310" in filename and "win32" in filename:
                    wheel_url = f"https://pypi.tuna.tsinghua.edu.cn/packages/{release['url'].split('/packages/')[-1]}"
                    wheel_filename = filename
        
        if not wheel_url:
            # 尝试源码包
            for release in releases:
                if release["filename"].endswith(".tar.gz"):
                    print(f"警告: {package_name} 只有源码包，可能需要编译")
                    return None
        
        if wheel_url and wheel_filename:
            output_path = os.path.join(download_dir, wheel_filename)
            
            # 删除旧的macOS版本
            for f in os.listdir(download_dir):
                if package_name.replace("-", "_") in f and "macosx" in f:
                    os.remove(os.path.join(download_dir, f))
                    print(f"删除macOS版本: {f}")
            
            if os.path.exists(output_path):
                print(f"{wheel_filename} 已存在")
                return output_path
                
            print(f"下载 {wheel_filename}...")
            urllib.request.urlretrieve(wheel_url, output_path)
            print(f"✓ 下载完成: {output_path}")
            return output_path
            
    except Exception as e:
        print(f"✗ 下载 {package_name} 失败: {e}")
        return None

def main():
    download_dir = "H:/AI/pip_packages"
    
    print("下载额外的Windows依赖...")
    print("="*50)
    
    for dep in deps:
        download_package(dep, download_dir)
    
    print("="*50)
    print("\n运行以下命令安装新的包：")
    print("cd H:/AI/pip_packages")
    print('Get-ChildItem -Filter *.whl | ForEach-Object { pip install --no-deps $_.FullName }')

if __name__ == "__main__":
    main()