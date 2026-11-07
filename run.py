import time

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


def banner():

    print()
    print("=" * 60)
    print(" YOUTUBE AI EDITOR ")
    print("=" * 60)
    print()


def main():

    start_time = time.time()

    banner()

    print(
        "[1/4] TRANSCRIBIENDO..."
    )

    transcribe_video()

    print(
        "[2/4] CREANDO BLOQUES..."
    )

    create_chunks()

    print(
        "[3/4] ANALIZANDO CON GEMMA..."
    )

    run_analysis()

    print(
        "[4/4] GENERANDO VIDEO..."
    )

    render_final_video()

    elapsed = (
        time.time() - start_time
    )

    minutes = elapsed / 60

    print()

    print("=" * 60)
    print(
        f"PROCESO TERMINADO ({minutes:.2f} min)"
    )
    print("=" * 60)


if __name__ == "__main__":
    main()