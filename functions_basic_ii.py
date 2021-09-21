# 1.Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, 
# from the number (as the 0th element) down to 0 (as the last element). Example: countdown(5) should return [5,4,3,2,1,0]

def listCreator(num):
    listLen = int(num)
    #print(listLen)
    list = []
    for i in  range ( listLen,-1,-1):
        list.append(i)
    #print(list)
    return list

newList = listCreator(5)
print(newList)

print("----------End of exercise 1------------")

# 2.Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2


def printAndReturn( a, b):
    print(a)
    return b

valueReturned = printAndReturn( 1, 2)
#print(valueReturned)

print("----------End of exercise 2------------")


# 3.First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def firstPlusLength(list):
    data = list
    l = len(data)-1
    #print(l)
    x = data[0]
    #print(x)
    y = data[l]
    #print(y)
    result =  x + y
    return result 

sum = firstPlusLength([1,2,3,4,5])
#sum = firstPlusLength([1,2,3,4,5,6,7,8,9,10])
print( sum )

print("----------End of exercise 3------------")

# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original 
# list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, 
# have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def valuesGreaterThanSecond(list):
    secondValue = list[1]
    #print(secondValue)
    newList = []
    counter = 0
    for i in range(0, len(list), 1):
        if( secondValue < list[i]):
            #print(list[i])
            newList.append(list[i])
            #print(newList)
            counter = counter +1
    #print(counter)
    print(counter)
    return newList

valuesGreater = valuesGreaterThanSecond([5,2,3,2,1,4])
print(valuesGreater)

print("----------End of exercise 4------------")




# 5.This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return 
# a list whose length is equal to the given size, and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]


def thisLengthThatValue(size, value):
    thisList = []
    #print(size)
    for i in range(0, size):
        thisList.append(value)
        #print(thisList)
    return thisList

#listSameValues =  thisLengthThatValue( 4, 7)
#print(listSameValues)
        

listSameValues =  thisLengthThatValue( 6, 2)
print(listSameValues)



print("----------End of exercise 5------------")