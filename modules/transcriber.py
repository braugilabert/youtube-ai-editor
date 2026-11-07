import json
from faster_whisper import WhisperModel
from config import (
    VIDEO_FILE,
    TRANSCRIPT_FILE,
    WHISPER_MODEL
)


def transcribe_video():

    print("[INFO] Cargando Whisper...")

    model = WhisperModel(
        WHISPER_MODEL,
        compute_type="float16"
    )

    print("[INFO] Transcribiendo vídeo...")

    segments, info = model.transcribe(
        VIDEO_FILE,
        beam_size=5
    )

    transcript = []

    for segment in segments:

        transcript.append({
            "start": round(segment.start, 2),
            "end": round(segment.end, 2),
            "text": segment.text.strip()
        })

    with open(
        TRANSCRIPT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            transcript,
            f,
            ensure_ascii=False,
            indent=2
        )

    print(
        f"[OK] Transcripción guardada en {TRANSCRIPT_FILE}"
    )

    return transcript