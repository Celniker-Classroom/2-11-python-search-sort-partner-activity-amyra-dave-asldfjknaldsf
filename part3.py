toDo = input("What do you want to do\n" 
"1. Generate a random list and search for a number\n" 
"2. Do three silly things to the list\n" \
"")
#add randint
from random import randint
#how many numbers in the list
howMany = randint(6,17)
#the range that random numbers can be generated in from 1-x
rangeLength = randint(20, 60)
#make empty lists
randomList = []
cubedList = []
if toDo == 1:
    searchNumber = int(input("Choose a number to search for: "))
    comparisons = 0
    found = False
    #create the random list
    for i in range(howMany):
        randomList.append(randint(1,rangeLength))
    print(f"The list has {howMany} numbers in it")
    print("the list is",randomList)
    print()
    print(f"searching for number {searchNumber}")
    #iterates through the list to see if the searchNumber is in the list
    for i in range(len(randomList)):
        comparisons += 1
        if randomList[i] == searchNumber:
            found = True
            print(f"I found the number {searchNumber}!!!")
            print("comparisons:", comparisons)
            break

elif toDo == 2:
    evens = 0
    odds = 0
    sortedList = sorted(randomList)
    print("the list, sorted, is", sortedList)
    #iterates through the list of numbers
    for i in range(len(randomList)):
        #cubes the list
        cubedList.append(randomList[i]**3)
        #counts evens and odds
        if randomList[i] % 2 == 0:
            evens += 1
        else:
            odds += 1
    print("The list cubed is",cubedList)
    sortedList.reverse()
    print("the list in reverse order from sorted is", sortedList)
    print(f"There are {odds} odd numbers and {evens} even numbers")