@echo off
echo Quick install for Open-LLM-VTuber...
echo.

cd /d "H:\AI\main\Open-LLM-VTuber"

REM Install essential dependencies
pip install tomli loguru fastapi uvicorn pydantic numpy requests aiofiles soundfile librosa websockets httpx openai

echo.
echo Basic dependencies installed! Starting server...
python run_server.py

pause