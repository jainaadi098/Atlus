# 🧩 ATLUS (Antakshari Text Logic Utility System)

![Python](https://img.shields.io/badge/Python-3.13.2-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Production_Ready-green?style=for-the-badge)
![Type](https://img.shields.io/badge/Type-Logic_Engine-orange?style=for-the-badge)

> **Version:** V5.0 (Sci-Fi Edition)

**ATLUS** is a robust, logic-based word engine developed in Python.
It digitizes the mechanics of the classic Indian game *"Antakshari"* (Word Chain), transforming it into a crash-proof software system using modern validation techniques, a modular architecture, and a polished **Sci-Fi Terminal Interface**.

---

## 🎮 How It Works
The system functions as a **Text Logic Utility** that validates user inputs against three strict logic gates in real-time.

1.  **The Seed:** The system derives the starting letter from the last character of the user's name.
2.  **The Loop:** The user must enter a valid English word starting with the target letter.
3.  **The Validation:** Every input must pass the **Three-Gate Architecture**:
    * 🚪 **Gate 1 (Syntax):** Does the word start with the correct letter?
    * 🚪 **Gate 2 (Memory):** Has the word been used before? (History Tracking)
    * 🚪 **Gate 3 (Semantics):** Is it a valid English word? (Dictionary Check via `pyspellchecker`)

If any gate fails, the user loses a life. If lives reach zero, the game ends.

---

## ⚙️ Key Features (V5 Edition)

### 🎨 The Sci-Fi Interface
* **Typewriter Effect:** Text renders character-by-character (`0.03s` delay) simulating a retro hacker terminal.
* **Dynamic Pacing:** Strategic pauses during system checks for dramatic tension.

### ⚖️ Dynamic Difficulty Scaling
| Mode | Lives | Skips | History | Scoring Logic |
| :--- | :--- | :--- | :--- | :--- |
| **Easy** | 3 | 3 | Visible | Flat (+1) |
| **Medium** | 2 | 1 | Visible | Step (+1 / +3) |
| **Hard** | 1 | 0 | **HIDDEN** | **Ladder (+1 ➞ +5)** |

### 🔒 Strategic Mechanics
* **Skip Lock Protocol:** Skips (`#@`) are strictly **LOCKED** until Round 6. This prevents players from taking easy escapes in the early game.

---

## 🧱 Version History & Engineering Journey
This project evolved through iterative development, moving from a basic script to a professional engine.

* **v1 (Prototype):** Proof of concept using mathematical loop control. Fragile input handling.
* **v2 (Functional):** Added `history_list` for memory and case-insensitive string handling.
* **v3 (Intelligent):** Integrated `pyspellchecker` API to reject non-dictionary words.
* **v4 (Robust):** Implemented `while True` validation loops to handle edge cases (empty inputs, numbers).
* **Modified v4 (Modular Refactor):** Transformed the monolithic V4 script into a Modular Architecture using functions.
* **v5 (The Engine):** *Current Build.* Introduced Sci-Fi UI, Difficulty Modes, Skip Locking, and removed recursion for better memory management.

---

## 🛠️ Technical Stack
* **Language:** Python 3.12
* **External Libraries:** `pyspellchecker`
* **Key Concepts:**
    * Modular Functional Programming
    * Boolean Logic Gates
    * Input Sanitization & Error Handling
    * Asynchronous Simulation (`time.sleep`)

---

## 🚀 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/jainaadi098/Atlus.git](https://github.com/jainaadi098/Atlus.git)
   cd Atlus
Install Dependencies: ATLUS requires the spell-checking library.

2. **Install Dependencies: ATLUS requires the spell-checking library.**

pip install -r requirements.txt
Run the Game:

3. **Run the Game:**

python atlus_v5.py

---

## 👨‍💻 Author
Aadi Jain Student Developer & Logic Enthusiast
