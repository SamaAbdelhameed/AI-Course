# -*- coding: utf-8 -*-
"""task 3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rohSCuzYEeWm_Y4ienHaB-iq3l8ZlVyi

### 1-Write a Python program that takes two numbers as user input and performs addition on them.
"""

def add_numbers(a, b):
    return a + b

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

sum= add_numbers(num1, num2)

print(f"The sum is:{sum}")

"""### 2-Write a Python program that takes an integer as input and checks if it is even or odd. Print "Even" if the number is divisible by 2, otherwise print "Odd"."""

def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

num = int(input("enter int num: "))
even_odd(num)

"""### 3-Write a Python program that prints all the even numbers from 1 to 20 using a for loop"""

def even_numbers():
    for i in range(1,21):
        if i%2 == 0:
            print(i)

even_numbers()

"""### 4-Write a Python function that takes a string as input and counts the number of vowels (a, e, i, o, u) in the string. The function should return the count"""

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text = input("enter text: ")
vowel_count = count_vowels(text)
print(f"num of vowels: {vowel_count}")

"""### 5-Write a Python program that creates a list of numbers from 1 to 10. Use a loop to iterate over the list and print each number of power 2."""

def square_of_numbers():
    numbers = list(range(1, 11))
    for num in numbers:
        print(num ** 2)

square_of_numbers()

"""### 6-Write a Python program that calculates the average grade for a student based on their scores in different subjects. The program should include the following steps:

#### 1-Create variables to store the student's name, subject names, and corresponding scores. Initialize the variables with sample data.

#### 2-Prompt the user to enter the student's name and assign it to the name variable.

#### 3-Use a loop to prompt the user to enter the subject names and corresponding scores. Store the subject names in a list and the scores in another list.

#### 4-After collecting the scores, calculate the average grade by summing up all the scores and dividing by the total number of subjects.

#### 5-Check if the average grade is above a 70, print a congratulatory message. Otherwise, print an encouragement message.
"""

student_name = ""
subjects = []
scores = []

student_name = input("enter the student's name: ")
num_subjects = int(input("enter num of subjects: "))

for i in range(num_subjects):
    subject = input("enter name of subject: ")
    score = float(input(f"enter score for {subject}: "))
    subjects.append(subject)
    scores.append(score)

avg_grade =int(sum(scores) / num_subjects)

print(f"student: {student_name}")
print("subjects and scores:")
for i in range(num_subjects):
    print(f"{subjects[i]}: {scores[i]}")

print(f"avg Score: {avg_grade}")

if avg_grade > 70:
    print("very good")
else:
    print("study more, please")

"""### 7-Find Common Elements
### Write a Python function that takes two lists as input and returns a new list containing the common elements present in both lists.
"""

def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = find_common_elements(list1, list2)
print(f"common elements: {common_elements}")



"""### 8-Write a Python function that takes a list of numbers and an element to remove from the list."""

def remove_element(list, element):
    if element in list:
        list.remove(element)
    return list

list = [10, 20, 30, 40, 50]
element_to_remove = int(input("enter element to remove: "))

new_list = remove_element(list, element_to_remove)
print(f"new list: {new_list}")

"""### 9-Given 4 numbers A, B, C and D. Print the last 2 digits from their Multiplication.
### Example :
### the Multiplication of 4 numbers is 5 * 7 * 2 * 4 = 280 so the answer will be the last 2 digits which are 80.
"""

def last_two_digit(a, b, c, d):
    result = (a* b* c* d)%100
    return result

a = int(input("enter number a: "))
b = int(input("enter number b: "))
c = int(input("enter number c: "))
d = int(input("enter number d: "))

print(f"Last two digit: {last_two_digit(a, b, c, d)}")

"""### 10- Given a number X. Determine if the number is prime or not"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("enter num: "))
if is_prime(num):
    print(f"{num} is prime num")
else:
    print(f"{num} is not prime num")



"""### 11- Given a number N and a list A of N numbers. Determine if the number X exists in array A or not and print its position (0-index)."""

def num_position(arr, x):
    if x in arr:
        print(f"position_of_num: {arr.index(x)}")
    else:
        print("num not found")

num = int(input("enter num of element: "))
arr = []

for i in range(num):
    arr.append(int(input("enter num: ")))

x = int(input("enter num to find: "))
num_position(arr, x)

"""### 12- Given a number N and a list A of N numbers. Determine if the array is lucky or not.

#### Note: the array is lucky if the frequency (number of occurrence) of the minimum element is odd.
"""

def lucky_array(arr):
    min_num = min(arr)
    freq = arr.count(min_num)
    if freq % 2 != 0:
        print("lucky")
    else:
        print("unlucky")

num= int(input("enter num_of_element: "))
arr= []

for i in range(num):
    arr.append(int(input("enter number: ")))

lucky_array(arr)

"""### 13-Given a number N and a list A of N numbers. Print the array after doing the following operations:

#### Find minimum number in these numbers.
#### Find maximum number in these numbers.
##### Swap minimum number with maximum number.
"""

def swap_min_max(num, arr):
    min_element = min(arr)
    max_element = max(arr)
    min_index = arr.index(min_element)
    max_index = arr.index(max_element)
    arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
    print("list:", arr)
num = 5
arr = [3, 1, 2, 1, 5]
swap_min_max(num,arr)

"""### 14-Given a number N and an array A of N numbers. Print the lowest number and its position.

### Note: if there are more than one answer print first one's position.
"""

def find_lowest_and_position(num, arr):
    min_element = min(arr)
    min_index = arr.index(min_element)
    print("Lowest num:" ,{min_element})
    print("Position:" ,{min_index})
num = 5
arr = [3, 10, 2, 1, 5]
find_lowest_and_position(num,arr)

"""### 15-Given a number N and an array A of N numbers. Print the numbers after sorting them"""

def sort_numbers(num, arr):
    arr.sort()
    for num in arr:
        print(num)

num = int(input("enter number_of_element: "))
arr = []

for i in range(num):
    num = int(input(f"enter number: "))
    arr.append(num)

sort_numbers(num, arr)

"""### 16- Write a Python program to remove spaces from a given string"""

def remove_space(text):
    return text.replace(" ", "")

string = input("enter text: ")
result = remove_space(string)
print(f"string without spaces: {result}")

"""### 17-write a Python program to swap first and last element of any list."""

def swap_first_last(list):
    if len(list) >= 2:
        temp = list[0]
        list[0] = list[-1]
        list[-1] = temp
    return list

my_list = [1, 2, 3, 4, 5]
new_list = swap_first_last(my_list)
print(f"After swap: {new_list}")

"""# **Write a Python Program to Find HCF.**
## Highest Common Factor(HCF): HCF, or Highest Common Factor, is the largest positive integer that divides two or more numbers without leaving a remainder. Formula: For two numbers a and b, the HCF can be found using the formula:

** HCF(𝑎, 𝑏) = GCD(𝑎, 𝑏)**
For more than two numbers, you can find the HCF by taking the GCD of pairs of numbers at a time until you reach the last pair.

# **Note: GCD stands for Greatest Common Divisor, use function.**

"""

num = int(input("enter num_of_element in list: "))
arr = []
for i in range(num):
    num = int(input(f"enter num: "))
    arr.append(num)
a = arr[0]
for b in arr[1:]:
    while b:
        a, b = b, a % b
print(f"HCF of the given num: {a} ")

