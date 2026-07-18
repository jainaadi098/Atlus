🌐 ATLUS v8.0

Antakshari Text Logic Utility System

ATLUS is an advanced, interactive, text-based word-chain game built in Python. Inspired by the classic game of "Antakshari," players must chain valid English words together, where each new word begins with the last letter of the previous word.

Featuring a built-in AI opponent, Text-to-Speech (TTS) integration, real-time dictionary validation, and dynamic scoring, ATLUS demonstrates robust Object-Oriented Programming (OOP) and algorithmic design.

✨ Features

3 Game Modes:

Solo Mode: Practice and set personal high scores.

Multiplayer Mode: Pass-and-play against a friend locally.

Computer (AI) Mode: Battle the ATLUS AI, which scales in difficulty and utilizes weighted probabilities to make "human-like" mistakes.

Dynamic Difficulty: Easy, Medium, and Hard (Grandmaster) modes with scaling score ladders, life limits, and history visibility.

Voice Integration: Fully voiced gameplay and rules using Windows SAPI (win32com).

Strict Validation: Real-time spell checking using pyspellchecker to prevent fake words.

Memory & State: Prevents word repetition and saves your Highest Score persistently across sessions.

Infinite Loop Failsafes: Built-in safeguards to prevent the AI from crashing when valid word options are exhausted.

🛠️ Prerequisites

To run ATLUS, you will need Python 3.x installed on a Windows machine (for the SAPI Voice engine).

You will also need to install the required external libraries:

pip install pyspellchecker pywin32


🚀 How to Run

Clone this repository to your local machine:

git clone https://github.com/jainaadi098/atlus-game.git


Navigate to the folder:

cd atlus-game


Run the game:

python main.py


🎮 How to Play

The Golden Rules:

Your word MUST start with the required assigned letter.

You CANNOT repeat a word that has already been used in the current game.

Your word MUST be a valid English dictionary word.

Surviving: You have a limited number of lives depending on your difficulty. Enter an invalid word, and you lose a life.

Scoring: Harder difficulties reward you with a progressive ladder scoring system (+1 to +5 points per round).

⚡ Special Commands

You can type these at any time during your turn:

#VOICE : Toggle the Text-to-Speech voice ON or OFF.

#RULES : Display the game rules.

#HISTORY: View all the words used so far (Disabled in Hard Mode).

#SKIP : Skip your turn and get a new random letter (Unlocks at Round 6).

#EXIT : Surrender and quit the current game.

🧠 Technical Highlights

OOP Architecture: The entire game loop, state management, and entity behaviors are encapsulated within the AtlusGame class.

Algorithmic Failsafes: The AI utilizes state-space exhaustion detection. If no valid 3-letter word is found, it automatically scales up the search length, with a hard cap to prevent infinite while loop crashes.

Created by Aadi Jain. Digitizing the logic of words.
