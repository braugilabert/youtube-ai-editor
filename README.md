# 🎬 YouTube AI Editor

Editor autónomo de vídeo para YouTube basado en IA local.

Este proyecto transforma automáticamente vídeos largos (gameplays, podcasts, directos o grabaciones) en una versión mucho más corta y apta para YouTube utilizando únicamente herramientas gratuitas ejecutadas en local.

No utiliza APIs de pago.

No envía información a servicios externos.

Todo se ejecuta en tu propio ordenador.

---

# 🚀 Objetivo

Convertir automáticamente:

```text
Vídeo de 3 horas
```

en algo parecido a:

```text
Vídeo de 30-60 minutos
```

eliminando:

- silencios
- tiempos muertos
- errores
- pausas largas
- repeticiones

y conservando:

- progreso importante
- momentos divertidos
- explicaciones relevantes
- descubrimientos
- eventos clave

---

# 🧠 Tecnologías Utilizadas

## Ollama

Ejecuta el modelo local.

Modelo principal:

```bash
gemma3:12b-it-qat
```

Opcional:

```bash
llama3.1:8b
```

---

## Faster Whisper

Convierte automáticamente el audio del vídeo en texto.

```text
Video
↓
Audio
↓
Transcripción
```

---

## Gemma 3

Actúa como editor virtual.

Analiza bloques de aproximadamente 2 minutos y decide:

- conservar
- eliminar
- puntuar interés

Ejemplo:

```json
{
  "score": 8,
  "keep": true,
  "reason": "evento importante"
}
```

---

## FFmpeg

Realiza los cortes reales del vídeo.

```text
Segmentos seleccionados
↓
Corte
↓
Montaje
↓
Exportación
```

---

# ✅ Características actuales

La versión actual incorpora:

✅ Transcripción automática con Faster Whisper

✅ Compatibilidad CPU y GPU

✅ División automática en bloques

✅ Análisis mediante Gemma 3

✅ Recuperación de JSON roto

✅ Gestión de errores

✅ Fusión automática de segmentos consecutivos

✅ Limpieza automática de archivos temporales

✅ Renderizado automático del vídeo final

✅ Métricas de duración

✅ Métricas de tiempo de proceso

✅ Funcionamiento completamente local

---

# 📂 Estructura del Proyecto

```text
youtube-ai-editor/

├── run.py
├── config.py
├── requirements.txt

├── input/
│   └── video.mp4

├── output/

├── transcripts/

├── analysis/

└── modules/

    ├── __init__.py

    ├── transcriber.py
    ├── chunker.py
    ├── ollama_editor.py
    ├── analyzer.py
    └── ffmpeg_tools.py
```

---

# ⚙️ Instalación

## 1. Python

Versión recomendada:

```text
Python 3.10+
```

---

## 2. Ollama

Descargar:

```text
https://ollama.com
```

---

## 3. Descargar Gemma

```bash
ollama pull gemma3:12b-it-qat
```

Opcional:

```bash
ollama pull llama3.1:8b
```

---

## 4. Instalar FFmpeg

Comprobar:

```bash
ffmpeg -version
```

---

## 5. Crear entorno virtual

Windows:

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux:

```bash
python -m venv .venv

source .venv/bin/activate
```

---

## 6. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# 📄 Configuración

Archivo:

```python
config.py
```

Configuración actual:

```python
VIDEO_FILE = "input/video.mp4"

WHISPER_MODEL = "large-v3"

OLLAMA_MODEL = "gemma3:12b-it-qat"

OLLAMA_URL = "http://localhost:11434/api/generate"

CHUNK_SECONDS = 120

MIN_SCORE = 7

TARGET_DURATION_MINUTES = 50

MIN_SILENCE_DURATION = 2

MIN_SILENCE_DB = -35

TRANSCRIPT_FILE = "transcripts/transcript.json"

CHUNKS_FILE = "analysis/chunks.json"

DECISIONS_FILE = "analysis/decisions.json"

SEGMENTS_FILE = "analysis/segments.json"

OUTPUT_VIDEO = "output/final_video.mp4"
```

