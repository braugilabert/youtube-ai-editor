# 🎬 YouTube AI Editor

Editor de vídeo autónomo local basado en IA.

El objetivo de este proyecto es transformar automáticamente vídeos largos (gameplays, podcasts, directos o grabaciones) en una versión mucho más corta y apta para YouTube utilizando únicamente herramientas gratuitas y ejecutadas en local.

---

# 🚀 Objetivo

Convertir automáticamente:

```text
Vídeo de 3 horas
```

en:

```text
Vídeo de 30-60 minutos
```

eliminando:

- silencios
- tiempos muertos
- repeticiones
- errores
- pausas innecesarias

manteniendo:

- progreso importante
- momentos divertidos
- explicaciones útiles
- eventos relevantes

Todo ello sin APIs de pago.

---

# 🧠 Tecnologías Utilizadas

## Ollama

Ejecuta el modelo local.

Modelo recomendado:

```text
gemma3:12b-it-qat
```

---

## Faster Whisper

Responsable de convertir el audio del vídeo en texto.

```text
Vídeo → Transcripción
```

---

## Gemma 3

Actúa como editor.

Analiza cada parte de la transcripción y decide:

```text
Conservar
o
Eliminar
```

---

## FFmpeg

Realiza los cortes reales sobre el vídeo.

```text
Segmentos elegidos
↓
Vídeo final
```

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

## 1. Instalar Python

Versión recomendada:

```text
Python 3.10 o superior
```

---

## 2. Instalar Ollama

Descargar desde:

https://ollama.com

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

## 5. Instalar dependencias

Crear entorno virtual:

```bash
python -m venv .venv
```

Activar:

Windows:

```bash
.venv\Scripts\activate
```

Linux:

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

# 📄 Configuración

Editar:

```python
config.py
```

Opciones principales:

```python
VIDEO_FILE = "input/video.mp4"

WHISPER_MODEL = "large-v3"

OLLAMA_MODEL = "gemma3:12b-it-qat"

CHUNK_SECONDS = 300

MIN_SCORE = 7

TARGET_DURATION_MINUTES = 50
```

---

# ▶️ Uso

Colocar el vídeo a editar:

```text
input/video.mp4
```

Ejecutar:

```bash
python run.py
```

---

# 🔄 Flujo Interno

## Paso 1

Whisper genera:

```text
transcripts/transcript.json
```

Ejemplo:

```json
{
  "start": 0,
  "end": 4,
  "text": "Hola chicos bienvenidos."
}
```

---

## Paso 2

La transcripción se divide en bloques:

```text
0-5 min

5-10 min

10-15 min
```

---

## Paso 3

Gemma analiza cada bloque.

Respuesta típica:

```json
{
  "score": 8,
  "keep": true,
  "reason": "evento importante"
}
```

---

## Paso 4

Se guardan las decisiones:

```text
analysis/decisions.json
```

---

## Paso 5

Se generan los segmentos:

```text
analysis/segments.json
```

Ejemplo:

```json
[
  {
    "start": 0,
    "end": 300
  },
  {
    "start": 1200,
    "end": 1500
  }
]
```

---

## Paso 6

FFmpeg corta y une los vídeos.

Resultado:

```text
output/final_video.mp4
```

---

# 📁 Archivos Generados

## transcript.json

Contiene toda la transcripción.

---

## chunks.json

Contiene la división en bloques.

---

## decisions.json

Contiene todas las decisiones de Gemma.

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

Contiene únicamente los bloques aprobados.

---

## final_video.mp4

Versión final editada.

---

# ⚠️ Limitaciones Actuales

La V1 es funcional, pero tiene limitaciones:

- Analiza bloques completos de 5 minutos.
- No entiende imágenes.
- No entiende lo que sucede visualmente en el juego.
- No detecta eventos épicos automáticamente.
- No reconoce expresiones faciales.
- No genera subtítulos.

---

# 🚧 Roadmap V2

## Eliminación automática de silencios

Integrar:

```bash
ffmpeg -af silencedetect
```

---

## Edición más precisa

Permitir que Gemma devuelva:

```json
{
  "start": 121,
  "end": 166
}
```

en lugar de bloques completos.

---

## Objetivo

Pasar de:

```text
3 horas
↓
1 hora
```

a:

```text
3 horas
↓
30-50 minutos
```

---

# 🚧 Roadmap V3

Generación automática de:

- título
- descripción
- hashtags
- capítulos

para YouTube.

---

# 🚧 Roadmap V4

Integración futura con:

- FilmCraft
- MCP
- Agentes autónomos

---

# 🎯 Objetivo Final

Construir un editor de vídeo completamente autónomo capaz de:

```text
Vídeo bruto
↓
Transcripción
↓
Análisis IA
↓
Selección automática
↓
Edición
↓
Exportación
↓
Título y descripción
↓
Listo para YouTube
```

Todo local.

Todo gratuito.

Todo basado en modelos abiertos.