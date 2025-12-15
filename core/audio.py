import os
import tempfile
from typing import Optional

from utils.ffmpeg_utils import extract_audio_ffmpeg


def extract_audio(
    video_path: str,
    sample_rate: int = 16000,
    output_dir: Optional[str] = None
) -> str:
    """
    Extract audio from a video file and return the path to a WAV file.

    Args:
        video_path (str): Path to input video
        sample_rate (int): Audio sample rate for Whisper compatibility
        output_dir (Optional[str]): Directory to save extracted audio

    Returns:
        str: Path to extracted WAV audio file
    """

    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    if output_dir is None:
        output_dir = tempfile.mkdtemp()

    audio_path = os.path.join(output_dir, "extracted_audio.wav")

    extract_audio_ffmpeg(
        video_path=video_path,
        out_audio_path=audio_path,
        sample_rate=sample_rate
    )

    return audio_path
