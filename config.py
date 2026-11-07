# =====================================
# CONFIGURACIÓN GENERAL
# =====================================

VIDEO_FILE = "input/video.mp4"

WHISPER_MODEL = "large-v3"

OLLAMA_MODEL = "gemma3:12b-it-qat"

OLLAMA_URL = "http://localhost:11434/api/generate"

# Fragmentos para analizar
CHUNK_SECONDS = 300

# Mínimo para conservar
MIN_SCORE = 7

# Duración deseada
TARGET_DURATION_MINUTES = 50

# Carpetas
TRANSCRIPT_FILE = "transcripts/transcript.json"

CHUNKS_FILE = "analysis/chunks.json"

DECISIONS_FILE = "analysis/decisions.json"

SEGMENTS_FILE = "analysis/segments.json"

OUTPUT_VIDEO = "output/final_video.mp4"