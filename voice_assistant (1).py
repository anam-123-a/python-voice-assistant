import os
import sys
import time
import threading
import msvcrt
import sounddevice as sd
import soundfile as sf
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
import ollama

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "JBFqnCBsd6RMkjVDRZzb")
TTS_MODEL = os.getenv("ELEVENLABS_TTS_MODEL", "eleven_flash_v2_5")
STT_MODEL = os.getenv("ELEVENLABS_STT_MODEL", "scribe_v1")

if not ELEVENLABS_API_KEY or ELEVENLABS_API_KEY.startswith("your_"):
    print("ERROR: ElevenLabs API key .env mein set nahi hai.")
    sys.exit()

eleven = ElevenLabs(api_key=ELEVENLABS_API_KEY)


def record_audio(filename="input.wav", seconds=6):
    print("\n🎤 Listening...")
    print("Speak now!")

    recording = sd.rec(
        int(seconds * 16000),
        samplerate=16000,
        channels=1,
        dtype="float32"
    )

    sd.wait()
    sf.write(filename, recording, 16000)

    print("✅ Recording complete.")
    return filename


def speech_to_text(filename):
    print("🔄 Converting speech to text...")

    with open(filename, "rb") as audio_file:
        result = eleven.speech_to_text.convert(
            file=audio_file,
            model_id=STT_MODEL
        )

    text = getattr(result, "text", "")
    return text.strip()


def ask_ollama(user_text):
    print("🤖 Thinking...")

    response = ollama.chat(
        model="gemma3:1b",
   messages=[
    {
        "role": "system",
        "content": "Give short, clear answers. Keep responses under 50 words."
    },
    {
        "role": "user",
        "content": user_text
    }
]
    )

    return response["message"]["content"]


def text_to_speech(text):
    print("🔊 Speaking...")

    audio = eleven.text_to_speech.convert(
        text=text,
        voice_id=VOICE_ID,
        model_id=TTS_MODEL,
        output_format="mp3_44100_128"
    )

    output_file = "response.mp3"

    with open(output_file, "wb") as f:
        for chunk in audio:
            f.write(chunk)

    return output_file


def play_audio(filename):
    data, samplerate = sf.read(filename)

    sd.default.device = (1, 3)

    print("🔊 Speaking...")

    sd.play(data, samplerate)
    sd.wait()
    



def main():
    print("=" * 50)
    print("        🎙️ PYTHON VOICE ASSISTANT")
    print("=" * 50)
    print("Press ENTER to speak.")
    print("Type 'exit' and press ENTER to quit.")
    print("=" * 50)

    while True:
        command = input("\n> ")

        if command.lower() == "exit":
            print("Goodbye! 👋")
            break

        audio_file = record_audio()

        user_text = speech_to_text(audio_file)

        if not user_text:
            print("❌ I couldn't understand you.")
            continue

        print(f"\nYou: {user_text}")

        answer = ask_ollama(user_text)

        print(f"\nAssistant: {answer}")

        response_file = text_to_speech(answer)

        play_audio(response_file)


if __name__ == "__main__":
    main()
