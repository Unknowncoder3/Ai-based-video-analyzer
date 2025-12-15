import shutil
import subprocess


def find_ffmpeg() -> str:
    ff = shutil.which("ffmpeg")
    if ff:
        return ff

    try:
        import imageio_ffmpeg as iio
        return iio.get_ffmpeg_exe()
    except Exception:
        raise RuntimeError(
            "ffmpeg not found. Install via `brew install ffmpeg` or `apt install ffmpeg`."
        )


def extract_audio_ffmpeg(video_path: str, out_audio_path: str, sample_rate: int = 16000) -> str:
    ffmpeg_exe = find_ffmpeg()

    cmd = [
        ffmpeg_exe,
        "-y",
        "-i",
        video_path,
        "-vn",
        "-ac",
        "1",
        "-ar",
        str(sample_rate),
        "-f",
        "wav",
        out_audio_path,
    ]

    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return out_audio_path
