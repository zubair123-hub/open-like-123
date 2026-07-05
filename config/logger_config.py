#!/usr/bin/env python3
"""
Logger Configuration
"""

import logging
import logging.config
import sys
from pathlib import Path
import yaml
from datetime import datetime


def setup_logging():
    """Setup logging configuration."""
    log_dir = Path("./logs")
    log_dir.mkdir(exist_ok=True)
    
    config_file = Path("./config/logging.yaml")
    
    try:
        if config_file.exists():
            with open(config_file) as f:
                config = yaml.safe_load(f)
                logging.config.dictConfig(config)
        else:
            # Fallback to basic config
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                handlers=[
                    logging.StreamHandler(sys.stdout),
                    logging.FileHandler(log_dir / 'app.log')
                ]
            )
    except Exception as e:
        logging.basicConfig(
            level=logging.ERROR,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        logging.error(f"Failed to load logging config: {e}")
    
    return logging.getLogger(__name__)
