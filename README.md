# 🎙️ Python Voice Assistant

A Python-based AI Voice Assistant that listens to your voice, converts speech into text, generates an AI response using a locally running LLM, and speaks the response back to you.

### Voice Assistant Flow

**🎤 Microphone → ElevenLabs STT → Ollama (Gemma 3:1B) → ElevenLabs TTS → 🔊 Speaker**

---

## ✨ Features

- 🎤 Records voice input through the microphone
- 📝 Converts speech to text using ElevenLabs Speech-to-Text
- 🤖 Generates responses using Ollama with Gemma 3:1B
- 🔊 Converts AI responses into natural speech using ElevenLabs Text-to-Speech
- 💻 Runs locally on Windows
- ⚡ Uses a local LLM for AI response generation
- 🔐 API keys are stored using environment variables

---

## 🛠️ Technologies Used

- **Python**
- **Ollama**
- **Gemma 3:1B**
- **ElevenLabs Speech-to-Text**
- **ElevenLabs Text-to-Speech**
- **SoundDevice**
- **SoundFile**
- **python-dotenv**

---

## 🔄 How It Works

### 1. Listen 🎤

The assistant records audio from the microphone using `sounddevice`.

### 2. Speech-to-Text 📝

The recorded audio is sent to ElevenLabs Speech-to-Text using the `scribe_v1` model.

### 3. AI Response 🤖

The converted text is sent to a locally running Ollama model:

```text
gemma3:1b


