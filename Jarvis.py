from voice import speak
from memory import last_memories
from listening import listen

def start_jarvis():
    print("Jarvis starting...")

    speak("Jarvis is online")

    print("Voice module loaded")
    print("Memory module loaded")
    print("Vision module ready")

    print("Recent memories:")
    last_memories()

    text = listen()

    print("Jarvis heard:", text)

    if text:
        speak(f"You said {text}")

start_jarvis()