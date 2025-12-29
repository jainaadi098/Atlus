from spellchecker import SpellChecker 
import random
import string
import sys
import time
import os
import win32com.client as wincl

class AtlusGame:
    def __init__(self):
        
        self.speaker = wincl.Dispatch("SAPI.SpVoice")
        self.speaker.Rate=3  # Speed of speech
        self.speaker.Volume=100  # Volume 0-100
        
        
        self.spell=SpellChecker()
        self.high_score_file="high_score.txt"
        self.current_high_score=self.get_high_score()
        
        self.name=""
        self.letter=""
        self.word_used=[]
        self.Round=1
        self.score=0
        self.difficulty=1
        self.lives=3
        self.skips=3
        self.word=""
        self.text=""
        
   
    def speak(self):
        
        self.speaker.Voice=self.speaker.GetVoices().Item(0) # 0 for male, 1 for female   
        
        self.slow_print(self.text)
        self.speaker.Speak(self.text)

    
    def speaken(self):
        
        self.speaker.Voice=self.speaker.GetVoices().Item(1) # 0 for male, 1 for female      
        
        self.speaker.Speak(self.text)
        
  
   
    
    def get_high_score(self):
        if os.path.exists("high_score.txt"):
            try:
                with open("high_score.txt", "r") as file:
                    high_score = int(file.read())
            except:
                return 0
        else:
            high_score = 0
        return high_score
    
    def new_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.score))
    
      
    
    def slow_print(self,text):
        delay=0.03
        # Print text slowly to simulate typing effect
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # for newline after the text
        
    def valid_name_input(self):
        # Define allowed characters for manual validation   
        letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # --- NAME INPUT SECTION ---
        self.text="Enter your name : "
        self.speak()
        
        self.name=str(input())   # it might also be username
    
        name1=self.name.strip() # Remove extra spaces from the start and end
        while True:
            # Check if name is NOT empty AND the last character is inside our 'letters' string
            if len(name1)!=0 and name1[-1].upper() in letters:    
                self.name= name1 # Input is valid, return the name
                break

            else:
                # If input is invalid, ask again
                self.text="Invalid name entered."
                self.speak()
                self.text="please enter your name to play the game"
                self.speak()
                self.text="Enter your name : "
                self.speak()
                self.name=str(input())
                name1=self.name.strip()
                
    
    def starting_message(self):
        print("\n")
        self.text="INITIALIZING ATLUS SYSTEM..."
        self.speak()
        time.sleep(0.5)
        self.text=f"USER DETECTED: {self.name.title()}"
        self.speak() 
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
        self.text="Welcome to ATLUS Game Version 7"
        self.speaken()
        time.sleep(0.8) # 1 second wait
        self.text="Press Enter to load rules..."
        self.speak()
        input()
        self.display_rules()
        print()
        print()
        
    
    def calculate_score(self):  
    
        if self.difficulty=='1':self.score += 1  # Flat +1 per valid word
    
        elif self.difficulty=='2':  # Medium Mode
            if self.Round <= 10:self.score += 1  # +1 per valid word till Round 10
            else:self.score += 3  # +3 per valid word after Round 10
    
        else:  # Hard Mode
            if self.Round <= 5:self.score += 1
            elif self.Round <= 10:self.score += 2
            elif self.Round <= 15:self.score += 3
            elif self.Round <= 20:self.score += 4
            else:self.score += 5

    def game_rules_check(self,word):
    
    # --- LOGIC GATES ---
    
    # Rule 1: Does the word start with the required letter?
        if self.letter!=word[0] :
        # Fail: Wrong starting letter
            return False,"your word does not start with the given letter"
    # Rule 2: Has the word been used before?
        if word in self.word_used :
            # Fail: Word repeated
            return False ,"You have already used this word"
    # Rule 3: Is the spelling valid?
        
        if word.lower() not in self.spell:
            return False,"Your word is not valid"
    # If all checks passed
        return True, "Valid Turn"

    def congratulations_message(self):
        print("\n" + "═"*50)
        self.text="    GAME OVER DETECTED..."
                       
        self.speak()   
        time.sleep(0.5)
        self.text="    GENERATING PERFORMANCE REPORT..."
        
        self.speak()
        time.sleep(0.5)
    
        if self.score>self.current_high_score:
            print("-" * 50)
            self.text=f"""Congratulation New High Score {self.score}"""
            self.speak()
        print("-" * 50)
        self.text=f"   ➤ PLAYER NAME    : {self.name.upper()}"
        
        self.speak()
        self.text=f"   ➤ FINAL SCORE    : {self.score}"
        
        self.speak()
        self.text=f"   ➤ ROUNDS CLEARED : {self.Round-1}"
        
        self.speak()

        print("═"*50 + "\n")
        time.sleep(0.5)
    
    def display_rules(self):
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
        self.text="These are the game rules. Enter 'listen' to listen the rules or Enter to continue."
        print(self.text)
        self.speaken()
        choice=input().lower()
        if choice=='listen':
            self.text="""This game is a word-chain challenge. 
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
            and #EXIT to leave the game at any time."""
            self.speaken()
        print()
        print()
        

    def access_used_words(self):
        if int(self.difficulty)<3:
            time.sleep(0.5)
            self.text=f"\nUsed words :{self.word_used}\n\n"
            self.speak()
            print()
        else:
            time.sleep(0.5)
            self.text="there is no access to used words in hard mode"
            self.speak()

    def skip(self):
        if self.skips==0:
            self.text="You have no skips left!"
            self.speak()
        elif self.Round<6:
            self.text="Skips are locked until Round 6!"
            self.speak()
        else:
            self.skips-=1
            self.letter=random.choice(string.ascii_uppercase)
            self.text=f"Skip used!  {self.letter}"
            self.speak()

    def difficulty_level(self):
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
    ║     ❤️  Lives: 2   | ⏭️  Skips: 1                ║
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

    
        ''')
        self.text="These are the difficulty levels. Enter 'listen' to listen the levels or Enter to continue."
        print(self.text)
        self.speaken()
        choice=input().lower()
        if choice=='listen':
            self.text="""The game offers three difficulty modes, 
          each designed to provide a different level of challenge: 
          1. Easy Mode You receive 3 lifes and 3 skips. Your word history remains visible at all times, making it easier to track what has been used. Every correct word gives you a flat +1 point. 
          2. Medium Mode This mode provides 2 lifes and 1 skip. The history is still visible, but scoring becomes progressive — you earn +1 point for each correct word until Round 10, after which each correct answer awards +3 points. 
          3. Hard Mode (Grandmaster) This is the highest difficulty. You get only 1 life and no skips. Your previously used words remain hidden, increasing the challenge. Scoring follows a ladder pattern, starting with +1 and gradually rising to +5 as you progress. Please note that skips remain locked until Round 6, regardless of the chosen mode."""
            self.speaken()

        self.text="Enter 1, 2, or 3 to select difficulty: "
        self.speak()
        self.difficulty=input()
        while self.difficulty not in ['1','2','3']:
            self.text="Invalid input. Please enter 1, 2, or 3 to select difficulty: "
            self.speak()
            self.difficulty=input("Enter 1, 2, or 3 to select difficulty: ")


    def main_game_loop(self):
        # 3. Main Game Loop
        while True :
            print()
            print() 
            time.sleep(0.5)
            self.text=f"Round {self.Round}"
            self.speak()
            self.text=f"Your letter is {self.letter}"
            self.speak()
            self.text="Enter your word: "
            self.speak()
            word=str(input())
            #########################################
            word=word.upper()
            if word== "#RULES":  # display Rules again
                self.display_rules()
                continue
            elif word=="#HISTORY":  # display used words
                self.access_used_words()
                continue
            elif word=="#SKIP":  # skip
                self.skip()
                continue
            elif word=="#EXIT":  # quit game
                self.text="You chose to quit the game."
                self.speak()
                self.text=f"\nUsed words :{self.word_used}\n\n"
                self.speak()
                self.congratulations_message()
                break
            else:
                pass
            #########################################
            word=word.strip()
            # SAFETY CHECK: If user hits Enter without typing
            if len(word)==0:
                self.text="You did not type any word "
                self.speak()
                self.text="please try agian"
                self.speak()
                continue # Skip the rest and restart the loop

            # Convert input to uppercase for game logic comparison

            # Game Rules Check
            valid, message = self.game_rules_check(word)

            #####################################

            if not valid:
                self.lives-=1
                if self.lives==0:
                    time.sleep(0.5)
                    self.text=f"\n\nGame Over\n {message}"
                    self.speak()
                    self.text=f"\nUsed words :{self.word_used}\n\n"
                    self.speak()
                    time.sleep(0.5)
                    self.congratulations_message()
                    break
                else:
                    time.sleep(0.5)
                    self.text=f"Invalid Turn! You have {self.lives} lives left."
                    self.speak()
                    self.text=f"Reason: {message}"
                    self.speak()
                    self.text="Please try again."
                    self.speak()
                    print()
                    print("-----------------------------------")
                    print()
                    continue
           
            ######################################
        
            # If all checks passed
            self.word_used.append(word)  # Add word to used list
        
            self.calculate_score()           # Increment score
            self.Round=self.Round+1
            self.letter = word[-1]       # Update letter for next round

    def start(self):
        self.valid_name_input()
        
        self.starting_message()

        first_letter=self.name[-1] # first letter to begin (taken from name)
        self.letter=first_letter.upper()  # converting to uppercase

        self.difficulty_level()
    
    
        if self.difficulty=='1':
            self.lives=3
            self.skips=3
        elif self.difficulty=='2':
            self.lives=2
            self.skips=1
        else:
            self.lives=1
            self.skips=0

        self.main_game_loop()
    
        if self.current_high_score<self.score:
            self.new_high_score()
    
if __name__ == "__main__":
    
    while True:
        game=AtlusGame()
        
        game.start()
        print()
        game.text="Do you want to play again? (yes/no)"
        game.speak()
        reply=input().lower()
        if reply!='yes':
            time.sleep(0.5)
            game.text="Thank you for playing."
            game.speak()
            break
