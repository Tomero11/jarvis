import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
from pathlib import Path
import sys


if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).resolve().parent


MODEL_PATH = BASE_DIR / "whisper-model"


MODEL = WhisperModel(
    str(MODEL_PATH),
    device="cpu",
    compute_type="int8"
)


def listen():

    fs = 44100
    duration = 5

    print("Listening...")

    try:
        recording = sd.rec(
            int(duration * fs),
            samplerate=fs,
            channels=1,
            dtype="int16",
            device=1
        )

        sd.wait()

        write("temp.wav", fs, recording)

    except Exception as e:
        print(f"Microphone Error: {type(e).__name__}: {e}")
        return None

    try:
        segments, info = MODEL.transcribe(
            "temp.wav",
            language="he",
            beam_size=5,
            vad_filter=True
        )

        text = " ".join(
            segment.text.strip()
            for segment in segments
        ).strip()

        if text:
            print("You said:", text)
            return text

        return None

    except Exception as e:
        print(f"Whisper Error: {type(e).__name__}: {e}")
        return None