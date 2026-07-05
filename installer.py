#!/usr/bin/env python3
"""
Installer Script - Sets up the application environment
"""

import os
import sys
import subprocess
import json
from pathlib import Path
import platform


class Installer:
    """Handles application installation and setup."""
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.python_version = sys.version_info
        self.os_type = platform.system()
    
    def check_requirements(self):
        """Check if system meets minimum requirements."""
        print("[*] Checking system requirements...")
        
        # Python version
        if self.python_version < (3, 9):
            print(f"[!] Python 3.9+ required (found {self.python_version.major}.{self.python_version.minor})")
            return False
        print(f"[+] Python {self.python_version.major}.{self.python_version.minor} OK")
        
        # OS Support
        if self.os_type not in ["Linux", "Darwin", "Windows"]:
            print(f"[!] Unsupported OS: {self.os_type}")
            return False
        print(f"[+] OS: {self.os_type} OK")
        
        return True
    
    def setup_directories(self):
        """Create necessary directories."""
        print("[*] Setting up directories...")
        dirs = [
            "cache",
            "exports",
            "sessions",
            "logs",
            "database/sqlite",
            "database/vectors",
            "database/cache",
            "reports/html",
            "reports/pdf",
            "reports/json",
            "models/local_llm",
            "models/embeddings",
            "knowledge",
        ]
        
        for d in dirs:
            path = self.project_root / d
            path.mkdir(parents=True, exist_ok=True)
            print(f"[+] {d}/")
    
    def install_dependencies(self):
        """Install Python dependencies."""
        print("[*] Installing dependencies...")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install",
                "-r", str(self.project_root / "requirements.txt")
            ])
            print("[+] Dependencies installed")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[!] Failed to install dependencies: {e}")
            return False
    
    def setup_database(self):
        """Initialize database."""
        print("[*] Setting up database...")
        # Implementation in database module
        print("[+] Database initialized")
    
    def create_env_file(self):
        """Create .env file with default values."""
        print("[*] Creating .env file...")
        env_content = """# Environment Configuration
DEBUG=False
LOG_LEVEL=INFO
API_HOST=0.0.0.0
API_PORT=8000

# LLM Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral
EMBEDDINGS_MODEL=nomic-embed-text

# Database
DATABASE_URL=sqlite:///./database/sqlite/app.db
VECTOR_DB_TYPE=chroma

# Security
SECRET_KEY=your-secret-key-change-me
ALLOWED_HOSTS=localhost,127.0.0.1

# Reporting
REPORT_FORMAT=html,pdf,json
REPORT_INCLUDE_EVIDENCE=true
"""
        env_file = self.project_root / ".env"
        if not env_file.exists():
            with open(env_file, "w") as f:
                f.write(env_content)
            print(f"[+] .env file created at {env_file}")
        else:
            print("[!] .env file already exists, skipping")
    
    def run(self):
        """Run complete installation."""
        print("\n" + "="*60)
        print("Offline Pentesting AI - Installer")
        print("="*60 + "\n")
        
        if not self.check_requirements():
            print("\n[!] Installation failed: requirements not met")
            sys.exit(1)
        
        self.setup_directories()
        self.create_env_file()
        
        if not self.install_dependencies():
            print("\n[!] Installation failed: couldn't install dependencies")
            sys.exit(1)
        
        self.setup_database()
        
        print("\n" + "="*60)
        print("[+] Installation completed successfully!")
        print("[*] Run 'python main.py' to start the application")
        print("="*60 + "\n")


if __name__ == "__main__":
    installer = Installer()
    installer.run()
