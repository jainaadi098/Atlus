# 🧩 Word Chain Game (Python)

A simple **word-chain game** built in Python.  
The player must enter a word starting with the **last letter of the previous word**.  
The game continues until a wrong input or repeated word is entered.

---

## 🎮 How to Play
1. Enter your name.  
2. The game gives you a letter.  
3. Type a valid English word starting with that letter.  
4. Each correct word adds **+1** to your score.  
5. If you repeat a word or make a wrong entry — **Game Over!**

---

## 🧱 Versions
- **v1:** Basic loop and core logic.  
- **v2:** Added scoring, repetition check, and uppercase handling.  
- **v3:** Added spell-check validation using `pyspellchecker` for real-word validation.

---

## 🛠️ Requirements
Install the spellchecker module before running version 3:
```bash
pip install pyspellchecker
