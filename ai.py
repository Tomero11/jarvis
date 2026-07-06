from ollama import chat

def ask_ai(question):

    try:
        response = chat(
           model="qwen3:4b",
            messages=[
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