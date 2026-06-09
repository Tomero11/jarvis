import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile("test.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)

except Exception as e:
    print("Error:", e)