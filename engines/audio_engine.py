from gtts import gTTS
import os

def generate_audio(script_lines, output_dir):
    """
    Generates MP3 files for each line of the script.
    Returns a list of file paths.
    """
    audio_paths = []
    for i, text in enumerate(script_lines):
        tts = gTTS(text=text, lang='en')
        filename = os.path.join(output_dir, f"audio_{i}.mp3")
        tts.save(filename)
        audio_paths.append(filename)
        print(f"Generated audio: {filename}")
    
    return audio_paths
