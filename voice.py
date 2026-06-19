import asyncio
import edge_tts
from playsound3 import playsound

VOICE = "he-IL-HilaNeural"

def speak(text):

    async def _speak():
        await edge_tts.Communicate(
            text,
            VOICE
        ).save("jarvis_voice.mp3")

    asyncio.run(_speak())

    playsound("jarvis_voice.mp3")