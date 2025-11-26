# 🧩 ATLUS (Antakshari Text Logic Utility System)

![Python](https://img.shields.io/badge/Python-3.12-blue.svg) ![Status](https://img.shields.io/badge/Status-Stable-green.svg) ![Logic](https://img.shields.io/badge/Architecture-Modular-orange.svg)

**ATLUS** is a robust, logic-based word engine developed in Python.
It digitizes the mechanics of the classic Indian game *"Antakshari"* (Word Chain), transforming it into a crash-proof software system using modern validation techniques and modular architecture.

---

## 🎮 How It Works
The system functions as a **Text Logic Utility** that validates user inputs against three strict logic gates in real-time.

1.  **Start:** The user enters a name (validated to ensure it ends with an alphabet character).
2.  **The Seed:** The system derives the starting letter from the last character of the user's name.
3.  **The Loop:** The user must enter a valid English word starting with the target letter.
4.  **The Validation:** Every input must pass the **Three-Gate Architecture**:
    * 🚪 **Gate 1 (Syntax):** Does the word start with the correct letter?
    * 🚪 **Gate 2 (Memory):** Has the word been used before? (History Tracking)
    * 🚪 **Gate 3 (Semantics):** Is it a valid English word? (Dictionary Check via `pyspellchecker`)

If any gate fails, the game ends immediately (**Sudden Death Mode**).

---

## 🧱 Version History & Engineering Journey
This project evolved through iterative development, moving from a basic script to a professional engine.

* **v1 (Prototype):** Proof of concept using mathematical loop control. Fragile input handling.
* **v2 (Functional):** Added `history_list` for memory and case-insensitive string handling.
* **v3 (Intelligent):** Integrated `pyspellchecker` API to reject non-dictionary words (e.g., "asdf").
* **v4 (Robust):** Implemented `while True` validation loops to handle edge cases (empty inputs, numbers, symbols).
* **Modified v4 (Modular Refactor):** *Current Build.* Transformed the monolithic V4 script into a **Modular Architecture**. Logic is now separated into reusable functions (`game_rules_check`, `valid_name_input`) for scalability and clean code standards.

---

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **External Libraries:** `pyspellchecker`
* **Key Concepts:**
    * Modular Programming (Functions)
    * Boolean Logic Gates
    * Input Sanitization & Error Handling
    * State Management

---

## 🚀 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/jainaadi098/Atlus.git](https://github.com/jainaadi098/Atlus.git)
Install Dependencies: ATLUS requires the spell-checking library.

Bash

pip install pyspellchecker
Run the Game:

Bash

python game.py
📂 Project Structure
Plaintext

ATLUS/
│
├── game.py            # The main game engine (Modified V4 Modular Code)
├── requirements.txt   # Dependency list
├── README.md          # Project documentation
└── details.md         # Detailed development log and version history


👨‍💻 Author
Aadi Jain Student Developer & Logic Enthusiast
