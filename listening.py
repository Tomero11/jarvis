import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr

def listen():

    fs = 44100
    sd.default.device = (1, 10)

    print("Listening...")

    recording = sd.rec(
        int(3 * fs),
        samplerate=fs,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write("temp.wav", fs, recording)

    recognizer = sr.Recognizer()

    with sr.AudioFile("temp.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="he-IL")

        print("You said:", text)

        return text

    except sr.UnknownValueError:
        return None

    except Exception as e:
        print(f"Listening Error: {type(e).__name__}: {e}")
        return None