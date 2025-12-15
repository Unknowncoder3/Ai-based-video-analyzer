try:
    import whisper
except Exception:
    whisper = None


def load_whisper_model(model_name: str):
    if whisper is None:
        raise RuntimeError("Whisper is not installed")
    return whisper.load_model(model_name)


def transcribe_audio(model, audio_path: str) -> str:
    result = model.transcribe(audio_path)
    return result.get("text", "")
