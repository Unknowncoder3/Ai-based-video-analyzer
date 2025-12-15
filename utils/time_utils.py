def format_time(seconds: float) -> str:
    if seconds is None:
        return "00:00"
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m:02d}:{s:02d}"

