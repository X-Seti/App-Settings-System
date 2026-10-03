# Global App System Settings
<!-- Updated: October 2026 - per-colour transparency, panel image across window, settings layout rework, Windows exe -->

A reusable theming, settings and panel effects system for PyQt6 applications.
Used by IMG Factory 1.6, COL Workshop, TXD Workshop, Model Workshop, DP5 Workshop and more.

---

## Overview

`app_settings_system.py` provides a complete theme and UI management solution for any PyQt6 application:
theme creation, saving, loading, applying, panel fill/gradient/pattern effects, button styles, progress bar styles, localisation foundation, and a self-contained settings dialog with live previews.

---

## Features

- **Theme Management** — create, save, load, delete custom themes; 41 bundled themes
- **Colour Customisation** — full colour editor with live preview and XP-style picker
- **Button Styles** — 11 styles: Flat, Gradient H/V/45°, Banded (Win ME), Zen, Indented, Bump, Amiga WB, Half-shine, Shadow-dark
- **Panel Effects** — fill (solid/two-tone), gradient (6 directions, 3 stops), pattern (9 styles), image background (per panel or across the whole window), transparency — applied live via `AppPanelEffect`
- **Per-colour Transparency** — alpha column in the Colors tab (0-100) for backgrounds, panels, ribbons, buttons, title/menu/gadget bars, table rows, scrollbars, dialogs
- **Theme Effects** — panel image (copied to `images/`) and transparency saved and loaded with each theme JSON
- **Progress Bar Styles** — 8 styles with colour pickers and height control
- **Hero Banner** — configurable dark/light gradient for welcome screens
- **Localisation** — auto-detect, 12 language stubs, date/number format, per-app overrides
- **Settings Dialog** — always-frameless with COL-workshop-pattern titlebar `[Menu] [Settings] | Title | [i] [—] [□] [✕]`, draggable via `startSystemMove()` (Wayland safe)
- **Live Previews** — every panel sub-tab shows a live preview alongside the controls in a two-column layout
- **SVG Icon Provider** — theme-aware icons in `depends/App_System_Setting_Svg_icons.py`
- **Persistent Storage** — settings as JSON, themes as JSON files
- **Cross-platform** — Linux, Windows, macOS; Wayland and X11

---

## File Structure

```
App-Settings-System/
├── launch_settings.py                  # Standalone launcher
├── app_settings_system.spec            # PyInstaller spec (Windows exe)
├── appfactory.settings.json            # Default settings
├── apps/
│   ├── utils/app_settings_system.py    # Main settings system
│   ├── methods/imgfactory_svg_icons.py # SVG icons (optional)
│   └── themes/*.json                   # 41 bundled themes
└── depends/App_System_Setting_Svg_icons.py
```

---

## Running

```bash
python3 launch_settings.py
```

Windows: download `App_Settings_System_Windows.zip` from the `windows-build` release, unzip, run `App_Settings_System.exe`. Built by GitHub Actions on every push to main.

---

## Integration

### 1. Set App Name

```python
import apps.utils.app_settings_system as settings_module
settings_module.App_name = "My Application"
```

### 2. Import

```python
from apps.utils.app_settings_system import (
    AppSettings, SettingsDialog, apply_theme_to_app,
    AppPanelEffect, apply_panel_effects
)
```

### 3. Initialise

```python
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.app_settings = AppSettings()
        apply_theme_to_app(self, self.app_settings)
```

### 4. Open Settings Dialog

```python
def open_settings(self):
    dialog = SettingsDialog(self.app_settings, self, main_window=self)
    dialog.themeChanged.connect(lambda t: apply_theme_to_app(self, self.app_settings))
    dialog.exec()
```

### 5. Apply Panel Effects

```python
# After applying theme — draws fill/gradient/pattern on QGroupBox and panels
apply_panel_effects(self, self.app_settings)
```

### 6. Use SVG Icons

```python
from utils.depends.App_System_Setting_Svg_icons import IconProvider
self.icons = IconProvider(self, self.app_settings)
btn.setIcon(self.icons.settings_icon())
```

---

## Settings Dialog Tabs

| Tab | Contents |
|-----|----------|
| **Colors** | Colour picker, per-colour transparency column, theme load/save/delete, Apply Theme |
| **Fonts** | One row per font: family, size, weight |
| **Buttons** | Button style dropdown, live preview, tint on/off, per-panel tint grid |
| **Panels** | Four panel previews; fill / gradient / pattern / image (per panel or across window) / opacity |
| **Gadgets** | Amiga MUI-style gadgets; sliders, buttons, splitter width |
| **Shadows** | Shadow depth and colour controls |
| **UI Management** | Group, scrollbar, listview components; progress bar styles |
| **Interface** | Toolbar, statusbar, menu visibility |
| **Localisation** | Locale auto-detect, language, date/number format, per-app overrides |
| **Debug** | Debug mode, log level, category filters |

---

## Panel Effects

Set `panel_effect_type` in settings to `fill`, `gradient`, or `pattern`:

```python
app_settings.current_settings['panel_effect_type'] = 'gradient'
app_settings.current_settings['panel_grad_dir'] = 1        # V top→bottom
app_settings.current_settings['panel_grad_stop1'] = '#1a1a2e'
app_settings.current_settings['panel_grad_stop2'] = '#2d1b4e'
app_settings.current_settings['panel_grad_stop3'] = '#16213e'
apply_panel_effects(my_window, app_settings)
```

---

## Button Styles

Set `button_style` in settings — applied globally via `_generate_stylesheet`:

```python
app_settings.current_settings['button_style'] = 'amiga_wb'
my_window.setStyleSheet(app_settings.get_stylesheet())
```

Available: `flat`, `gradient_h`, `gradient_v`, `gradient_45`, `banded`, `zen`, `indented`, `bump`, `amiga_wb`, `half_shine`, `shadow_dark`

---

## Bundled Themes (41)

Amiga MUI Light/Dark, Amiga WB Light, App Factory, Blue Panels Dark, Blue/Green/Lavender/Pastel/Peach/Pink/Red/Yellow Light, Classic Dark, Cyberpunk Dark, Default Green, Garujaro Dark, GTA Forums Light/Dark, GTA Liberty City/San Andreas/Vice City Dark, IMG Factory Light/Dark, Knight Rider Dark, Manjaro Dark, Matrix Dark, Professional Light, Red Dead Dark, Rockstar Dark, Synthwave Outrun Dark, System KDE, Tea and Toast Dark, Yellow Sunshine Light.

---

## Requirements

- Python 3.10+
- PyQt6
- PyQt6-Qt6 / PyQt6-sip

---

## Applications Using This System

- **IMG Factory 1.6** — GTA modding suite (IMG, TXD, COL, DFF, IPL, IDE)
- **COL Workshop** — GTA collision editor
- **TXD Workshop** — GTA texture editor
- **Model Workshop** — GTA DFF model editor
- **DP5 Workshop** — Deluxe Paint 5 clone bitmap editor
- **Radar Workshop** — GTA radar tile editor
- **AI Workshop** — AI assistant integration
- **Map, Timecyc, Paths, Vehicle, Zon, Water, Hex Workshops**, Model Viewer, RW CoreFramework

---

See [CHANGELOG.md](CHANGELOG.md) for full history.
