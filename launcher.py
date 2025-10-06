# launcher.py
"""
Launcher script for Disk Scheduling Simulator.
"""

import sys
import os

def get_icon_path():
    """Get the path to the icon file, handling both development and bundled modes."""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        base_path = os.path.dirname(sys.executable)
    else:
        # Running as script
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    icon_path = os.path.join(base_path, 'icon.ico')
    return icon_path if os.path.exists(icon_path) else None

def get_src_path():
    """Get the path to the src directory."""
    base_path = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(base_path, 'src')
    return src_path

# Add src to path
src_path = get_src_path()
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from disk_scheduling_simulator.gui import run_simulator

if __name__ == "__main__":
    run_simulator()