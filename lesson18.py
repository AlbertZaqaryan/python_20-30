# def reverse_calendar(year, day):
#     day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if year % 4 == 0:
#         day_list[1] = 29
#     month = 0
#     while day_list[month] < day:
#         day -= day_list[month]
#         month += 1
#     month += 1
#     return f'{year}:{month}:{day}'
# print(reverse_calendar(2024, 248))

# def func(a):
    
#     return a

# print(func(9))
# print(func.__doc__)

# x = 5
# y = 5
# print(id(x))
# print(id(y))




# def gumar(a, b, c):return a + b + c
# print(gumar(5, 4, 3))

# x = lambda a, b, c: a + b + c
# print(x(7, 5, 6))

# x = lambda number: "Even" if number % 2 == 0 else "Odd"
# number = int(input('Enter number: '))
# print(x(number))


# def magic_date(day, month, year):
#     month_dict = {
#         'hunvar':1,
#         'petrvar':2,
#         'mart':3,
#         'april':4,
#         'mayis':5,
#         'hunis':6,
#         'hulis':7,
#         'ogostos':8,
#         'september':9,
#         'hoktember':10,
#         'noyember':11,
#         'dektember':12,
#     }
#     return day * month_dict[month] == year % 100
# print(magic_date(10, 'ogostos', 1980))

