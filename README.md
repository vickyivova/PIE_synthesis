# PIE_synthesis 📜🏺🗡️
**Visit the web app:** https://piesynthesis.streamlit.app/

This repository is almost entirely comprised of the original code of IMS-Toucan by Florian Lux and Julia Koch and Ngoc Thang Vu. 
The changes made include:
1. Adding preprocessing methods for Abkhaz and Proto-Indo-European
2. Adjusting the provided fine-tuning script in order to fine-tune on Abkhaz data
3. A fine-tuned on Abkhaz version of the provided pre-trained multilanguage model
4. Adjusted read-to-file inference script in order to infer PIE
5. A new script that deploys a web app for easy, user-friendly PIE synthesis

In order to operate this toolkit, you need to fist create a virtual environment and install the requirements:
```
python -m venv <path_to_where_you_want_your_env_to_be>

source <path_to_where_you_want_your_env_to_be>/bin/activate

pip install --no-cache-dir -r requirements.txt
```
Since not the Abkhaz, nor the Proto-Indo-European preprocessing uses espeak-ng, you do not need to install it if you only use the toolkit for
PIE inference or to test the fine-tuning pipeline.

Once you have activated the environment you can navigate towards the top level and run the following command to synthesise PIE from the command line:
```
python run_text_to_file_reader.py
```
This will activate user input prompts where you can enter the name/path of the file that you want to save the synthesised speech (include .wav in the name)
and enter the text you want synthesised. Only standard PIE notation is recognised by the model. You cam try this example sentence:

**Dʰúɡh₂tēr toj dōm gʷegʷome.**
It means "Your daughter has come home."!

It is more user friendly to use the web app with this domain to obtain synthesised speech with the model: https://piesynthesis.streamlit.app/
There you can easily choose whether to use the pre-trained model or the fine-tuned model and input the text you want synthesised. You can also use
the pre-filled example sentence, which is the beginning of the poem "The King and the God", created by linguist following reconstruction rules.

There is also a jobscript tailored to be used in the system of the University of Groningen computer cluster Habrok. By submitting it, you can start
the fine-tuning of the multi-language model using one GPU. You can do that by running this command from the top level:
```
sbatch sbatch abkhaz_finetune.sh
```
Have fun listening to the past!
