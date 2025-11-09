name=str(input('Enter your name : '))
print('Hi,',name,'''
      In this game 
      we give you letter 
      And you had to tell a word 
      starting from that letter ''')
n=10

word=name[-1]
b=0
while n>0:
    n=n+1
    b=b+1
    print(b)
    
    print('Your letter is ',word)
    word1=str(input('Enter your word : '))
    if word[-1]==word1[0]:
        word=word1[-1]
        print('check')
    else:
        print('game Over')
        n=-n
