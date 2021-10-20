print('Enter two numbers (not zero)')
number1 = int(input('Number1: '))
number2 = int(input('Number2: '))

if number2 > number1 :
    smaller = number1

else:
    smaller = number2

for i in range(1 , smaller+1):
   
    if ((number1 % i == 0) and (number2 % i == 0)):
        bmm =i

kmm = (number1*number2) / bmm

print('k m m  is : ' , kmm)