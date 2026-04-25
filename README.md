# Global App System Settings
<!-- Updated: April 2026 — Major overhaul: Panels tab, Buttons v2, Localisation, Progress Bars, SVG icons depends, panel effects engine -->

A reusable theming, settings and panel effects system for PyQt6 applications.
Used by IMG Factory 1.6, COL Workshop, TXD Workshop, Model Workshop, DP5 Workshop and more.

---

## Overview

`app_settings_system.py` provides a complete theme and UI management solution for any PyQt6 application:
theme creation, saving, loading, applying, panel fill/gradient/pattern effects, button styles, progress bar styles, localisation foundation, and a self-contained settings dialog with live previews.

---

## Features

- **Theme Management** — create, save, load, delete custom themes; 37 bundled themes
- **Colour Customisation** — full colour editor with live preview and XP-style picker
- **Button Styles** — 11 styles: Flat, Gradient H/V/45°, Banded (Win ME), Zen, Indented, Bump, Amiga WB, Half-shine, Shadow-dark
- **Panel Effects** — fill (solid/two-tone), gradient (6 directions, 3 stops), pattern (9 styles), image background, transparency — applied live via `AppPanelEffect`
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
your_project/
├── utils/
│   ├── app_settings_system.py          # Main settings system
│   └── depends/
│       ├── __init__.py
│       └── App_System_Setting_Svg_icons.py  # SVG icon provider
├── themes/
│   └── *.json                          # 37 bundled themes
└── your_main_app.py
```

---

## Integration

### 1. Set App Name

```python
import utils.app_settings_system as settings_module
settings_module.App_name = "My Application"
```

### 2. Import

```python
from utils.app_settings_system import (
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
| **Colors** | XP-style colour picker, theme load/save/delete |
| **Fonts** | Font family, size, weight per UI element |
| **Buttons** | 11 button styles with live preview row, tint on/off, per-panel tint colours |
| **Panels** | Fill / Gradient / Pattern / Image / Transparency / Gadgets — all with two-column live preview |
| **Gadgets** | Amiga MUI-style gadget styling (string, gauge, scale, knob…) |
| **Shadows** | Shadow depth and colour controls |
| **UI Management** | Components (group, scrollbar, listview) + Progress Bar styles |
| **Interface** | Toolbar, statusbar, menu visibility |
| **Localisation** | Locale auto-detect, language selector, date/number format, per-app overrides |
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

## Bundled Themes (37)

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

---

See [CHANGELOG.md](CHANGELOG.md) for full history.
