import json
import re
import requests

from config import (
    OLLAMA_MODEL,
    OLLAMA_URL
)


SYSTEM_PROMPT = """
Eres un editor profesional de YouTube especializado
en gameplays y videos hablados.

Tu tarea consiste en determinar si el fragmento
de transcripción merece mantenerse en la edición final.

Puntúa cada bloque de 0 a 10.

CRITERIOS PARA CONSERVAR:

- progreso importante
- eventos clave
- descubrimientos
- combates importantes
- explicaciones útiles
- momentos divertidos
- momentos con emoción

CRITERIOS PARA ELIMINAR:

- silencios
- tiempos muertos
- repetir información
- caminar sin objetivo
- gestión rutinaria de inventario
- esperas innecesarias
- errores

RESPONDE EXCLUSIVAMENTE JSON.

Formato obligatorio:

{
    "score": 0,
    "keep": true,
    "reason": ""
}

No escribas texto adicional.
"""


def extract_json(text):

    match = re.search(
        r"\{.*\}",
        text,
        flags=re.DOTALL
    )

    if not match:
        raise ValueError(
            "No se encontró JSON válido"
        )

    return json.loads(
        match.group()
    )


def build_prompt(chunk):

    transcript_text = "\n".join(
        segment["text"]
        for segment in chunk["segments"]
    )

    return f"""
{SYSTEM_PROMPT}

BLOQUE A ANALIZAR

Duración aproximada:
{chunk["duration"]} segundos

Contenido:

{transcript_text}

FIN DEL BLOQUE
"""


def call_ollama(prompt):

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json"
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=600
    )

    response.raise_for_status()

    return response.json()


def analyze_chunk(chunk):

    try:

        prompt = build_prompt(
            chunk
        )

        response = call_ollama(
            prompt
        )

        raw_answer = response.get(
            "response",
            "{}"
        )

        parsed = extract_json(
            raw_answer
        )

        score = int(
            parsed.get(
                "score",
                0
            )
        )

        score = max(
            0,
            min(
                score,
                10
            )
        )

        keep = bool(
            parsed.get(
                "keep",
                False
            )
        )

        reason = str(
            parsed.get(
                "reason",
                ""
            )
        )

        return {
            "start": chunk["start"],
            "end": chunk["end"],
            "score": score,
            "keep": keep,
            "reason": reason
        }

    except Exception as error:

        print()
        print(
            "[ERROR] Fallo analizando bloque"
        )

        print(
            str(error)
        )

        print()

        return {
            "start": chunk["start"],
            "end": chunk["end"],
            "score": 0,
            "keep": False,
            "reason": "error"
        }