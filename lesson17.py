# def myfunc():
#     text = 'hello'
#     dict_ = {}
#     for i in text:
#         if i in dict_:
#             dict_[i] += 1
#         else:
#             dict_[i] = 1
#     print(dict_)
# ----------------------------------------------

# myfunc()
# myfunc()
# myfunc()
# myfunc()
# myfunc()
# myfunc()


# def func():
#     print(10)

# x = func() + 5
# print(x)
# ----------------------------------------------

# def func():
#     return 10

# print(func() + 6)
# ----------------------------------------------

# def func():
#     for i in range(10):
#         print(i)
# func()
# ----------------------------------------------


# def armat(tiv=25):
#     return tiv ** 0.5

# print(armat(16))

# ----------------------------------------------

# def armat(tiv):
#     return tiv ** 0.5

# print(armat(int(input('Greq tiv: '))))
# x = int(input('Greq tiv: '))
# print(armat(x))
# ----------------------------------------------

# def gumar(tiv1, tiv2):
#     return tiv1 + tiv2

# print(gumar(8, tiv2=9))
# ----------------------------------------------

# x = 10

# def func():
#     global x
#     x += 5
#     return x

# print(func())
# ----------------------------------------------


# def func(*args):
#     return args

# print(func())
# ----------------------------------------------

# def func(**kwargs):
#     return kwargs
# print(func(a=5, b=7, c=9))
# ----------------------------------------------

# def func1(a, b):
#     def func2(c, d):
#         return c + d
#     return func2(a, b)
# print(func1(5, 10))
# ----------------------------------------------

# def func():
#     # return 10
#     print(10)

#     None
# ----------------------------------------------

# import matem

# print(matem.armat(25))
# ----------------------------------------------
# def taxi(s):
#     return round(4 + (s / 140) * 0.25, 2)

# print("$",taxi(1490))
# ----------------------------------------------
# def delivery(count):
#     return 10.95 + (count - 1) * 2.95
# print(delivery(5))
# ----------------------------------------------
# def median(a, b, c):
#     return (a + b + c) - min(a, b, c) - max(a, b, c)
# print(median(10, -6, 3))
# ----------------------------------------------
# def is_prime(number):
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     else:
#         return True
# number = int(input('Enter number: '))
# print(is_prime(number))
# ----------------------------------------------
# def calendar(year, month, day):
#     day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if year % 4 == 0:
#         day_list[1] = 29
#     return sum(day_list[:month - 1]) + day
# print(calendar(2024, 3, 15))
# ----------------------------------------------
