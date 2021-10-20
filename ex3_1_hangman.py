import random

wordsBank = ['tree' , 'book' , 'python' , 'linux' ,'java' , 'android' ,'mac', 'windows']

word = random.choice(wordsBank)
joon = len(word)

true_chars = []

while True:
    
    count = 0
    for char in word:
      if char in true_chars:
        print (char, end =' ')
        count += 1
      else:
        print(' _ ', end =' ')
      
    if count == len(word):
      print('\nYou win\nteded joon ha :', joon)
      break
    
    choice_user = input("\nEnter a character : ")

    if choice_user in word:
        print('✅')
        true_chars.append(choice_user)
        
    else :
        joon -= 1
        print('❌')


    if joon == 0 :
        print('Game Over')
        break