from typing import List, Tuple
from PIL import Image

try:
    import cv2
except Exception:
    cv2 = None
    import imageio


def sample_frames_opencv(video_path: str, fps: float) -> List[Tuple[float, Image.Image]]:
    cap = cv2.VideoCapture(video_path)
    video_fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    frame_interval = max(1, int(round(video_fps / fps)))

    frames = []
    idx = 0
    while True:
        grabbed, frame = cap.read()
        if not grabbed:
            break
        if idx % frame_interval == 0:
            t = idx / video_fps
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            frames.append((round(t, 3), img))
        idx += 1

    cap.release()
    return frames


def sample_frames(video_path: str, fps: float):
    if cv2 is not None:
        return sample_frames_opencv(video_path, fps)

    reader = imageio.get_reader(video_path)
    frames = []
    for i, frame in enumerate(reader):
        if i % int(30 / fps) == 0:
            frames.append((i / 30, Image.fromarray(frame)))
    reader.close()
    return frames
