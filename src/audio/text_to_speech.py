def speak(text: str):
    """
    Uses a Text-To-Speech engine to speak the provided text.
    Could utilize pyttsx3 (local) or ElevenLabs API (cloud).
    """
    # Real implementation:
    # engine = pyttsx3.init()
    # engine.say(text)
    # engine.runAndWait()
    print(f"Assistant: {text}")
