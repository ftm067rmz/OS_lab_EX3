number = int(input('Enter a number : '))

fact = i = 1

while fact < number:
    fact = i * fact
    i +=1

if number == fact:
    print('Yes')
else:
    print('No')