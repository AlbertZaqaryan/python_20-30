# import math

# n = int(input('Enter number: '))
# print(math.factorial(n))

# age = int(input('Enter age: '))
# print(17 <= age <= 25)
# print(age >= 17 and age <= 25)
# --------------------------------------------------
# import random

# pc_number = random.randint(0, 9) # 5
# numbers = input('Enter 5 numbers: ')
# print(pc_number)
# print(str(pc_number) in numbers)
# print('5' in '12345')
# --------------------------------------------------
# if 
# elif
# else

# a = int(input('Enter number a: '))
# b = int(input('Enter number b: '))
# if a > b:
#     print('a is max!!')
# elif a == b:
#     print('equal')
# else:
#     print('b is max!!')
# --------------------------------------------------


# age = int(input('Enter your age: '))
# if 10 >= age >= 0:
#     print('Free')
# elif 30 >= age > 10:
#     print('Pay 10$')
# elif 65 >= age > 30:
#     print('Pay 5$')
# elif 80 >= age > 65:
#     print('Pay 1$')
# else:
#     print('Pay 0.25$')
# --------------------------------------------------


number = int(input('Enter number: ')) # 15
if number % 3 == 0 and number % 5 == 0:
    print('fizz buzz')
elif number % 5 == 0:
    print('buzz')
elif number % 3 == 0:
    print('fizz')
else:
    print(number)
# --------------------------------------------------
# number = int(input('Enter number:  '))
# if number % 2 == 0:
#     print('even')
# else:
#     print('odd')
# --------------------------------------------------
# dzaynavorner = 'aeiou'
# tar = input('Mutqagreq tar:  ').lower()
# if tar in dzaynavorner:
#     print('dzaynavor')
# else:
#     print('baxadzayn')
# --------------------------------------------------
# tariq = int(input("Qani tarekan es? "))
# if tariq >= 18:
#     alkohol = input('Inch alkohol eq uzum: ')
#     if alkohol == 'oxi':
#         print('Gnum es xmelu')
#     elif alkohol == 'viski':
#         print('Gnum es tun')
#     else:
#         print('Hastat xmum es piva')
# else:
#     print('Qony sokerna')
# --------------------------------------------------
# import random
# import time

# name = input('Enter your name: ')
# ready = input(f'Hello {name} are you ready? ')
# if ready == 'yes':
#     print(f'{name} welcome the best game!!!!!')
#     print(3)
#     time.sleep(1)
#     print(2)
#     time.sleep(1)
#     print(1)
#     time.sleep(1)
#     print('Start game...')
#     pc = random.randint(0, 5)
#     user = int(input('Enter number in range(0, 5):  '))
#     pc_points = 0
#     user_points = 0
#     if user == pc: # round 1| user = 1, pc = 0
#         user_points += 1
#         print(f'--> WIN USER <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#         pc = random.randint(0, 5)
#         user = int(input('Enter number in range(0, 5):  '))
#         if user == pc: # round 2| user = 2, pc = 0 END GAME WIN USER
#             user_points += 1
#             print(f'--> WIN USER <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#             print('################## END GAME WIN USER ##################')
#         else: # round 2| user = 1, pc = 1
#             pc_points += 1
#             print(f'--> WIN PC <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#             pc = random.randint(0, 5)
#             user = int(input('Enter number in range(0, 5):  '))
#             if user == pc: # round 3| user = 2, pc = 1 END GAME WIN USER
#                 user_points += 1
#                 print(f'--> WIN USER <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#                 print('################## END GAME WIN USER ##################')
#             else: # round 3| user = 1, pc = 2 END GAME WIN PC
#                 pc_points += 1
#                 print(f'--> WIN PC <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#                 print('################## END GAME WIN PC ##################')
#     else: # round 1| user = 0, pc = 1
#         pc_points += 1
#         print(f'--> WIN PC <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#         pc = random.randint(0, 5)
#         user = int(input('Enter number in range(0, 5):  '))
#         if user == pc: # round 2| user = 1, pc = 1
#             user_points += 1
#             print(f'--> WIN USER <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#             pc = random.randint(0, 5)
#             user = int(input('Enter number in range(0, 5):  '))
#             if user == pc: # round 3| user = 2, pc = 1 END GAME WIN USER
#                 user_points += 1
#                 print(f'--> WIN USER <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#                 print('################## END GAME WIN USER ##################')
#             else: # round 3| user = 1, pc = 2 END GAME WIN PC
#                 pc_points += 1
#                 print(f'--> WIN PC <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#                 print('################## END GAME WIN PC ##################')
#         else: # round 2| user = 0, pc = 2 END GAME WIN PC
#             pc_points += 1
#             print(f'--> WIN PC <---\nuser = {user}, pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#             print('################## END GAME WIN PC ##################')
# else:
#     print('------------------------- EXIT -------------------------')
# --------------------------------------------------
# import random

# pc = random.choice(('Rock', 'Paper', 'Scissors'))
# user = input('Enter Rock or Paper or Scissors:  ')
# if (user == 'Rock' and pc == 'Scissors') or (user == 'Paper' and pc == 'Rock') or (user == 'Scissors' and pc == 'Paper'):
#     print(f'User = {user}, pc = {pc}')
#     print('-------------- WIN USER -------------------')
# elif (pc == 'Rock' and user == 'Scissors') or (pc == 'Paper' and user == 'Rock') or (pc == 'Scissors' and user == 'Paper'):
#     print(f'User = {user}, pc = {pc}')
#     print('-------------- WIN PC -------------------')
# else:
#     print(f'User = {user}, pc = {pc}')
#     print('------------ EQUAL --------------')
# --------------------------------------------------
# tar = input('Mutq tar: ')
# tiv = int(input('Mutq tiv: '))
# if (tar in 'aceg' and tiv % 2 != 0) or (tar in 'bdfh' and tiv % 2 == 0):
#     print('Sev')
# else:
#     print('Spitak')
# --------------------------------------------------
# import random

# pc_followers = random.randint(1, 100000)
# user_followers = int(input('Enter ..'))
# if user_followers >= pc_followers + pc_followers * 20 / 100:
#     print('user blogger')
# else:
#     print('pc blogger')
# --------------------------------------------------
# dog      human
#  1        10.5
#  2         21
#  3         25
#  4         29
#  5         33 
#  .          .
#  .          .
#  .          .

# dog_age = int(input('Enter dog age: '))
# if dog_age <= 2:
#     print(f'Human age = {dog_age * 10.5}')
# else:
#     print(f'Human age = {21 + (dog_age - 2) * 4}')
# --------------------------------------------------
