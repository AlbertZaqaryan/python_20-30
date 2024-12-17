# for i in range(0, 6):
#     for j in range(i, 11 + i, 2):
#         print(f'{j:>3}', end='')
#     print()
# ----------------------------------------------------
# n = int(input('Enter number:  '))
# for i in range(1, n + 1):
#     for _ in range(i):
#         print(i, end=' ')
#     print()
# ----------------------------------------------------
# n = int(input('Enter number:  '))
# for i in range(1, n + 1):
#     for _ in range(i):
#         print('*', end=' ')
#     print()
# ----------------------------------------------------
# n = int(input('Enter number:  '))
# for i in range(0, n + 1):
#     for j in range(0, n + 1):
#         if j == 0 or j == n:
#             print('|', end='')
#         elif i == 0 or i == n:
#             print('--', end='')
#         else:
#             print('  ', end='')
#     print()
# ----------------------------------------------------
# n = int(input('Enter number:  '))
# for i in range(n + 1):
#     for j in range(n + 1):
#         if i == j or n == i + j:
#             print('^', end='')
#         else:
#             print(' ', end='')
#     print()
# ----------------------------------------------------
# n = int(input('Enter number: '))
# for i in range(2, n):
#     if n % i == 0:
#         print('Parz che')
#         break
# else:
#     print('Parz e')
# ----------------------------------------------------

# summ = 0
# n = int(input('Enter number count:  '))
# for _ in range(n):
#     number = int(input('Enter your number: '))
#     for i in range(2, number):
#         if number % i == 0:
#             break
#     else:
#         summ += 1
# print(summ)
# ----------------------------------------------------


# n = int(input('Enter number: '))
# for i in range(n):
#     for j in range(2 * n - 1):
#         if j < (2 * n - 1) // 2 - i or j > (2 * n - 1) // 2 + i:
#             print(' ', end='')
#         else:
#             print('#', end='')
#     print()
# ----------------------------------------------------

# n = int(input('Enter number: '))
# summ = 0
# for i in range(1, n + 1):
#     fact = 1
#     for j in range(1, i + 1):
#         fact *= j
#     summ += fact
# print(summ)
# ----------------------------------------------------

# n = int(input('Enter number: '))
# summ = 0
# for i in range(0, n + 1, 5):
#     price = int(input(f'{i} partqater inchqan es partq: '))
#     summ += price
# print(summ)

# ----------------------------------------------------

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# c = int(input('Enter c: '))
# for i in range(a, b):
#     if i % c == 0:
#         print(i)

# ----------------------------------------------------

# n = int(input('Enter number: '))
# count = 0
# while n > 12:
#     n /= 2
#     count += 2
# print(count)
# ----------------------------------------------------



