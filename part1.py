#add randint
howMany = 10
from random import randint
randomList = []
for i in range(howMany):
    randomList.append(randint(1,50))

print(randomList)   