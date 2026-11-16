ArgyllCMS 3.5.0 + Spyder 2024 OLED patch (custom Windows x64 build)
====================================================================

Important: This is NOT an official ArgyllCMS 3.5.1 release.

Upstream base: ArgyllCMS 3.5.0 source.
Actual driver patch: Spyder 2024 calibration table is resized from the
5-entry Spyder X2 table to the 7-entry Spyder 2024 table.

This derivative reports version "3.5.1_spyder2024fix" to the DisplayCAL GUI
so its blanket safety guard for <= 3.5.0 does not reject this specifically
patched driver. Its numeric ARGYLL_VERSION remains 0x03050 internally for
calibration-file compatibility. All other original 3.5.0 features are unchanged.

Test status:
- Compiled and checked as Windows x64 executables on GitHub Actions.
- No guarantee of calibration accuracy or hardware functionality until
  verified with a real Spyder 2024 on the target display.

Use DisplayCAL 3.10.0.dev115 or newer with the folder containing bin/ and ref/.
Ensure appropriate USB driver, select Spyder 2024 and OLED panel.
First test white and black separately and confirm measured Y changes plausibly.
Preserve your prior ICC profile until measurements are verified.
