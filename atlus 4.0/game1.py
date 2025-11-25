from spellchecker import SpellChecker # pyright: ignore[reportMissingImports]
spell = SpellChecker()

letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

name=str(input('Enter your name : '))   # it might also be username
name=name.strip()





while True:
    if len(name)!=0 and name[-1].upper() in letters:    
        break
        
    else:
        print("You did not enter any name")
        print("please enter your name to play the game")
        name=str(input('Enter your name : '))
        name=name.strip()
        
         
    
    
    

print('Hi,',name,'''
      In this game 
      we give you letter 
      And you had to tell a word 
      starting from that letter ''')


word_used=[]   # to check repeated words 
first_letter=name[-1] # first letter to begin
letter=first_letter.upper()  # converting to uppercase
Round=0        # rounds count
score=0      # score count


while True :
    print()
    print() 
    Round=Round+1
    print("Round ",Round)
    
    print('Your letter is ',letter)
    word=str(input('Enter your word : '))
    
    word=word.strip()
    if len(word)==0:
        print("You did not type any word ")
        print("please try agian")
        Round=Round-1
        continue
    
    
    spelling_check=word in spell
    word=word.upper()
    
    
    if letter==word[0] :
        if word not in word_used :
            if spelling_check==True:
                letter=word[-1]
                word_used.append(word)
                score=score+1
            else:
                print()
                print()
                print('Game Over')
                print("Your word is not valid")
                break
        else:
            print()
            print()
            print('Game Over')
            print("You have already used this word")
            break
    else:
        print()
        print()
        print('Game Over')
        print("your word does not start with the given letter")
        break



print()
print()

if score==0:
    print("better luck next time ",name.upper())
else:
    print("Congratulation !!  ",name.upper())

print("Your Score : ",score)

print(word_used)
