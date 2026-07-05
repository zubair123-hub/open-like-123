#!/bin/bash

################################################################################
# Offline Pentesting AI - Quick Start Script
# 
# This script automates the installation and setup process
# Usage: bash QUICKSTART.sh
################################################################################

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Utility functions
print_header() {
    echo -e "${BLUE}===============================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}===============================================${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

# Detect OS
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="Linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macOS"
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
        OS="Windows"
    else
        OS="Unknown"
    fi
    print_info "Detected OS: $OS"
}

# Check Python installation
check_python() {
    print_info "Checking Python installation..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
        print_success "Python $PYTHON_VERSION found"
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
        print_success "Python $PYTHON_VERSION found"
        PYTHON_CMD="python"
    else
        print_error "Python 3.9+ not found"
        print_info "Please install Python 3.9 or higher from https://www.python.org/downloads/"
        exit 1
    fi
}

# Check Git installation
check_git() {
    print_info "Checking Git installation..."
    
    if command -v git &> /dev/null; then
        GIT_VERSION=$(git --version 2>&1 | awk '{print $3}')
        print_success "Git $GIT_VERSION found"
    else
        print_error "Git not found"
        print_info "Please install Git from https://git-scm.com/downloads"
        exit 1
    fi
}

# Install system dependencies
install_system_deps() {
    print_header "Installing System Dependencies"
    
    if [ "$OS" = "Linux" ]; then
        if command -v apt-get &> /dev/null; then
            print_info "Using apt-get to install dependencies..."
            sudo apt-get update
            sudo apt-get install -y \
                build-essential \
                libssl-dev \
                libffi-dev \
                python3-dev \
                git \
                curl \
                wget \
                nmap \
                whois \
                dnsutils
            print_success "System dependencies installed"
        elif command -v yum &> /dev/null; then
            print_info "Using yum to install dependencies..."
            sudo yum install -y \
                gcc \
                make \
                openssl-devel \
                libffi-devel \
                python3-devel \
                git \
                curl \
                wget \
                nmap \
                whois
            print_success "System dependencies installed"
        else
            print_warning "Could not determine package manager"
        fi
    elif [ "$OS" = "macOS" ]; then
        if command -v brew &> /dev/null; then
            print_info "Using Homebrew to install dependencies..."
            brew install git curl nmap wget
            print_success "System dependencies installed"
        else
            print_warning "Homebrew not found. Some dependencies may need to be installed manually"
        fi
    fi
}

# Clone repository or verify existing
setup_repo() {
    print_header "Setting Up Repository"
    
    if [ -d ".git" ]; then
        print_info "Repository already cloned, pulling latest changes..."
        git pull origin main || print_warning "Could not pull latest changes"
    else
        print_error "Not in the repository directory"
        print_info "Please run this script from the project root directory"
        exit 1
    fi
}

# Create virtual environment
setup_venv() {
    print_header "Setting Up Python Virtual Environment"
    
    if [ ! -d "venv" ]; then
        print_info "Creating virtual environment..."
        $PYTHON_CMD -m venv venv
        print_success "Virtual environment created"
    else
        print_info "Virtual environment already exists"
    fi
    
    # Activate venv
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
        print_success "Virtual environment activated"
    else
        print_error "Could not activate virtual environment"
        exit 1
    fi
}

# Install Python dependencies
install_python_deps() {
    print_header "Installing Python Dependencies"
    
    print_info "Upgrading pip..."
    $PYTHON_CMD -m pip install --upgrade pip setuptools wheel
    
    print_info "Installing requirements from requirements.txt..."
    pip install -r requirements.txt
    
    print_success "Python dependencies installed"
}

# Create directory structure
create_directories() {
    print_header "Creating Directory Structure"
    
    dirs=(
        "cache"
        "exports"
        "sessions"
        "logs"
        "database/sqlite"
        "database/vectors"
        "database/cache"
        "reports/html"
        "reports/pdf"
        "reports/json"
        "models/local_llm"
        "models/embeddings"
        "knowledge"
    )
    
    for dir in "${dirs[@]}"; do
        mkdir -p "$dir"
        print_success "Created $dir/"
    done
}

# Create environment file
create_env_file() {
    print_header "Creating Environment Configuration"
    
    if [ ! -f ".env" ]; then
        print_info "Creating .env file..."
        
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
        
        print_success ".env file created"
        print_info "Edit .env to customize configuration"
    else
        print_warning ".env file already exists, skipping creation"
    fi
}

# Check Ollama installation
check_ollama() {
    print_header "Checking Ollama Installation"
    
    if command -v ollama &> /dev/null; then
        print_success "Ollama is installed"
    else
        print_warning "Ollama not installed"
        print_info "Install from: https://ollama.ai"
        print_info "Or run the installer with:"
        if [ "$OS" = "macOS" ]; then
            echo -e "${YELLOW}brew install ollama${NC}"
        elif [ "$OS" = "Linux" ]; then
            echo -e "${YELLOW}curl https://ollama.ai/install.sh | sh${NC}"
        fi
    fi
}

# Test installation
test_installation() {
    print_header "Testing Installation"
    
    print_info "Testing Python imports..."
    $PYTHON_CMD -c "import fastapi; import ollama; print('✓ Core modules imported successfully')" || \
        print_warning "Some modules may not be installed"
    
    print_success "Installation test completed"
}

# Print next steps
print_next_steps() {
    print_header "Installation Complete! 🎉"
    
    echo ""
    echo -e "${GREEN}Next Steps:${NC}"
    echo ""
    echo "1. Start Ollama service (in a new terminal):"
    echo -e "   ${YELLOW}ollama serve${NC}"
    echo ""
    echo "2. Pull a language model (in another terminal):"
    echo -e "   ${YELLOW}ollama pull mistral${NC}"
    echo ""
    echo "3. Start the application (in the main terminal):"
    echo -e "   ${YELLOW}python main.py${NC}"
    echo ""
    echo "📖 For more information, see:"
    echo -e "   ${BLUE}README.md${NC} - Overview and features"
    echo -e "   ${BLUE}INSTALL.md${NC} - Detailed installation guide"
    echo -e "   ${BLUE}GETTING_STARTED.md${NC} - Quick start guide"
    echo ""
    echo -e "${RED}⚠️  IMPORTANT: This tool is for educational purposes only!${NC}"
    echo "   Only test systems you own or have explicit permission to test."
    echo ""
}

# Main execution
main() {
    clear
    print_header "Offline Pentesting AI - Quick Start Setup"
    
    echo ""
    
    # Run setup steps
    detect_os
    check_python
    check_git
    install_system_deps
    setup_repo
    setup_venv
    install_python_deps
    create_directories
    create_env_file
    check_ollama
    test_installation
    print_next_steps
    
    echo ""
    print_success "Setup completed successfully!"
    echo ""
}

# Run main if this script is executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
