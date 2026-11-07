import requests
import json

from config import (
    OLLAMA_URL,
    OLLAMA_MODEL
)


SYSTEM_PROMPT = """
Eres un editor profesional de YouTube.

Debes decidir si un fragmento de gameplay
merece conservarse en el montaje final.

Puntúa de 0 a 10.

Conserva:

- progreso importante
- eventos relevantes
- explicaciones útiles
- momentos divertidos
- descubrimientos
- combates importantes

Elimina:

- silencios
- repeticiones
- caminar sin objetivo
- gestión aburrida de inventario
- esperas
- errores

Debes responder SOLO JSON.

Formato:

{
    "score": 0,
    "keep": true,
    "reason": ""
}
"""


def analyze_chunk(chunk):

    text = "\n".join(
        seg["text"]
        for seg in chunk["segments"]
    )

    prompt = f"""
{SYSTEM_PROMPT}

INICIO DEL BLOQUE

{text}

FIN DEL BLOQUE
"""

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json"
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=300
        )

        response.raise_for_status()

        result = response.json()

        answer = result["response"]

        data = json.loads(answer)

        return {
            "start": chunk["start"],
            "end": chunk["end"],
            "score": data.get("score", 0),
            "keep": data.get("keep", False),
            "reason": data.get("reason", "")
        }

    except Exception as error:

        print(
            f"[ERROR] Gemma falló: {error}"
        )

        return {
            "start": chunk["start"],
            "end": chunk["end"],
            "score": 0,
            "keep": False,
            "reason": "error"
        }