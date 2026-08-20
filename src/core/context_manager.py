from typing import List, Dict

class ContextManager:
    """Manages short-term and long-term conversation memory."""
    
    def __init__(self, max_history: int = 20):
        self.history: List[Dict[str, str]] = []
        self.max_history = max_history

    def add_message(self, role: str, content: str):
        """Appends a message to the context history."""
        self.history.append({"role": role, "content": content})
        if len(self.history) > self.max_history:
            self.history.pop(0)

    def get_history(self) -> List[Dict[str, str]]:
        """Returns the current conversation context."""
        return self.history
        
    def clear(self):
        """Clears the conversational context."""
        self.history = []
