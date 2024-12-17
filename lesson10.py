# -------------------------------------------------
# n = int(input('Enter n:  '))
# x = 1
# for i in range(0, n):
#     for j in range(0, 2 * n - 1):
#         if j < (2 * n - 1) // 2 - i or j > (2 * n - 1) // 2 + i:
#             print('   ', end='')
#         else:
#             if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
#                 print(f'{x:>3}', end='  ')
#                 x += 2

#     print()
# -------------------------------------------------
# n = int(input('Enter n:  '))
# for i in range(1, n + 1):
#     x = n
#     for j in range(1, n + 1):
#         if j <= i:
#             print(x, end=' ')
#             x -= 1
#         else:
#             print('.', end=' ')
#     x += 1
#     for j in range(1, n + 1):
#         if i + j > n:
#             print(x, end=' ')
#             x += 1
#         else:
#             print('.', end=' ')
#     print()
# -------------------------------------------------
# text = 'ssbsbsssbbbsbsbssssssssbs'
# text_s = 's' * len(text)
# while text_s not in text:
#     text_s = text_s[:-1]
# print(text_s, len(text_s))
# -------------------------------------------------
# n = int(input('Enter number count:  '))
# max_sum = 0
# for i in range(n):
#     number = int(input('Enter number: '))
#     number = str(number)
#     summ = 0
#     for j in number:
#         summ += int(j)
#     if summ > max_sum:
#         max_sum = summ
# print(max_sum)

# -------------------------------------------------
# x = (8, True, 'Barev', 11)
# print(type(x))

# x = [8, True, 'Barev', 11]
# print(type(x))


# x = 10
# y = x
# y += 5
# print(x)

# x = [1, 2, 3]
# y = x
# y.append(4)
# print(x)

# import random

# x = (8, True, 'Barev', 11)

# print(random.choice(x))
# for i in x:
#     print(i)
# -------------------------------------------------
# import random

# print(random.choice(('Qar', 'Mkrat', 'Tuxt')))
# -------------------------------------------------
# mylist = [4, 5, 'barev']
# mylist.sort()
# print(mylist)
# -------------------------------------------------
# mylist = [5, 4, 6.3, 7.1, 5, 8, 9, -10]
# mylist.sort(reverse=True)
# mylist.sort()
# print(mylist)
# -------------------------------------------------
# mylist = ['e', 'x', 'A', 'a', 't', 'h']
# mylist.sort()
# print(mylist)
# -------------------------------------------------
# mylist = ['Barev', 'python', 'xumb', 'programmer']
# mylist.sort(reverse=True)
# print(mylist)
# -------------------------------------------------
# mylist = ['Barev', 'python', 'xumb', 'programmer']
# mylist.sort(key=len, reverse=True)
# print(mylist)
# -------------------------------------------------
# mylist = ['a', 'b', 'c']
# mylist[2] = 'Ճ'
# print(mylist)
# -------------------------------------------------
# mylist = ['a', 'b', 'c']
# mylist.append('U')
# mylist.append('j')
# print(mylist)
# -------------------------------------------------
# mylist = ['a', 'b', 'c']
# mylist.insert(1, 'H')
# print(mylist)
# -------------------------------------------------
# mylist = ['a', 'b', 'c']
# mylist.remove('b')
# mylist.pop(1)
# mylist.pop()
# del mylist[1:]
# print(mylist)
# -------------------------------------------------
# mylist = ['a', 'b', 'c']
# mylist[1:] = ['Ճ', 'Կ']
# print(mylist)
# -------------------------------------------------
# list1 = [1, 2, 3]
# list2 = list1.copy()
# list2 = list(list1)
# list2 = list1[:]
# list2 = list1[::]
# list2.append(4)
# print(list1)
# -------------------------------------------------
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = list1 + list2
# print(list3)

# list1.extend(list2)
# print(list1)
# -------------------------------------------------
# mylist = [1, 2, 3]
# mylist.clear()
# print(mylist)
# -------------------------------------------------
# mylist = [4, 5, 7, 8, 5, 6, 9, 6, 6, 6, 5, 8, 7, 4]
# print(mylist.count(6))
# -------------------------------------------------
# mylist = [4, 5, 7, 8, 5, 6, 9, 6, 6, 6, 5, 8, 7, 4]
# print(mylist.index(6))
# for i in range(0, len(mylist)):
#     if mylist[i] == 6:
#         print(i)
# -------------------------------------------------
# text = 'python'
# print(list(text))

# text = 'python programming'
# text = text.split(' ')
# print(text)

# x = ['python', 'programming']
# print(' '.join(x))
# -------------------------------------------------
# mylist = [7, 4, 5, 8, 9, 6, 2, 1, 4, 5]
# newlist = []
# for i in mylist:
#     if i % 2 == 0:
#         newlist.append(i)
# print(newlist)
# -------------------------------------------------
# mylist = [7, 4, 5, 8, 9, 6, 2, 1, 4, 5]
# print([i for i in mylist if i % 2 == 0])
# -------------------------------------------------
# mylist = [7, 4, 5, 8, 9, 6, 2, 1, 4, 5]
# newlist = []
# for i in mylist:
#     if i % 2 == 0:
#         newlist.append('Even')
#     else:
#         newlist.append('Odd')
# print(newlist)
# -------------------------------------------------
# mylist = [7, 4, 5, 8, 9, 6, 2, 1, 4, 5]
# print(['Even' if i % 2 == 0 else 'Odd' for i in mylist])
# -------------------------------------------------
# l = [None] * 10
# print(len(l))
# -------------------------------------------------
# mylist = [7, 4, 1, 2, -10, 5, 6, 9, 8]
# newlist = []
# for i in mylist:
#     if i % 2 == 0:
#         newlist.append(i)
# print(newlist)
# -------------------------------------------------
# mylist = [7, 7, 4, 1, 5, 5, 9, 9, 8, 7, 6]
# for i in mylist:
#     if mylist.count(i) == 1:
#         print(i)
# -------------------------------------------------
