# file = open('info.txt', 'r')
# print(file.read())
# -------------------------------------------------------
# file = open('../../information.txt', 'r') # relative path
# print(file.read())
# -------------------------------------------------------
# PATH = "C:\\Users\\ASUS\\Desktop\\information.txt" # absolute path
# file = open(PATH, 'r')
# print(file.read())
# -------------------------------------------------------
# file = open('info.txt', 'r')
# print(file.read())

# file.close()
# -------------------------------------------------------
# def open_file():
#     with open('info.txt', 'r') as file:
#         print(file.read())

# open_file()
# ------------------
# | r -> kardal     |
# | w -> jnjel grel |
# | a -> avelacnel  |
# ------------------
# -------------------------------------------------------
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# -------------------------------------------------------
# try:
#     x = int(input('Enter number1: '))
#     y = int(input('Enter number2: '))
#     print(x / y)
# except ValueError:
#     print('Enter only numbers')
# except ZeroDivisionError:
#     print('Cannot divide by zero')
# -------------------------------------------------------
# def read_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             return file.read()
#     except FileNotFoundError:
#         return "No File"
# myfile = input('Enter filename: ')
# print(read_file(myfile))
# -------------------------------------------------------
# file = open('info.txt', 'r')
# print(file.read())
# file.close()


# with open('info.txt', 'r') as file:
#     print(file.read())
# -------------------------------------------------------
# with open('info.txt', 'r') as file:
#     print(file.readlines())
# -------------------------------------------------------
# with open('info.txt', 'r') as file:
#     print(file.read().split('\n'))
# -------------------------------------------------------
# with open('lesson.csv', 'r') as file:
#     print(file.read())
# -------------------------------------------------------
# with open('info.txt', 'r') as file:
#     mylist = file.read().split('\n')
# for i in mylist.copy():
#     if i[0] == 'b':
#         mylist.remove(i)
# with open('info.txt', 'w') as file:
#     for i in mylist:
#         file.write(f'{i}\n')
# -------------------------------------------------------
# def delete_sharps(filename):
#     try:
#         with open(filename, 'r') as file:
#             res = file.readlines()
#         for i in res.copy():
#             if i[0] == '#':
#                 res.remove(i)
#         with open(filename, 'w') as file:
#             for i in res:
#                 file.write(i)
#         return "Success"
#     except FileNotFoundError:
#         return "No File"
# print(delete_sharps('info.txt'))
# -------------------------------------------------------
# def head(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             for i in range(5):
#                 print(file.readline().replace('\n', ''))
#     except FileNotFoundError:
#         print("No File")
# head('info.txt')
# -------------------------------------------------------
# def max_word(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             mylist = file.read().replace('\n', ' ').split(' ')
#         mylist.sort(key=len)
#         return mylist[-1]
#     except FileNotFoundError:
#         return "No File"
# print(max_word('info.txt'))
# -------------------------------------------------------
def max_letter_count(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().replace('\n', ' ').replace(' ', '')
        dict_ = {i:text.count(i) for i in text}
        return sorted(dict_, key=dict_.get)[-1]
    except FileNotFoundError:
        return "No File"
print(max_letter_count('info.txt'))
# -------------------------------------------------------
# text = 'HSKAHSASJKAHSasjkahjska'
# print(list(text))
# -------------------------------------------------------
summ = 0
with open('info.txt', 'r', encoding='utf-8') as file:
    text = file.read()
for i in text:
    if i.isdigit():
        summ += int(i)
print(summ)
# -------------------------------------------------------
