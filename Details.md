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
**Status:** Professional Engine (Current Build)
- **The Problem:** V4 was robust but hard to maintain. Adding features (like Lives or Multiplayer) would require breaking the main loop.
- **The Solution:** Refactored the V4 script into **Reusable Functions** (Modular Programming) without altering the "Sudden Death" gameplay mechanics.
    1. **`valid_name_input()`**: An independent function to handle user name validation.
    2. **`game_rules_check()`**: A pure logic function that returns Boolean values (`True`/`False`) and specific error messages.
    3. **`main()`**: A clean controller function that manages game state and flow.
- **Result:** The codebase now follows professional Software Engineering standards (Separation of Concerns).

---
*Last Updated: Modified V4 Refactor*