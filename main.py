#!/usr/bin/env python3
"""
Offline Pentesting AI - Main Entry Point
"""

import os
import sys
import logging
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from launcher import Launcher
from config.logger_config import setup_logging

# Setup logging
logger = setup_logging()


def main():
    """Main entry point for the application."""
    logger.info("="*60)
    logger.info("Offline Pentesting AI - Starting...")
    logger.info("="*60)
    
    try:
        launcher = Launcher()
        launcher.run()
    except KeyboardInterrupt:
        logger.info("\nApplication interrupted by user.")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
