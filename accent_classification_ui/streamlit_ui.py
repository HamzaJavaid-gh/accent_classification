import streamlit as st
st.set_page_config(page_title="Accent Classification App", layout="centered")

import tempfile
import os
from accent_classification_engine.classifier import classify_accent
from accent_classification_engine.audio_utils import SUPPORTED_AUDIO_EXT, SUPPORTED_VIDEO_EXT, convert_to_wav_if_needed

st.title("🗣️ Accent Classification App")

# --- Upload Section ---
uploaded_file = st.file_uploader("Upload an audio or video file", type=SUPPORTED_AUDIO_EXT + SUPPORTED_VIDEO_EXT)

if uploaded_file:
    ext = os.path.splitext(uploaded_file.name)[1].lower()
    is_audio = ext in SUPPORTED_AUDIO_EXT
    file_type = "Audio" if is_audio else "Video"

    st.success(f"✅ You uploaded a {file_type} file: `{uploaded_file.name}`")
    
    # Save uploaded file to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    if is_audio:
        st.audio(tmp_file_path, format="audio/wav")
    else:
        st.video(tmp_file_path)

    st.markdown("---")

    # Show supported formats
    with st.expander("📄 Supported Formats"):
        st.write("**Audio:**", ", ".join(SUPPORTED_AUDIO_EXT))
        st.write("**Video:**", ", ".join(SUPPORTED_VIDEO_EXT))

    # Classify button
    if st.button("🔍 Start Accent Classification"):
        with st.spinner("Processing... Please wait..."):
            label, prob, score = classify_accent(tmp_file_path)

        st.markdown("---")
        st.subheader("🧾 Classification Result")
        st.write(f"**Detected Accent:** `{label[0]}`")
        st.write(f"**Confidence Score:** `{score.item():.4f}`")

else:
    st.info("Please upload a valid audio or video file to begin.")
