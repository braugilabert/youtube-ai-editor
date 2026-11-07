import json
import subprocess
import os

from config import (
    VIDEO_FILE,
    SEGMENTS_FILE,
    OUTPUT_VIDEO
)

TEMP_FOLDER = "output/temp_segments"


def create_temp_folder():

    if not os.path.exists(TEMP_FOLDER):
        os.makedirs(TEMP_FOLDER)


def extract_segments():

    create_temp_folder()

    with open(
        SEGMENTS_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        segments = json.load(f)

    files = []

    for idx, segment in enumerate(segments):

        start = segment["start"]
        end = segment["end"]

        duration = end - start

        output_file = (
            f"{TEMP_FOLDER}/part_{idx}.mp4"
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

            "-c:a",
            "aac",

            output_file

        ]

        print(
            f"[INFO] Extrayendo segmento {idx+1}"
        )

        subprocess.run(
            command,
            check=True
        )

        files.append(output_file)

    return files


def create_concat_file(files):

    concat_path = (
        f"{TEMP_FOLDER}/concat.txt"
    )

    with open(
        concat_path,
        "w",
        encoding="utf-8"
    ) as f:

        for file in files:

            f.write(
                f"file '{os.path.abspath(file)}'\n"
            )

    return concat_path


def merge_segments(files):

    concat_file = create_concat_file(files)

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

    print(
        "[INFO] Uniendo segmentos..."
    )

    subprocess.run(
        command,
        check=True
    )

    print(
        f"[OK] Vídeo exportado: {OUTPUT_VIDEO}"
    )


def render_final_video():

    files = extract_segments()

    merge_segments(files)