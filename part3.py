#add randint
howMany = 10
rangeLength = 50
from random import randint
randomList = []
cubedList = []
#searchNumber = int(input("Choose a number to search for: "))
#comparisons = 0
#found = False
#currentSum = 0
#create the random list
for i in range(howMany):
    randomList.append(randint(1,rangeLength))
print("the list is",randomList)
print()
sortedList = sorted(randomList)

#print(f"searching for number {searchNumber}")
#print("the list, sorted, is", sortedList)
for i in range(len(randomList)):
    #cubes the list
    cubedList.append(randomList[i]**3)
    #comparisons += 1
    #currentSum += int(randomList[i])
    '''if randomList[i] == searchNumber:
        found = True
        print(f"I found the number {searchNumber}!!!")
        print("comparisons:", comparisons)
        break
        '''
print("The list cubed is",cubedList)
sortedList.reverse()
print("the list in reverse order from sorted is", sortedList)

#print(f"the sum is {currentSum}")