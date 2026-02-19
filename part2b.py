#add randint
howMany = 10
rangeLength = 50
from random import randint
randomList = []
searchNumber = randint(1,rangeLength)
comparisons = 0
found = False

for i in range(howMany):
    randomList.append(randint(1,rangeLength))
print("the list is",randomList)
print(f"searching for number {searchNumber}")
for i in range(len(randomList)):
    comparisons += 1
    if randomList[i] == searchNumber:
        found = True
        print(f"I found the number {searchNumber}!!!")
        print("comparisons:", comparisons)
        break

if searchNumber in randomList:
    pass
else:
    print(f"the number {searchNumber} was not found after {comparisons} comparisons")