#!/usr/bin/env python3
"""测试Edge TTS男声"""
import asyncio
import edge_tts

async def test_tts():
    # 使用男性中文声音
    voice = "zh-CN-YunxiNeural"
    text = "大家好，我是晓风，很高兴见到大家！"
    
    # 生成语音
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("test_voice.mp3")
    print(f"语音已保存到 test_voice.mp3")
    print(f"使用的声音: {voice}")

if __name__ == "__main__":
    asyncio.run(test_tts())