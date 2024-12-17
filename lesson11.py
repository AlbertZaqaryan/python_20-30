# --------------------------- ex 1 -------------------------
# x = 5
# y = 7.6
# z = 'Barev'
# h = (1, 2, 3)
# u = True
# l = [1, 2, 3]
# --------------------------- ex 2 -------------------------
# my_list =["Hp", "Asus", "Dell", "Mac", "Lenovo"] 
# print("Mac" in my_list)
# --------------------------- ex 3 -------------------------
# password = input('Enter password:  ')
# number_count = 0
# char_count = 0
# if password[0].isupper():
#     if len(password) >= 8:
#         for i in password:
#             if i.isalpha():
#                 continue
#             elif i.isdigit():
#                 number_count += 1
#             else:
#                 char_count += 1
#         if number_count >= 2 and char_count >= 2:
#             print(password, 'Is very strong!!')
#         else:
#             print('Your password is not strong!!!')
#     else:
#         print('Your password is not strong!!!')
# else:
#     print('Your password is not strong!!!')
# --------------------------- ex 4 -------------------------
# link = "https://www.youtube.com/watch?v=RRW2aUSw5vU"
# print(link[link.index('=') + 1:])

# link = link.split('=')
# print(link[1])
# --------------------------- ex 5 -------------------------
# text = input('Enter text:  ')
# if text == text[::-1]:
#     print('Open')
# else:
#     print('Close')
# --------------------------- ex 6 -------------------------
# text = input('Enter text: ')
# print(list(text))
# --------------------------- ex 7 -------------------------
# numbers = input('Enter 5 numbers: ')
# print([int(i) for i in numbers.split(' ') if int(i) % 2 == 0])
# --------------------------- ex 9 -------------------------
# import random

# group1 = ['Armen', 'Sahak', 'Karine', 'Anna', 'David']
# group2 = ['Armen', 'Sahak', 'Karine', 'Anna', 'David']
# final_list = []
# while group1 != []:
#     u1 = random.choice(group1)
#     u2 = random.choice(group2)
#     if u1 == u2:
#         if len(group1) == 1 == len(group2):
#             group1 = ['Armen', 'Sahak', 'Karine', 'Anna', 'David']
#             group2 = ['Armen', 'Sahak', 'Karine', 'Anna', 'David']
#             final_list = []
#         else:
#             continue
#     else:
#         final_list.append(f'{u1} --> {u2}')
#         group1.remove(u1)
#         group2.remove(u2)
# for i in final_list:
#     print(i)
# ----------------------------------------------------
# number = int(input('Enter number: '))
# mylist = []
# for i in range(1, number + 1):
#     if number % i == 0:
#         mylist.append(i)
# print(mylist)

# print([i for i in range(1, number + 1) if number % i == 0])
# ----------------------------------------------------
# master = ['♥', '♦', '♣', '♠']
# karter = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# kalod = []
# for i in master:
#     for j in karter:
#         kalod.append(i + j)
# print(kalod)
# ----------------------------------------------------
# import random

# master = ['♥', '♦', '♣', '♠']
# karter = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# kalod = [i + j for i in master for j in karter]
# nor_kalod = []
# while kalod != []:
#     random_kart = random.choice(kalod)
#     nor_kalod.append(random_kart)
#     kalod.remove(random_kart)
# users = []
# for i in range(4):
#     users.append(input('Enter username:  '))
# for i in users:
#     print(f'{i} - {nor_kalod[:8]}')
#     nor_kalod = nor_kalod[8:]
# ----------------------------------------------------
# mylist = [1, 2, 3, 4]
# [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [2], [2, 3], [2, 3, 4], [3], [3, 4], [4]]
# ----------------------------------------------------
mylist = [7, 4, 5, 8, 1, 3, 6, 9]
# mylist.sort()
mylist[0], mylist[1] = mylist[1], mylist[0]
print(mylist)
