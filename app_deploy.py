import streamlit as st

import os
import sys
import torch
import base64
import random
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

set_png_as_page_bg("/mount/src/pie_synthesis/app_background.png")

st.title("Synthesise PIE")
st.write("Bring to life the ancient extinct language from which most European languages evolved.\n Write down a Proto-Indo-European sentence in PIE standard notation or choose one of the sample sentences. You can choose the model behind the synthesis: one trained on European languages (pre-trained) or one further fine-tuned on Abkhaz (fine-tuned). Hit 'Synthesise' and wait for your synthesised audio!")


example_input = {
    "The King and the God poem": "Tór h3re?s h1ést. Só h2népotlos h1ést. Só h3re?s suHnúm welh1t.",
    "Your daughter has come home.": "D?ugh2ter toi dom g?eg?ome.",
}

for label, input_value in example_input.items():
    if st.button(label):
        input_to_fill = input_value
        st.write(input_to_fill)
    else:
        input_to_fill = ""
        
text_input = st.text_input("Enter text to synthesize", "")

if input_to_fill:
    user_input = input_to_fill
else: 
    user_input = text_input
    
file_name = "synth_app_audios/default_synth_web_app.wav"

selected_model = st.radio("Select which model to use: ", ("Pre-trained model", "Fine-tuned model"))

if selected_model == "Pre-trained model":
    model_input = "Meta"
elif selected_model == "Fine-tuned model":
    model_input = "MultiAbkhaz"
else:
    model_input = "MultiAbkhaz"


if st.button("Synthesise"):
	if user_input:
		synthesized_text = custom_app(file_name, user_input, model_id=model_input)
		st.success("Text synthesised!")
		audio_file = open(file_name, "rb")
		audio_bytes  = audio_file.read()

		#st.audio(synthesized_text, format="audio/wav")
		st.audio(audio_bytes, format="audio/wav")

	else:
		st.warning("Please enter valid PIE text.")

