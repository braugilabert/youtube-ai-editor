import os
import time
import json

from modules.transcriber import (
    transcribe_video
)

from modules.chunker import (
    create_chunks
)

from modules.analyzer import (
    run_analysis
)

from modules.ffmpeg_tools import (
    render_final_video
)

from config import (
    SEGMENTS_FILE
)


def print_banner():

    print()
    print("=" * 60)
    print(" AI YOUTUBE EDITOR ")
    print("=" * 60)
    print()


def seconds_to_human(seconds):

    hours = int(seconds // 3600)

    minutes = int(
        (seconds % 3600) // 60
    )

    secs = int(
        seconds % 60
    )

    return (
        f"{hours:02}:{minutes:02}:{secs:02}"
    )


def calculate_final_duration():

    if not os.path.exists(
        SEGMENTS_FILE
    ):
        return 0

    with open(
        SEGMENTS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        segments = json.load(
            file
        )

    total = 0

    for segment in segments:

        total += (
            segment["end"]
            - segment["start"]
        )

    return total


def main():

    start_time = time.time()

    try:

        print_banner()

        print(
            "[1/4] TRANSCRIPCION"
        )

        transcribe_video()

        print()
        print(
            "[2/4] CREACION DE BLOQUES"
        )

        create_chunks()

        print()
        print(
            "[3/4] ANALISIS IA"
        )

        run_analysis()

        duration = (
            calculate_final_duration()
        )

        print()
        print(
            "[4/4] RENDERIZADO VIDEO"
        )

        render_final_video()

        total_time = (
            time.time()
            - start_time
        )

        print()
        print("=" * 60)
        print("PROCESO COMPLETADO")
        print("=" * 60)

        print()

        print(
            "[RESUMEN]"
        )

        print()

        print(
            f"Duracion seleccionada:"
        )

        print(
            f"{seconds_to_human(duration)}"
        )

        print()

        print(
            f"Tiempo total proceso:"
        )

        print(
            f"{seconds_to_human(total_time)}"
        )

        print()

    except Exception as error:

        print()

        print("=" * 60)
        print("ERROR")
        print("=" * 60)

        print()

        print(
            str(error)
        )

        print()

        raise


if __name__ == "__main__":

    main()