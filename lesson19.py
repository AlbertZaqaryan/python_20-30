# n = 5
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print(factorial)
# -------------------------------------------------
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#     #         5 * 4 * 3 * 2 * 1 = 120
# print(factorial(5))
# -------------------------------------------------
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 2) + fib(n - 1)
#     # fib(4) + fib(5)
#     # fib(2) + fib(3) + fib(5)
#     # fib(0) + fib(1) + fib(3) + fib(5)
#     # 0 + 1 + fib(3) + fib(5)
#     # 0 + 1 + fib(1) + fib(2) + fib(5)
#     # 0 + 1 + 1 + fib(2) + fib(5)
#     # 0 + 1 + 1 + fib(0) + fib(1) + fib(5)
#     # 0 + 1 + 1 + 0 + 1 + fib(5)
#     # 0 + 1 + 1 + 0 + 1 + fib(3) + fib(4)
#     # 0 + 1 + 1 + 0 + 1 + fib(1) + fib(2) + fib(4)
#     # 0 + 1 + 1 + 0 + 1 + 1 + fib(2) + fib(4)
#     # 0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(4)
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(4)
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(2) + fib(3)
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(0) + fib(1) + fib(3)
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + fib(3)
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + fib(1) + fib(2)
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(2)
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1 = 8
# print(fib(6))
# -------------------------------------------------
# def even_elements(mylist):
#     if mylist == []:
#         return []
#     elif mylist[0] % 2 == 0:
#         return [mylist[0]] + even_elements(mylist[1:])
#     else:
#         return even_elements(mylist[1:])
# print(even_elements([7, 4, 1, 5, 8, 9, 6, 5, 8, 7, 4]))
# -------------------------------------------------
# def encoding(mylist):
#     if mylist == []:
#         return []
#     else:
#         return [mylist[0]] * mylist[1] + encoding(mylist[2:])

# print(encoding(["A", 12, "B", 4, "A", 6, "B", 1]))
# -------------------------------------------------
# def decoding(mylist, count=1):
#     if len(mylist) == mylist.count(mylist[0]):
#         return [mylist[0], len(mylist)]
#     if mylist[0] == mylist[1]:
#         return decoding(mylist[1:], count + 1)
#     else:
#         return [mylist[0], count] + decoding(mylist[1:], count=1)

# print(decoding(["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]))
# -------------------------------------------------
# def primelist(mylist):
#     if mylist == []:
#         return []
#     elif type(mylist[0]) == int:
#         return [mylist[0]] + primelist(mylist[1:])
#     else:
#         return primelist(mylist[0]) + primelist(mylist[1:])

# print(primelist([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))
# -------------------------------------------------
# def dec_to_bin(number):
#     if number == 1:
#         return "1"
#     else:
#         return dec_to_bin(number // 2) + str(number % 2)
# number = int(input('Enter number: '))
# print(dec_to_bin(number))
# -------------------------------------------------
