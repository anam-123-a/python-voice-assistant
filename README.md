# Voice Virtual Assistant

A voice-enabled conversational AI assistant in Python. It listens to you,
understands what you said, thinks of a reply, and speaks it back — a full
loop of:

**Microphone → ElevenLabs Speech-to-Text → Claude (Anthropic) → ElevenLabs Text-to-Speech → Speakers**

## How it works

| Step | What happens | Service used |
|---|---|---|
| 1. Listen | Push-to-talk recording from your mic | `sounddevice` |
| 2. Understand | Your speech is transcribed to text | ElevenLabs Scribe (STT) |
| 3. Think | A reply is generated from the conversation | Claude API (Anthropic) |
| 4. Speak | The reply is turned into natural speech and played | ElevenLabs TTS |

> **Note on "response generation":** ElevenLabs' API is built for speech
> (recognition + synthesis), not open-ended text generation, so this project
> pairs it with the Claude API for the "thinking" step. That's a very common
> pairing and keeps each part of the pipeline using the tool it's best at.
> If you'd rather use OpenAI's API for that step, see "Swapping the LLM"
> below — it's a ~10 line change.

## 1. Install

You need Python 3.10+.

```bash
pip install -r requirements.txt
```

**Microphone support (`sounddevice`) needs the PortAudio system library:**

- **Ubuntu/Debian:** `sudo apt-get install libportaudio2`
- **macOS:** usually works out of the box; if not, `brew install portaudio`
- **Windows:** works out of the box (bundled in the wheel)

## 2. Configure your API keys

```bash
cp .env.example .env
```

Then edit `.env` and fill in:
- `ELEVENLABS_API_KEY` — from https://elevenlabs.io/app/settings/api-keys
- `ANTHROPIC_API_KEY` — from https://console.anthropic.com/settings/keys

Both have free tiers, which are enough to test this.

## 3. Run it

```bash
python voice_assistant.py
```

- Press **Enter** to start talking, speak, then press **Enter** again to
  stop recording (push-to-talk — this is far more reliable than automatic
  silence detection, especially on a laptop mic in a noisy room).
- The assistant transcribes what you said, thinks of a reply with Claude,
  and speaks it back to you.
- Say **"exit"**, **"quit"**, **"stop"**, or **"goodbye"** any time to end
  the conversation.

No microphone handy, or just testing? Set `INPUT_MODE=text` in `.env` — you
type your side of the conversation instead, and replies are still spoken
out loud.

## Customizing

All of this is in `.env`, no code changes needed:

- **Voice** — set `ELEVENLABS_VOICE_ID` to any voice from your ElevenLabs
  Voice Library (Voices tab in the ElevenLabs dashboard has the IDs).
- **Speed vs. quality** — `ELEVENLABS_TTS_MODEL=eleven_flash_v2_5` is the
  snappiest; `eleven_multilingual_v2` sounds a little more natural but is
  slower.
- **Claude model** — `CLAUDE_MODEL=claude-haiku-4-5-20251001` for the
  fastest/cheapest replies, or `claude-sonnet-5` (default) for better
  reasoning.
- **Personality** — edit `SYSTEM_PROMPT` near the top of
  `voice_assistant.py` to change how the assistant talks (tone, persona,
  how long its answers are, etc).
- **Wrong microphone picked up** — list devices and set
  `MIC_DEVICE_INDEX` (see the comment in `.env.example`).

## Swapping the LLM (optional)

To use OpenAI's API instead of Claude for the "response generation" step,
replace `generate_reply()` in `voice_assistant.py` with:

```python
from openai import OpenAI
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_reply(client, history):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}, *history],
        max_tokens=300,
    )
    return response.choices[0].message.content.strip()
```
and pass `openai_client` into it instead of `anthropic_client` in `main()`.
(`pip install openai` first.)

## Troubleshooting

- **`Missing required environment variable(s)`** — you haven't filled in
  `.env` yet, or you're running from a different folder than the one that
  has it.
- **`PortAudio library not found` / microphone errors** — install
  PortAudio (see step 1), or set `INPUT_MODE=text` to bypass the mic
  entirely.
- **No sound plays / "Couldn't play audio directly"** — this usually means
  there's no audio output device available (e.g. running on a headless
  server). The script falls back to saving the reply as `last_reply.wav`
  in the current folder so you don't lose it.
- **401 errors** — double-check the API key in `.env` matches the service
  reporting the error (ElevenLabs vs. Anthropic keys are not
  interchangeable).
- **Transcription comes back empty** — speak a bit louder/closer to the
  mic, or check `MIC_DEVICE_INDEX` is pointing at the right input device.

## Files

```
voice_assistant.py   # the app
requirements.txt     # pip dependencies
.env.example          # copy to .env and fill in your keys
README.md            # this file
```
