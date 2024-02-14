import streamlit as st
import os
from streamlit_app.MusicLM.MusicLM import Music

st.title("QM/MAI MVP")
# Soft-fix given dotenv not working
os.environ["TOKEN"] = ""

if st.button("Generate"):
    music = Music()
    input = "Ambient, soft sounding music I can study to"
    tracks = music.get_tracks(input, 2)

    if isinstance(tracks, list):
        music.b64toMP3(tracks, input)
