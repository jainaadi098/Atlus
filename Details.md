# 🧩 ATLUS — Word Chain Game (Development Details)

This project demonstrates the step-by-step development of a **Word Chain Game** in Python.  
Each version adds new functionality, improving gameplay, fairness, and accuracy.

---

## 🚀 Game Concept
The game gives a **letter** based on the last letter of the previous word.  
The player must enter a **valid English word** that starts with that letter.  
If the input is wrong, repeated, or misspelled — **Game Over!**

---

## 🧱 Version Overview

### 🔹 V1: Core Concept
- Takes user input for a word.  
- Checks if the entered word starts with the given letter.  
- Game continues if the rule matches, otherwise ends.  
➡️ *Basic proof-of-concept.*

---

### 🔹 V2: Functional Version
- Checks for word **repetition** to avoid reuse.  
- Ends the game if a word is repeated.  
- Adds **score keeping** and **word history** tracking.  
➡️ *V1 + Repetition Prevention + Score System.*

---

### 🔹 V3: Polished Version
- Integrates **spell checking** using the `pyspellchecker` library.  
- Accepts only real English words.  
- Ensures gameplay accuracy and fairness.  
➡️ *Feature-complete and professional version.*

---

## 🧠 Summary
ATLUS evolved from a simple input-checking program into a more robust, feature-rich game with:
- Word validation  
- Repetition prevention  
- Scoring  
- Spell checking  

---

## 👨‍💻 Author
**Aadi Jain**  
🎓 B.Tech Engineering Student | 💡 Python Learner | 🕹️ Hobby Game Developer  
