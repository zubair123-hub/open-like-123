#!/usr/bin/env python3
"""
Main GUI Window - PyQt6 Application
"""

import sys
import logging
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QPushButton, QLabel, QLineEdit, QComboBox, QTabWidget
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor, QFont, QIcon
from PyQt6.QtWebEngineWidgets import QWebEngineView

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    """Main application window."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Offline Pentesting AI")
        self.setGeometry(100, 100, 1400, 900)
        self.setup_style()
        self.init_ui()
    
    def setup_style(self):
        """Setup application styling."""
        # Red and black theme
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a1a1a;
            }
            QWidget {
                background-color: #1a1a1a;
                color: #ffffff;
            }
            QPushButton {
                background-color: #cc0000;
                color: #ffffff;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #ff0000;
            }
            QPushButton:pressed {
                background-color: #990000;
            }
            QLineEdit, QComboBox {
                background-color: #2a2a2a;
                color: #ffffff;
                border: 1px solid #cc0000;
                padding: 6px;
                border-radius: 3px;
            }
            QTabWidget::pane {
                border: 1px solid #cc0000;
            }
            QTabBar::tab {
                background-color: #2a2a2a;
                color: #ffffff;
                padding: 8px 20px;
                border: 1px solid #cc0000;
            }
            QTabBar::tab:selected {
                background-color: #cc0000;
            }
            QLabel {
                color: #ffffff;
            }
        """)
    
    def init_ui(self):
        """Initialize user interface."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Title
        title = QLabel("Offline Pentesting AI")
        title.setFont(QFont("Roboto Mono", 18, QFont.Weight.Bold))
        title.setStyleSheet("color: #cc0000; margin: 10px;")
        layout.addWidget(title)
        
        # Tabs
        tabs = QTabWidget()
        tabs.addTab(self.create_scan_tab(), "Scan")
        tabs.addTab(self.create_reports_tab(), "Reports")
        tabs.addTab(self.create_settings_tab(), "Settings")
        layout.addWidget(tabs)
    
    def create_scan_tab(self) -> QWidget:
        """Create scan tab."""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Target input
        target_label = QLabel("Target:")
        target_input = QLineEdit()
        target_input.setPlaceholderText("Enter target URL or IP...")
        layout.addWidget(target_label)
        layout.addWidget(target_input)
        
        # Scan type
        scan_type_label = QLabel("Scan Type:")
        scan_type = QComboBox()
        scan_type.addItems(["Quick", "Full", "Custom"])
        layout.addWidget(scan_type_label)
        layout.addWidget(scan_type)
        
        # Start button
        start_btn = QPushButton("Start Scan")
        start_btn.clicked.connect(lambda: self.start_scan(target_input.text()))
        layout.addWidget(start_btn)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def create_reports_tab(self) -> QWidget:
        """Create reports tab."""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Reports will appear here"))
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def create_settings_tab(self) -> QWidget:
        """Create settings tab."""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Settings"))
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def start_scan(self, target: str):
        """Start a security scan."""
        if not target:
            logger.warning("No target specified")
            return
        
        logger.info(f"Starting scan on {target}")
        # Implementation in controllers
    
    def show(self):
        """Display the window."""
        super().show()
        logger.info("GUI window displayed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
