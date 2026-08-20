from typing import Dict, Any
import os
import platform
import psutil
import webbrowser
from datetime import datetime

def execute_system_command(params: Dict[str, Any]) -> str:
    """Executes a system-level command based on structured parameters."""
    task = params.get("task")
    
    if task == "open_browser":
        url = params.get("url", "https://google.com")
        webbrowser.open(url)
        return f"Opening browser to {url.replace('https://', '')}"
        
    elif task == "get_stats":
        cpu = psutil.cpu_percent(interval=0.5)
        ram = psutil.virtual_memory().percent
        return f"System check complete. CPU is at {cpu} percent, and RAM is at {ram} percent."
        
    elif task == "get_time":
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        return f"The current time is {current_time}."
        
    return "I am not programmed to handle that specific action yet."
