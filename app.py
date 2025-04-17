import streamlit as st
import time
import os
import random
from PIL import Image
from pathlib import Path
import base64

# Page configuration
st.set_page_config(page_title="🪖 PPDT Test Simulator", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS styling
st.markdown("""
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
        font-size: 2rem;
        color: white;
        background-color: black;
        border-radius: 10px;
    }
    .button-style {
        width: 100%;
        font-size: 18px;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Helper function to show full screen image
def show_fullscreen_image(img_path, duration, caption=""):
    image = Image.open(img_path)
    st.image(image, use_column_width=True, caption=caption)
    time.sleep(duration)
    st.empty()

# Play audio using base64 encoding
def play_audio(file_path):
    with open(file_path, "rb") as f:
        audio_bytes = f.read()
    audio_b64 = base64.b64encode(audio_bytes).decode()
    audio_html = f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
        </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# Show black screen with a message
def show_black_screen(message, duration):
    st.markdown(f"<div class='centered'>{message}</div>", unsafe_allow_html=True)
    time.sleep(duration)
    st.empty()

# Title
st.markdown("<h1 style='text-align: center;'>🪖 PPDT Test Simulator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Simulate Real-Time Picture Perception and Discussion Test</h4>", unsafe_allow_html=True)
st.write("")

# Main Buttons
col1, col2 = st.columns(2)
with col1:
    show_instruction = st.button("📘 Show Instructions", type="primary")
with col2:
    start_test = st.button("🚩 Start New PPDT", type="primary")

# === Instructions Flow ===
if show_instruction:
    st.info("🔍 Showing Instruction Page 1...")
    show_fullscreen_image("images/instr1.jpg", 30, "Instruction Page 1 (30 seconds)")

    st.info("🔍 Showing Instruction Page 2...")
    show_fullscreen_image("images/instr2.jpg", 30, "Instruction Page 2 (30 seconds)")

    st.success("✅ Instructions Complete! You're ready for the test.")

# === Test Flow ===
if start_test:
    st.warning("🕒 Get Ready... Test will begin shortly.")
    time.sleep(5)

    # Load random image from test image folder
    image_folder = "images"
    test_images = [f for f in os.listdir(image_folder) if f.lower().endswith((".jpg", ".png")) and "test" in f.lower()]
    selected_image = random.choice(test_images)

    # Show PPDT image
    st.info("📸 Observe the image carefully...")
    show_fullscreen_image(os.path.join(image_folder, selected_image), 20, "Observe for 20 seconds")

    # Black screen for 30 seconds
    show_black_screen("🧠 Think and prepare your story...", 30)
    play_audio("sounds/bell1.mp3")

    # Writing time: 4 minutes
    show_black_screen("📝 Write your story now (4 minutes)...", 240)
    play_audio("sounds/bell2.mp3")

    st.balloons()
    st.success("🎯 Test Finished! Well done, candidate!")

