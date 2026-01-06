"""Command-line interface for QuickCall VoiceOver."""

import argparse
import sys
from pathlib import Path

from quickcall_voiceover.generator import generate_voiceover


def main() -> int:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="quickcall-voiceover",
        description="Generate voice-over audio from a config file using Piper TTS",
    )
    parser.add_argument(
        "config",
        type=Path,
        help="Path to the JSON configuration file",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output directory for generated audio files (default: ./output)",
    )
    parser.add_argument(
        "-m",
        "--models",
        type=Path,
        default=None,
        help="Directory for voice models (default: ./models)",
    )
    parser.add_argument(
        "-c",
        "--combine",
        action="store_true",
        help="Also create a single combined audio file from all segments",
    )
    parser.add_argument(
        "--combined-name",
        type=str,
        default="combined_voiceover.wav",
        help="Filename for the combined output (default: combined_voiceover.wav)",
    )

    args = parser.parse_args()

    if not args.config.exists():
        print(f"Error: Config file not found: {args.config}")
        return 1

    success = generate_voiceover(
        config_path=args.config,
        output_dir=args.output,
        models_dir=args.models,
        combine=args.combine,
        combined_filename=args.combined_name,
    )

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
