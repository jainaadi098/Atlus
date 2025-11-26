from spellchecker import SpellChecker # pyright: ignore[reportMissingImports]


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
    print(f"\nHi, {name}")
    print('''
    Welcome to ATLUS (Antakshari Text Logic Utility System)
    -------------------------------------------------------
    In this game, the system gives you a letter.
    You must enter a valid English word starting with it.
    And the repetition of words is not allowed.
    -------------------------------------------------------
    ''')


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
    
    
    return True, "Valid Turn"


def congratulations_message(name,score):
    print(f"\nCongratulations, {name} !")
    print(f"Your score  {score} !")
    


def main():
    # 1. Setup Tools
    spell=SpellChecker()
    name=valid_name_input()
    starting_message(name)
    
    # 2. Game State Setup
    word_used=[]   # to check repeated words 
    first_letter=name[-1] # first letter to begin (taken from name)
    letter=first_letter.upper()  # converting to uppercase
    Round=0        # rounds count
    score=0      # score count
    
    # 3. Main Game Loop
    while True :
        print()
        print() 
        Round=Round+1
        print("Round ",Round)
        
        print('Your letter is ',letter)
        word=str(input('Enter your word : '))
        
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
        
        if not valid:
            print( "\n\nGame Over\n" , message)
            print("\nUsed words :",word_used,"\n\n")
            congratulations_message(name,score)
            return 
        
        # If all checks passed
        word_used.append(word)  # Add word to used list
        score += 1              # Increment score
        letter = word[-1]       # Update letter for next round
      

    
    
      

main()
