import time
from .nlp_processor import NLPProcessor
from .context_manager import ContextManager
from audio.speech_to_text import listen_continuously
from audio.text_to_speech import speak
from automation.system_ops import execute_system_command

class OmniEngine:
    """Core orchestrator for the Voice Assistant."""
    
    def __init__(self):
        self.nlp = NLPProcessor()
        self.context = ContextManager()
        self.is_running = False

    def start(self):
        """Starts the main event loop listening for commands."""
        self.is_running = True
        print("Engine started. Listening for wake word...")
        speak("Aura system online and ready.")
        
        while self.is_running:
            # In a real scenario, this would be an async stream.
            text = listen_continuously()
            if text:
                print(f"Heard: {text}")
                self.process_command(text)
            time.sleep(0.1)

    def process_command(self, text: str):
        """Processes a transcribed command and executes the corresponding action."""
        self.context.add_message("user", text)
        intent = self.nlp.extract_intent(text, self.context.get_history())
        
        if intent.get("action") == "system_op":
            response = execute_system_command(intent.get("parameters", {}))
            speak(response)
        else:
            speak("I'm not sure how to handle that yet.")
            
    def stop(self):
        """Stops the engine gracefully."""
        self.is_running = False
        print("Engine stopped.")
