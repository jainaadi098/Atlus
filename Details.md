# 📂 Development Log: The Evolution of ATLUS

This document tracks the engineering decisions, logic implementation, and refactoring process during the development of **ATLUS** (Antakshari Text Logic Utility System).

---

### 🟢 Version 1: The Prototype
**Status:** Proof of Concept
- **Goal:** Create a basic infinite loop where the user links words by the last letter.
- **Implementation:** Used a unique mathematical trick (`n = -n`) to control the loop termination.
- **Issues:** The code was extremely fragile. It crashed on empty inputs, had no case sensitivity, and accepted non-dictionary words (like "asdf").

### 🟡 Version 2 & 3: Intelligence & Memory
**Status:** Functional Script
- **Memory Integration:** Introduced a list (`word_used`) to track history and prevent players from repeating words.
- **AI Integration:** Implemented the `pyspellchecker` library to validate if a word actually exists in the English dictionary.
- **Issues:** While functional, the code structure became "Spaghetti Code" (deeply nested if-else statements), making it difficult to read and debug.

### 🟠 Version 4: Robustness (The Production Script)
**Status:** Stable Release
- **Focus:** Crash-proofing the application.
- **Input Validation:** Replaced simple inputs with `while True` validation loops. The game could now handle accidental spaces, numbers, and empty Enter presses without crashing.
- **Logic Gates:** Implemented a strict "Three-Gate Architecture" (Start Letter Check → History Check → Spell Check).
- **Architecture:** Monolithic (Single block of code). All logic, input handling, and game flow were inside one massive `while` loop.

### 🔵 Modified Version 4: Modular Architecture (The Refactor)
**Status:** Clean Codebase
- **The Problem:** V4 was robust but hard to maintain. Adding features (like Lives or Multiplayer) would require breaking the main loop.
- **The Solution:** Refactored the V4 script into **Reusable Functions** (Modular Programming) without altering the "Sudden Death" gameplay mechanics.
    1. **`valid_name_input()`**: An independent function to handle user name validation.
    2. **`game_rules_check()`**: A pure logic function that returns Boolean values (`True`/`False`) and specific error messages.
    3. **`main()`**: A clean controller function that manages game state and flow.
- **Result:** The codebase now follows professional Software Engineering standards (Separation of Concerns).

### 🟣 Version 5: The Game Design Update
**Status:** Full Feature Release
- **Focus:** User Experience (UX) and Gameplay Mechanics.
- **Gamification:** Introduced **Difficulty Levels** (Easy, Medium, Hard) impacting Lives and Skips.
- **Scoring Algorithms:** Implemented distinct scoring logic (Flat vs. Progressive vs. Ladder scoring) based on difficulty.
- **Command System:** Added in-game "Cheat Codes" (`#SKIP`, `#HISTORY`, `#RULES`) accessible directly via the input prompt.
- **Aesthetics:** Implemented `slow_print` algorithms and ASCII art to create a retro "Sci-Fi Terminal" atmosphere.

### 🟤 Version 6: The System Update (I/O & Audio)
**Status:** Interactive System
- **Focus:** Persistence and Immersion.
- **File I/O:** Added **Persistent Memory**. The game now uses `os` modules to read/write a `high_score.txt` file, allowing records to survive even after the computer is restarted.
- **Voice Integration:** Integrated `pyttsx3` (Text-to-Speech) to give the system a voice.
- **Error Handling:** Implemented `try-except` blocks to handle missing file errors gracefully.

### ⚫ Version 7: The Architect (Object-Oriented Programming)
**Status:** Professional Engine (Final Build)
- **The Problem:** Global variables in V6 were becoming unmanageable.
- **The Solution:** A complete rewrite using **Object-Oriented Programming (OOP)**.
- **Class Architecture:** The entire game is now encapsulated in the `AtlusGame` class. All variables (`self.score`, `self.lives`) are protected within the object instance.
- **Engine Swap:** Replaced the `pyttsx3` voice engine with the Windows native **SAPI Engine** (`win32com.client`) for superior stability and speed.
- **Logic Perfection:** Fixed a critical logic flaw where uppercase inputs caused valid words to fail the spell check (`word.lower()` fix).

---
*Last Updated: Version 7.0 Final Release*
