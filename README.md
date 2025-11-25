# 🧩 Word Chain Game (Python)

A robust and interactive **word-chain game** built in Python.  
The player must enter a valid English word starting with the **last letter of the previous word** (or the last letter of their name to start).  
The game continues indefinitely until a wrong input, spelling mistake, or repeated word is entered.

---

## 🎮 How to Play
1. **Start:** Enter your name (must end with a letter A-Z).
2. **The Letter:** The game assigns you a starting letter.
3. **The Challenge:** Type a valid English word starting with that letter.
4. **Score:** Each correct word adds **+1** to your score.
5. **Game Over:** The game ends if you:
   - Use a word that doesn't start with the correct letter.
   - Repeat a word you already used.
   - Enter a word with incorrect spelling.

---

## 🧱 Versions History
- **v1:** Basic loop and core logic implementation.
- **v2:** Added scoring system, word repetition check, and uppercase handling.
- **v3:** Integrated spell-check validation using `pyspellchecker` to ensure words are real.
- **v4 (Final):** Added robust input safety (anti-crash), manual name validation logic, and detailed error messages.

---

## 🛠️ Requirements
This game requires Python and the `pyspellchecker` library.

**Installation:**
```bash
pip install pyspellchecker
Run the Game:

Bash

python game.py
📂 Project Structure
game.py - The main source code for the game.

details.md - A step-by-step development log explaining how the logic evolved.

README.md - This documentation file.

👨‍💻 Author
Aadi Jain B.Tech Engineering Student | Python Developer
