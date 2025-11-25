from spellchecker import SpellChecker # pyright: ignore[reportMissingImports]
spell = SpellChecker()

# Define allowed characters for manual validation
letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# --- NAME INPUT SECTION ---
name=str(input('Enter your name : '))   # it might also be username
name=name.strip() # Remove extra spaces from the start and end





while True:
    # Check if name is NOT empty AND the last character is inside our 'letters' string
    if len(name)!=0 and name[-1].upper() in letters:    
        break # Input is valid, stop the loop
        
    else:
        # If input is invalid, ask again
        print("You did not enter any name")
        print("please enter your name to play the game")
        name=str(input('Enter your name : '))
        name=name.strip()
        
         
    
    
    

print('Hi,',name,'''
      In this game 
      we give you letter 
      And you had to tell a word 
      starting from that letter ''')


# --- GAME SETUP ---
word_used=[]   # to check repeated words 
first_letter=name[-1] # first letter to begin (taken from name)
letter=first_letter.upper()  # converting to uppercase
Round=0        # rounds count
score=0      # score count


# --- MAIN GAME LOOP ---
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
    
    
    # --- LOGIC GATES ---
    
    # Rule 1: Does the word start with the required letter?
    if letter==word[0] :
        
        # Rule 2: Has the word been used before?
        if word not in word_used :
            
            # Rule 3: Is the spelling valid?
            if spelling_check==True:
                # SUCCESS! Update game state
                letter=word[-1] # New letter is the last letter of current word
                word_used.append(word) # Add to used list
                score=score+1 # Increase score
            else:
                # Fail: Spelling incorrect
                print()
                print()
                print('Game Over')
                print("Your word is not valid")
                break
        else:
            # Fail: Word repeated
            print()
            print()
            print('Game Over')
            print("You have already used this word")
            break
    else:
        # Fail: Wrong starting letter
        print()
        print()
        print('Game Over')
        print("your word does not start with the given letter")
        break



print()
print()

# --- FINAL SCORE DISPLAY ---
if score==0:
    print("better luck next time ",name.upper())
else:
    print("Congratulation !!  ",name.upper())

print("Your Score : ",score)

print(word_used)