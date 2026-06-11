import pyttsx3

engine = pyttsx3.init()

for voice in engine.getProperty("voices"):
    print("ID:", voice.id)
    print("NAME:", voice.name)
    print("-" * 40)