---

# ▶️ Uso

Colocar el vídeo dentro de:

```text
input/video.mp4
```

Después:

```bash
python run.py
```

---

# 🔄 Flujo Completo

## Paso 1

Whisper transcribe el vídeo.

Resultado:

```text
transcripts/transcript.json
```

---

## Paso 2

La transcripción se divide en bloques de aproximadamente:

```text
2 minutos
```

Resultado:

```text
analysis/chunks.json
```

---

## Paso 3

Gemma analiza cada bloque.

Ejemplo:

```json
{
  "score": 9,
  "keep": true,
  "reason": "descubrimiento importante"
}
```

Resultado:

```text
analysis/decisions.json
```

---

## Paso 4

Se conservan únicamente los bloques aprobados.

Resultado:

```text
analysis/segments.json
```

Ejemplo:

```json
[
  {
    "start": 0,
    "end": 120
  },
  {
    "start": 340,
    "end": 600
  }
]
```

---

## Paso 5

Los segmentos cercanos se fusionan automáticamente.

Antes:

```json
[
  {
    "start": 0,
    "end": 120
  },
  {
    "start": 121,
    "end": 240
  }
]
```

Después:

```json
[
  {
    "start": 0,
    "end": 240
  }
]
```

---

## Paso 6

FFmpeg:

- corta
- une
- exporta

Resultado:

```text
output/final_video.mp4
```

---

# 📁 Archivos Generados

## transcript.json

Contiene la transcripción completa.

---

## chunks.json

Contiene la división de la transcripción.

---

## decisions.json

Contiene las decisiones tomadas por Gemma.

Ejemplo:

```json
{
  "score": 2,
  "keep": false,
  "reason": "tiempo muerto"
}
```

---

## segments.json

Contiene únicamente los fragmentos aprobados.

---

## final_video.mp4

Vídeo final exportado.

---

# 📊 Rendimiento esperado

Equipo de referencia:

```text
RTX 3060 / 4060
32 GB RAM
```

Vídeo de:

```text
3 horas
```

Tiempo aproximado:

### Whisper

```text
10-40 min
```

### Gemma

```text
10-30 min
```

### Exportación

```text
10-30 min
```

### Tiempo total

```text
30-100 min
```

Dependiendo del hardware.

---

# ⚠️ Limitaciones actuales

La IA trabaja únicamente con texto.

Actualmente NO analiza:

- imagen
- escenas
- inventario
- expresiones faciales
- HUD
- mapas
- combates silenciosos
- eventos visuales

Por lo tanto puede perder momentos importantes si no se hablan durante el vídeo.

---

# 🚧 Roadmap V2

Próximas mejoras previstas:

✅ Detección automática de silencios

✅ Eliminación automática de pausas largas

✅ Segmentos internos más precisos

✅ Detección de repeticiones

✅ Mejor reducción de duración

✅ Exportación optimizada

Objetivo:

```text
3 horas
↓
30-50 minutos
```

---

# 🚧 Roadmap V3

Automatización para YouTube:

- título automático
- descripción automática
- hashtags
- capítulos
- metadatos SEO

---

# 🚧 Roadmap V4

Integración futura con:

- FilmCraft
- MCP
- Agentes autónomos

---

# 🎯 Estado actual

Versión actual:

```text
Video
↓
Whisper
↓
Gemma
↓
FFmpeg
↓
Video final
```

Versión futura:

```text
Video
↓
Whisper
↓
Detección silencios
↓
Gemma
↓
Refinado avanzado
↓
FFmpeg
↓
Video optimizado
```

---

# 🎯 Visión Final

Construir un editor autónomo capaz de:

```text
Video bruto
↓
Transcripción
↓
Análisis IA
↓
Selección automática
↓
Montaje
↓
Exportación
↓
Título
↓
Descripción
↓
Capítulos
↓
Listo para YouTube
```

Todo local.

Todo gratuito.

Todo basado en software libre y modelos abiertos.