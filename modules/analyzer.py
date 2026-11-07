import json

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


def run_analysis():

    print(
        "[INFO] Cargando bloques..."
    )

    with open(
        CHUNKS_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        chunks = json.load(f)

    decisions = []

    kept_segments = []

    print(
        f"[INFO] Analizando {len(chunks)} bloques..."
    )

    for chunk in tqdm(chunks):

        result = analyze_chunk(chunk)

        decisions.append(result)

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

    print(
        f"[INFO] Segmentos conservados: {len(kept_segments)}"
    )

    with open(
        DECISIONS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            decisions,
            f,
            ensure_ascii=False,
            indent=2
        )

    with open(
        SEGMENTS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            kept_segments,
            f,
            ensure_ascii=False,
            indent=2
        )

    print(
        f"[OK] Guardado en {SEGMENTS_FILE}"
    )

    return kept_segments
