import random

numbers = []
size_input =  int(input('Enter the size of random array : '))

    
while size_input>0 :
    a = random.randint(1 , 100)

    if a in numbers:
        a = random.randint(a)    
    else:
        numbers.append(a)
        size_input -= 1

print('Random Array : ' , numbers)