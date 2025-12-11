# 🧩 ATLUS V6 (Voice-Activated Logic Engine)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Production_Ready-green?style=for-the-badge)
![Feature](https://img.shields.io/badge/Feature-Voice_Feedback-red?style=for-the-badge)
![Feature](https://img.shields.io/badge/Feature-Persistent_Memory-orange?style=for-the-badge)

> **Version:** V6.0 (The Jarvis Update)

**ATLUS** (Antakshari Text Logic Utility System) is a robust, logic-based word engine developed in Python.
It digitizes the mechanics of the classic game *"Antakshari"* (Word Chain), transforming it into a crash-proof software system featuring **Voice Feedback (TTS)**, **Persistent High Score Memory**, and a **Sci-Fi Terminal Interface**.

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

## ⚙️ Key Features (V6 Edition)

### 🗣️ Voice Feedback Core (New in V6)
* **Text-to-Speech Integration:** The system now speaks to the user using the `pyttsx3` engine.
* **Audio Feedback:** It announces round numbers, reads out letters, explains errors verbally, and congratulates the user on new records.

### 💾 Persistent Memory (New in V6)
* **High Score Tracking:** The game uses File I/O to create and read a `high_score.txt` file on the hard disk.
* **Legacy Preservation:** The system remembers the World Record even after the application is closed and restarted.

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
This project evolved through iterative development, moving from a basic script to a professional engine.



* **v1 (Prototype):** Proof of concept using mathematical loop control. Fragile input handling.
* **v2 (Functional):** Added `history_list` for memory and case-insensitive string handling.
* **v3 (Intelligent):** Integrated `pyspellchecker` API to reject non-dictionary words.
* **v4 (Robust):** Implemented `while True` validation loops to handle edge cases (empty inputs, numbers).
* **v5 (The Interface):** Introduced Sci-Fi UI, Difficulty Modes, and Skip Locking.
* **v6 (The Jarvis Update):** *Current Build.* Integrated **Text-to-Speech (Voice)** and **File Handling (Memory)**. Fixed logic return values for production stability.

---

## 🛠️ Technical Stack
* **Language:** Python 3.12+
* **External Libraries:** `pyspellchecker`, `pyttsx3`
* **Key Concepts:**
    * File Handling (Read/Write I/O)
    * Modular Functional Programming
    * Boolean Logic Gates
    * Input Sanitization & Exception Handling (`try-except`)

---

## 🚀 Installation & Usage

### 1. Clone the repository
```bash
git clone [https://github.com/jainaadi098/Atlus.git](https://github.com/jainaadi098/Atlus.git)
cd Atlus
2. Install Dependencies
You need the spell checker and the text-to-speech engine.

Bash

pip install pyspellchecker pyttsx3
3. Run the Game
Bash

python atlus_v6.py
👨‍💻 Author
Aadi Jain Student Developer & Logic Enthusiast