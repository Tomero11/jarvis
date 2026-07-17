import asyncio
import edge_tts
from playsound3 import playsound

VOICE = "he-IL-HilaNeural"
VOICE_FILE = "jarvis_voice.mp3"


def speak(text):
    async def _speak():
        await edge_tts.Communicate(
            text,
            VOICE,
        ).save(VOICE_FILE)

    try:
        asyncio.run(_speak())
        playsound(VOICE_FILE)

    except Exception as e:
        print(f"Voice Error: {e}")