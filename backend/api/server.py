#!/usr/bin/env python3
"""
API Server - FastAPI application
"""

import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

logger = logging.getLogger(__name__)


class APIServer:
    """FastAPI server for the pentesting application."""
    
    def __init__(self, host: str = "0.0.0.0", port: int = 8000):
        self.host = host
        self.port = port
        self.app = self._create_app()
    
    def _create_app(self) -> FastAPI:
        """Create FastAPI application."""
        app = FastAPI(
            title="Offline Pentesting AI",
            description="Free offline AI for penetration testing",
            version="1.0.0"
        )
        
        # Add CORS middleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        
        # Routes
        @app.get("/")
        async def root():
            return {
                "name": "Offline Pentesting AI",
                "version": "1.0.0",
                "status": "running"
            }
        
        @app.get("/health")
        async def health():
            return {"status": "healthy"}
        
        @app.post("/api/scan")
        async def start_scan(target: str, scan_type: str = "full"):
            """Start a security scan."""
            return {
                "scan_id": "scan_001",
                "target": target,
                "type": scan_type,
                "status": "started"
            }
        
        @app.get("/api/scan/{scan_id}")
        async def get_scan_status(scan_id: str):
            """Get scan status."""
            return {
                "scan_id": scan_id,
                "status": "in_progress",
                "progress": 45
            }
        
        @app.get("/api/reports")
        async def list_reports():
            """List all reports."""
            return {"reports": []}
        
        @app.get("/api/tools")
        async def list_tools():
            """List available tools."""
            return {
                "tools": [
                    {"name": "nmap", "status": "installed"},
                    {"name": "nuclei", "status": "not_installed"}
                ]
            }
        
        return app
    
    def run(self):
        """Run the API server."""
        logger.info(f"Starting API server on {self.host}:{self.port}")
        uvicorn.run(
            self.app,
            host=self.host,
            port=self.port,
            log_level="info"
        )
