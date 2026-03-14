from elevenlabs.client import ElevenLabs
from config import APIKEY
import os

client = ElevenLabs(api_key=APIKEY)

# Simple TTS: generate audio bytes from text
def text_to_speech_file(text : str, folder : str) -> str:
    audio = client.text_to_speech.convert(
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_turbo_v2_5",
        text=text
    )

    save_path = os.path.join("user_uploads", folder, "output.mp3")

    with open(save_path, "wb") as f:
        for chunk in audio:
            f.write(chunk)

    return save_path

# if __name__ == "__main__":
    # print(text_to_audio("hello world", "c2523f22-1d7a-11f1-a3ee-502f9b7edf0a"))