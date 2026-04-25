#!/usr/bin/env python3
#this belongs in root /launch_settings.py - Version: 1
# X-Seti - April25 2026 - App Settings System - Root Launcher

import sys
from pathlib import Path

root_dir = Path(__file__).parent.resolve()
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

if __name__ == "__main__":
    try:
        print("App Settings System Starting...")
        from PyQt6.QtWidgets import QApplication
        from apps.utils.app_settings_system import AppSettings, SettingsDialog
        app = QApplication(sys.argv)
        settings = AppSettings()
        dialog = SettingsDialog(settings)
        dialog.show()
        sys.exit(app.exec())
    except ImportError as e:
        print(f"ERROR: Failed to import app_settings_system: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Failed to start App Settings System: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)
