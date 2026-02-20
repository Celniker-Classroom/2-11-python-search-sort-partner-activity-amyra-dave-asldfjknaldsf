#add randint
from random import randint
#how many numbers in the list
howMany = randint(6,17)
#the range that random numbers can be generated in from 1-x
rangeLength = randint(20, 60)
#make empty lists
randomList = []
cubedList = []
evens = 0
odds = 0
#searchNumber = int(input("Choose a number to search for: "))
#comparisons = 0
#found = False
#currentSum = 0
#create the random list
for i in range(howMany):
    randomList.append(randint(1,rangeLength))
print(f"The list has {howMany} numbers in it")
print("the list is",randomList)
print()
sortedList = sorted(randomList)

#print(f"searching for number {searchNumber}")
#print("the list, sorted, is", sortedList)
#iterates through the list of numbers
for i in range(len(randomList)):
    #cubes the list
    cubedList.append(randomList[i]**3)
    #counts evens and odds
    if randomList[i] % 2 == 0:
        evens += 1
    else:
        odds += 1
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
print(f"There are {odds} odd numbers and {evens} even numbers")