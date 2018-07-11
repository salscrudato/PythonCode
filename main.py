from person import Person

def bubbleSort(unsorted):
    tempList = unsorted
    for i in range(0,len(tempList)-1):
        for j in range(0, len(tempList) - 1 - i):
            if tempList[j] > tempList[j+1]:
                temp=tempList[j]
                tempList[j]=tempList[j+1]
                tempList[j+1]=temp
    return tempList

def printAllInList(list):
    for i in range(0,len(list)):
        print(list[i])
        
list = [100, 2, 4, 3, 7, 5, 10, 50, 101, 9, 1]
print('Unsorted List:')
print(list)
list = bubbleSort(list)
print('Sorted List:')
print(list)
print('Each Element in List:')
printAllInList(list)

p1 = Person("Sal", 26)
print(p1.sayHello())