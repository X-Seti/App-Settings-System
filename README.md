# App Settings System - Feb 2025 - X-Seti
# updated - Oct 25 - Added the complete color set to QT6

A reusable theming and settings system for PyQt6 applications.

## Overview

`app_settings_system.py` provides a complete theme management solution that can be integrated into any PyQt6 application. It handles theme creation, saving, loading, and applying themes across your entire application.

## Features

- **Theme Management**: Create, save, load, and delete custom themes
- **Colour Customisation**: Customise colours for various UI elements
- **Theme Preview**: Real-time preview of theme changes
- **Settings Dialog**: User-friendly interface for managing themes
- **Persistent Storage**: Themes saved as JSON files
- **Reusable**: Works with multiple applications

## Integration

### 1. Setup App Name

At the top of your main application file, set the app name in the settings module:

```python
from utils.app_settings_system import *
import utils.app_settings_system as settings_module

# Set your application name
settings_module.App_name = "Your App Name"
```

### 2. Import Required Components

```python
from utils.app_settings_system import AppSettings, apply_theme_to_app, SettingsDialog
```

### 3. Initialise in Your Main Application

```python
class YourMainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Initialise app settings
        self.app_settings = AppSettings()
        
        # Apply saved theme on startup
        apply_theme_to_app(self.app, self.app_settings.current_theme)
```

### 4. Add Settings Menu Option

```python
# In your menu bar or settings button
settings_action = QAction("Settings", self)
settings_action.triggered.connect(self.open_settings)

def open_settings(self):
    dialog = SettingsDialog(self.app_settings, self.app_settings.current_theme, self)
    if dialog.exec() == QDialog.DialogCode.Accepted:
        # Apply the new theme
        apply_theme_to_app(self.app, self.app_settings.current_theme)
```

## File Structure

```
your_project/
├── utils/
│   └── app_settings_system.py
└── your_main_app.py
```

## Theme Storage

Themes are stored as JSON files in:
- **Linux/Mac**: `~/.config/your_app_name/themes/`
- **Windows**: `%APPDATA%/your_app_name/themes/`

## Example Applications

- **Img Factory 1.5**: Image processing tool
- **Multi Emulation Launcher**: Emulator management system

## Customization

The default app name in `app_settings_system.py` is:
```python
App_name = "Application"
```

This is overridden by each application that uses the system.

## Requirements

- Python 3.x
- PyQt6
