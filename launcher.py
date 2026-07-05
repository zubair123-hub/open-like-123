#!/usr/bin/env python3
"""
Application Launcher - Handles CLI and GUI modes
"""

import logging
import sys
from pathlib import Path
from typing import Optional

import click
from backend.api.server import APIServer
from frontend.gui.main_window import MainWindow

logger = logging.getLogger(__name__)


class Launcher:
    """Handles application startup modes."""
    
    def __init__(self):
        self.mode = "gui"  # Default to GUI
        self.api_server: Optional[APIServer] = None
    
    def run(self):
        """Launch the application."""
        logger.info(f"Launching in {self.mode} mode...")
        
        if self.mode == "gui":
            self.launch_gui()
        elif self.mode == "api":
            self.launch_api()
        elif self.mode == "cli":
            self.launch_cli()
        else:
            logger.error(f"Unknown mode: {self.mode}")
    
    def launch_gui(self):
        """Launch GUI application."""
        logger.info("Initializing GUI...")
        try:
            app = MainWindow()
            app.show()
            logger.info("GUI launched successfully")
        except Exception as e:
            logger.error(f"Failed to launch GUI: {e}")
            raise
    
    def launch_api(self):
        """Launch API server."""
        logger.info("Initializing API Server...")
        try:
            self.api_server = APIServer(host="0.0.0.0", port=8000)
            self.api_server.run()
            logger.info("API Server running on http://0.0.0.0:8000")
        except Exception as e:
            logger.error(f"Failed to launch API: {e}")
            raise
    
    def launch_cli(self):
        """Launch CLI interface."""
        logger.info("Initializing CLI...")
        try:
            cli()
        except Exception as e:
            logger.error(f"Failed to launch CLI: {e}")
            raise


@click.group()
def cli():
    """Offline Pentesting AI - CLI Interface."""
    pass


@cli.command()
@click.option('--target', required=True, help='Target URL or IP')
@click.option('--scan-type', default='full', help='Type of scan: quick, full, custom')
def scan(target: str, scan_type: str):
    """Start a security scan."""
    logger.info(f"Starting {scan_type} scan on {target}")
    # Implementation in controllers


@cli.command()
@click.option('--report-id', required=True, help='Report ID')
def report(report_id: str):
    """Generate a report."""
    logger.info(f"Generating report {report_id}")
    # Implementation in controllers


if __name__ == "__main__":
    cli()
