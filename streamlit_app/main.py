import os
from MusicLM.MusicLM import Music

# Soft-fix given dotenv not working
os.environ["TOKEN"] = ""

music = Music()
input = "Ambient, soft sounding music I can study to"
tracks = music.get_tracks(input, 2)

if isinstance(tracks, list):
    music.b64toMP3(tracks, input)
