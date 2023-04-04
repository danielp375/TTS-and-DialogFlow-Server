from TTS.api import TTS #TTS api for converting text to speech
from settings import MODEL_NAME, CONFIG_PATH, OUTPUT_FILE #Importing model path, config path and output path

#Creating the TTS object using Trained model and config file
tts = TTS(model_path=MODEL_NAME,config_path=CONFIG_PATH,progress_bar=False, gpu=False)
 #Converting text to speech when method is called and saving file as output.wav
def process_message(message, output_dir = OUTPUT_FILE):
    tts.tts_to_file(text=message, file_path=output_dir)
    return output_dir
    