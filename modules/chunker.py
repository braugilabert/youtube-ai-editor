import json
import os

from config import (
    TRANSCRIPT_FILE,
    CHUNKS_FILE,
    CHUNK_SECONDS
)


def create_chunks():

    print()
    print("=" * 50)
    print("DIVISION EN BLOQUES")
    print("=" * 50)
    print()

    if not os.path.exists(
        TRANSCRIPT_FILE
    ):
        raise FileNotFoundError(
            f"No existe {TRANSCRIPT_FILE}"
        )

    with open(
        TRANSCRIPT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        transcript = json.load(file)

    if len(transcript) == 0:

        raise ValueError(
            "La transcripción está vacía"
        )

    chunks = []

    current_chunk = []

    chunk_start = None

    for segment in transcript:

        if chunk_start is None:

            chunk_start = segment["start"]

        current_chunk.append(
            segment
        )

        current_duration = (
            segment["end"] - chunk_start
        )

        if current_duration >= CHUNK_SECONDS:

            chunks.append(
                {
                    "start": current_chunk[0]["start"],
                    "end": current_chunk[-1]["end"],
                    "duration": round(
                        current_chunk[-1]["end"]
                        - current_chunk[0]["start"],
                        2
                    ),
                    "segments": current_chunk
                }
            )

            current_chunk = []
            chunk_start = None

    if current_chunk:

        chunks.append(
            {
                "start": current_chunk[0]["start"],
                "end": current_chunk[-1]["end"],
                "duration": round(
                    current_chunk[-1]["end"]
                    - current_chunk[0]["start"],
                    2
                ),
                "segments": current_chunk
            }
        )

    os.makedirs(
        os.path.dirname(
            CHUNKS_FILE
        ),
        exist_ok=True
    )

    with open(
        CHUNKS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            chunks,
            file,
            ensure_ascii=False,
            indent=2
        )

    print(
        f"[OK] Bloques creados: {len(chunks)}"
    )

    if chunks:

        first = chunks[0]

        print()

        print(
            "[INFO] Primer bloque:"
        )

        print(
            f"Inicio: {first['start']}s"
        )

        print(
            f"Fin: {first['end']}s"
        )

        print(
            f"Duración: {first['duration']}s"
        )

    return chunks