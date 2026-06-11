import anthropic
from voice import speak
from memory import last_memories, save_event
from listening import listen

# ========== הגדרות ==========
ANTHROPIC_API_KEY = "YOUR_API_KEY_HERE"  # ← שים כאן את ה-API Key שלך
YOUR_NAME = "Tomer"

SYSTEM_PROMPT = f"""You are Jarvis, a smart home AI assistant for {YOUR_NAME}.
You can speak both Hebrew and English — always respond in the same language the user spoke to you.
You are helpful, friendly, and concise (short answers — this is voice, not text).
You have access to a memory log of recent home events (like person/cat detection).
Keep answers brief — 1-3 sentences max, since they will be spoken out loud."""

# ========== היסטוריית שיחה ==========
conversation_history = []

# ========== פונקציה ראשית ==========
def chat_with_jarvis(user_text):
    """שולח הודעה ל-Claude ומחזיר תשובה"""
    
    # הוסף הודעת משתמש להיסטוריה
    conversation_history.append({
        "role": "user",
        "content": user_text
    })
    
    # שלח ל-Claude API
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",  # מהיר וזול — מתאים לעוזר קולי
        max_tokens=200,
        system=SYSTEM_PROMPT,
        messages=conversation_history
    )
    
    assistant_reply = response.content[0].text
    
    # הוסף תשובה להיסטוריה
    conversation_history.append({
        "role": "assistant",
        "content": assistant_reply
    })
    
    return assistant_reply


def start_jarvis():
    print("Jarvis starting...")
    speak("Jarvis is online")

    print("Voice module loaded")
    print("Memory module loaded")
    print("AI module loaded (Claude)")

    print("Recent memories:")
    last_memories()

    print("\nJarvis ready. Say something! (Ctrl+C to stop)\n")

    # ========== לולאה ראשית ==========
    while True:
        try:
            # הקשב
            text = listen()

            if not text:
                print("Didn't catch that, trying again...")
                continue

            print(f"\n{YOUR_NAME} said: {text}")

            # שמור בזיכרון
            save_event(f"{YOUR_NAME} said: {text}")

            # שלח ל-Claude וקבל תשובה
            print("Jarvis thinking...")
            reply = chat_with_jarvis(text)

            print(f"Jarvis: {reply}")

            # דבר בקול
            speak(reply)

            # שמור תשובה בזיכרון
            save_event(f"Jarvis replied: {reply}")

        except KeyboardInterrupt:
            print("\nJarvis shutting down...")
            speak("Goodbye!")
            break

        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, something went wrong.")


start_jarvis()
