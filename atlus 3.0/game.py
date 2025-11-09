from spellchecker import SpellChecker # pyright: ignore[reportMissingImports]
spell = SpellChecker()

name=str(input('Enter your name : '))
print('Hi,',name,'''
      In this game 
      we give you letter 
      And you had to tell a word 
      starting from that letter ''')


list=[]   # to check repeated words 
l1=name[-1] # first letter to begin
l=l1.upper()  # converting to uppercase
b=0        # rounds count
sco=0      # score count


while True :
    print()
    print() 
    b=b+1
    print("Round ",b)
    
    print('Your letter is ',l)
    word=str(input('Enter your word : '))
    sc=word in spell
    word=word.upper()
    
    if l==word[0] and word not in list and sc==True:
        l=word[-1]
        list.append(word)
        sco=sco+1
        
    else:
        print()
        print()
        print('Game Over')
        break



print()
print()

print("Congratulation !! ",name.upper())

print("Your Score : ",sco)

print(list)
