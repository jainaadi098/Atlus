# 🧩 ATLUS — Word Chain Game (Development Details)

This project demonstrates the step-by-step development of a **Word Chain Game** in Python.  
Each version adds new functionality, improving gameplay, fairness, and code robustness.

---

## 🚀 Game Concept
The game gives a **letter** based on the last letter of the previous word (or the player's name).  
The player must enter a **valid English word** that starts with that letter.  
If the input is wrong, repeated, or misspelled — **Game Over!**

---

## 🧱 Version Overview

### 🔹 V1: Core Concept
- Takes user input for a word.  
- Checks if the entered word starts with the given letter.  
- Game continues if the rule matches, otherwise ends.  
➡️ *Basic proof-of-concept.*

### 🔹 V2: Functional Version
- Checks for word **repetition** to avoid reuse.  
- Ends the game if a word is repeated.  
- Adds **score keeping** and **word history** tracking.  
➡️ *V1 + Repetition Prevention + Score System.*

### 🔹 V3: Polished Version
- Integrates **spell checking** using the `pyspellchecker` library.  
- Accepts only real English words.  
- Ensures gameplay accuracy and fairness.  
➡️ *Feature-complete prototype.*

### 🔹 V4: Robust & Crash-Proof (Current)
- **Input Safety:** Handles empty inputs and accidental spaces (using `.strip()` and loop checks).
- **Manual Validation:** Uses custom logic (`name[-1] in letters`) to ensure player names are valid.
- **Logic Gates:** Uses a nested `if/else` structure to provide specific error messages (e.g., "Invalid Word" vs "Already Used").
- **Professional Code:** Includes detailed comments and clean variable naming.
➡️ *The final, stable, and professional version.*

---

## ⚙️ Technical Highlights
- **Library:** Uses `pyspellchecker` for dictionary validation.
- **Logic Architecture:** Implements a "Three Gate" system:
  1.  **Gate 1:** Start Letter Check
  2.  **Gate 2:** Repetition Check
  3.  **Gate 3:** Spelling Check
- **Data Structures:** Uses Lists (`[]`) for history and Strings for validation.

---

## 📦 How to Run
1. Install the required library:
   ```bash
   pip install pyspellchecker
2. Run the script
   python game.py



## 👨‍💻 Author
Aadi Jain 🎓 B.Tech Engineering Student | 💡 Python Learner | 🕹️ Hobby Game Developer