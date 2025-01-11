# --------------------------------------------
# def summ():
#     number = input('Enter number: ')
#     if number == '':
#         return 0
#     else:
#         return int(number) + summ()
# print(summ())
# --------------------------------------------
# def func(a, b):
#     if b == 0:
#         return a
#     else:
#         return func(b, a % b)
# print(func(17, 5))
# --------------------------------------------
# def nato(text):
#     nato_alphabet = {
#         'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
#         'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
#         'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo',
#         'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whisky', 'X': 'X-ray',
#         'Y': 'Yankee', 'Z': 'Zulu'
#     }
#     if text == '':
#         return ''
#     else:
#         return nato_alphabet[text[0]] + " " + nato(text[1:])
# print(nato("HELLO"))
# --------------------------------------------



# users = {
#     'Hamlet':20,
#     'Vardan':22
# }
# name = input("Enter name: ")
# age = int(input("Enter age: "))
# print(users.get(name) == age)


# a = 6
# b = 10
# c = -1
# x1 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
# x2 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
# print(x1, x2)

# a = 3
# b = 4
# c = 5
# p = (a + b + c) / 2
# S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(S)


# import random

# pc = random.choice(('Rock', 'Paper', 'Scissors: '))
# user = input('Rock or Paper or Scissors: ')
# if user == 'Rock' and pc == 'Scissors' or user == 'Paper' and pc == 'Rock'

# users = {
#     'Hamlet':20,
#     'Vardan':22
# }
# for i in users:
#     print(i)


# dict_ = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# print({i:dict_[i] for i in sorted(dict_, key=dict_.get, reverse=True)[:3]})

# def myfunc(mylist):
#     mult = 1
#     for i in mylist:
#         mult *= i
#     return mult
# a = [1, 2, 3, 4, 5] 
# print(myfunc(a))


# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
# print(fact(5))
import random


def func1():
    password = ''
    for i in range(0, random.randint(1, 16)):
        password += chr(random.randint(33, 126))
    return password

def func2(password):
    if len(password) < 8:
        return False
    else:
        char_count = 0
        number_count = 0
        upper_case_count = 0
        for i in password:
            if i.isupper():
                upper_case_count += 1
            elif i.isdigit():
                number_count += 1
            elif i.isalpha():
                continue
            else:
                char_count += 1
        if char_count >= 1 and number_count >= 1 and upper_case_count >= 1:
            return True
        else:
            return False


def func3(): 
    count = 1
    while True:
        mypassword = func1()
        pass_ = func2(mypassword)
        print(mypassword)
        if pass_ == True:
            break
        else:
            count += 1
    return count


print(func3())