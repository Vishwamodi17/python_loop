# WHAT IS LOOP?
# A loop in Python is used to repeat a block of code multiple times instead of writing it again and again. It helps automate repetitive tasks..

# TYPES OF LOOP

# FOR LOOP :- Used when you know how many times you want to repeat something.
# for i in range(1,6):
#     print(i)

# KEY POINTS :- 
# 1. range (starts,stops) generates a number
# 2. can run infinite loop 


# WHILE LOOP :- Used when you want to repeat until a condition becomes false.
# i = 0
# while i < 5:
#     print(i)
#     i += 1

# LOOP CONTRROL STATEMENT

# 1. break
# stops the loop imediately
# for i in range: 
#     if(i==3):
#         break
#     print(i)

# 2. continue
# skips current itrearion
# for i in range: 
#     if(i==3):
#         continue
#     print(i)

# 3. pass
# does nothing (placeholder)
# for i in range(5):
#     pass


# TASK 1
# Print number for 1 to 10 using a for loop
# for i in range(1, 11):
#     print(i)

# TASK 2
# print even numbers from 1 to 20
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

# for i in range(2,21,2):
#     print(i)

# TASK 3
# print the odd number from 1 to 15
# for i in range(1, 16):
#     if i % 2 != 0:
#         print(i)

# for i in range(1,16,2):
#     print(i)

# TASK 4
# print each character of the string 
# text = "Python"
# for char in text:
#     print(char)

# TASK 5
# print all items in list
# items = ['data','science','python']
# for item in items:
#     print(item)

# TASK 6
# find the sum of numbers from 1 to 10
# total = 0
# for i in range(1, 11):
#     total += i
# print("Sum:", total)

# TASK 7
# print multiplication table for 5
# for i in range(1, 11):
#     print("5 x", i, "=", 5 * i)

# TASK 8
# count the how many vowels in string
# text = "Hello World"
# count = 0
# for char in text:
#     if char.lower() in "aeiou":
#         count += 1
# print(count)

# TASK 9
# print the reverse number from 10 to 1
# for i in range(10, 0, -1):
#     print(i)

# TASK 10 
# print square of number from 1 to 5
for i in range(1, 6):
    print(i, "->", i * i)

