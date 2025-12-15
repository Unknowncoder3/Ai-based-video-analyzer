import os
import tempfile
import streamlit as st
import torch

# ---- FIX: OpenMP duplicate runtime issue (macOS) ----
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from utils.time_utils import format_time
from utils.ffmpeg_utils import extract_audio_ffmpeg
from core.transcription import load_whisper_model, transcribe_audio
from core.video import sample_frames
from core.captioning import load_blip, caption_image
from core.summarizer import load_llm, summarize


# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="AI Video Analyzer", layout="wide")
st.title("🎬 AI-Based Video Analyzer")
st.caption("Transcribe • Caption • Summarize videos using local AI models")

# -------------------------------
# Upload UI
# -------------------------------
uploaded = st.file_uploader(
    "Upload a video file",
    type=["mp4", "mov", "mkv", "avi", "webm"]
)

process = st.button("🛠️ Analyze Video")

# -------------------------------
# Main Processing
# -------------------------------
if uploaded and process:

    with st.spinner("Processing video... This may take a few minutes."):

        # Save uploaded video
        tmpdir = tempfile.mkdtemp()
        video_path = os.path.join(tmpdir, uploaded.name)

        with open(video_path, "wb") as f:
            f.write(uploaded.getbuffer())

        # -------------------------------
        # Audio Extraction
        # -------------------------------
        audio_path = os.path.join(tmpdir, "audio.wav")
        extract_audio_ffmpeg(video_path, audio_path)

        # -------------------------------
        # Transcription (Whisper)
        # -------------------------------
        whisper_model = load_whisper_model("base")
        transcript = transcribe_audio(whisper_model, audio_path)

        # -------------------------------
        # Frame Sampling
        # -------------------------------
        frames = sample_frames(video_path, fps=0.5)

        # -------------------------------
        # Captioning (BLIP)
        # -------------------------------
        device = "cuda" if torch.cuda.is_available() else "cpu"
        processor, blip = load_blip(
            "Salesforce/blip-image-captioning-base",
            device
        )

        captions = []
        for t, img in frames[:20]:
            caption = caption_image(processor, blip, img, device)
            captions.append(f"{format_time(t)} — {caption}")

        # -------------------------------
        # Aggregation + Summary (LLM)
        # -------------------------------
        aggregated = transcript + "\n" + "\n".join(captions)

        llm = load_llm()
        summary = summarize(llm, aggregated)

    # -------------------------------
    # Results UI
    # -------------------------------
    st.success("Analysis complete")

    st.subheader("📜 Transcript")
    st.text_area(
        label="Transcript Output",
        value=transcript,
        height=220,
        label_visibility="collapsed"
    )

    st.subheader("📝 Summary")
    st.write(summary)

    st.subheader("🕒 Timeline (Visual Captions)")
    for c in captions:
        st.write(c)
