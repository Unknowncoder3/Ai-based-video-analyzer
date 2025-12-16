
# 🎥 AI-Based Video Analyzer

> **Offline multimodal video intelligence powered by state-of-the-art open-source AI.**
>
> Extract speech, understand visuals, and generate intelligent summaries from videos — all locally, with zero paid APIs.

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue" />
  <img src="https://img.shields.io/badge/Streamlit-App-red" />
  <img src="https://img.shields.io/badge/Whisper-ASR-green" />
  <img src="https://img.shields.io/badge/BLIP-Image%20Captioning-purple" />
  <img src="https://img.shields.io/badge/Ollama-LLM-orange" />
  <img src="https://img.shields.io/badge/License-MIT-brightgreen" />
</p>

---

## 📌 Overview

**AI-Based Video Analyzer** is an end-to-end multimodal AI system that converts raw video files into structured, meaningful insights. It integrates **speech recognition**, **computer vision**, and **large language models** into a single pipeline — designed to run completely **offline** for maximum privacy and control.

This project demonstrates real-world application of modern AI systems and is ideal for **research, content analysis, and production-grade prototyping**.

---

## ✨ Key Features

- 🎧 **Automatic Speech Transcription**  
  Converts video audio into accurate text using OpenAI Whisper (local execution).

- 🖼️ **Visual Frame Understanding**  
  Samples video frames and generates contextual captions using BLIP.

- 🧠 **LLM-Powered Semantic Summaries**  
  Combines audio and visual insights to generate coherent summaries via Mistral (Ollama).

- ⏱️ **Timestamped Insights**  
  Visual captions aligned with timestamps for better interpretability.

- 🔒 **Local-First & Privacy-Focused**  
  No cloud APIs, no data leakage — everything runs on your machine.

- 💻 **Interactive Web Interface**  
  Streamlit-based UI for smooth uploads, analysis, and result visualization.

---

## 🧠 Architecture (High-Level)

```

Video Input
│
├──► Audio Extraction ──► Whisper ASR ──► Transcript
│
├──► Frame Sampling ──► BLIP ──► Visual Captions
│
└──► Transcript + Captions ──► LLM (Mistral via Ollama) ──► Summary

````

---

## 🖼️ Application Screenshots 
### 📤 Video Upload & Configuration ![Video Upload](screenshots/first.jpeg) 
--- 
### 🗣️ Speech Transcription Output ![Transcription](screenshots/second.jpeg) 
--- 
### 🧠 AI-Generated Summary ![Summary](screenshots/third.jpeg) 
--- 
### 🕒 Timeline-Based Caption Analysis ![Timeline](screenshots/fourth.jpeg) 
---

---

## ⚙️ System Requirements

- Python **3.9+**
- FFmpeg installed and added to PATH
- 8GB+ RAM recommended
- GPU optional (improves performance)

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Unknowncoder3/Ai-based-video-analyzer.git
cd Ai-based-video-analyzer
````

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Install & Run Ollama (LLM Backend)

```bash
ollama pull mistral
ollama serve
```

> **Why Ollama?**
> Enables fast, local execution of LLMs without relying on paid APIs.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧪 How to Use

1. Upload a video file (MP4 / MOV / MKV / AVI)
2. Click **Analyze Video**
3. View:

   * Speech transcription
   * AI-generated semantic summary
   * Timestamped visual captions
4. Review or download extracted insights

---

## 📈 Use Cases

* 🎥 Video content summarization
* 🧑‍🏫 Lecture & tutorial analysis
* 🎤 Interview & meeting review
* 🧠 Multimodal AI demonstrations
* 📊 Media intelligence & research workflows

---

## 🔮 Future Enhancements

* Scene change detection
* Speaker diarization
* Emotion & sentiment analysis
* Batch video processing
* Timestamp-level summaries

---

## 👤 Author

**Snehasish Das**
Final Year CSBS Student | AI & Python Developer

* GitHub: [https://github.com/Unknowncoder3](https://github.com/Unknowncoder3)
* LinkedIn: [https://www.linkedin.com/in/snehasish-das-7a9803219](https://www.linkedin.com/in/snehasish-das-7a9803219)

---

## ⭐ Support

If you find this project useful, please ⭐ **star the repository** — it helps improve visibility and motivates future development.

---

## 📄 License

This project is licensed under the **MIT License**.


