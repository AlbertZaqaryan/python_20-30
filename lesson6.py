# import random


# pc_followers = random.randint(1, 100)
# user_followers = int(input('Enter your followers count: '))
# if user_followers >= pc_followers + pc_followers * 20 / 100:
#     print('user blogger')
# else:
#     print('pc blogger')
# -------------------------------------------------------
# human1 = int(input('Enter human1 age: '))
# human2 = int(input('Enter human2 age: '))
# human3 = int(input('Enter human3 age: '))
# print(min(human1, human2, human3))
# print(max(human1, human2, human3))
# -------------------------------------------------------
# for i in 'python':
#     print(i)
# -------------------------------------------------------
# for i in range(1, 10):
#     print(i)
# -------------------------------------------------------

# text = 'Hello Python'
# print(text.index('o'))
# -------------------------------------------------------

# for i in range(1, 101):
#     if i % 5 == 0:
#         print(i)
# -------------------------------------------------------
# for i in range(101, -1, -1):
#     print(i)
# -------------------------------------------------------
# for i in range(10, 100):
#     x1 = i % 10
#     x2 = i // 10
#     if x1 + x2 == 10:
#         print(i)
# -------------------------------------------------------
# n = int(input('Enter interval: '))
# for i in range(n):
#     if i % 7 == 0:
#         print(i)
# -------------------------------------------------------
# n1 = int(input('Enter number1:  '))
# n2 = int(input('Enter number2:  '))
# for i in range(1, n1 * n2 + 1):
#     if i % n1 == 0 and i % n2 == 0:
#         print(i)
#         break
# -------------------------------------------------------

# for number in range(1, 100):
#     if number % 6 == 0:
#         print(number)
# -------------------------------------------------------


# for i in range(1, 100):
#     print(i)
# -------------------------------------------------------

# import math

# for i in range(11):
#     print(math.factorial(i))
# -------------------------------------------------------


# for i in range(10, 2, -1):
#     print(i)
# -------------------------------------------------------

# for i in range(50, 600):
#     if i % 100 == 0:
#         print(i)
#         break
# -------------------------------------------------------

# count = 0
# for i in range(1, 100):
#     if i % 5 == 0:
#         print(i)
#         count += 1
#     if count == 3:
#         break
# -------------------------------------------------------
# x = 745896
# for i in x:
#     print(i)

# for i in range(745896):
#     print(i)


# x = '745896'
# for i in x:
#     print(i)


# text = 'python'
# for i in text:
#     print(i)

# text = 'python'
# for i in text:
#     if i == 'o':
#         break
#     else:
#         print(i)
# -------------------------------------------------------
# count = 0
# for i in range(1, 21):
#     if i % 5 == 0:
#         count += 1
# print(count)
# -------------------------------------------------------
# count_odd = 0
# count_even = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1
# print(f'Odd -> {count_odd}\nEven -> {count_even}')
# -------------------------------------------------------
# text = input('Enter text:   ')
# count_let = 0
# count_number = 0
# count_char = 0
# for i in text:
#     if i.isdigit():
#         count_number += 1
#     elif i.isalpha():
#         count_let += 1
#     else:
#         count_char += 1
# print(f'Let -> {count_let}\nNumber -> {count_number}\nChar -> {count_char}')
# -------------------------------------------------------
# n1 = int(input('Enter number1:  '))
# n2 = int(input('Enter number2:  '))
# if n1 > n2:
#     for i in range(n1, n1 * n2 + 1, n1):
#         if i % n2 == 0:
#             print(i)
#             break
# elif n2 > n1:
#     for i in range(n2, n1 * n2 + 1, n2):
#         if i % n1 == 0:
#             print(i)
#             break
# else:
#     print(n1)
# -------------------------------------------------------
# for i in range(1, 10):
#     if i % 17 == 0:
#         break
# else:
#     print('ok')
# -------------------------------------------------------
# for i in range(1, 10):
#     if i == 5:
#         print('gta')
#     else:
#         print('chgta')
# -------------------------------------------------------
# for i in range(15, 10):
#     if i == 5:
#         print('gta')
#         break
# else:
#     print('chgta')
# -------------------------------------------------------
# number = int(input('Enter number: '))
# summ = 0
# for i in str(number):
#     summ += int(i)
# print(summ)
# -------------------------------------------------------
# text = 'python 3.13'
# summ = 0
# for i in text:
#     if i.isdigit():
#         summ += int(i)
# print(summ)
# -------------------------------------------------------
# import math

# n = 5
# print(math.factorial(n))
# 1 * 2 * 3 * 4 * 5
# -------------------------------------------------------


# n = int(input('Enter number: '))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print(factorial)

# -------------------------------------------------------

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print('fizz buzz')
#     elif number % 5 == 0:
#         print('buzz')
#     elif number % 3 == 0:
#         print('fizz')
#     else:
#         print(number)
# -------------------------------------------------------
# text = input('Enter text: ').lower()
# count = 0
# for i in text:
#     if i == 'a':
#         count += 1
# print(count)