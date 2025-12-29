from spellchecker import SpellChecker 
import random
import string
import sys
import time
import pyttsx3
import os

spell=SpellChecker()

def get_high_score():
    if os.path.exists("high_score.txt"):
        try:
            with open("high_score.txt", "r") as file:
                high_score = int(file.read())
        except:
            return 0
    else:
        high_score = 0
    return high_score

def new_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))


def speak(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(text)
    slow_print(text)
    
    engine.runAndWait()

def speaken(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.say(text)
    engine.setProperty('voice',voices[1].id)
    engine.runAndWait()

def slow_print(text, delay=0.03):
    # Print text slowly to simulate typing effect
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # for newline after the text

def valid_name_input():
    # Define allowed characters for manual validation   
    letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # --- NAME INPUT SECTION ---
    speak('Enter your name : ')
    name=str(input())   # it might also be username
    
    name1=name.strip() # Remove extra spaces from the start and end
    while True:
        # Check if name is NOT empty AND the last character is inside our 'letters' string
        if len(name1)!=0 and name1[-1].upper() in letters:    
            return name1 # Input is valid, return the name
            
        else:
            # If input is invalid, ask again
            speak("You did not enter any name")
            speak("please enter your name to play the game")
            speak("Enter your name : ")
            name=str(input())
            name1=name.strip()

def starting_message(name):
    print("\n")
    speak(f"CONNECTING TO SERVER...")
    time.sleep(0.3)
    speak(f"USER DETECTED: {name.upper()}") 
    time.sleep(0.3)
    print('''
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║                   🌐  SYSTEM ONLINE  🌐                  ║
    ║                                                          ║
    ║                      A  T  L  U  S                       ║
    ║             Antakshari Text Logic Utility System         ║
    ║                                                          ║
    ╠══════════════════════════════════════════════════════════╣
    ║             ⚡  Digitizing the Logic of Words  ⚡            ║
    ╚══════════════════════════════════════════════════════════╝
    ''')
    speaken("Welcome to ATLUS Game Version 6")
    time.sleep(0.8) # 1 second wait
    speak("Press Enter to load rules...")
    input()
    display_rules()
    print()
    print()
    speak("Press Enter to start the game...")
    input()
    print()
    print()

def calculate_score(score,Round,dificulty):  
    
    if dificulty=='1':  # Easy Mode
        score += 1  # Flat +1 per valid word
    
    elif dificulty=='2':  # Medium Mode
        if Round <= 10:
            score += 1  # +1 per valid word till Round 10
        else:
            score += 3  # +3 per valid word after Round 10
    
    else:  # Hard Mode
        if Round <= 5:
            score += 1
        elif Round <= 10:
            score += 2
        elif Round <= 15:
            score += 3
        elif Round <= 20:
            score += 4
        else:
            score += 5
    
    return score

def game_rules_check(word,word_used,letter,spell):
    
    # --- LOGIC GATES ---
    
    # Rule 1: Does the word start with the required letter?
    if letter!=word[0] :
        # Fail: Wrong starting letter
        
        return False,"your word does not start with the given letter"
    
    # Rule 2: Has the word been used before?
    if word in word_used :
            # Fail: Word repeated
            return False ,"You have already used this word"
    
    # Rule 3: Is the spelling valid?
    if word not in spell:
        return False,"Your word is not valid"
    
    # If all checks passed
    return True, "Valid Turn"

def congratulations_message(name, score, Round,current_high_score):
    print("\n" + "═"*50)
    speak("🛑  GAME OVER DETECTED...")
    time.sleep(0.5)
    speak("    GENERATING PERFORMANCE REPORT...")
    time.sleep(0.5)
    
    if score>current_high_score:
        print("-" * 50)
        speak(f"""Congratulation New High {score}""")
    print("-" * 50)
    speak(f"   ➤ PLAYER NAME    : {name.upper()}")
    speak(f"   ➤ FINAL SCORE    : {score}")
    speak(f"   ➤ ROUNDS CLEARED : {Round-1}")
    
    
    
    print("═"*50 + "\n")
    time.sleep(0.5)
    
def display_rules():
    time.sleep(1)
    print('''
    ============================================================
                 📜 ATLUS GAME RULES & SURVIVAL GUIDE           
    ============================================================
    
    🔹 OBJECTIVE:
       Chain English words together. The last letter of your word
       becomes the starting letter for the next round.

    🔹 THE 3 GOLDEN GATES:
       1. MUST start with the assigned letter.
       2. NO repetition of previously used words.
       3. MUST be a valid word in the dictionary.

    🔹 DIFFICULTY MODES:
    ------------------------------------------------------------
    | MODE     | LIVES | SKIPS | HISTORY | SCORING         |
    ------------------------------------------------------------
    | EASY     | 3     | 3     | Show    | Flat (+1)       |
    | MEDIUM   | 2     | 1     | Show    | Step (+1 / +3)  |
    | HARD     | 1     | 0     | HIDDEN  | Ladder (+1 -> +5)|
    ------------------------------------------------------------

    🔹 SPECIAL COMMANDS:
         Type '#RULES' to view the game rules again.
         Type '#HISTORY' to view used words so far.
         Type '#SKIP'to skip and get randonly new letter.
       ⚠️  IMPORTANT: Skips are LOCKED until Round 6!
         Type '#EXIT' to quit the game anytime.

    ============================================================
    ''')
    speaken("""This game is a word-chain challenge. 
            Your goal is to keep forming valid English words where each new word starts with the last letter of the previous one. 
            There are three core rules: 
            The word must begin with the assigned starting letter. 
            You cannot repeat any word that has already been used. 
            Every word must be valid and recognized in the dictionary. 
            The game offers three difficulty modes — Easy, Medium, and Hard — each with different lives, skip limits, and scoring styles. 
            You can also use special commands during the game: 
            #RULES to view the rules, 
            #HISTORY to check previously used words, 
            #SKIP to change the letter (available from Round 6 onward), 
            and #EXIT to leave the game at any time.""")

def access_used_words(word_used,dificulty_level):
    if dificulty_level<3:
        time.sleep(0.5)
        speak("\nUsed words so far:")
        print(word_used)
        print()
    else:
        time.sleep(0.5)
        speak("there is no access to used words in hard mode")

def skip(skips,word_used,letter,Round):
    if skips==0:
        speak("You have no skips left!")
        return skips,letter
    elif Round<6:
        speak("Skips are locked until Round 6!")
        return skips,letter
    else:
        skips-=1
        letter=random.choice(string.ascii_uppercase)
        speak(f"Skip used! '")
        
        return skips,letter

def difficulty_level():
    time.sleep(1)
    print('''
          
    ╔══════════════════════════════════════════════════╗
    ║          🎯  SELECT DIFFICULTY LEVEL  🎯           ║
    ╠══════════════════════════════════════════════════╣
    ║                                                  ║
    ║  1️⃣  EASY MODE                                   ║
    ║     ❤️  Lives: 3   | ⏭️  Skips: 3                 ║
    ║     📜  History: Visible                         ║
    ║     ⭐  Score: +1 Flat                           ║
    ║                                                  ║
    ║  2️⃣  MEDIUM MODE                                 ║
    ║     ❤️  Lives: 2   | ⏭️  Skips: 1                 ║
    ║     📜  History: Visible                         ║
    ║     ⭐  Score: +1 (till R10) then +3             ║
    ║                                                  ║
    ║  3️⃣  HARD MODE (Grandmaster)                     ║
    ║     ❤️  Life:  1   | ⏭️  Skips: 0                 ║
    ║     🚫  History: HIDDEN                          ║
    ║     🔥  Score: Ladder System (+1 to +5)          ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝

    ⚠️  NOTE: Skips are LOCKED until Round 6!

    👉 Choose your level (1, 2, or 3):
    ''')
    speaken("""The game offers three difficulty modes, 
          each designed to provide a different level of challenge: 
          1. Easy Mode You receive 3 lives and 3 skips. Your word history remains visible at all times, making it easier to track what has been used. Every correct word gives you a flat +1 point. 
          2. Medium Mode This mode provides 2 lives and 1 skip. The history is still visible, but scoring becomes progressive — you earn +1 point for each correct word until Round 10, after which each correct answer awards +3 points. 
          3. Hard Mode (Grandmaster) This is the highest difficulty. You get only 1 life and no skips. Your previously used words remain hidden, increasing the challenge. Scoring follows a ladder pattern, starting with +1 and gradually rising to +5 as you progress. Please note that skips remain locked until Round 6, regardless of the chosen mode. Now, 
          choose your difficulty level — 1, 2, or 3.""")
    
    speak("Enter 1, 2, or 3 to select difficulty: ")
    difficulty=input()
    while difficulty not in ['1','2','3']:
        speak("Invalid choice. Please enter 1, 2, or 3.")
        difficulty=input("Enter 1, 2, or 3 to select difficulty: ")
    return difficulty

def main_game_loop(word_used,letter,Round,score,difficulty,lives,skips,name,current_high_score):
    # 3. Main Game Loop
    
    while True :
        
        print()
        print() 
        time.sleep(0.5)
        speak(f"Round {Round}")
        
        speak(f"Your letter is {letter}")
        speak("Enter your word : ")
        word=str(input())
        
        #########################################
        word=word.upper()
        
        if word== "#RULES":  # display Rules again
            display_rules()
            continue
        elif word=="#HISTORY":  # display used words
            access_used_words(word_used,int(difficulty))
            continue
        elif word=="#SKIP":  # skip
            skips,letter=skip(skips,word_used,letter,Round)
            continue
        elif word=="#EXIT":  # quit game
            print("You chose to quit the game.")
            print("\nUsed words :",word_used,"\n\n")
            congratulations_message(name,score,Round,current_high_score)
            return score
        else:
            pass
        #########################################
        
        word=word.strip()
        
        # SAFETY CHECK: If user hits Enter without typing
        if len(word)==0:
            speak("You did not type any word ")
            speak("please try agian")
            continue # Skip the rest and restart the loop
        
        
        
        # Convert input to uppercase for game logic comparison
        
        
        
        # Game Rules Check
        valid, message = game_rules_check(word, word_used, letter, spell)
        
        
        
        #####################################
        
        
        
        if not valid:
            lives-=1
            if lives==0:
                time.sleep(0.5)
                speak(f"\n\nGame Over\n {message}")
                speak(f"\nUsed words :{word_used}\n\n")
                time.sleep(0.5)
                congratulations_message(name,score,Round,current_high_score)
                return score
            else:
                time.sleep(0.5)
                speak(f"Invalid Turn! You have {lives} lives left.")
                speak(f"Reason: {message}")
                speak("Please try again.")
                print()
                print("-----------------------------------")
                print()
                continue
            
        
        
        
        
        ######################################
        
        # If all checks passed
        word_used.append(word)  # Add word to used list
        
        score = calculate_score(score,Round,difficulty)           # Increment score
        Round=Round+1
        letter = word[-1]       # Update letter for next round

def main():
    # 1. Setup Tools
    current_high_score=get_high_score()
    
    name=valid_name_input()
    starting_message(name)
    
    
    
    
    # 2. Game State Setup
    word_used=[]   # to check repeated words 
    first_letter=name[-1] # first letter to begin (taken from name)
    letter=first_letter.upper()  # converting to uppercase
    Round=1        # rounds count
    score=0      # score count
    difficulty=difficulty_level()
    
    
    if difficulty=='1':
        lives=3
        skips=3
    elif difficulty=='2':
        lives=2
        skips=1
    else:
        lives=1
        skips=0
    
    # Start Main Game Loop
    score=main_game_loop(word_used,letter,Round,score,difficulty,lives,skips,name,current_high_score)
    
    if current_high_score<score:
        new_high_score(score)
    

while True:
    main()
    speak("Do you want to play again? (yes/no)")
    reply=input().lower()
    if reply!='yes':
        time.sleep(0.5)
        speak("Thanks for playing!")
        break
