# Birth_year = input("Enter the birth year ")
# current_year = 2024
# age = current_year - int(Birth_year)
# print(age)


#exercise 
# First = input("enter first number: ")

# Second = input("enter second number: ")
# Sum = float(First)+ int(Second)
# print(Sum)

#Operations on strings

# course = 'Python for beginners'
#print(course.upper()) # to convert to upper case
# print(course.lower()) # to convert to lower case
# print(course.find('r')) # to fine the index of given argument
# print('Python' in course)  # to check the contents are available in the data
# print(course)

# arthmatic operators

# x = 10 
# x = x + 3
# x += 3
# print(x)

#operator precedence

# x = 10 + 3 * 2 #here the multiplication operator has more higher precedence than first solve multiplication
# x = (10 + 3) * 2 #here the prenthesis has more precedence than the first solve prenthesis than multiplication
# print(x)

#comparison operators

# x = 5 < 3 # it will give the answer in boolean form true or false
# print(x)
#here is the comparison operators
# <
# <=
# >
# >=
# ==
# !=


# Logical operators
# price = 20
# print(price > 15 and price < 30) #in and gate case the output will be true if both conditions are true 
# print(price < 15 or price < 30) # in or gate case the output will be true if at-least one of the  conditions is  true
# print(not price > 30) #not operator inverse the condition

#there are 3 logical operators
# and #both conditions are true
# or # at least one of the conditions is true
# not # inverse the variable 

#if statements
# temperature = input("enter temperature")
# if int(temperature) > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif int(temperature) > 20:
#     print("It's a nice day")
# elif int(temperature) > 10:
#     print("It's a bit cold day")
# else:
#     print("It's a cold day")
# print("Done")

#exercise
# Weight = input("Enter your weight:")
# unit = input("(K)g or (L)bs:")
# if unit == "K":
#     converted_weight = float(Weight) * 2.20462
#     print("Your weight in pounds is:" + str(converted_weight))
# else:
#     converted_weight = float(Weight) / 2.20462
#     print("Your weight in kilograms is:" + str(converted_weight))
     


#while loop
# i = 1
# while i <= 10:
#     # print(i*2)
#     print(i * '*')
#     i += 1

#string methods

# age = 21
# txt = "my name is Rocky and i'm " + str(age) + " " + "years old"
# print(txt.capitalize())
# print(txt.casefold())
# print(txt.find("is")
#       print(txt.()

# data = [1, 2, 3, 4, 5]
# while (n := len(data)) > 0:
#     print(f"Processing {n} items")
#     data.pop()


# thislist = ["apple", "banana", "cherry"]
# thislist[0], thislist[-1] = thislist[-1], thislist[0] 
# print(thislist)


# a = 2
# b = 4
 
# minimum = min(a, b)
# print(minimum)




def mySwapFunction(mylist, p1, p2):
    temp = mylist[p1]
    mylist[p1] = mylist[p2]
    mylist[p2] = temp
    print(mylist)
    return mylist

oldlist = [2, 4, 51, 6]
swappedList = mySwapFunction(oldlist, 0, 2)
print(swappedList)

for x in swappedList:
    print(x)

[print(x) for x in swappedList] 


test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
 
# printing original lists
print("The original list is : " + str(test_list))
 
# Swap elements in String list
# using replace() + list comprehension
res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]

# ['-fg', 'is', 'best', 'for', '-eeks']
# ['-fg', 'is', 'bGst', 'for', '-GGks']
# ['efg', 'is', 'bGst', 'for', 'eGGks']


# length = sum(1 for _ in test_list)
xyz = [1 for x in test_list]

print(sum(xyz))

def maxOfTwo(x, y):
    if x > y:
        return f" {x} is greater than {y}"
    elif y > x:
        return f" {y} is greater than {x}"
    else:
        return f"{x} and {y} are equal"
    
print('Maximum of 151, 5 is ' + maxOfTwo(151, 5))
print('Maximum of 1, 5 is ' + maxOfTwo(1, 5))
print('Maximum of 151, 151 is ' + maxOfTwo(151, 151))



check_list = [1, 6, 5, 4]
 # Check if 3 exist or not.
if 3 in check_list:
    print("3 does exist in list")
