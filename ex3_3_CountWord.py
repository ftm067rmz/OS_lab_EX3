String = input('Enter a Sentence : ') 
counter = 1

for char in String:
    if char == ' ':
        counter += 1

print('Number of Words: ', counter)