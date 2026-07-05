# Offline Pentesting AI - Implementation Guide

## Project Overview

This is a comprehensive offline AI-powered penetration testing framework designed for educational purposes. It provides a GUI-based interface with red and black theming for conducting security assessments.

## Quick Start

### Prerequisites
- Python 3.9+
- Docker (optional)
- Ollama (for offline LLM)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/zubair123-hub/open-like-123.git
cd open-like-123

# 2. Run the installer
python installer.py

# 3. Start Ollama service
ollama serve

# 4. In another terminal, run the application
python main.py
```

### Docker Setup

```bash
# Build and run with Docker Compose
docker-compose up -d

# Access the application
# API: http://localhost:8000
# GUI: http://localhost:3000
```

## Project Structure

```
offline-pentest-ai/
├── main.py                 # Entry point
├── launcher.py             # CLI/GUI launcher
├── installer.py            # Installation script
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose setup
│
├── config/                 # Configuration files
│   ├── config.yaml         # Main config
│   ├── models.yaml         # LLM models config
│   ├── tools.yaml          # Security tools config
│   ├── logging.yaml        # Logging setup
│   └── logger_config.py    # Logger initialization
│
├── ai/                     # AI modules
│   ├── planner.py          # Pentesting strategy planner
│   ├── reasoning.py        # AI reasoning engine
│   ├── router.py           # Request routing
│   ├── memory.py           # Context memory management
│   └── ... (other AI modules)
│
├── controllers/            # Business logic
│   ├── tool_manager.py     # Security tools management
│   ├── plugin_manager.py   # Plugin management
│   ├── reporting.py        # Report generation
│   └── ... (other controllers)
│
├── backend/                # Backend services
│   ├── api/                # REST API
│   ├── websocket/          # WebSocket support
│   ├── auth/               # Authentication
│   ├── services/           # Business services
│   ├── middleware/         # Custom middleware
│   └── database/           # Database layer
│
├── frontend/               # Frontend
│   ├── gui/                # PyQt6 GUI
│   ├── chat/               # Chat interface
│   ├── dashboard/          # Dashboard components
│   ├── reports/            # Report viewers
│   └── themes/             # UI themes
│
├── database/               # Database files
│   ├── sqlite/             # SQLite databases
│   ├── vectors/            # Vector store
│   └── cache/              # Cache storage
│
├── tests/                  # Unit tests
├── docs/                   # Documentation
├── scripts/                # Utility scripts
└── .gitignore              # Git ignore rules
```

## Features

### 1. AI-Powered Planning
- Automatic pentesting strategy generation
- Intelligent tool selection
- Phase-based execution workflow

### 2. Security Tools Integration
- Network scanning (nmap)
- Vulnerability assessment
- Web application testing
- API security analysis

### 3. Offline Capabilities
- Local LLM support (Ollama)
- Offline knowledge base
- No internet required for core functions

### 4. GUI Interface
- Red and black color scheme
- Real-time scan monitoring
- Interactive dashboards
- Report generation and viewing

### 5. Comprehensive Reporting
- HTML reports
- PDF export
- JSON output
- Executive summaries

## Configuration

### Environment Variables

Edit `.env` file:

```bash
DEBUG=False
LOG_LEVEL=INFO
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral
DATABASE_URL=sqlite:///./database/sqlite/app.db
```

### Models Configuration

Edit `config/models.yaml`:

```yaml
default_llm: "mistral"
default_embeddings: "nomic-embed-text"
```

## API Endpoints

### Core Endpoints

```
GET /                      # Status
GET /health                # Health check
GET /api/tools             # List available tools
POST /api/scan             # Start a scan
GET /api/scan/{scan_id}    # Get scan status
GET /api/reports           # List reports
```

## Usage

### Command Line

```bash
# Quick scan
python main.py scan --target example.com --scan-type quick

# Full scan
python main.py scan --target example.com --scan-type full

# Generate report
python main.py report --report-id report_001
```

### GUI Application

1. Run `python main.py`
2. Enter target URL or IP
3. Select scan type (Quick/Full/Custom)
4. Click "Start Scan"
5. Monitor progress in real-time
6. View and export reports

## Security Considerations

⚠️ **IMPORTANT**: This tool is for **educational purposes only**.

- Only test systems you own or have explicit permission to test
- Unauthorized testing is illegal
- Always follow responsible disclosure practices
- Keep the tool and knowledge base updated

## Development

### Running Tests

```bash
pytest tests/ -v
pytest tests/ --cov=. --cov-report=html
```

### Adding New Tools

```python
from controllers.tool_manager import Tool, ToolManager

# Register a new tool
tool = Tool("mytool", "mytool_command")
tool_manager.register_tool(tool)
```

### Creating Custom Plugins

```python
# plugins/my_plugin.py
from plugins.base import BasePlugin

class MyPlugin(BasePlugin):
    def run(self, *args, **kwargs):
        # Implementation
        pass
```

## Troubleshooting

### Ollama Connection Error

```bash
# Make sure Ollama is running
ollama serve

# In another terminal, pull a model
ollama pull mistral
```

### GUI Not Starting

```bash
# Ensure PyQt6 is installed
pip install PyQt6 PyQt6-WebEngine

# Try running in CLI mode
python main.py --mode cli
```

### Database Issues

```bash
# Reset database
rm database/sqlite/app.db
python main.py  # Will reinitialize
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push and create a Pull Request

## License

Boost Software License 1.0 - See LICENSE file

## Disclaimer

This tool is provided for educational purposes only. Users are responsible for ensuring their use complies with all applicable laws and regulations. Unauthorized access to computer systems is illegal.

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review the knowledge base

## Roadmap

- [ ] Advanced AI reasoning with chain-of-thought
- [ ] Real-time collaboration features
- [ ] Multi-target scanning
- [ ] Custom plugin marketplace
- [ ] Mobile application
- [ ] Cloud integration (optional)
- [ ] Advanced reporting with ML insights
- [ ] Automated remediation suggestions

---

**Made with ❤️ for the security community**
