import os

class WakeWordDetector:
    """Listens continuously in the background for a specific wake word."""
    
    def __init__(self):
        self.wake_word = os.getenv("WAKE_WORD", "omni").lower()
        
    def detect(self, audio_stream) -> bool:
        """Analyzes an audio stream chunk to detect the wake word."""
        # Implementation using Porcupine or pocketsphinx goes here.
        return False
