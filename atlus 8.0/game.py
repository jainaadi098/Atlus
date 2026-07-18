from spellchecker import SpellChecker 
import random
import string
import sys
import time
import os
import win32com.client as wincl
    # --- GAME CLASS ---
class AtlusGame:
    def __init__(self):
        
        self.speaker = wincl.Dispatch("SAPI.SpVoice")
        self.speaker.Rate=3  # Speed of speech
        self.speaker.Volume=100  # Volume 0-100
        
        
        self.spell=SpellChecker()
        self.high_score_file="high_score.txt"
        self.current_high_score=self.get_high_score()
        
        self.mode="computer"
        self.turn=""
        
        self.name="AJ"
        self.name2="SJ"
        
        self.letter="A"
        
        
        self.word_used=[]
        
        self.Round=1
        self.Round2=1
        
        self.score=0
        self.score2=0
        
        self.difficulty=3
        self.correctness="tttt"
        
        self.lives=3
        self.lives2=3
        
        
        self.skips=3
        self.skips2=3
        
        self.word=""
        self.text=""
        
        self.voice="ON"








    # --- VOICE ON OFF ---    
    def voicechange(self):
        if self.voice=="OFF":
            self.voice="ON"
            print("Voice ON")
        else:
            self.voice="OFF"
            print("Voice OFF")
    # --- VOICE 1 ---
    def speak(self):
        self.slow_print(self.text)
        if self.voice=="OFF":
            return
        
        self.speaker.Voice=self.speaker.GetVoices().Item(0) # 0 for male, 1 for female   
        
        
        self.speaker.Speak(self.text)
    # --- VOICE 2 ---
    def speaken(self):
        if self.voice=="OFF":
            return
        
        
        self.speaker.Voice=self.speaker.GetVoices().Item(1) # 0 for male, 1 for female      
        
        self.speaker.Speak(self.text)





    # --- HIGH SCORE FILES ---
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
    # --- SET HIGH SCORE ---
    def new_high_score(self,score):
        with open("high_score.txt", "w") as file:
            file.write(str(score))




    # --- PRINTING TEXT ---
    def slow_print(self,text):
        delay=0.03
        # Print text slowly to simulate typing effect
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # for newline after the text



    # --- NAME CHECK ---
    def valid_name_input1(self):
        # Define allowed characters for manual validation   
        letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # --- NAME INPUT SECTION ---
        self.text="Enter your name : "
        self.speak()
        
        name=str(input())   # it might also be username
    
        name1=name.strip() # Remove extra spaces from the start and end
        
        
        while True:
            # Check if name is NOT empty AND the last character is inside our 'letters' string
            if name1!="#VOICE" and len(name1)!=0 and name1[-1].upper() in letters:    
                self.name= name1 # Input is valid, return the name
                break

            else:
                # If input is invalid, ask again
                if name1!="#VOICE" and name1!="#voice" :
                    self.text="Invalid name entered."
                    self.speak()
                    self.text="please enter your name to play the game"
                    self.speak()
                self.text="Enter your name : "
                self.speak()
                name=str(input())
                name1=name.strip()
                name1=name1.upper()
                if name1=="#VOICE":
                    self.voicechange()
                    
                    
        print("Name selected")

    # --- NAME CHECK ---
    def valid_name_input2(self):
        # Define allowed characters for manual validation   
        letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # --- NAME INPUT SECTION ---
        self.text="Enter your name : "
        self.speak()
        
        name=str(input())   # it might also be username
    
        name1=name.strip() # Remove extra spaces from the start and end
        if name1.upper()=="#VOICE":
            self.voicechange()
        
        while True:
            # Check if name is NOT empty AND the last character is inside our 'letters' string
            if name1!="#VOICE" and len(name1)!=0 and name1[-1].upper() in letters:    
                self.name2= name1 # Input is valid, return the name
                break

            else:
                # If input is invalid, ask again
                if name1!="#VOICE":
                    self.text="Invalid name entered."
                    self.speak()
                    self.text="please enter your name to play the game"
                    self.speak()
                self.text="Enter your name : "
                self.speak()
                name=str(input())
                name1=name.strip()
                if name1=="#VOICE":
                    self.voicechange()
        print("Name2 selected")
  
                          
    # --- STARTING MESSAGE ---   
    def initializing_message(self):
        print("\n")
        self.text="INITIALIZING ATLUS SYSTEM..."
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
        self.text="Welcome to ATLUS Game Version 8"
        self.speaken()
        time.sleep(0.8) # 1 second wait
        self.text="Press Enter to load rules..."
        self.speak()
        input()
        
    # --- DISPLAY RULES ---
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
           
        
        🔹 SPECIAL COMMANDS:
             Type '#RULES' to view the game rules again.
             Type '#VOICE' to turn ON or OFF Voice.
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
            #VOICE to turn ON or OFF voice, 
            #HISTORY to check previously used words, 
            #SKIP to change the letter (available from Round 6 onward), 
            and #EXIT to leave the game at any time."""
            self.speaken()
        print()
        print()


    # --- WORDS HISTORY ---
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
    # --- SKIPS ---
    def skip(self):
        if self.turn=="player":
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
        
        else:
            if self.skips2==0:
                self.text="You have no skips left!"
                self.speak()
            elif self.Round2<6:
                self.text="Skips are locked until Round 6!"
                self.speak()
            else:
                self.skips2-=1
                self.letter=random.choice(string.ascii_uppercase)
                self.text=f"Skip used!  {self.letter}"
                self.speak()
        
        
        
        
        
    # --- SPECIAL COMMANDS ---
    def special_commands(self):
        self.word=self.word.upper()
        if self.word=="#VOICE":
            self.voicechange()
            return "continue"
        elif self.word== "#RULES":  # display Rules again
            self.display_rules()
            return "continue"
        elif self.word=="#HISTORY":  # display used words
            self.access_used_words()
            return "continue"
        elif self.word=="#SKIP":  # skip
            self.skip()
            return "continue"
        elif self.word=="#EXIT":  # quit game
            self.text="You chose to quit the game."
            self.speak()
            self.text=f"\nUsed words :{self.word_used}\n\n"
            self.speak()
            self.congratulations_message()
            return "break"
        else:
            pass
        #########################################






    # --- LIFE SETUP ---
    def life_setup(self):
        if self.difficulty=='1':
            lives=3
            skips=3
        elif self.difficulty=='2':
            lives=2
            skips=1
        else:
            lives=1
            skips=0
        self.lives=lives
        self.skips=skips
        if self.mode!='solo':
            self.lives2=lives
            self.skips2=skips
        
        print("life setup done")





    # --- DIFFICULTY LEVEL INPUT ---
    def difficulty_level_input(self):
        self.text="Enter 1, 2, or 3 to select difficulty: "
        self.speak()
        difficulty=input()
        
        while (difficulty!='1' and difficulty!='2' and difficulty!="3") or difficulty=="":
            self.text="Invalid input. Please enter 1, 2, or 3 to select difficulty: "
            self.speak()
            difficulty=input("Enter 1, 2, or 3 to select difficulty: ")
            
        self.difficulty=difficulty
            

    # --- DIFFICULTY LEVEL ---
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

        
        self.difficulty_level_input()
        
        print("dificulty selected")
        self.life_setup()
        
    # --- MODE SELECTION INPUT ---
    def mode_selection_input(self):
        self.text = "Enter 1, 2, or 3 to select mode: "
        self.speak()
        mode_n=input()
        while mode_n != '1' and mode_n != '2' and mode_n != '3':
            self.text="Invalid input. Please enter 1, 2, or 3 to select mode: "
            self.speak()
            mode_n=input()
        
        return mode_n


    # --- MODE SELECTION ---
    def mode_selection(self):
        print("""
            ╔══════════════════════════════════════════════════╗
            ║               🎮  SELECT GAME MODE  🎮          ║
            ╠══════════════════════════════════════════════════╣
            ║                                                  ║
            ║  1️⃣  SOLO MODE                                  ║
            ║                                                  ║
            ║  2️⃣  MULTIPLAYER PLAYER MODE                     ║          
            ║                                                  ║
            ║  3️⃣  COMPUTER (ATLUS AI)                         ║
            ║                                                  ║
            ╚══════════════════════════════════════════════════╝

              """)
        self.text="These are the game modes. Enter 'listen' to listen the modes or Enter to continue."
        print(self.text)
        self.speaken()
        choice=input().lower()
        if choice=='listen':
            self.text="""The game offers three exciting modes:
            1. Solo Mode. Play alone, practice your vocabulary, and set a new high score.
            2. Two Player Mode. Pass and play with a friend in a head-to-head battle.
            3. VS Computer Mode. Challenge the Atlus Artificial Intelligence and test your limits."""
            self.speaken()
            print()
        
        
        mode_n=self.mode_selection_input()
        
        if mode_n=='1':
            self.mode='solo'
            self.valid_name_input1()
            
        elif mode_n=='2':
            self.mode='multiplayer'
            self.valid_name_input1()
            self.valid_name_input2()
            
        else:
            self.mode='computer'
            self.valid_name_input1()
        
        print("Mode selected")



    # --- CALCULATING SCORE ---
    def calculate_score(self):  
        score=0
        if self.difficulty=='1':score += 1  # Flat +1 per valid word
    
        elif self.difficulty=='2':  # Medium Mode
            if self.Round <= 10:score += 1  # +1 per valid word till Round 10
            else:score += 3  # +3 per valid word after Round 10
    
        else:  # Hard Mode
            if self.Round <= 5:score += 1
            elif self.Round <= 10:score += 2
            elif self.Round <= 15:score += 3
            elif self.Round <= 20:score += 4
            else:score += 5
        if self.turn=="player":
            self.score+=score
        else:
            self.score2+=score

    # --- LOGIC GATE CONDITIONS ---
    def condition1(self):
    # Rule 1: Does the word start with the required letter?
        if self.letter!=self.word[0] :
        # Fail: Wrong starting letter
            return False,"your word does not start with the given letter"
        return True, "Valid"
    def condition2(self):
    # Rule 2: Has the word been used before?
        if self.word in self.word_used :
            # Fail: Word repeated
            return False ,"You have already used this word"
        return True, "Valid"
    def condition3(self):
    # Rule 3: Is the spelling valid?
        if self.word.lower() not in self.spell:
            return False,"Your word is not valid"
        return True, "Valid"
    # --- LOGIC GATE CHECK ---
    def game_rules_check(self):
        valid, message = self.condition1()
        if valid==False:
            return valid, message
        valid, message = self.condition2()
        if valid==False:
            return valid, message
        valid, message = self.condition3()
        if valid==False:
            return valid, message
        # If all checks passed
        return True, "Valid Turn"


    # --- CHECK HIGH SCORE ---
    def check_high_score(self):
        score=self.score
        
        if self.mode=='multiplayer' and self.score2>score:
            score=self.score2

        if score>self.current_high_score :
            self.new_high_score(score)
            print("-" * 50)
            self.text=f"""Congratulation New High Score {score}"""
            self.speak()
        
        
        
    # --- CONGRATULATIONS MESSAGE ---
    def congratulations_message(self):
        print("\n" + "═"*50)
        # self.text="    GAME OVER DETECTED..."
                       
        # self.speak()   
        time.sleep(0.5)
        self.text="    GENERATING PERFORMANCE REPORT..."
        
        self.speak()
        time.sleep(0.5)
    
        self.check_high_score()
        print("-" * 50)
        self.text=f"   ➤ PLAYER NAME    : {self.name.upper()}"
        
        self.speak()
        self.text=f"   ➤ FINAL SCORE    : {self.score}"
        
        self.speak()
        self.text=f"   ➤ ROUNDS CLEARED : {(self.Round-1)}"
        self.speak()
        if self.mode!='solo':
            print("\n" + "-"*50)
            
            if self.mode=='multiplayer':
                self.text=f"   ➤ PLAYER NAME    : {self.name2.upper()}"
            else:
                self.text=f"   ➤ COMPUTER NAME  : ATLUS AI"
            self.speak()
            self.text=f"   ➤ FINAL SCORE    : {self.score2}"
            self.speak()
            self.text=f"   ➤ ROUNDS CLEARED : {self.Round2-1}"
            self.speak()
        
            
        
        

        print("\n","═"*50 + "\n")
        time.sleep(0.5)
        if self.mode!='solo':
            if self.score>self.score2:
                self.text=f"CONGRATULATIONS {self.name.upper()}! YOU WIN!"
            elif self.score<self.score2:
                if self.mode=='multiplayer':
                    self.text=f"CONGRATULATIONS {self.name2.upper()}! YOU WIN!"
                else:
                    self.text=f"COMPUTER WINS! BETTER LUCK NEXT TIME!"
            else:
                self.text="IT'S A TIE!"
            self.speak()
        
            
    # --- WORD GENERATOR ---
    def word_generator(self): # random word generated
        letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        length=random.randint(3,6)
        
        sd=self.difficulty
        if sd=='1':
            self.correctness='f'*2+'t'*6
        elif sd=='2':
            self.correctness='f'*1+'t'*6
        else:
            self.correctness='f'*1+'t'*7
        con=self.correctness[random.randint(0,len(self.correctness)-1)]
        try_count=0
        while True:
            try_count+=1
            if try_count>20**length:
                length+=1
            word=""
            for i in range(length):
                l=random.choice(letters)
                word+=l
            if con=='f':
                return word
            if word in self.spell and word not in self.word_used and word[0]==self.letter:
                return word
    # --- COMPUTER GAME LOOP ---
    def computer_game_loop(self):
        self.letter=random.choice(string.ascii_uppercase)
        
        self.turn="player"
        print("work progess")
        while True:
            message=self.one_step()
            if message=="break":
                break
            if message=="continue":
                continue
            print(f"message is :{message}")  
            if message=="Correct":
                self.calculate_score()
                if self.turn=="player":
                    self.Round=self.Round+1
                    self.turn="computer"
                else:
                    self.Round2=self.Round2+1
                    self.turn="player"
    

    
    ########################################
    # --- SINGLE GAME LOOP ---
    def single_game_loop(self):
        self.letter=random.choice(string.ascii_uppercase)
        
        self.turn="player"
        while True:
            print(593)
            message=self.one_step()
            if message=="break":
                break
            if message=="continue":
                continue
            if message=='Correct':
                self.calculate_score()
                
                self.Round=self.Round+1



    # --- ONE BLOCK ---
    def One_block(self) :
        print()
        print()
        time.sleep(0.5)
        self.text=f"Round {self.Round}"
        self.speak()
        self.text=f"player letter is {self.letter}"
        self.speak()
        self.text="Enter your word: "
        
        self.speak()
        word=str(input())
        
        
        self.word=word.upper()
    # --- COMPUTER BLOCK ---
    def Computer_block(self) :
        print()
        print() 
        time.sleep(0.5)
        self.text=f"Round {self.Round2}"
        self.speak()
        if self.mode=='computer':
            self.text=f"Computer letter is {self.letter}"
        else:
            self.text=f"player2 letter is {self.letter}"
        self.speak()
        
        
        if self.mode=='computer':
            word=self.word_generator()
            self.text=f"Computer word:{word.lower()} "
            self.speak()
        else:
            self.text="player2 Enter your word: "
            self.speak()
            word=str(input())
        
        
        
        
        self.word=word.upper()



    # --- ONE STEP ---
    def one_step(self):
        # Selecting the turn
        print(640)
        if self.turn=="player":
            self.One_block()
        elif self.turn=="computer":
            self.Computer_block()
        
        # Special Commands Check
        message=self.special_commands()
        if message:
            return message
        
        word=self.word.upper()
        self.word=self.word.strip()
        # SAFETY CHECK: If user hits Enter without typing
        if len(word)==0:
            self.text="You did not type any word "
            self.speak()
            self.text="please try agian"
            self.speak()
            return "continue" # Skip the rest and restart the loop

        if len(self.word)==0:
            return "continue"
            # Game Rules Check
        valid, message = self.game_rules_check()

            #####################################
        if not valid and self.turn=="player":
            self.lives-=1
            if self.lives==0:
                time.sleep(0.5)
                self.text=f"\n\nGame Over\n {message}"
                self.speak()
                self.text=f"\nUsed words :{self.word_used}\n\n"
                self.speak()
                time.sleep(0.5)
                self.congratulations_message()
                return "break"
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
                return "continue"
        # computer
        if not valid and self.turn!="player":
            
            self.lives2-=1
            if self.mode=='computer':
                self.text=f"Invalid Turn! Computer have {self.lives2} lives left."
            else:
                self.text=f"Invalid Turn! player2 have {self.lives2} lives left."
            
            self.speak()
            if self.lives2==0:
                if self.mode=='computer':
                    self.text="Computer Loss"
                    self.speak()
                    self.text=f"\nUsed words :{self.word_used}\n\n"
                    self.speak()
                    time.sleep(0.5)
                    self.congratulations_message()
                else:
                    time.sleep(0.5)
                    self.text=f"\n\nGame Over\n {message}"
                    self.speak()
                    self.text=f"\nUsed words :{self.word_used}\n\n"
                    self.speak()
                    time.sleep(0.5)
                    self.congratulations_message()
                return "break"
                
                
            return "Invalid"
        ######################################
        
        
        self.letter = word[-1]    
           
        
        if self.turn=="player":
            self.word_used.append(self.word)
            
        else:
            self.word_used.append(self.word)
                
        
        
        return "Correct"




    # --- MODE LOOP SELECTION ---
    def mode_loop_selection(self):
        if self.mode=='solo':
            self.turn="player"

            self.single_game_loop()
        elif self.mode=='multiplayer':
            self.computer_game_loop()
        else:
            self.computer_game_loop()
    

    def start_game_engine(self):
        self.initializing_message()
        self.display_rules()
        self.mode_selection()
    
        self.difficulty_level()
        print(763)
        self.mode_loop_selection()
    
    
    


if __name__ == "__main__":
    
    while True:
        game=AtlusGame()
        
        
        game.start_game_engine()
        
        print()
        game.text="Do you want to play again? (yes/no)"
        game.speak()
        reply=input().lower()
        if reply!='yes':
            time.sleep(0.5)
            game.text="Thank you for playing."
            game.speak()
            break
