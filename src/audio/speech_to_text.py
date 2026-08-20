import speech_recognition as sr
import os
import logging

logger = logging.getLogger("AuraMain")

def listen_continuously() -> str:
    """
    Listens using the microphone and transcribes via Google's free STT API.
    Returns transcribed text when speech is detected.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        logger.info("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=1)
        logger.info("Listening...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            text = r.recognize_google(audio)
            return text.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            logger.debug("Could not understand audio")
            return ""
        except sr.RequestError as e:
            logger.error(f"Could not request results from Google STT API; {e}")
            return ""

def transcribe_audio_file(filepath: str) -> str:
    """Transcribes a specific audio file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Audio file not found: {filepath}")
    
    r = sr.Recognizer()
    with sr.AudioFile(filepath) as source:
        audio = r.record(source)
    try:
        return r.recognize_google(audio).lower()
    except Exception as e:
        logger.error(f"Failed to transcribe file: {e}")
        return ""
