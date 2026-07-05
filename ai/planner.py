#!/usr/bin/env python3
"""
AI Planner Module - Plans pentesting strategy
"""

import logging
from typing import List, Dict, Any
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


class PentestPhase(Enum):
    """Pentesting phases."""
    RECONNAISSANCE = "reconnaissance"
    SCANNING = "scanning"
    ENUMERATION = "enumeration"
    VULNERABILITY_ANALYSIS = "vulnerability_analysis"
    EXPLOITATION = "exploitation"
    POST_EXPLOITATION = "post_exploitation"
    REPORTING = "reporting"


@dataclass
class PentestPlan:
    """Pentesting plan structure."""
    target: str
    phases: List[PentestPhase]
    tools: List[str]
    estimated_duration: int
    risk_level: str
    objectives: List[str]


class Planner:
    """Plans and orchestrates pentesting workflow."""
    
    def __init__(self):
        self.available_tools = [
            "nmap", "nuclei", "subfinder", "nessus",
            "burpsuite", "zaproxy", "metasploit", "sqlmap"
        ]
        self.phases = list(PentestPhase)
    
    def create_plan(self, target: str, scan_type: str = "full") -> PentestPlan:
        """Create a pentesting plan for target.
        
        Args:
            target: Target URL or IP
            scan_type: Type of scan (quick, full, custom)
        
        Returns:
            PentestPlan object
        """
        logger.info(f"Creating {scan_type} plan for {target}")
        
        if scan_type == "quick":
            phases = [
                PentestPhase.RECONNAISSANCE,
                PentestPhase.SCANNING,
                PentestPhase.VULNERABILITY_ANALYSIS,
            ]
            tools = ["nmap", "nuclei"]
            duration = 60
        elif scan_type == "full":
            phases = self.phases
            tools = self.available_tools
            duration = 480
        else:
            phases = [PentestPhase.SCANNING]
            tools = []
            duration = 120
        
        plan = PentestPlan(
            target=target,
            phases=phases,
            tools=tools,
            estimated_duration=duration,
            risk_level="medium",
            objectives=self._generate_objectives(target)
        )
        
        logger.info(f"Plan created with {len(phases)} phases")
        return plan
    
    def _generate_objectives(self, target: str) -> List[str]:
        """Generate pentesting objectives."""
        return [
            "Identify all exposed services",
            "Discover vulnerabilities",
            "Test access controls",
            "Evaluate security posture",
            "Generate remediation recommendations"
        ]
    
    def get_next_phase(self, current_phase: PentestPhase) -> PentestPhase:
        """Get next phase in workflow."""
        phases = list(PentestPhase)
        try:
            idx = phases.index(current_phase)
            if idx < len(phases) - 1:
                return phases[idx + 1]
        except ValueError:
            pass
        return None
