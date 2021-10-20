num = number = int(input("Enter a number : "))

pow = len(str(number))
sum = 0

while  number > 0 :
    rem = number % 10
    number //= 10
    sum += rem**pow

if sum == num :
    print('Yes')
else:
   print('No')
