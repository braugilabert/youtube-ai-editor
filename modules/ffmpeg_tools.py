import json
import os
import shutil
import subprocess

from config import (
    VIDEO_FILE,
    SEGMENTS_FILE,
    OUTPUT_VIDEO
)

TEMP_DIR = "output/temp_segments"


def run_command(command):

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:

        print(result.stderr)

        raise RuntimeError(
            "FFmpeg devolvió un error"
        )

    return result


def create_temp_dir():

    if os.path.exists(TEMP_DIR):

        shutil.rmtree(
            TEMP_DIR
        )

    os.makedirs(
        TEMP_DIR,
        exist_ok=True
    )


def validate_segments():

    if not os.path.exists(
        SEGMENTS_FILE
    ):
        raise FileNotFoundError(
            SEGMENTS_FILE
        )

    with open(
        SEGMENTS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        segments = json.load(
            file
        )

    if len(segments) == 0:

        raise ValueError(
            "No hay segmentos para exportar"
        )

    return segments


def extract_segment(
    segment,
    output_path
):

    start = segment["start"]

    end = segment["end"]

    duration = (
        end - start
    )

    command = [

        "ffmpeg",

        "-y",

        "-ss",
        str(start),

        "-i",
        VIDEO_FILE,

        "-t",
        str(duration),

        "-c:v",
        "libx264",

        "-preset",
        "fast",

        "-crf",
        "23",

        "-c:a",
        "aac",

        "-b:a",
        "192k",

        output_path
    ]

    run_command(
        command
    )


def extract_all_segments(
    segments
):

    files = []

    print()
    print(
        "[INFO] Extrayendo segmentos..."
    )
    print()

    for index, segment in enumerate(
        segments
    ):

        output_file = os.path.join(
            TEMP_DIR,
            f"segment_{index}.mp4"
        )

        print(
            f"[{index+1}/{len(segments)}] "
            f"{segment['start']} -> {segment['end']}"
        )

        extract_segment(
            segment,
            output_file
        )

        files.append(
            output_file
        )

    return files


def build_concat_file(
    files
):

    concat_file = os.path.join(
        TEMP_DIR,
        "concat.txt"
    )

    with open(
        concat_file,
        "w",
        encoding="utf-8"
    ) as file:

        for path in files:

            absolute = os.path.abspath(
                path
            )

            file.write(
                f"file '{absolute}'\n"
            )

    return concat_file


def merge_segments(
    files
):

    concat_file = build_concat_file(
        files
    )

    command = [

        "ffmpeg",

        "-y",

        "-f",
        "concat",

        "-safe",
        "0",

        "-i",
        concat_file,

        "-c",
        "copy",

        OUTPUT_VIDEO
    ]

    print()
    print(
        "[INFO] Uniendo segmentos..."
    )

    run_command(
        command
    )


def render_final_video():

    print()
    print("=" * 50)
    print("EXPORTACION FINAL")
    print("=" * 50)

    segments = validate_segments()

    create_temp_dir()

    files = extract_all_segments(
        segments
    )

    merge_segments(
        files
    )

    print()

    print(
        "[OK] Video generado:"
    )

    print(
        OUTPUT_VIDEO
    )

    print()