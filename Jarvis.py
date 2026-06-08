from voice import speak
from memory import last_memories

def start_jarvis():
    print("Jarvis starting...")

    speak("Jarvis is online")

    print("Voice module loaded")
    print("Memory module loaded")
    print("Vision module ready")

    print("Recent memories:")
    last_memories()

start_jarvis()