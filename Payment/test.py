import random

number = ""

for i in range(4):
    number += str(random.randint(3, 9))
    
print(number)