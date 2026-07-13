from voice import speak
from memory import (
    get_last_memories,
    what_i_said_today,
    get_profile_value,
    update_profile,
    load_profile,
)
from listening import listen
from ai import ask_ai
from people_detection import start_vision
import threading
import re


def say(text):
    print(f"Jarvis: {text}")
    speak(text)


def clean_for_speech(text):
    return re.sub(r"[^\w\s.,!?א-ת]", "", text)


def start_jarvis():
    print("Jarvis starting...")
    speak("Jarvis is online")

    print("Voice module loaded")
    print("Memory module loaded")
    print("Vision module ready")

    threading.Thread(target=start_vision, daemon=True).start()

    print("Vision started")

    while True:
        text = listen()

        if not text:
            continue

        elif "להתראות" in text or "ביי" in text:
            name = get_profile_value("name")
            if name:
                say(f"להתראות {name}")
            else:
                say("להתראות")
            break

        elif "hello" in text.lower() or "שלום" in text:
            name = get_profile_value("name")
            if name:
                say(f"שלום {name}, מה שלומך?")
            else:
                say("שלום")
            continue

        elif "what did i say today" in text.lower():
            results = what_i_said_today()
            if results:
                print("\n".join(results[-10:]))
                speak(f"You said {len(results)} things today")
            else:
                speak("I do not remember anything from today")
            continue

        elif text.startswith("קוראים לי"):
            name = text.replace("קוראים לי", "").strip()
            update_profile("name", name)
            say(f"נעים להכיר {name}")
            continue

        elif "איך קוראים לי" in text:
            name = get_profile_value("name")
            if name:
                say(f"קוראים לך {name}")
            else:
                say("אני עדיין לא יודע איך קוראים לך")
            continue

        elif text.startswith("אני גר ב"):
            city = text.replace("אני גר ב", "").strip()
            update_profile("city", city)
            say(f"אוקיי, אז אתה גר ב{city}")
            continue

        elif "איפה אני גר" in text:
            city = get_profile_value("city")
            if city:
                say(f"אתה גר ב{city}")
            else:
                say("אני עדיין לא יודע איפה אתה גר")
            continue

        elif text.startswith("יש לי"):
            cats = text.replace("יש לי", "").strip()
            update_profile("cats", "שני חתולים")
            say(f"אוקיי, רשמתי שיש לך {cats}")
            continue

        elif "כמה חתולים יש לי" in text:
            cats = get_profile_value("cats")
            if cats:
                say(f"יש לך {cats}")
            else:
                say("אני עדיין לא יודע כמה חתולים יש לך")
            continue

        elif "מה אתה יודע עליי" in text:
            name = get_profile_value("name")
            city = get_profile_value("city")
            cats = get_profile_value("cats")
            info = []
            if name:
                info.append(f"קוראים לך {name}")
            if city:
                info.append(f"אתה גר ב{city}")
            if cats:
                info.append(f"יש לך {cats}")

            if info:
                say(". ".join(info))
            else:
                say("אני עדיין לא יודע עליך הרבה")
            continue

        else:
            try:
                profile = load_profile()
                memories = get_last_memories()
                reply = ask_ai(text, profile, memories)
                print("AI:", reply)
                say(clean_for_speech(reply))
            except Exception as e:
                print("AI Error:", e)
                say("AI is offline")


start_jarvis()
