import os
import tempfile
import pytest
import torch
from accent_classification_engine.classifier import classify_accent
from accent_classification_engine.audio_utils import convert_to_wav_if_needed

@pytest.fixture
def sample_audio_file():
    return "accent_classification/resources/audio/english_uk.mp3"  # Ensure this file exists in your repo

def test_convert_to_wav_if_needed_audio(sample_audio_file):
    result_path = convert_to_wav_if_needed(sample_audio_file)
    assert result_path.endswith(".wav")
    assert os.path.exists(result_path)

def test_classify_accent_output_types(sample_audio_file):
    label, prob, score = classify_accent(sample_audio_file)
    assert isinstance(label, (str, list))
    assert isinstance(prob, float)
    assert isinstance(score, torch.Tensor)

def test_classify_accent_confidence_range(sample_audio_file):
    _, prob, _ = classify_accent(sample_audio_file)
    assert 0.0 <= prob <= 1.0

def test_classify_accent_result(sample_audio_file):
    label, prob, score = classify_accent(sample_audio_file)
    assert label  # Not empty
    assert score.item() > 0.0