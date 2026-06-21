from voice import speak
from memory import (
    last_memories,
    get_last_memories,
    last_memory_of,
    search_memory,
    save_event,
    what_i_said_today,
    get_name,
    get_city,
    get_cats
    
)

last_memory_of


from listening import listen
from memory import last_user_message
from ai import ask_ai

def say(text):
    print(f"Jarvis: {text}")
    speak(text)

def start_jarvis():
    print("Jarvis starting...")

    speak("Jarvis is online")

    print("Voice module loaded")
    print("Memory module loaded")
    print("Vision module ready")

    while True:
        
        text = listen()

        if not text:
            continue

        #save_event(f"Tomer said: {text}")

        elif "goodbye" in text.lower() \
            or "bye" in text.lower() \
            or "ביי" in text \
            or "להתראות" in text:

              say("Goodbye")
              break

        elif "hello" in text.lower() \
            or "שלום" in text:

            print("HELLO COMMAND DETECTED")
            say("Hello")
             
            continue


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
        elif "איך קוראים לי" in text:

         name = get_name()

         if name:
          print(f"Jarvis: קוראים לך {name}")
          speak(f"קוראים לך {name}")
         else:
          speak("אני עדיין לא יודע איך קוראים לך")

         continue


        elif "איך קוראים לי" in text:

            name = get_name()

            if name:
                say(f"קוראים לך {name}")
            else:
                say("אני עדיין לא יודע איך קוראים לך")

            continue


        elif "קוראים לי" in text:

            name = text.replace("קוראים לי", "").strip()

            save_event(f"NAME:{name}")

            say(f"נעים להכיר {name}")

            continue


        elif text.startswith("אני גר ב"):

            city = text.replace("אני גר ב", "").strip()

            save_event(f"CITY:{city}")

            say(f"אוקיי, אז אתה גר ב{city}")

            continue


        elif "איפה אני גר" in text:

            city = get_city()

            if city:
                say(f"אתה גר ב{city}")
            else:
                say("אני עדיין לא יודע איפה אתה גר")

            continue
          
        elif text.startswith("יש לי"):

         cats = text.replace("יש לי", "").strip()

         save_event(f"CATS:{cats}")

         say(f"אוקיי, רשמתי שיש לך {cats}")

         continue

        elif "כמה חתולים יש לי" in text:

         cats = get_cats()

         if cats:
          say(f"יש לך {cats}")
         else:
          say("אני עדיין לא יודע כמה חתולים יש לך")

         continue

        elif "מה אתה יודע עליי" in text:

         name = get_name()
         city = get_city()
         cats = get_cats()

         info = []

         if name:
          info.append(f"קוראים לך {name}")

         if city:
          info.append(f"אתה גר ב{city}")

         if cats:
          info.append(f"יש לך {cats}")

         if info:

          summary = ". ".join(info)

          say(summary)

         else:

          say("אני עדיין לא יודע עליך הרבה")

          continue

        else:

            try:

                reply = ask_ai(text)

                print("AI:", reply)

                say(reply)

            except Exception as e:

                print("AI Error:", e)

                say("AI is offline")


start_jarvis()