# 🎙️ Python Voice Assistant

A Python-based AI Voice Assistant that listens to your voice, converts speech into text, generates an AI response using a locally running LLM, and speaks the response back to you.

## 🔄 Voice Assistant Flow

**🎤 Microphone → ElevenLabs STT → Ollama (Gemma 3:1B) → ElevenLabs TTS → 🔊 Speaker**

---

## ✨ Features

- 🎤 Records voice input through the microphone
- 📝 Converts speech to text using ElevenLabs Speech-to-Text
- 🤖 Generates AI responses using Ollama and Gemma 3:1B
- 🔊 Converts AI responses into speech using ElevenLabs Text-to-Speech
- 💻 Runs locally on Windows
- ⚡ Uses a local LLM for AI responses
- 🔐 API keys are stored using environment variables
- 💬 Provides short and clear AI responses

---

## 🛠️ Technologies Used

- Python
- Ollama
- Gemma 3:1B
- ElevenLabs Speech-to-Text
- ElevenLabs Text-to-Speech
- SoundDevice
- SoundFile
- NumPy
- python-dotenv

---

## 🔄 How It Works

### 1. Voice Input 🎤

The assistant records the user's voice through the microphone using `sounddevice`.

### 2. Speech-to-Text 📝

The recorded audio is sent to ElevenLabs Speech-to-Text using the `scribe_v1` model.

### 3. AI Processing 🤖

The converted text is sent to the locally running Ollama model:

`gemma3:1b`

The model generates a short response.

### 4. Text-to-Speech 🔊

The AI response is sent to ElevenLabs Text-to-Speech using:

`eleven_flash_v2_5`

### 5. Audio Playback 🔊

The generated audio is played through the computer's speaker.

---

# 📁 Project Structure

```text
python-voice-assistant/
│
├── voice_assistant (1).py
├── requirements.txt
├── README.md
├── .env
└── venv/
```

> `.env` and `venv/` should NOT be uploaded to GitHub.

---

# 🚀 Installation & Setup

## 1. Check Python

```powershell
python --version
```

Python 3.10 or newer is recommended.

---

## 2. Create Virtual Environment

```powershell
python -m venv venv
```

---

## 3. Activate Virtual Environment

```powershell
venv\Scripts\activate
```

---

## 4. Install Project Dependencies

```powershell
pip install -r requirements.txt
```

---

## 5. Install Ollama Python Package

```powershell
pip install ollama
```

---

## 6. Install Ollama

Install Ollama from the official Ollama website.

Then download the Gemma 3:1B model:

```powershell
ollama pull gemma3:1b
```

---

## 7. Test Ollama

```powershell
ollama run gemma3:1b
```

If Gemma responds, Ollama is working correctly.

---

# 🔑 API Configuration

Create a `.env` file inside the project folder.

Add:

```text
ELEVENLABS_API_KEY=your_elevenlabs_api_key
ELEVENLABS_VOICE_ID=JBFqnCBsd6RMkjVDRZzb
ELEVENLABS_TTS_MODEL=eleven_flash_v2_5
ELEVENLABS_STT_MODEL=scribe_v1
```

⚠️ Never upload your real API key to GitHub.

---

# ▶️ Run the Voice Assistant

Make sure the virtual environment is activated:

```powershell
venv\Scripts\activate
```

Then run:

```powershell
python "voice_assistant (1).py"
```

The assistant will show:

```text
Press ENTER to speak.
Type 'exit' and press ENTER to quit.
```

Press **Enter**, speak into the microphone, and the assistant will process and speak the response.

---

# 💻 Commands Used

These are the main commands used while building and running the project:

### Create Virtual Environment

```powershell
python -m venv venv
```

### Activate Virtual Environment

```powershell
venv\Scripts\activate
```

### Install Dependencies

```powershell
pip install -r requirements.txt
```

### Install Ollama Python Package

```powershell
pip install ollama
```

### Download Gemma Model

```powershell
ollama pull gemma3:1b
```

### Run Gemma

```powershell
ollama run gemma3:1b
```

### Run Voice Assistant

```powershell
python "voice_assistant (1).py"
```

### Exit Assistant

```text
exit
```

### Stop Running Program

Press:

```text
Ctrl + C
```

---

# 💬 Example

```text
You: What is Python?

Assistant: Python is a high-level programming language used for
web development, data analysis, AI, automation and more.
```

The response is generated locally using Gemma 3:1B and then converted into speech.

---

# 🧩 Main Components

| Component | Technology |
|---|---|
| Programming Language | Python |
| Speech Recognition | ElevenLabs Scribe |
| AI / LLM | Ollama + Gemma 3:1B |
| Text-to-Speech | ElevenLabs |
| Audio Recording | SoundDevice |
| Audio Processing | SoundFile |
| Environment Variables | python-dotenv |

---

# 🔐 Security

The following files should never be uploaded to GitHub:

```text
.env
venv/
*.wav
*.mp3
__pycache__/
*.pyc
```

The `.env` file contains the ElevenLabs API key.

---

# 🚧 Future Improvements

- 🌐 Web-based user interface
- 🎤 Browser-based voice interaction
- 💬 Conversation history
- 🎨 Modern UI
- ☁️ Cloud deployment
- 🔗 Public shareable web link
- 🛑 Voice command to stop the assistant

---

# 👩‍💻 Author

**Anam Maria**

GitHub: `https://github.com/anam-123-a`

---

## ⭐ Project

A voice-based AI assistant built with Python, ElevenLabs, and a locally running Gemma LLM through Ollama.


