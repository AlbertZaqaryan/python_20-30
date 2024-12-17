# ---------------------------------------------------
# n1, n2 = 0, 1
# for i in range(40):
#     print(n1)
#     n1, n2 = n2, n1 + n2
# ---------------------------------------------------
# for i in range(1, 11):
#     print(i)
# ---------------------------------------------------

# i = 1
# while i < 11:
#     print(i)
#     i += 1
# ---------------------------------------------------


# while True:
#     number = int(input('Enter number: '))
#     if number == 128:
#         break
#     else:
#         print(number)
# ---------------------------------------------------



# summ = 0
# while True:
#     number = int(input('Enter number: '))
#     if number == 0:
#         break
#     else:
#         summ += number
# print(summ)
# ---------------------------------------------------


# summ = 0
# while True:
#     number = input('Enter number: ')
#     if number == '':
#         break
#     else:
#         summ += int(number)
# print(summ)
# ---------------------------------------------------


# count_ = 0
# sum_ = 0
# while True:
#     number = input('Enter number: ')
#     if number == '':
#         break
#     else:
#         sum_ += int(number)
#         count_ += 1
# print(sum_ / count_)
# ---------------------------------------------------


# kassa = 0
# while True:
#     age = input('Enter age:  ')
#     if age == '':
#         break
#     else:
#         age = int(age)
#         if 2 >= age >= 0:
#             continue
#         elif 12 >= age > 2:
#             kassa += 14
#         elif 65 >= age > 12:
#             kassa += 23
#         else:
#             kassa += 18
# print(kassa)
# ---------------------------------------------------

# text = input('Enter text:  ')
# for i in text:
#     print(chr(ord(i) + 3), end='')
# ---------------------------------------------------

# pi = 3
# a = 2
# b = 3
# c = 4
# for i in range(15):
#     pi += (4 / (a * b * c)) * ((-1) ** i)
#     a, b, c = a + 2, b + 2, c + 2
# print(pi)
# ---------------------------------------------------
# import random

# count_o = 0
# count_p = 0
# s = ''
# while True:
#     if count_o == 3 or count_p == 3:
#         break
#     random_letter = random.choice("OP")
#     if random_letter == "O":
#         s += 'O'
#         count_o += 1
#         count_p = 0
#     else:
#         s += 'P'
#         count_p += 1
#         count_o = 0
# print(s)
# ---------------------------------------------------
