from ollama import chat

def ask_ai(question, profile=None, memories=None):

    system_prompt = """
אתה ג'רוויס, עוזר אישי.

ענה בעברית בלבד.
ענה בקצרה.
אל תמציא מידע.

פרופיל המשתמש:
שם: תומר
עיר: חדרה
חתולים: שני חתולים

זיכרונות אחרונים:
...

"""

    try:
        response = chat(
            model="gemma3:4b",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        print("AI Error:", e)
        return "AI is offline."