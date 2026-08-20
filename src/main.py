import sys
from utils.logger import setup_logger
from utils.config_parser import load_env
from core.engine import OmniEngine

logger = setup_logger("AuraMain")

def main():
    logger.info("Initializing Voice Assistant...")
    load_env()
    
    try:
        engine = OmniEngine()
        engine.start()
    except KeyboardInterrupt:
        logger.info("Received exit signal. Shutting down...")
        engine.stop()
    except Exception as e:
        logger.error(f"Critical error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
