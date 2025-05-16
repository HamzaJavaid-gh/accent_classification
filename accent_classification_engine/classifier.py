import os
from typing import Tuple
from speechbrain.pretrained.interfaces import foreign_class
from .audio_utils import convert_to_wav_if_needed

# Load the classifier using the pretrained SpeechBrain model
classifier = foreign_class(
    source="Jzuluaga/accent-id-commonaccent_xlsr-en-english",
    pymodule_file="custom_interface.py",  # fallback path handled inside SpeechBrain
    classname="CustomEncoderWav2vec2Classifier"
)

def classify_accent(file_path: str) -> Tuple[str, float, float]:
    """
    Classifies the accent of a given audio or video file.

    Args:
        file_path (str): Path to the audio or video file (.wav, .mp3, .mp4, etc.)

    Returns:
        Tuple[str, float, float]: 
            - label (str): predicted accent label (e.g., "English-Australian")
            - probability (float): model's confidence in the predicted class
            - score (float): internal score assigned by the model
    """
    wav_path = convert_to_wav_if_needed(file_path)
    out_prob, score, index, text_lab = classifier.classify_file(wav_path)
    return text_lab, out_prob, score

def classify_media(file_path: str) -> Tuple[str, float, float]:
    """
    Classifies a media file and prints the predicted accent label.

    Args:
        file_path (str): Path to the audio or video file.

    Returns:
        Tuple[str, float, float]: same as classify_accent()
    """
    label, prob, score = classify_accent(file_path)
    return label, prob, score.item()
