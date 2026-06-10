from voice import speak
from memory import (
    last_memories,
    get_last_memories,
    last_memory_of
)
from listening import listen


def start_jarvis():
    print("Jarvis starting...")

    speak("Jarvis is online")

    print("Voice module loaded")
    print("Memory module loaded")
    print("Vision module ready")

    print("Recent memories:")
    last_memories()

    while True:

        text = listen()

        print("Jarvis heard:", text)

        if not text:
            continue

        if "hello" in text.lower():
            print("HELLO COMMAND DETECTED")
            speak("Hello Tomer")

        elif "who are you" in text.lower():
            speak("I am Jarvis, your personal life assistant")

        elif "what did you see today" in text.lower():
            memories = get_last_memories()

            print(memories)

            speak("Here are my latest memories")

        elif "when did you last see a cat" in text.lower():
            memory = last_memory_of("cat")

            print(memory)

            speak(memory)

        elif "how are you" in text.lower():
            speak("I am doing great")

        elif "goodbye" in text.lower() or "bye" in text.lower():
            speak("Goodbye Tomer")
            break

        else:
            speak("I don't understand yet")


start_jarvis()