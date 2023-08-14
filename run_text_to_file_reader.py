import os
import sys
import torch

from InferenceInterfaces.ToucanTTSInterface import ToucanTTSInterface


def read_texts(model_id, sentence, filename, device="cpu", language="pie", speaker_reference=None, faster_vocoder=False):
    tts = ToucanTTSInterface(device=device, tts_model_path=model_id, faster_vocoder=faster_vocoder)
    tts.set_language(language)
    if speaker_reference is not None:
        tts.set_utterance_embedding(speaker_reference)
    if type(sentence) == str:
        sentence = [sentence]
    tts.read_to_file(text_list=sentence, file_location=filename)
    del tts
    
#ADDED BY VICKY IVOVA, AUGUST 2023
#Used for command line inference
def custom(version, model_id="MultiAbkhaz", exec_device="cpu", speed_over_quality=True, speaker_reference=None):
    os.makedirs("audios", exist_ok=True)
    file_name = input("\What should the file be named? (or 'exit')\n")
    if file_name == "exit":
        sys.exit()
    sentence = input("\nWhat should I say? (or 'exit')\n")
    if sentence == "exit":
        sys.exit()
    read_texts(model_id=model_id,
                sentence=sentence,
                filename=file_name,
                device=exec_device,
                language="pie",
                speaker_reference=speaker_reference,
                faster_vocoder=speed_over_quality)

#ADDED BY VICKY IVOVA, AUGUST 2023
#Called in the app script              
def custom_app(file_name, sentence, version="MetaBaseline", model_id="MultiAbkhaz", exec_device="cpu", speed_over_quality=True, speaker_reference=None):
    os.makedirs("audios", exist_ok=True)
    read_texts(model_id=model_id,
                sentence=sentence,
                filename=file_name,
                device=exec_device,
                language="pie",
                speaker_reference=speaker_reference,
                faster_vocoder=speed_over_quality)


if __name__ == '__main__':
    exec_device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"running on {exec_device}")

    custom(version="MetaBaseline",
              model_id="MultiAbkhaz",
              exec_device=exec_device,
              speed_over_quality=exec_device != "cuda")
