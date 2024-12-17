# 63, 64, 65, 75, 76, 81

# sum_ = 0
# count_ = 0
# while True:
#     number = int(input('Enter number: '))
#     if number == 0:
#         break
#     else:
#         sum_ += number
#         count_ += 1
# print(sum_ / count_)
# ------------------------------------------------------------
# for i in range(5, 26, 5):
#     number = i - 0.05
#     print(f'price = ${number} - discount = ${round(number*60/100, 2)} = final_price = {round(number - number * 60 / 100, 2)}')
# ------------------------------------------------------------
# print('price\t\tdiscount\tfinal price')
# for i in range(5, 26, 5):
#     number = i - 0.05
#     print(f'{number}\t\t{round(number*60/100, 2)}\t\t{round(number - number * 60 / 100, 2)}')
# ------------------------------------------------------------

# for i in range(0, 101, 10):
#     print(f'{i}(C) = {round(i * 1.8 + 32, 2)}(F)')
# ------------------------------------------------------------

# text = input('Enter text:  ')
# print(text == text[::-1])
# ------------------------------------------------------------


# text = input('Enter text:  ')
# for i in text:
#     if i.isdigit():
#         continue
#     elif i.isalpha():
#         continue
#     else:
#         text = text.replace(i, '')
# print(text == text[::-1])
# ------------------------------------------------------------

# bin_code = input('Enter code: ')
# bin_code = bin_code[::-1]
# number = 0
# for i in range(0, len(bin_code)):
#     number += int(bin_code[i]) * 2 ** i
# print(number)
# ------------------------------------------------------------
# for i in 'abc':
#     for j in range(1, 4):
#         print(i, j, end=' ')
#     print()
# ------------------------------------------------------------
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i * j:>5}', end='')
#     print()
# ------------------------------------------------------------
# if -3:
#     print('Ok')

# ------------------------------------------------------------

# n = int(input('Enter number:  '))
# for i in range(1, n + 1):
#     for _ in range(i):
#         print(i, end=' ')
#     print()
# ------------------------------------------------------------


# n = int(input('Enter n: '))
# for i in range(n + 1):
#     for j in range(n + 1):
#         if j == 0 or j == n:
#             print('|', end='')
#         elif i == 0 or i == n:
#             print('--', end='')
#         else:
#             print('  ', end='')
#     print()
# ------------------------------------------------------------


# n = int(input('Enter n: '))
# for i in range(n + 1):
#     for j in range(n + 1):
#         if i == j or n == i + j:
#             print('^', end='')
#         else:
#             print(' ', end='')
#     print()
# ------------------------------------------------------------


# n = int(input('Enter n: ')) # 24
# for i in range(2, n): # 2, 3, 4, 5, 6, 7, 8, ...., 22, 23
#     if n % i == 0:
#         print(False)
#         break
# else:
#     print(True)
# ------------------------------------------------------------
# number = int(input('Enter number: '))
# text = ''
# while number > 1:
#     text += str(number % 2)
#     number //= 2
# print("1" + text[::-1])
# ------------------------------------------------------------


