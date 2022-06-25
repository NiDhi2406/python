def calculateValueByUsage(users, priority, usage):
    iterator = 0
    tempArray = []
    while iterator < users:
        value = priority[iterator] / usage[iterator]
        tempArray.append(value)
        iterator += 1
    return tempArray

def calculateOptimalUsage(ram, usage, priority):
    tempPriority = priority
    tempRam = ram
    iterator = 0
    optimalValue = 0
    while tempRam > 0:
        if tempRam < usage[iterator]:
            iterator += 1
            break
        else:
            tempRam = tempRam - usage[iterator]
            optimalValue = optimalValue + tempPriority[iterator]
            iterator += 1
    print(optimalValue)
    return optimalValue
def sortValueByUsageAndFindOptimalValue(array, priority, usage, capacity):
    iterator, mainIterator = 0, 0
    # Temp variables for each parameter
    tempArray = array
    tempPriority = priority
    tempRamUsage = usage

    while mainIterator < len(array):
        while iterator < len(array) - 1:
            # Sorting in descending order
            if tempArray[iterator] < tempArray[iterator + 1]:
                temp = tempArray[iterator]
                temp1 = tempPriority[iterator]
                temp2 = tempRamUsage[iterator]

                tempPriority[iterator] = tempPriority[iterator + 1]
                tempRamUsage[iterator] = tempRamUsage[iterator + 1]
                tempArray[iterator] = tempArray[iterator + 1]

                tempPriority[iterator + 1] = temp1
                tempRamUsage[iterator + 1] = temp2
                tempArray[iterator + 1] = temp
            iterator += 1
        
        iterator = 0
        mainIterator += 1
    result = calculateOptimalUsage(capacity, tempRamUsage, tempPriority)
    return result

total = 0
noOfServers = int(input()) 
for i in range(noOfServers):
    noOfUsers = int(input())  
    serverCapacity = int(input()) 
    priorityNo = list(map(int, input().split())) 
    ramUsage = list(map(int, input().split())) 
    valueByEachUser = calculateValueByUsage(noOfUsers, priorityNo, ramUsage)
    total = total + sortValueByUsageAndFindOptimalValue(valueByEachUser, priorityNo, ramUsage, serverCapacity)
print(total)
