import json
import os

from tqdm import tqdm

from config import (
    CHUNKS_FILE,
    DECISIONS_FILE,
    SEGMENTS_FILE,
    MIN_SCORE
)

from modules.ollama_editor import (
    analyze_chunk
)


def merge_segments(segments):

    if not segments:
        return []

    merged = [
        segments[0]
    ]

    for current in segments[1:]:

        previous = merged[-1]

        gap = (
            current["start"]
            - previous["end"]
        )

        if gap <= 5:

            previous["end"] = max(
                previous["end"],
                current["end"]
            )

        else:

            merged.append(
                current
            )

    return merged


def save_json(path, data):

    os.makedirs(
        os.path.dirname(path),
        exist_ok=True
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2
        )


def run_analysis():

    print()
    print("=" * 50)
    print("ANALISIS IA")
    print("=" * 50)
    print()

    if not os.path.exists(
        CHUNKS_FILE
    ):
        raise FileNotFoundError(
            f"No existe {CHUNKS_FILE}"
        )

    with open(
        CHUNKS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        chunks = json.load(file)

    print(
        f"[INFO] Bloques encontrados: {len(chunks)}"
    )

    decisions = []

    kept_segments = []

    for index, chunk in enumerate(
        tqdm(chunks)
    ):

        result = analyze_chunk(
            chunk
        )

        decisions.append(
            result
        )

        score = result.get(
            "score",
            0
        )

        keep = result.get(
            "keep",
            False
        )

        if keep and score >= MIN_SCORE:

            kept_segments.append({
                "start": result["start"],
                "end": result["end"]
            })

    print()

    print(
        f"[INFO] Segmentos antes de fusionar: {len(kept_segments)}"
    )

    merged_segments = merge_segments(
        kept_segments
    )

    print(
        f"[INFO] Segmentos finales: {len(merged_segments)}"
    )

    save_json(
        DECISIONS_FILE,
        decisions
    )

    save_json(
        SEGMENTS_FILE,
        merged_segments
    )

    print()

    print(
        f"[OK] Decisiones guardadas en:"
    )

    print(
        f"     {DECISIONS_FILE}"
    )

    print()

    print(
        f"[OK] Segmentos guardados en:"
    )

    print(
        f"     {SEGMENTS_FILE}"
    )

    return merged_segments