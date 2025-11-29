from spellchecker import SpellChecker # pyright: ignore[reportMissingImports]
import random
import string
import sys
import time

spell=SpellChecker()

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
    name=str(input('Enter your name : '))   # it might also be username
    
    name1=name.strip() # Remove extra spaces from the start and end
    while True:
        # Check if name is NOT empty AND the last character is inside our 'letters' string
        if len(name1)!=0 and name1[-1].upper() in letters:    
            return name1 # Input is valid, return the name
            
        else:
            # If input is invalid, ask again
            print("You did not enter any name")
            print("please enter your name to play the game")
            name=str(input('Enter your name : '))
            name1=name.strip()

def starting_message(name):
    print("\n")
    slow_print(f"CONNECTING TO SERVER...", 0.05)
    time.sleep(0.5)
    slow_print(f"USER DETECTED: {name.upper()}") 
    time.sleep(0.5)
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
    time.sleep(1) # 1 second wait
    input("Press Enter to load rules...")
    display_rules()
    print()
    print()
    input("Press Enter to start the game...")
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

def congratulations_message(name, score, Round):
    print("\n" + "═"*50)
    slow_print("🛑  SYSTEM FAILURE DETECTED...", 0.05)
    time.sleep(0.5)
    slow_print("📉  GENERATING PERFORMANCE REPORT...", 0.05)
    time.sleep(0.5)
    
    print("-" * 50)
    print(f"   ➤ PILOT NAME    : {name.upper()}")
    print(f"   ➤ FINAL SCORE   : {score}")
    print(f"   ➤ ROUNDS CLEARED: {Round}")
    print("-" * 50)
    
    time.sleep(0.5)
    slow_print("💾  DATA ARCHIVED. SESSION TERMINATED.", 0.05)
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
         Type '#!' to view the game rules again.
         Type '#$' to view used words so far.
         Type '#@'to skip and get randonly new letter.
       ⚠️  IMPORTANT: Skips are LOCKED until Round 6!
         Type '#~' to quit the game anytime.

    ============================================================
    ''')

def access_used_words(word_used,dificulty_level):
    if dificulty_level<3:
        time.sleep(0.5)
        print("\nUsed words so far:")
        print(word_used)
        print()
    else:
        time.sleep(0.5)
        print("there is no access to used words in hard mode")

def skip(skips,word_used,letter,Round):
    if skips==0:
        print("You have no skips left!")
        return skips,letter
    elif Round<6:
        print("Skips are locked until Round 6!")
        return skips,letter
    else:
        skips-=1
        letter=random.choice(string.ascii_uppercase)
        print(f"Skip used! '")
        
        return skips,letter

def dificulty_level():
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
    dificulty_level=input("Enter 1, 2, or 3 to select difficulty: ")
    while dificulty_level not in ['1','2','3']:
        print("Invalid choice. Please enter 1, 2, or 3.")
        dificulty_level=input("Enter 1, 2, or 3 to select difficulty: ")
    return dificulty_level

def main_game_loop(word_used,letter,Round,score,dificulty,lives,skips,name):
    # 3. Main Game Loop
    play=True
    while play==True :
        
        print()
        print() 
        time.sleep(0.5)
        print("Round ",Round)
        
        print('Your letter is ',letter)
        word=str(input('Enter your word : '))
        
        #########################################
        
        if word== "#!":  # display Rules again
            display_rules()
            continue
        elif word=="#$":  # display used words
            access_used_words(word_used,int(dificulty))
            continue
        elif word=="#@":  # skip
            skips,letter=skip(skips,word_used,letter,Round)
            continue
        elif word=="#~":  # quit game
            print("You chose to quit the game.")
            print("\nUsed words :",word_used,"\n\n")
            congratulations_message(name,score,Round)
            return play==False
        else:
            pass
        #########################################
        
        word=word.strip()
        
        # SAFETY CHECK: If user hits Enter without typing
        if len(word)==0:
            print("You did not type any word ")
            print("please try agian")
            Round=Round-1 # Do not count this round
            continue # Skip the rest and restart the loop
        
        
        # Check spelling (Checking exact word matches in dictionary)
        spelling_check=word in spell
        
        # Convert input to uppercase for game logic comparison
        word=word.upper()
        
        
        # Game Rules Check
        valid, message = game_rules_check(word, word_used, letter, spell)
        
        
        
        #####################################
        
        
        
        if not valid:
            lives-=1
            if lives==0:
                time.sleep(0.5)
                print( "\n\nGame Over\n" , message)
                print("\nUsed words :",word_used,"\n\n")
                time.sleep(0.5)
                congratulations_message(name,score,Round)
                return play==False
            else:
                time.sleep(0.5)
                print(f"Invalid Turn! You have {lives} lives left.")
                print("Reason:", message)
                print("Please try again.")
                print()
                print("-----------------------------------")
                print()
                continue
            
        
        
        
        
        ######################################
        
        # If all checks passed
        word_used.append(word)  # Add word to used list
        
        score = calculate_score(score,Round,dificulty)           # Increment score
        Round=Round+1
        letter = word[-1]       # Update letter for next round

def main():
    # 1. Setup Tools
    
    name=valid_name_input()
    starting_message(name)
    
    
    
    
    # 2. Game State Setup
    word_used=[]   # to check repeated words 
    first_letter=name[-1] # first letter to begin (taken from name)
    letter=first_letter.upper()  # converting to uppercase
    Round=1        # rounds count
    score=0      # score count
    dificulty=dificulty_level()
    
    
    if dificulty=='1':
        lives=3
        skips=3
    elif dificulty=='2':
        lives=2
        skips=1
    else:
        lives=1
        skips=0
    
    # Start Main Game Loop
    main_game_loop(word_used,letter,Round,score,dificulty,lives,skips,name)

while True:
    main()
    print("Do you want to play again? (yes/no)")
    reply=input().lower()
    if reply!='yes':
        time.sleep(0.5)
        slow_print("Thanks for playing!")
        break
