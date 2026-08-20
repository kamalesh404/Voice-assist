import os
import re
from typing import Dict, Any, List

class NLPProcessor:
    """Handles parsing and intent extraction using local keyword matching (Free Fallback)."""
    
    def __init__(self):
        pass
        
    def extract_intent(self, text: str, context: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        Uses keyword and regex matching to parse natural language into a structured JSON intent.
        """
        text = text.lower().strip()
        
        # Check for browser intent
        if "open" in text and ("browser" in text or "chrome" in text or "firefox" in text or "website" in text):
            url = "https://google.com"
            if "youtube" in text:
                url = "https://youtube.com"
            elif "github" in text:
                url = "https://github.com"
            return {"action": "system_op", "parameters": {"task": "open_browser", "url": url}}
            
        # Check for stats intent
        if "cpu" in text or "ram" in text or "memory" in text or "stats" in text or "status" in text:
            return {"action": "system_op", "parameters": {"task": "get_stats"}}
            
        # Check for time intent
        if "time" in text:
            return {"action": "system_op", "parameters": {"task": "get_time"}}
            
        return {"action": "unknown", "error": "No matching intent found."}
