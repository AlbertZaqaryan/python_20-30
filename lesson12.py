# --------------> 110 <----------------------
# mylist = []
# while True:
#     number = int(input('Enter number:  '))
#     if number == 0:
#         break
#     mylist.append(number)
# mylist.sort()
# print(mylist)

# --------------> 111 <----------------------
# mylist = []
# while True:
#     number = int(input('Enter number:  '))
#     if number == 0:
#         break
#     mylist.append(number)
# mylist.sort(reverse=True)
# print(mylist)
# --------------> 112 <----------------------
# mylist = []
# while True:
#     number = input('Enter number: ')
#     if number == '':
#         break
#     mylist.append(int(number))
# if len(mylist) < 4:
#     print('ERROR')
# else:
#     print(mylist)
#     mylist.remove(min(mylist))
#     mylist.remove(max(mylist))
#     print(mylist)
# --------------> 113 <----------------------
# mylist = []
# while True:
#     word = input('Enter word:  ')
#     if word == '':
#         break
#     if word not in mylist:
#         mylist.append(word)
# print(mylist)
# --------------> 114 <----------------------
# list1 = []
# list2 = []
# list3 = []
# while True:
#     number = input('Enter number: ')
#     if number == '':
#         break
#     number = int(number)
#     if number < 0:
#         list1.append(number)
#     elif number == 0:
#         list2.append(number)
#     else:
#         list3.append(number)
# print(list1, list2, list3)
# --------------> 116 <----------------------
# summ = 0
# n = int(input('Enter number: '))
# for i in range(1, n // 2 + 1):
#     if n % i == 0:
#         summ += i
# if summ == n:
#     print(True)
# else:
#     print(False)


# for n in range(1, 10001):
#     summ = 0
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             summ += i
#     if summ == n:
#         print(n)
# ------------------------------------------------
# mylist = [7, 4, 5, 1, 2, 3, 6, 9, 8]
# for _ in range(0, len(mylist)):
#     for j in range(0, len(mylist) - 1):
#         if mylist[j] > mylist[j + 1]:
#             mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
# print(mylist)
# ------------------------------------------------
# mylist = [1, 2, 3, 4]
# print([mylist[i:j] for i in range(len(mylist)) for j in range(i + 1, len(mylist) + 1)])
# ------------------------------------------------
# mylist = [1, 2, 3, 4]
# newlist = []
# for i in range(0, len(mylist)):
#     for j in range(i + 1, len(mylist) + 1):
#         newlist.append(mylist[i:j])
# print(newlist)
# ------------------------------------------------
# mylist = [4, 7, 15, 28, 36, 48, 59, 67, 84, 125, 325, 478, 965, 1024, 1563, 8541, 10207, 27458]
# n = 8541
# for i in range(0, len(mylist)):
#     if mylist[i] == n:
#         print(i)
# ------------------------------------------------
# mylist = [4, 7, 15, 28, 36, 48, 59, 67, 84, 125, 325, 478, 965, 1024, 1563, 8541, 10207, 27458]
# n = 8541
# start = 0
# stop = len(mylist)
# while True:
#     mid = (start + stop) // 2
#     if mylist[mid] == n:
#         print(mid)
#         break
#     elif n > mylist[mid]:
#         start = mid + 1
#     else:
#         stop = mid - 1
# ------------------------------------------------
# mylist = [7, 4, 1, 5, 8, 9, 6, 5, 8, 7, 4]
# for i in mylist:
#     if mylist.count(i) == 1:
#         print(i)
# ------------------------------------------------
mylist = [3, 1, 2, 1, 1, 6]
jump = 0
while True:
    if jump >= len(mylist):
        print(False)
        break
    elif jump == len(mylist) - 1:
        print(True)
        break
    if mylist[jump] == 0:
        print(False)
        break
    jump += mylist[jump]
# ------------------------------------------------
# text = 'hello'
# mylist = []
# for i in text:
#     if i not in mylist:
#         mylist.append(i)
# print(len(mylist))
# ------------------------------------------------
# mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(0, len(mylist)):
#     if mylist[i] % 2 == 0:
#         mylist[i] = 1
#     else:
#         mylist[i] = mylist[i] % 5
# print(mylist)
# ------------------------------------------------
# mylist = []
# while True:
#     number = input('Enter number: ')
#     if number == '':
#         break
#     mylist.append(int(number))
# print(mylist)
# ------------------------------------------------
# mylist = [0, 2, 1, 0, 0, 0, 1, 0, 2, 0]
# print([i for i in mylist if i != 0])
# ------------------------------------------------
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# print([i for i in nice_list for i in i for i in i])
# newlist = []
# for i in nice_list:
#     for j in i:
#         for k in j:
#             newlist.append(k)
# print(newlist)
# ------------------------------------------------
# text = 'hello python team'
# text = text.split(' ')
# text.sort(key=len)
# print(text[-1])
# ------------------------------------------------
