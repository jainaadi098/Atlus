name=str(input('Enter your name : '))
print('Hi,',name,'''
      In this game 
      we give you letter 
      And you had to tell a word 
      starting from that letter ''')
n=10

list=[]
l1=name[-1]
l=l1.upper()
b=0
sco=0


while n>0:
    print()
    print()
    n=n+1
    b=b+1
    print("Round ",b)
    
    print('Your letter is ',l)
    word=str(input('Enter your word : '))
    word=word.upper()
    
    if l==word[0] and word not in list:
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
