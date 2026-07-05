#!/usr/bin/env python3
"""
Tool Manager - Manages security tools
"""

import logging
import subprocess
from typing import List, Dict, Any, Optional
from pathlib import Path

logger = logging.getLogger(__name__)


class Tool:
    """Security tool wrapper."""
    
    def __init__(self, name: str, command: str, args: List[str] = None):
        self.name = name
        self.command = command
        self.args = args or []
        self.installed = self.check_installed()
    
    def check_installed(self) -> bool:
        """Check if tool is installed."""
        try:
            subprocess.run(
                ["which", self.command],
                capture_output=True,
                check=True,
                timeout=5
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def run(self, target: str, **kwargs) -> Dict[str, Any]:
        """Run the tool."""
        if not self.installed:
            logger.error(f"Tool {self.name} is not installed")
            return {"error": f"{self.name} not installed"}
        
        try:
            cmd = [self.command] + self.args + [target]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300
            )
            
            return {
                "tool": self.name,
                "target": target,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        except subprocess.TimeoutExpired:
            return {"error": f"{self.name} timed out"}
        except Exception as e:
            logger.error(f"Error running {self.name}: {e}")
            return {"error": str(e)}


class ToolManager:
    """Manages security tools."""
    
    def __init__(self):
        self.tools: Dict[str, Tool] = {}
        self._register_default_tools()
    
    def _register_default_tools(self):
        """Register default security tools."""
        tools = [
            Tool("nmap", "nmap", ["-sV", "-sC"]),
            Tool("curl", "curl", ["-I", "-L"]),
            Tool("dig", "dig"),
            Tool("whois", "whois"),
        ]
        
        for tool in tools:
            self.register_tool(tool)
    
    def register_tool(self, tool: Tool):
        """Register a security tool."""
        self.tools[tool.name] = tool
        status = "installed" if tool.installed else "not installed"
        logger.info(f"Registered tool {tool.name} ({status})")
    
    def get_tool(self, name: str) -> Optional[Tool]:
        """Get a tool by name."""
        return self.tools.get(name)
    
    def list_tools(self) -> Dict[str, bool]:
        """List all registered tools and their status."""
        return {name: tool.installed for name, tool in self.tools.items()}
    
    def run_tool(self, tool_name: str, target: str, **kwargs) -> Dict[str, Any]:
        """Run a specific tool."""
        tool = self.get_tool(tool_name)
        if not tool:
            logger.error(f"Tool not found: {tool_name}")
            return {"error": f"Tool not found: {tool_name}"}
        
        logger.info(f"Running {tool_name} on {target}")
        return tool.run(target, **kwargs)
