<p align="center">
  <img src="https://quickcall.dev/assets/v1/qc-full-512px-white.png" alt="QuickCall" width="400">
</p>

<h3 align="center">QuickCall VoiceOver</h3>

<p align="center">
  <em>Utility tool for creating voice-over audio assets for QuickCall videos</em>
</p>

<p align="center">
  <a href="https://pypi.org/project/quickcall-voiceover/"><img src="https://img.shields.io/pypi/v/quickcall-voiceover?color=blue" alt="PyPI"></a>
  <a href="https://github.com/quickcall-dev/quickcall-voiceover/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-green" alt="License"></a>
  <a href="https://quickcall.dev"><img src="https://img.shields.io/badge/Web-quickcall.dev-000000?logo=googlechrome&logoColor=white" alt="Web"></a>
  <a href="https://discord.gg/DtnMxuE35v"><img src="https://img.shields.io/badge/Discord-Join%20Us-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
</p>

<p align="center">
  <a href="#install">Install</a> |
  <a href="#quick-start">Quick Start</a> |
  <a href="#cli-options">CLI Options</a> |
  <a href="#voice-models">Voice Models</a> |
  <a href="#configuration">Configuration</a> |
  <a href="#docker">Docker</a> |
  <a href="#license">License</a>
</p>

---

## Install

```bash
uv pip install quickcall-voiceover
```

Or with pip:

```bash
pip install quickcall-voiceover
```

## Quick Start

### Config Mode

Create a JSON config file with your segments:

```bash
quickcall-voiceover config.json --combine
```

### Text Mode (Interactive)

Generate voice-over from text lines interactively:

```bash
quickcall-voiceover --text
```

### Show Available Voices

```bash
quickcall-voiceover --voices
```

## CLI Options

```
quickcall-voiceover [CONFIG] [OPTIONS]

Arguments:
  CONFIG                Path to JSON configuration file

Options:
  -t, --text            Interactive text mode (line by line input)
  -o, --output DIR      Output directory (default: ./output)
  -m, --models DIR      Models directory (default: ./models)
  -c, --combine         Create a combined audio file from all segments
  --combined-name       Filename for combined output (default: combined_voiceover.wav)
  --voices              Show available voice models and exit
  -h, --help            Show help message
```

### Examples

```bash
# Generate from config file
quickcall-voiceover voiceover.json

# Generate and combine into one file
quickcall-voiceover voiceover.json --combine

# Interactive text mode
quickcall-voiceover --text

# Show available voices
quickcall-voiceover --voices
```

## Voice Models

Popular voice models available:

| Model ID | Name | Description |
|----------|------|-------------|
| `en_US-hfc_male-medium` | Male (US) | Clear male voice (default) |
| `en_US-hfc_female-medium` | Female (US) | Clear female voice |
| `en_US-amy-medium` | Amy (US) | Natural female voice |
| `en_US-joe-medium` | Joe (US) | Natural male voice |
| `en_US-ryan-high` | Ryan (US) | High quality male voice |
| `en_US-lessac-high` | Lessac (US) | High quality female voice |
| `en_GB-alan-medium` | Alan (UK) | British male voice |
| `en_GB-alba-medium` | Alba (UK) | British female voice |
| `en_GB-cori-high` | Cori (UK) | High quality British female |

Browse all voices at [Piper samples](https://rhasspy.github.io/piper-samples/).

## Configuration

### Config File Format

```json
{
  "voice": {
    "model": "en_US-hfc_male-medium",
    "length_scale": 1.0,
    "noise_scale": 0.667,
    "noise_w": 0.8,
    "sentence_silence": 0.5
  },
  "output": {
    "format": "wav"
  },
  "segments": [
    {
      "id": "01_intro",
      "text": "Welcome to the demo."
    },
    {
      "id": "02_main",
      "text": "This is the main content."
    },
    {
      "id": "03_outro",
      "text": "Thanks for watching!"
    }
  ]
}
```

### Voice Settings

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `model` | string | `en_US-hfc_male-medium` | Piper voice model name |
| `length_scale` | float | `1.0` | Speech speed (lower = faster) |
| `noise_scale` | float | `0.667` | Voice variation |
| `noise_w` | float | `0.8` | Phoneme width noise |
| `sentence_silence` | float | `0.5` | Silence between sentences (seconds) |

### Segment Format

Each segment requires:
- `id`: Unique identifier (used as filename)
- `text`: The text to convert to speech

## Programmatic Usage

```python
from pathlib import Path
from quickcall_voiceover import generate_voiceover, generate_from_text

# From config file
generate_voiceover(
    config_path=Path("voiceover.json"),
    output_dir=Path("./output"),
    combine=True,
)

# From text lines
lines = [
    "First line of voice over.",
    "Second line of voice over.",
    "Final line."
]

generate_from_text(
    lines=lines,
    voice="en_US-hfc_male-medium",
    output_dir=Path("./output"),
    combine=True,
)
```

## Docker

Build the image:

```bash
docker build -t quickcall-voiceover .
```

Run with a config file:

```bash
docker run -v $(pwd)/config:/config -v $(pwd)/output:/app/output \
  quickcall-voiceover /config/voiceover.json --combine
```

## License

This project is licensed under Apache-2.0.

**Note:** This tool depends on [Piper TTS](https://github.com/OHF-Voice/piper1-gpl) which is licensed under GPL-3.0. Piper is installed as a separate dependency and is not bundled with this package.

---

<p align="center">
  Built with ❤️ by <a href="https://quickcall.dev">QuickCall</a>
</p>
