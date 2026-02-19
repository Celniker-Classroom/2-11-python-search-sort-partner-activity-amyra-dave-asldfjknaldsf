#add randint
howMany = 10
from random import randint
randomList = []
searchNumber = randint(1,50)
for i in range(howMany):
    randomList.append(randint(1,50))

print("Generated list: ",randomList)
print("Searching for number",str(searchNumber)+"...")
if searchNumber in randomList:
    print("The number", searchNumber,"was found!!!!!")
else:
    print("The number",searchNumber,"was not found :(")