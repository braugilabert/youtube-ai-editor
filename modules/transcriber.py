import json
import os

from faster_whisper import WhisperModel

from config import (
    VIDEO_FILE,
    TRANSCRIPT_FILE,
    WHISPER_MODEL
)


def validate_video():

    if not os.path.exists(VIDEO_FILE):

        raise FileNotFoundError(
            f"No existe el vídeo: {VIDEO_FILE}"
        )


def transcribe_video():

    validate_video()

    print()
    print("=" * 50)
    print("TRANSCRIPCION")
    print("=" * 50)
    print()

    print("[INFO] Cargando Whisper...")

    model = WhisperModel(
        WHISPER_MODEL,
        compute_type="auto"
    )

    print("[INFO] Iniciando transcripción...")

    segments, info = model.transcribe(
        VIDEO_FILE,
        beam_size=5,
        vad_filter=True
    )

    transcript = []

    count = 0

    for segment in segments:

        count += 1

        transcript.append(
            {
                "start": round(
                    segment.start,
                    2
                ),

                "end": round(
                    segment.end,
                    2
                ),

                "text": segment.text.strip()
            }
        )

        if count % 100 == 0:

            print(
                f"[INFO] {count} segmentos procesados..."
            )

    os.makedirs(
        os.path.dirname(
            TRANSCRIPT_FILE
        ),
        exist_ok=True
    )

    with open(
        TRANSCRIPT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            transcript,
            file,
            ensure_ascii=False,
            indent=2
        )

    print()
    print(
        f"[OK] Transcripción guardada en:"
    )
    print(
        f"     {TRANSCRIPT_FILE}"
    )
    print()

    print(
        f"[INFO] Total segmentos: {len(transcript)}"
    )

    return transcript