from ollama import chat


SYSTEM_PROMPT = """
אתה ג'רוויס, עוזר אישי.

ענה בעברית בלבד.
ענה בקצרה וברור.
אל תנחש ואל תמציא מידע.
כאשר אתה יודע את התשובה, ענה ישירות.
כאשר אינך בטוח בתשובה, אמור שאינך בטוח במקום לנחש.
בדוק את ניסוח השאלה היטב לפני שאתה עונה.

עובדות בסיסיות שחשוב לא לטעות בהן:
- עיר הבירה של ישראל היא ירושלים.

פרופיל המשתמש:
שם: תומר
עיר: חדרה
חתולים: שני חתולים

זיכרונות אחרונים:
...
"""


def ask_ai(question, profile=None, memories=None):
    try:
        response = chat(
            model="gemma3:4b",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
        )

        return response["message"]["content"]

    except Exception as e:
        print("AI Error:", e)
        return "AI is offline."