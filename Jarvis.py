from voice import speak
from memory import (
    last_memories,
    get_last_memories,

    last_memory_of,
    search_memory,
    save_event,
    what_i_said_today
    )

last_memory_of


from listening import listen
from memory import last_user_message
from ai import ask_ai


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

        #save_event(f"Tomer said: {text}")

        if "goodbye" in text.lower() \
            or "גוד ביי" in text \
            or "להתראות" in text:

              speak("Goodbye Tomer")
              break

        elif "hello" in text.lower() \
            or "שלום" in text:

            print("HELLO COMMAND DETECTED")
            speak("Hello Tomer")
        
        elif "what did i say today" in text.lower():

          results = what_i_said_today()

          if results:
            print("\n".join(results[-10:]))
            speak(f"You said {len(results)} things today")

          else:
              speak("I do not remember anything from today")    

        elif "who are you" in text.lower() \
            or "מי אתה" in text:

         while True:

          text = listen()

        print("Jarvis heard:", text)

        if not text:
            continue

        if "hello" in text.lower():
            print("HELLO COMMAND DETECTED")
            speak("Hello Tomer")


            speak("I am Jarvis, your personal life assistant")


        elif "what was the last thing i said" in text.lower() \
              or "מה הדבר האחרון שאמרתי" in text:

              last_message = last_user_message()

              print(last_message)

              speak("I found your last message")    

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
        elif "what was the last thing i said" in text.lower() \
            or "מה הדבר האחרון שאמרתי" in text:

            last_message = last_user_message()

            print(last_message)

            speak("I found your last message")      

        elif "goodbye" in text.lower() or "bye" in text.lower():
            speak("Goodbye Tomer")
            break

        else:

            reply = ask_ai(text)

            print("AI:", reply)

            print("AI:", reply)

# speak(reply)
  


start_jarvis()