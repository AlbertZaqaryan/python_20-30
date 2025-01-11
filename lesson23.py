# -------------------- ex 149 -------------------------
# def head(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             for i in range(10):
#                 print(file.readline().replace('\n', ''))
#     except FileNotFoundError:
#         print('No file')
# head(input('Enter filename:  '))
# -------------------- ex 150 -------------------------
# def tail(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             mylist = file.readlines()
#         for i in range(len(mylist) - 1, len(mylist) - 10, -1):
#             print(mylist[i].replace('\n', ''))
#     except FileNotFoundError:
#         print('No File')
# tail(input('Enter filename: '))
# -------------------- ex 151 -------------------------
# def cat(src_file, dst_file):
#     try:
#         with open(src_file, 'r', encoding='utf-8') as file1:
#             text = file1.read()
#         with open(dst_file, 'a', encoding='utf-8') as file2:
#             file2.write(text)
#         return 'Success'
#     except FileNotFoundError:
#         return 'No file'
# print(cat('info.txt', 'doc.txt'))
# -------------------- ex 152 -------------------------
# def numberic_file(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             mylist = file.readlines()
#         with open(filename, 'w', encoding='utf-8') as file:
#             for i in range(0, len(mylist)):
#                 file.write(f'{i + 1}. {mylist[i]}')
#         return 'Success'
#     except FileNotFoundError:
#         return 'No file'
# print(numberic_file('info.txt'))    
# -------------------- ex 153 -------------------------
# def max_word(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             text = file.read().replace('\n', ' ').split(' ')
#         text.sort(key=len)
#         return text[-1]
#     except FileNotFoundError:
#         return "No file"
# print(max_word('doc.txt'))
# -------------------- ex 154 -------------------------
# def letter_count(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             text = file.read().replace('\n', '').replace(' ', '')
#         return {i:text.count(i) for i in text}
#     except FileNotFoundError:
#         return "No file"
# print(letter_count('doc.txt'))
# -------------------- ex 155 -------------------------
# def word_count(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             mylist = file.read().replace('\n', ' ').split(' ')
#         return {i:mylist.count(i) for i in mylist}
#     except FileNotFoundError:
#         return 'No file'
# print(word_count('doc.txt'))
# -------------------- ex 156 -------------------------
# def digit_sum(filename):
#     summ = 0
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             text = file.read()
#         for i in text:
#             if i.isdigit():
#                 summ += int(i)
#         return summ
#     except FileNotFoundError:
#         return 'No file'
# print(digit_sum('doc.txt'))
# --------------------------------------------------
# import random

# def word_count(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             mylist = file.read().replace('\n', ' ').split(' ')
#         mylist = [i for i in mylist if len(i) >= 3]
#         word1 = random.choice(mylist)
#         word2 = random.choice(mylist)
#         return word1 + word2
#     except FileNotFoundError:
#         return 'No file'
# print(word_count('doc.txt'))
# --------------------------------------------------
# element = input('Enter element: ')

# with open('elements.txt', 'r') as file:
#     mylist = file.read().replace('\n', ' ').split(' ')
# elements_dict = {}
# for i in mylist:
#     info = i.split(',')
#     elements_dict[info[2]] = int(info[0])
# print(elements_dict[element])
# --------------------------------------------------
# import os

# names_list = os.listdir('C:\\Users\\ASUS\\Desktop\\python_20-30_basic\\python_20-30\\BabyNames')
# for i in names_list:
#     with open(f'C:\\Users\\ASUS\\Desktop\\python_20-30_basic\\python_20-30\\BabyNames\\{i}', 'r') as file:
#         print(file.read())
# --------------------------------------------------
# mylist = [22, -6, 32, 82, 4, 25]
# for i in range(1, len(mylist)):
#     if mylist[i] % i == 0:
#         print(mylist[i])
# --------------------------------------------------
# mylist = ['pythonn', 'hello']
# mylist = [list(i) for i in mylist]
# newlist = []
# for i in mylist:
#     for j in i.copy():
#         if i.count(j) > 1:
#             i.remove(j)
#     newlist.append(''.join(i))
# print(newlist)
# --------------------------------------------------
mylist = [7, 4, 10, 6, 9, 8, 3, 2]
for i in range(2, len(mylist)):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(mylist[i])