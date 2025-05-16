import os
import subprocess

# Supported extensions for audio and video files
SUPPORTED_AUDIO_EXT = [".wav", ".mp3"]
SUPPORTED_VIDEO_EXT = [".mp4", ".mov", ".avi", ".mkv"]

def convert_to_wav_if_needed(file_path: str) -> str:
    """
    Converts a given audio or video file to a mono-channel 16kHz WAV file,
    which is required by the SpeechBrain classifier.

    If the input file is already a WAV file, it is returned as-is.
    If a converted version already exists, it is reused.

    Args:
        file_path (str): Path to the audio or video file

    Returns:
        str: Path to the converted (or original) .wav file

    Raises:
        RuntimeError: If FFmpeg fails to convert the file
    """
    base, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext == ".wav":
        return file_path

    output_path = base + "_converted.wav"
    if os.path.exists(output_path):
        return output_path

    command = [
        "ffmpeg",
        "-i", file_path,
        "-ar", "16000",  # Required sample rate
        "-ac", "1",      # Mono
        output_path,
        "-y"
    ]

    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"FFmpeg failed to convert {file_path}: {e.stderr.decode()}")

    return output_path