else:
    print("3 does not exist in list")

for x in check_list:
    # print(x)
    if x == 3:
        print("3 does exist")
        break
    else:
        continue



list = [4, 5, 6, 11, 7, 8, 9]
# Output: [9, 8, 7, 6, 5, 4]
lastIndex = len(list)-1
for x in range(len(list)):
    # before swapping the values check if x has crossed last index
    if x >= lastIndex:
        break
    temp = list[x]
    print(temp)
    list[x] = list[lastIndex]
    list[lastIndex] = temp
    lastIndex = lastIndex -1


print(list)


count = [4, 5, 4, 11, 4, 7, 4, 8, 4, 9]
x = 4
cnt = 0
for num in count:
    if num == x: 
        cnt += 1
print(f'4 occurred {cnt} times')




# Input: [4, 5, 1, 2, 9, 7, 10, 8]
# Output:
# sum =  46
# average =  5.75

sumAvg = [4, 5, 1, 2, 9, 7, 10, 8]
sum = 0
for x in sumAvg:
    sum += x
avg = sum/len(sumAvg)
print(f'Sum of list is {sum}')
print(f'Average of list is {avg}')

sumAvg.append(3)
print(sumAvg)


#multiplaction of list elements
multiplyList = [4, 5, 1, 2, 9, 7, 10, 8]
multiply = 1
for x in multiplyList:
    multiply = multiply * x
print(multiply)

#smallest number 
list = [10, 20, 4]
smallest = list[0]

for x in list:
    if x < smallest:
        smallest = x

print(smallest)

#largest number
list = [10, 20, 4]
largest = list[0]

for x in list:
    if x > smallest:
        larges = x

print(larges)
    

# Even number 
list1 = [4, 5, 1, 2, 9, 7, 10, 8]
for x in list1:
    if x % 2 == 0:   
        print(x)
# Odd number 
list1 = [4, 5, 1, 2, 9, 7, 10, 8]
for x in list1:
    if x % 2 != 0:   
        print(x)

Odd = [x for x in list1 if x % 2 != 0]
print(Odd)



# Input: list1 = [2, 7, 5, 64, 14]
# Output: Even = 3, odd = 2

OddEvin = [2, 7, 5, 64, 14]
Even = 0
Odd = 0
x = 0
for x in OddEvin:
    if x % 2 ==  0:
        Even += 1
        
    else:
        Odd += 1
        
print("Even numbers in this list: ", Even)
print("Odd numbers in this list: ", Odd)  

#using while loop

while (x < len(OddEvin)):
    if OddEvin[x] % 2 == 0:
        Even += 1
    else:
        Odd += 1

    x += 1
print("Even numbers in this list: ", Even)
print("Odd numbers in this list: ", Odd)


# positive number in list 
# Input: list1 = [12, -7, 5, 64, -14]
# Output: 12, 5, 64

Positivelist  = [12, -7, 5, 64, -14]
for x in Positivelist:
    if x >= 0:
        print(x)

#using while loop
list1 = [-10, 21, -4, -45, -66, 93]
x = 0

while(x < len(list1)):
    if list1[x] >= 0:
        print(list1[x])
    x += 1


nagetivelist  = [12, -7, 5, 64, -14]
for x in nagetivelist:
    if x <= 0:
        print(x)

#using while loop
list1 = [-10, 21, -4, -45, -66, 93]
x = 0

while(x < len(list1)):
    if list1[x] <= 0:
        print(list1[x])
    x += 1


name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f"Hello, {name} You are an adult.")
elif age >= 13:
    print(f"Hello, {name} You are a teenager.")
else:
    print(f"Hey, {name} You are a child.")
    

# Writing to a file
with open("students.txt", "w") as file:
    file.write("Alice,90\n")
    file.write("Bob,85\n")
    file.write("Charlie,95\n")

# Reading from the file and finding the student with the highest grade
with open("students.txt", "r") as file:
    lines = file.readlines()

highest_grade = 0
top_student = ""

for line in lines:
    name, grade = line.split(",")  # Split the name and grade
    grade = int(grade)  # Convert the grade to an integer
    if grade > highest_grade:
        highest_grade = grade
        top_student = name


print(f"The top student is {top_student} with a grade of {highest_grade}.")




