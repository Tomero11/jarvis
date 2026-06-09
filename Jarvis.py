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

        if "hello" in text.lower():
             print("HELLO COMMAND DETECTED")
             speak("Hello Tomer")

        elif "who are you" in text.lower():
            speak("I am Jarvis, your personal life assistant")

        elif "how are you" in text.lower():
            speak("I am doing great")

        else:
            speak("I don't understand yet")

start_jarvis()