"""#sum of two number
def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
n1 = 2
n2 = 3
print(maximum(n1,n2))
# sum of two number using max()
a = 2
b = 4
maximum = max(a,b)
print(maximum)

#factorial using recursion
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1);
num = 5;
print("factorial of", num, "is", factorial(num))


#using ternery operator

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
num = 5
print("Factorial of", num, "is", factorial(num))

#using inbuilt fctorila
import math
def factorial(n):
    return (math.factorial(n))
num = 5
print("Factorial of ", num, 'is', factorial(num))

#simple Interest
def simple_interest(p, t, r):
    print('the principle is', p)
    print('the time is ', t)
    print('the rate of interest', r)

    si = (p * t * r)/100

    print('the Simple Interest', si)
    return si
simple_interest(1000,8,4)

# check for compound interest

def compound_interest(principle, rate, time):
    Amount = principle * (pow((1+rate/100), time))
    CI = Amount - principle
    print("Compount interest is", CI)

compound_interest(10000, 10.25, 5)


#checking prime number
num = 11

if num > 1:
    # iterate from 2 to n/2
    for i in range(2, int(num/2)+1):
        #if number is divisible by any number
        #between 2 and n/2, it is not prime
        if (num % i) == 0:
            prime(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# swaping first and last element of list

def swapList(newList):
    size = len(newList)

    #swaping
    temp = newList[0]
    newList[0] = newList[size -1]
    newList[size - 1] = temp

    return newList
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

#swapingusing simple swap method

def swapList(newList):

    newList[0], newList[-1] = newList[-1], newList[0]

    return newList
newList = [12,34,23,32,13]
print(swapList(newList))
    

# using tuple for storing first and last elements
def swapList(lst):
    tpl = lst[-1], lst[0]
    lst[0], lst[-1] = tpl

    return lst
newList = [34,54,65,43,64]
print(swapList(newList))


# using pop method
def swapList(lst):

    first = lst.pop(0)
    last = lst.pop(-1)

    lst.insert(0, last)
    lst.append(first)

    return lst
newList = [23,34,23,54]
print(swapList(newList))
    


# lenth of list using counter
test_list = [10,20,30,23,65]

print("The list is :" +str(test_list))

#count lenth of list using loop
counter = 0
for i in test_list:
    counter = counter + 1

print("Lenth of list using loop : " +str(counter))

"""


#using len meethod

a =[]
a.append("Hello")
a.append("anand")
a.append("how are u")
a.append("doing")
print("The lenth of list is: ", len(a))






























    

        






















    
