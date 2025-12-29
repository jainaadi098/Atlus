# 🧩 ATLUS V7 (Object-Oriented Logic Engine)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Production_Ready-green?style=for-the-badge)
![Architecture](https://img.shields.io/badge/Architecture-OOP_Class_Based-purple?style=for-the-badge)
![Feature](https://img.shields.io/badge/Feature-SAPI_Voice_Engine-red?style=for-the-badge)

> **Version:** V7.0 (The Architect Edition)

**ATLUS** (Antakshari Text Logic Utility System) is a professional-grade, terminal-based Word Chain engine built in Python.

Originally a simple script, **V7** represents the final evolution into a fully **Object-Oriented Software System**. It features a robust Class architecture, the high-performance **Windows SAPI Voice Engine**, and persistent memory, all wrapped in a sci-fi command-line interface.

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

## ⚙️ Key Features (V7 Edition)

### 🏗️ Object-Oriented Architecture (New in V7)
* **Class-Based Design:** The entire engine is encapsulated within the `AtlusGame` class.
* **Encapsulation:** Game states (score, lives, history) are protected within the object (`self`), eliminating global variable errors.
* **Scalability:** The modular design allows for easy addition of new methods or game modes.

### 🗣️ SAPI Voice Engine (Upgraded in V7)
* **Windows Native Audio:** Switched from `pyttsx3` to `win32com.client` (SAPI) for faster, smoother, and more stable voice feedback.
* **Dynamic Interaction:** The system verbally announces rounds, explains specific errors, and reads out rules.

### 💾 Persistent Memory
* **High Score Tracking:** Automatically creates and updates a `high_score.txt` file.
* **Legacy Preservation:** Retains records even after the application is closed.

### 🎨 The Sci-Fi Interface
* **Typewriter Effect:** Text renders character-by-character (`0.03s` delay) simulating a retro hacker terminal.
* **Dynamic Pacing:** Strategic pauses during system checks for dramatic tension.

### ⚖️ Dynamic Difficulty Scaling
| Mode | Lives | Skips | History | Scoring Logic |
| :--- | :--- | :--- | :--- | :--- |
| **Easy** | 3 | 3 | Visible | Flat (+1) |
| **Medium** | 2 | 1 | Visible | Step (+1 / +3) |
| **Hard** | 1 | 0 | **HIDDEN** | **Ladder (+1 ➞ +5)** |

---

## 🧱 Version History & Engineering Journey
This project evolved through iterative development, moving from a basic script to professional software engineering.



* **v1 (Prototype):** Proof of concept using mathematical loop control. Fragile input handling.
* **v2 (Functional):** Added `history_list` for memory and case-insensitive string handling.
* **v3 (Intelligent):** Integrated `pyspellchecker` API to reject non-dictionary words.
* **v4 (Robust):** Implemented `while True` validation loops to handle edge cases.
* **v5 (The Interface):** Introduced Sci-Fi UI, Difficulty Modes, and Skip Locking.
* **v6 (The System):** Integrated Voice (TTS) and File Handling.
* **v7 (The Architect):** *Current Build.* Refactored into **Object-Oriented Programming (OOP)**. Switched to **SAPI Voice** for stability. Fixed uppercase logic bugs for 100% accuracy.

---

## 🛠️ Technical Stack
* **Language:** Python 3.12+
* **Architecture:** Object-Oriented Programming (OOP)
* **External Libraries:**
    * `pyspellchecker` (Logic Validation)
    * `pywin32` (Audio/SAPI Engine)
* **Key Concepts:**
    * Classes & Objects (`self`, `__init__`)
    * Encapsulation
    * File Handling (Read/Write I/O)
    * Exception Handling (`try-except`)

---

## 🚀 Installation & Usage

### 1. Clone the repository
```bash
git clone [https://github.com/jainaadi098/Atlus.git](https://github.com/jainaadi098/Atlus.git)
cd Atlus
2. Install Dependencies
You need the spell checker and the Windows extensions for audio.

Bash

pip install pyspellchecker pywin32
3. Run the Game
Bash

python atlus_v7.py
👨‍💻 Author
Aadi Jain Student Developer & Logic Enthusiast
