import json

from config import (
    TRANSCRIPT_FILE,
    CHUNKS_FILE,
    CHUNK_SECONDS
)


def create_chunks():

    print("[INFO] Dividiendo transcripción...")

    with open(
        TRANSCRIPT_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        transcript = json.load(f)

    chunks = []

    current_chunk = []

    chunk_start = None

    for segment in transcript:

        if chunk_start is None:
            chunk_start = segment["start"]

        current_chunk.append(segment)

        duration = (
            segment["end"] - chunk_start
        )

        if duration >= CHUNK_SECONDS:

            chunks.append({
                "start": chunk_start,
                "end": segment["end"],
                "segments": current_chunk
            })

            current_chunk = []
            chunk_start = None

    if current_chunk:

        chunks.append({
            "start": current_chunk[0]["start"],
            "end": current_chunk[-1]["end"],
            "segments": current_chunk
        })

    with open(
        CHUNKS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            chunks,
            f,
            ensure_ascii=False,
            indent=2
        )

    print(
        f"[OK] Generados {len(chunks)} bloques"
    )

    return chunks