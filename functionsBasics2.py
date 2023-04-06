#1
def counDown (startingNr,endingNr):
    myList=[]
    if (startingNr<endingNr):
        print('Numri perfundimtar duhet te jet me i vogel se ai i fillimit')
    else:
        for x in range (startingNr,endingNr-1,-1):
            myList.append(x)
        return myList
print(counDown(5,int(input())))

#2
def printAndReturn(myList):
    print(myList[0])
    return myList[1]
print(printAndReturn([3,2,1]))

#3
def printsum(myList):
    return(myList[0]+len(myList))
myList=[3,2,4,7,9]
result=printsum(myList)
print(result)


#4
def graterThanSecond(myList):
    if len(myList)<2:
        return False
    newList =[]
    for i in range(len(myList)):
        if myList[i]>myList[1]:
            newList.append(myList[i])
    print(len(newList))
    return newList
print(graterThanSecond([2,5,8,7]))


#5
def length_and_value(sizeOf,expectedValue):
    return[expectedValue]*sizeOf
print(length_and_value(4,7))
