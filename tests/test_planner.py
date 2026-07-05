#!/usr/bin/env python3
"""
Unit tests for planner module
"""

import pytest
from ai.planner import Planner, PentestPhase, PentestPlan


class TestPlanner:
    """Test cases for Planner."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.planner = Planner()
    
    def test_create_quick_plan(self):
        """Test creating a quick scan plan."""
        plan = self.planner.create_plan("example.com", "quick")
        
        assert plan.target == "example.com"
        assert len(plan.phases) == 3
        assert plan.estimated_duration == 60
    
    def test_create_full_plan(self):
        """Test creating a full scan plan."""
        plan = self.planner.create_plan("example.com", "full")
        
        assert plan.target == "example.com"
        assert len(plan.phases) > 3
        assert plan.estimated_duration == 480
    
    def test_get_next_phase(self):
        """Test getting next phase."""
        next_phase = self.planner.get_next_phase(PentestPhase.RECONNAISSANCE)
        assert next_phase == PentestPhase.SCANNING
