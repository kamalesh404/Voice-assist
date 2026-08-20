import os

def load_env():
    """Simple env parser (stub for python-dotenv)."""
    # In reality, you'd use:
    # from dotenv import load_dotenv
    # load_dotenv()
    pass

class Config:
    """Central configuration store."""
    def __init__(self):
        self.wake_word = os.getenv("WAKE_WORD", "Aura")
        self.use_local_llm = os.getenv("USE_LOCAL_LLM", "False").lower() == "true"
