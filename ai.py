from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

def ask_ai(prompt):

    response = client.chat.completions.create(
    model="google/gemma-3-1b",
    messages=[
        {
            "role": "system",
            "content": "ענה בעברית בלבד. ענה בקצרה. אל תציג את תהליך החשיבה שלך."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.7
)

    return response.choices[0].message.content