#WRITTEN BY VICKY IVOVA, AUGUST 2023
#WEB APP - piesynthesis.streamlit.app

import streamlit as st

import os
import sys
import torch
import base64
import random
from run_text_to_file_reader import read_texts,custom_app


#Setting the background
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


st.set_page_config(page_title="Synthesise PIE", page_icon=":smiley:", layout="wide", theme="light")
st.write("Bring to life the ancient extinct language from which most European languages evolved.\n Write down a Proto-Indo-European sentence in PIE standard notation or try the sample sentence. You can choose the model behind the synthesis: one trained on European languages (pre-trained) or one further fine-tuned on Abkhaz (fine-tuned). Hit 'Synthesise' and wait for your synthesised audio!")

#Text input
user_input = st.text_input("Enter PIE text:", "Tór h₃rēǵs h₁ést. Só h₂népotlos h₁ést. Só h₃rēǵs suHnúm welh₁t.")

#Default file name for storage
file_name = "synth_app_audios/default_synth_web_app.wav"

#Model radials
selected_model = st.radio("Select which model to use: ", ("Pre-trained model", "Fine-tuned model"))

if selected_model == "Pre-trained model":
    model_input = "Meta"
elif selected_model == "Fine-tuned model":
    model_input = "MultiAbkhaz"
else:
    model_input = "MultiAbkhaz"

#Synthesise, save, open, play
if user_input: 
  if st.button("Synthesise"):
    synthesized_text = custom_app(file_name, user_input, model_id=model_input)
    st.success("Text synthesised!")
    audio_file = open(file_name, "rb")
    audio_bytes  = audio_file.read()
    st.audio(audio_bytes, format="audio/wav")
else:
  st.warning("Please input valid PIE text.")



