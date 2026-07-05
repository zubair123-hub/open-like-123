# Getting Started - Quick Start Guide

Get Offline Pentesting AI up and running in minutes! 🚀

---

## ⚡ The Fastest Way (10 minutes)

### All Platforms (Linux, macOS, Windows)

```bash
# Step 1: Clone
git clone https://github.com/zubair123-hub/open-like-123.git
cd open-like-123

# Step 2: Run installer
python installer.py

# Step 3: Start Ollama (in a new terminal)
ollama serve

# Step 4: Pull a model (in another new terminal)
ollama pull mistral

# Step 5: Run the app (in another new terminal)
python main.py
```

**Done!** The GUI should open automatically. If not, visit http://localhost:8000 in your browser.

---

## 🎯 What to Do Next

### 1. First Scan (Try it now!)

In the GUI:
1. Enter a test target: `example.com` or `8.8.8.8`
2. Select "Quick Scan"
3. Click "Start"
4. Watch the progress in real-time
5. View results when complete

### 2. Generate a Report

After a scan completes:
1. Click "Generate Report"
2. Choose format: HTML, PDF, or JSON
3. Report saves to `reports/` folder

### 3. Try the REST API

```bash
# Check if API is running
curl http://localhost:8000/health

# List available tools
curl http://localhost:8000/api/tools

# Start a scan via API
curl -X POST http://localhost:8000/api/scan \
  -H "Content-Type: application/json" \
  -d '{"target": "example.com", "scan_type": "quick"}'
```

---

## 🐳 Docker Quick Start (Even Faster!)

```bash
git clone https://github.com/zubair123-hub/open-like-123.git
cd open-like-123
docker-compose up -d
```

Access at: http://localhost:8000

---

## 📁 File Structure Overview

```
your-project/
├── main.py              ← Run this to start
├── installer.py         ← Run this for setup
├── requirements.txt     ← Dependencies
├── Dockerfile           ← For Docker
├── docker-compose.yml   ← For Docker Compose
├── .env.example         ← Copy to .env for config
│
├── config/              ← Configuration files
├── controllers/         ← Core logic
├── backend/             ← API & services
├── frontend/            ← GUI interface
├── ai/                  ← AI reasoning
└── tests/               ← Test files
```

---

## 🔧 Configuration Basics

### Environment File (.env)

```bash
# Copy the example
cp .env.example .env

# Edit with your settings (optional)
nano .env  # Linux/macOS
# or
notepad .env  # Windows
```

**Key settings:**
- `OLLAMA_MODEL=mistral` - Which AI model to use
- `OLLAMA_BASE_URL=http://localhost:11434` - Where Ollama runs
- `DEBUG=False` - Turn on for development
- `LOG_LEVEL=INFO` - Verbosity level

---

## 🎮 Usage Examples

### GUI Application
```bash
python main.py
```
- Click "New Scan" → Enter target → Select scan type → Start

### Command Line
```bash
# Quick scan
python main.py scan --target example.com --type quick

# Full scan
python main.py scan --target example.com --type full

# List tools
python main.py tools list

# View help
python main.py --help
```

### REST API
```bash
# Start scan
curl -X POST http://localhost:8000/api/scan \
  -H "Content-Type: application/json" \
  -d '{"target": "example.com"}'

# Check status
curl http://localhost:8000/api/scan/{scan_id}

# Get reports
curl http://localhost:8000/api/reports
```

---

## 🤖 Ollama Models

### View Available Models
```bash
ollama list
```

### Install Models
```bash
# Recommended for pentesting (small, fast)
ollama pull mistral

# Alternative options
ollama pull llama2
ollama pull neural-chat
ollama pull orca-mini
ollama pull dolphin-mixtral
```

### Set Default Model
Edit `.env`:
```bash
OLLAMA_MODEL=mistral  # Change to your preferred model
```

---

## ✅ Verify Installation

```bash
# Test 1: Python version
python --version  # Should be 3.9+

# Test 2: Dependencies installed
python -c "import fastapi; print('✓ FastAPI OK')"

# Test 3: Ollama running
curl http://localhost:11434/api/tags  # Should return models

# Test 4: App starts
python main.py  # Should start without errors

# Test 5: API responds
curl http://localhost:8000/health  # Should return {"status": "ok"}
```

---

## 🐛 Common Issues & Quick Fixes

| Problem | Solution |
|---------|----------|
| **"Python not found"** | Use `python3` instead, or install Python 3.9+ |
| **"Module not found"** | Run `pip install -r requirements.txt` |
| **"Ollama not running"** | Run `ollama serve` in a new terminal |
| **"Port 8000 in use"** | Use `python main.py --port 8001` |
| **"GUI won't open"** | Try CLI mode: `python main.py --mode cli` |
| **"Database error"** | Delete `database/sqlite/app.db` and restart |

For more help, see [INSTALL.md](INSTALL.md) or [Troubleshooting](README.md#-troubleshooting).

---

## 📚 Next Steps

1. ✅ **Installation complete** - You're here!
2. 📖 Read [README.md](README.md) - Full documentation
3. 🔍 Check [INSTALL.md](INSTALL.md) - Detailed setup guide
4. 🚀 Run your first scan
5. 📊 Generate a report
6. 🤝 Contribute or customize

---

## 🚨 Important Reminders

> ⚠️ **Educational Use Only**
> 
> - Only test systems you own or have **permission** to test
> - Unauthorized testing is **illegal**
> - Use responsibly and ethically
> - Always get written authorization

---

## 💡 Pro Tips

### Tip 1: Screen Sessions (Linux/macOS)
Keep multiple terminals running with tmux or screen:
```bash
# Terminal 1: Ollama
screen -S ollama
ollama serve

# Terminal 2: App (Ctrl+A then C to create new window)
python main.py

# Detach with Ctrl+A then D
```

### Tip 2: Background Ollama
Run Ollama in the background:
```bash
nohup ollama serve > ollama.log 2>&1 &
python main.py
```

### Tip 3: Custom Scans
Create a scan configuration file:
```yaml
# scan_config.yml
target: example.com
scan_type: custom
tools:
  - nmap
  - ssl-scan
  - web-scan
timeout: 600
```

### Tip 4: API Automation
Script repeated scans:
```bash
#!/bin/bash
targets=("target1.com" "target2.com" "target3.com")

for target in "${targets[@]}"; do
  echo "Scanning $target..."
  curl -X POST http://localhost:8000/api/scan \
    -H "Content-Type: application/json" \
    -d "{\"target\": \"$target\", \"scan_type\": \"quick\"}"
done
```

---

## 🎓 Learning Path

1. **Day 1**: Install and run first scan
2. **Day 2**: Try different scan types and tools
3. **Day 3**: Generate reports and explore results
4. **Day 4**: Use REST API for automation
5. **Day 5**: Customize tools and create plugins

---

## 🤝 Get Help

- **Quick Questions**: [GitHub Discussions](https://github.com/zubair123-hub/open-like-123/discussions)
- **Report Bugs**: [GitHub Issues](https://github.com/zubair123-hub/open-like-123/issues)
- **Full Docs**: [README.md](README.md) and [docs/](docs/) folder
- **Email**: Contact via GitHub profile

---

## 🎉 You're All Set!

```bash
# Run this command to start:
python main.py

# Then open in browser (if CLI mode):
# http://localhost:8000
```

**Happy Pentesting! 🛡️**

---

<div align="center">

**Have questions?** Check [README.md](README.md#-documentation) or [INSTALL.md](INSTALL.md)

[← Back to README](README.md)

</div>
