import subprocess

def ask_ai(prompt):

    prompt = f"""
ענה בעברית בלבד.
ענה בקצרה.
אל תציג את תהליך החשיבה שלך.

שאלה:
{prompt}
"""

    result = subprocess.run(
        ["ollama", "run", "qwen3:4b", prompt],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    return result.stdout.strip()