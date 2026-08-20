import os

def listen_continuously() -> str:
    """
    Simulates continuous listening using PyAudio and SpeechRecognition.
    Returns transcribed text when speech is detected.
    """
    # In a real implementation, this would use speech_recognition library:
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     audio = r.listen(source)
    #     return r.recognize_google(audio)
    return ""

def transcribe_audio_file(filepath: str) -> str:
    """Transcribes a specific audio file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Audio file not found: {filepath}")
    return "Dummy transcription"
