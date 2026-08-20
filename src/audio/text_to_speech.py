import pyttsx3
import logging

logger = logging.getLogger("AuraMain")

def speak(text: str):
    """
    Uses local pyttsx3 Text-To-Speech engine to speak the provided text.
    """
    logger.info(f"Assistant: {text}")
    try:
        engine = pyttsx3.init()
        # Optional: Configure voice rate and properties
        engine.setProperty('rate', 160)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        logger.error(f"TTS Error: {e}")
