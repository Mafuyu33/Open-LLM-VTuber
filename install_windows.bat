@echo off
echo Installing Open-LLM-VTuber on Windows...
echo.

cd /d "H:\AI\main\Open-LLM-VTuber"

REM Upgrade pip and install build tools
echo Upgrading pip and installing build tools...
python -m pip install --upgrade pip
pip install setuptools wheel

REM Install pyproject.toml dependencies
echo Installing dependencies from pyproject.toml...
pip install tomli
pip install uv

REM Use uv to install dependencies (like in WSL)
echo Installing project dependencies with uv...
uv pip install -r pyproject.toml

REM If uv fails, try direct installation of common dependencies
if errorlevel 1 (
    echo uv failed, installing dependencies directly...
    pip install fastapi uvicorn loguru pydantic numpy requests aiofiles
    pip install soundfile librosa torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    pip install openai httpx websockets
)

echo.
echo Installation complete! Now you can run: python run_server.py
pause