# ==========================================
# CONFIGURACION GENERAL
# ==========================================

# Video de entrada
VIDEO_FILE = "input/video.mp4"

# Whisper
WHISPER_MODEL = "large-v3"

# Ollama
OLLAMA_MODEL = "gemma3:12b-it-qat"
OLLAMA_URL = "http://localhost:11434/api/generate"

# Fragmentacion
#
# 120 segundos = 2 minutos
#
# Mucho mejor que los 5 minutos iniciales
#
CHUNK_SECONDS = 120

# Gemma debe puntuar al menos esto
# para que el segmento se conserve.

MIN_SCORE = 7

# Objetivo final aproximado
TARGET_DURATION_MINUTES = 50

# Deteccion de silencios
MIN_SILENCE_DURATION = 2
MIN_SILENCE_DB = -35

# Archivos generados

TRANSCRIPT_FILE = "transcripts/transcript.json"

CHUNKS_FILE = "analysis/chunks.json"

DECISIONS_FILE = "analysis/decisions.json"

SEGMENTS_FILE = "analysis/segments.json"

OUTPUT_VIDEO = "output/final_video.mp4"