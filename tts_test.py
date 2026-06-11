import asyncio
import edge_tts

async def test():
    communicate = edge_tts.Communicate(
        "שלום תומר, אני ג'רוויס",
        "he-IL-HilaNeural"
    )

    await communicate.save("test.mp3")

asyncio.run(test())