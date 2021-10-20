numbers = []
size = int(input('How many numbers do you want to enter? '))
print('Enter numbers : ')
i = 0

while size > i :
    temp = int(input())
    numbers.append(temp) 
    i += 1

print('Array :' , numbers) 

flag = 0 
while size > i:
    if numbers[i] < numbers[i+1] :
        i += 1
        flag = 1
    else :
        flag = 0
        break
       
if flag == 1:
    print('Array sorted')
else :
    print('Array not sorted')
    numbers.sort()
    print('Array sorted :' , numbers)

