# Global App System Settings — Changelog

---

## April 2026 — Major overhaul (Builds 337–345)

### Renamed: Global App System Settings
`App_name` changed from `"GUI - App System Settings"` to `"Global App System Settings"` — reflects use across all apps in the suite.

### New: `depends/` package
- `depends/App_System_Setting_Svg_icons.py` v1 — `IconProvider` class extracted from main file into its own module with full `##Methods` list and standalone import support.
- `depends/__init__.py` — clean package export.

### Settings Dialog — always frameless
- Dialog now always sets `FramelessWindowHint` regardless of `use_custom_gadgets` setting.
- Titlebar pattern matches COL Workshop: `[Menu] [Settings] | Title | [i] [—] [□] [✕]`
- Drag uses `windowHandle().startSystemMove()` — fully Wayland compatible.
- **Settings button** opens mini self-settings dialog (font family/size, titlebar height) — no longer disabled.
- `_is_on_draggable_area` v4: works for `toolbar`, `dialog_titlebar` and `custom_titlebar` — fixed AttributeError that prevented dragging.

### New Tab: Panels (replaces Background + Transparency + Advanced Gadgets)
All three old tabs merged into one with sub-tabs:
- **Fill** — solid/two-tone with 7 direction options; hero banner gradient colour pickers (dark/light theme variants); Active Panel Effect selector (None/Fill/Gradient/Pattern).
- **Gradient** — 6 directions (H, V, 4 diagonals), 3 colour stops.
- **Pattern** — 9 styles (Dots, Lines H/V/Diagonal, Check, Waves, Tartan, Picnic, Odd/Even rows), scale slider, light/dark colour pickers; Copper effect colour pickers.
- **Image** — panel background image with 5 display modes and blend opacity.
- **Transparency** — all 4 opacity sliders (Titlebar/Panels/Buttons/Widgets).
- **Gadgets** — existing Amiga MUI gadget settings.
- Every sub-tab uses a **two-column layout**: controls left (55%), live preview right (45%).

### New: `PanelPreviewWidget` and `AppPanelEffect`
- `PanelPreviewWidget` — custom `paintEvent` widget rendering fill/gradient/pattern/copper/image/transparency/hero modes. Updates live as you change controls.
- `AppPanelEffect` — mixin installed on `QGroupBox` and `StyledPanel` `QFrame` widgets to draw effects in real windows. Call `apply_panel_effects(window, app_settings)` after theme apply.
- `apply_panel_effects()` now called in `_apply_settings` so effects take effect on Apply without restart.

### New: Buttons Tab v2
- 11 button styles with **live preview row**: Flat, Gradient H/V/45°, Banded (Win ME), Zen, Indented, Bump, Amiga WB, Half-shine, Shadow-dark.
- Workflow colour tints on/off toggle.
- Per-panel tint colour editors (IMG Files, File Entries, Editing Options).
- `_generate_stylesheet` extended to emit QPushButton QSS for gradient/banded/bump/amiga_wb/half_shine styles globally.

### New: Progress Bar Styles (UI Management tab)
- 8 styles: System, Flat, Gradient H/V, Banded, Amiga segments, Glow, Striped.
- Colour pickers for fill, background, text, stripe.
- Height slider (8–32px).
- Emitted in `_generate_stylesheet` as `QProgressBar` QSS.

### New: Localisation Tab
- Auto-detect system locale on/off.
- 12 language stubs (en_GB, en_US, de, fr, es, it, pt, nl, pl, ru, ja, zh_CN).
- Date format (4 options) and number format (4 options) selectors.
- Per-workshop language override dropdowns (foundation for future translation).

### New colour keys (31) added to all 37 theme files
`hero_gradient_dark/light_start/end`, `panel_fill_a/b/dir`, `panel_grad_dir/stop1/2/3`, `panel_pattern_style/scale/light/dark`, `copper_light/dark`, `panel_bg_image/mode/opacity`, `button_style`, `progressbar_style/fill/bg/text/stripe/height`, `panel_effect_type`, `locale_auto_detect`, `language`, `date_format_idx`, `number_format_idx`.

### Bug fixes
- `_get_default_button_colors` v3: replaced `_is_dark_theme()` call (wrong class) with luminance check on `bg_primary`.
- `_on_button_theme_type_changed` v2: no-op stub — detection now via luminance.
- `button_theme_type_combo` dummy created in `_create_buttons_tab_v2` for backward compat.
- Remaining emoji removed: `✓ Apply Theme` → `Apply Theme`, `⚙️ Advanced Styling` → `Advanced Styling`.

---

## March 2026 — Colors Tab Layout Fixes (Build 40 sync)

- Colour list now stretches correctly on window resize — `addWidget(scroll_area, 1)`.
- `QHBoxLayout(self)` bug fixed — parentless layout used instead.
- Left/right panels separated by draggable `QSplitter`.
- `tab_content_mode` setting added.

---

## October 2025

- Complete colour set for Qt6.
- Added `button_pressed`, `selection_background`, `selection_text`, `table_row_even`, `table_row_odd`.
- Updated all bundled theme JSON files.

---

## February 2025

- Initial release.
- Reusable theming and settings system for PyQt6.
- Theme create/save/load/apply, settings dialog, persistent JSON storage.
