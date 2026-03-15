# App Settings System — Changelog

## March 15, 2026

### Colors Tab Layout Fixes

Three bugs fixed in the Settings → Colors tab that caused the right-side colour
list to not stretch when the window was resized.

**Bug 1 — Colour list not expanding** (`scroll_area` had no stretch factor)
- `right_layout.addWidget(scroll_area)` gave equal weight to all items in the
  right panel, so the colour list, Global Theme Sliders, and Theme Actions all
  competed for space equally.
- Fixed: `addWidget(scroll_area, 1)` — colour list now fills all available
  space; sliders and action buttons stay at their natural height.

**Bug 2 — `QHBoxLayout(self)` corrupting the dialog**
- `theme_layout = QHBoxLayout(self)` passed the dialog as parent, silently
  replacing the dialog's own top-level layout and causing rendering issues.
- Fixed: changed to `QHBoxLayout()` (parentless; inserted into `right_layout`).

**Bug 3 — Left panel not user-resizable**
- The left (colour picker) and right (colour list) panels were in a plain
  `QHBoxLayout`. The left had `setMaximumWidth(350)` with no resize handle.
- Fixed: replaced with `QSplitter(Horizontal)`. Left panel: `min=220, max=400`.
  Right panel: `setStretchFactor(1, 1)`. User can now drag the divider freely.

---

## October 2025

- Added complete colour set for Qt6
- Theme system expansion: added `button_pressed`, `selection_background`,
  `selection_text`, `table_row_even`, `table_row_odd` colour variables
- Updated all bundled theme JSON files

## February 2025

- Initial release
- Reusable theming and settings system for PyQt6 applications
- Theme creation, saving, loading, applying
- Settings dialog with colour customisation
- Persistent JSON storage
