from voice import speak
from memory import (
    last_memories,
    get_last_memories,
    last_memory_of,
    search_memory,
    save_event,
    what_i_said_today
    )
from listening import listen


def start_jarvis():
    print("Jarvis starting...")

    speak("Jarvis is online")

    print("Voice module loaded")
    print("Memory module loaded")
    print("Vision module ready")

    while True:

        text = listen()

        print("Jarvis heard:", text)

        if not text:
            continue

        save_event(f"Tomer said: {text}")

        if "goodbye" in text.lower():
            speak("Goodbye Tomer")
            break

        elif "hello" in text.lower():
            print("HELLO COMMAND DETECTED")
            speak("Hello Tomer")
        
        elif "what did i say today" in text.lower():

          results = what_i_said_today()

          if results:
            print("\n".join(results[-10:]))
            speak(f"You said {len(results)} things today")

          else:
              speak("I do not remember anything from today")    

        elif "who are you" in text.lower():
            speak("I am Jarvis, your personal life assistant")

        elif "search memory for" in text.lower():

            keyword = text.lower().replace(
                "search memory for", ""
            ).strip()

            results = search_memory(keyword)

            if results:
                print("\n".join(results[-5:]))
                speak(
                    f"I found {len(results)} memories about {keyword}"
                )
            else:
                speak(
                    f"I found no memories about {keyword}"
                )

        elif "how are you" in text.lower():
            speak("I am doing great")

        else:
            speak("I don't understand yet")

start_jarvis()