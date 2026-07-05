# Installation Guide - Offline Pentesting AI

Complete step-by-step installation instructions for all platforms.

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Quick Start (5 minutes)](#quick-start-5-minutes)
3. [Linux Installation](#linux-installation)
4. [macOS Installation](#macos-installation)
5. [Windows Installation](#windows-installation)
6. [Docker Installation](#docker-installation)
7. [Verification](#verification)
8. [Troubleshooting](#troubleshooting)

---

## System Requirements

### Minimum Requirements

| Component | Requirement |
|-----------|------------|
| **OS** | Linux, macOS, or Windows |
| **Python** | 3.9 or higher |
| **RAM** | 4 GB minimum |
| **Disk Space** | 5 GB for app + models |
| **Network** | Internet (for setup), then offline capable |

### Recommended Specifications

| Component | Recommendation |
|-----------|------------|
| **OS** | Ubuntu 20.04+, macOS 11+, Windows 10+ |
| **Python** | 3.11 or higher |
| **RAM** | 8 GB or more |
| **Disk Space** | 10+ GB (for multiple models) |
| **CPU** | Multi-core processor |
| **GPU** | NVIDIA/AMD (optional, for faster AI inference) |

---

## Quick Start (5 minutes)

### For Everyone (All Platforms)

```bash
# 1. Clone the repository
git clone https://github.com/zubair123-hub/open-like-123.git
cd open-like-123

# 2. Run the installer
python installer.py

# 3. Follow the prompts and wait for completion
```

After installer completes, proceed to [Running the Application](#running-the-application).

---

## Linux Installation

### Prerequisites

```bash
# Update package manager
sudo apt-get update
sudo apt-get upgrade -y

# Install system dependencies
sudo apt-get install -y \
    python3.11 \
    python3.11-dev \
    python3.11-venv \
    git \
    curl \
    wget \
    build-essential \
    libssl-dev \
    libffi-dev \
    nmap \
    whois \
    dnsutils
```

### Step-by-Step Installation

```bash
# 1. Clone repository
git clone https://github.com/zubair123-hub/open-like-123.git
cd open-like-123

# 2. Create virtual environment
python3.11 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Install Python dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# 5. Create directory structure
mkdir -p cache exports sessions logs
mkdir -p database/sqlite database/vectors database/cache
mkdir -p reports/{html,pdf,json}
mkdir -p models/{local_llm,embeddings}
mkdir -p knowledge

# 6. Create .env file
cp .env.example .env 2>/dev/null || cat > .env << 'EOF'
DEBUG=False
LOG_LEVEL=INFO
API_HOST=0.0.0.0
API_PORT=8000
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral
EMBEDDINGS_MODEL=nomic-embed-text
DATABASE_URL=sqlite:///./database/sqlite/app.db
VECTOR_DB_TYPE=chroma
SECRET_KEY=your-secret-key-change-me
ALLOWED_HOSTS=localhost,127.0.0.1
REPORT_FORMAT=html,pdf,json
REPORT_INCLUDE_EVIDENCE=true
EOF

# 7. Install Ollama (optional but recommended)
curl https://ollama.ai/install.sh | sh
```

### Running on Linux

```bash
# Terminal 1: Start Ollama
ollama serve

# Terminal 2: Pull a model
ollama pull mistral

# Terminal 3: Activate venv and run app
source venv/bin/activate
python main.py
```

---

## macOS Installation

### Prerequisites

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install python@3.11 git curl nmap
```

### Step-by-Step Installation

```bash
# 1. Clone repository
git clone https://github.com/zubair123-hub/open-like-123.git
cd open-like-123

# 2. Create virtual environment
python3.11 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Install Python dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# 5. Create directory structure
mkdir -p cache exports sessions logs
mkdir -p database/sqlite database/vectors database/cache
mkdir -p reports/{html,pdf,json}
mkdir -p models/{local_llm,embeddings}
mkdir -p knowledge

# 6. Create .env file
cat > .env << 'EOF'
DEBUG=False
LOG_LEVEL=INFO
API_HOST=0.0.0.0
API_PORT=8000
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral
EMBEDDINGS_MODEL=nomic-embed-text
DATABASE_URL=sqlite:///./database/sqlite/app.db
VECTOR_DB_TYPE=chroma
SECRET_KEY=your-secret-key-change-me
ALLOWED_HOSTS=localhost,127.0.0.1
REPORT_FORMAT=html,pdf,json
REPORT_INCLUDE_EVIDENCE=true
EOF

# 7. Install Ollama (optional)
brew install ollama
```

### Running on macOS

```bash
# Terminal 1: Start Ollama
ollama serve

# Terminal 2: Pull a model
ollama pull mistral

# Terminal 3: Activate venv and run app
source venv/bin/activate
python main.py
```

---

## Windows Installation

### Prerequisites

1. **Python 3.11+**
   - Download from https://www.python.org/downloads/
   - ✅ Check "Add Python to PATH" during installation
   - ✅ Check "Install pip"

2. **Git for Windows**
   - Download from https://git-scm.com/download/win

3. **Visual C++ Build Tools** (if needed)
   - Download from Microsoft website

4. **Ollama** (optional)
   - Download from https://ollama.ai

### Step-by-Step Installation

```bash
# 1. Open Command Prompt (cmd) or PowerShell

# 2. Clone repository
git clone https://github.com/zubair123-hub/open-like-123.git
cd open-like-123

# 3. Create virtual environment
python -m venv venv

# 4. Activate virtual environment
venv\Scripts\activate

# 5. Upgrade pip
python -m pip install --upgrade pip setuptools wheel

# 6. Install Python dependencies
pip install -r requirements.txt

# 7. Create directory structure
mkdir cache exports sessions logs
mkdir database\sqlite database\vectors database\cache
mkdir reports\html reports\pdf reports\json
mkdir models\local_llm models\embeddings
mkdir knowledge

# 8. Create .env file
# Using PowerShell:
@'
DEBUG=False
LOG_LEVEL=INFO
API_HOST=0.0.0.0
API_PORT=8000
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral
EMBEDDINGS_MODEL=nomic-embed-text
DATABASE_URL=sqlite:///./database/sqlite/app.db
VECTOR_DB_TYPE=chroma
SECRET_KEY=your-secret-key-change-me
ALLOWED_HOSTS=localhost,127.0.0.1
REPORT_FORMAT=html,pdf,json
REPORT_INCLUDE_EVIDENCE=true
'@ | Out-File -Encoding UTF8 .env
```

### Running on Windows

```batch
# Terminal 1: Start Ollama
ollama serve

# Terminal 2: Pull a model (in new cmd/PowerShell)
ollama pull mistral

# Terminal 3: Activate venv and run app
venv\Scripts\activate
python main.py
```

### Windows Specific Tips

- Use **PowerShell** or **Windows Terminal** for better compatibility
- If `activation` fails, run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- For GUI issues, ensure display settings are configured properly
- Use `-NoProfile` flag if PowerShell has startup issues

---

## Docker Installation

### Prerequisites

- **Docker Desktop** (download from https://www.docker.com/products/docker-desktop)
- **Docker Compose** (usually included with Docker Desktop)

### Installation & Running

```bash
# 1. Clone repository
git clone https://github.com/zubair123-hub/open-like-123.git
cd open-like-123

# 2. Start all services
docker-compose up -d

# 3. Wait for services to start (30-60 seconds)

# 4. Check status
docker-compose ps

# 5. View logs
docker-compose logs -f app
```

### Accessing the Application

- **API**: http://localhost:8000
- **Ollama**: http://localhost:11434
- **Redis**: localhost:6379

### Common Docker Commands

```bash
# Stop services
docker-compose down

# Remove volumes (WARNING: deletes data)
docker-compose down -v

# Rebuild images
docker-compose build --no-cache

# Access container shell
docker exec -it pentesting-ai bash

# View specific service logs
docker-compose logs ollama

# Monitor resource usage
docker stats
```

---

## Verification

### Verify Installation

```bash
# Test Python installation
python --version          # Should show 3.9+

# Test Git installation
git --version            # Should show git version

# Test virtual environment activation
source venv/bin/activate  # (Linux/macOS)
# OR
venv\Scripts\activate     # (Windows)

# Test Python dependencies
python -c "import fastapi; import ollama; print('✓ Dependencies OK')"

# Test directory structure
ls -la                    # Should show created directories

# Test Ollama connection
curl http://localhost:11434/api/tags  # After Ollama is running
```

### Verify Application Runs

```bash
# Ensure Ollama is running first
ollama serve              # Terminal 1

# In another terminal
python main.py           # Should start without errors
```

---

## Troubleshooting

### Python Not Found

```bash
# Check Python installation
python3 --version

# If python3 works but python doesn't:
alias python=python3
# OR use python3 explicitly:
python3 installer.py
python3 main.py
```

### Permission Denied (Linux/macOS)

```bash
# Make scripts executable
chmod +x installer.py
chmod +x main.py

# Run with explicit python
python installer.py
```

### Virtual Environment Issues

```bash
# Remove corrupted venv
rm -rf venv  # (Linux/macOS)
rmdir /s venv  # (Windows)

# Recreate
python -m venv venv
source venv/bin/activate  # (Linux/macOS)
venv\Scripts\activate     # (Windows)

# Reinstall dependencies
pip install -r requirements.txt
```

### Port Already in Use

```bash
# Find process using port 8000
lsof -i :8000  # (Linux/macOS)
netstat -ano | findstr :8000  # (Windows)

# Kill process
kill -9 <PID>  # (Linux/macOS)
taskkill /PID <PID> /F  # (Windows)

# Use different port
python main.py --port 8001
```

### Ollama Connection Failed

```bash
# Ensure Ollama is running
ollama serve

# Check connectivity
curl http://localhost:11434/api/tags

# Pull default model
ollama pull mistral

# Verify model downloaded
ollama list
```

### GUI/PyQt6 Issues

```bash
# Reinstall PyQt6
pip install --upgrade --force-reinstall PyQt6 PyQt6-WebEngine

# Test PyQt6
python -c "from PyQt6.QtWidgets import QApplication; print('✓ PyQt6 OK')"

# Use CLI mode if GUI fails
python main.py --mode cli
```

### Database Corruption

```bash
# Reset database (WARNING: loses all data)
rm database/sqlite/app.db

# Reinitialize
python main.py
```

### Import Errors

```bash
# Verify virtual environment
which python  # (Linux/macOS)
where python  # (Windows)
# Should show path inside venv/

# Reinstall all dependencies
pip install -r requirements.txt --force-reinstall

# Check Python path
python -c "import sys; print('\n'.join(sys.path))"
```

---

## Next Steps

1. ✅ Complete installation
2. 📚 Read [README.md](README.md) for overview
3. 🎮 Check [Usage Section](README.md#-usage) for how to run
4. ⚙️ Configure [Environment Variables](#system-requirements)
5. 🚀 Start using the application!

---

## Getting Help

- **Installation Issues**: Check [Troubleshooting](#troubleshooting)
- **Documentation**: See [docs/](docs/) folder
- **GitHub Issues**: Report bugs at [Issues](https://github.com/zubair123-hub/open-like-123/issues)
- **Discussions**: Ask questions at [Discussions](https://github.com/zubair123-hub/open-like-123/discussions)

---

**Happy Pentesting! 🛡️**
