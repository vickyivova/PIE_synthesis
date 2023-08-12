import streamlit as st

import os
import sys
import torch
import base64
from run_text_to_file_reader import read_texts,custom_app

def get_base64_of_bin_file(bin_file):
	with open(bin_file, 'rb') as f:
		data = f.read()
	return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
	bin_str = get_base64_of_bin_file(png_file)
	page_bg_img = '''
	<style>
	.stApp {
	background-image: url("data:image/png;base64,%s");
	background-size: cover;
	}
	</style>
	''' % bin_str

	st.markdown(page_bg_img, unsafe_allow_html=True)
	return

set_png_as_page_bg("/mount/src/pie_synthesis/IMS-Toucan/app_background.png")

st.title('Synthesise PIE')

# User input text box
user_input = st.text_input("Enter text to synthesize", "")
file_name = st.text_input("Enter file name (no extension)", "")
file_name = "synth_app_audios/" + file_name + ".wav"
model_input = st.text_input("Enter model ID (Meta/MultiAbkhaz)", "")

# Synthesize button
if st.button("Synthesize"):
	if user_input:
		synthesized_text = custom_app(file_name, user_input, model_id=model_input)  # Call your synthesis function
		st.success("Text synthesized and stored successfully.")
		audio_file = open(file_name, "rb")
		audio_bytes  = audio_file.read()

		st.audio(audio_bytes, format="audio/wav")

	else:
        	st.warning("Please enter valid PIE text.")

