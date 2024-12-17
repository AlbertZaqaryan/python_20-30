# -------------------------------------------------
# s = 'a,2,b,5,c,8,a,4,e,11'
# s = s.split(',')
# dict_ = {}
# for i in range(0, len(s), 2):
#     if s[i] in dict_:
#         dict_[s[i]] += int(s[i + 1])
#     else:
#         dict_[s[i]] = int(s[i + 1])
# print(dict_)
# -------------------------------------------------
# text = input('Enter text: ')
# dict_ = {}
# for i in text:
#     dict_[i] = text.count(i)
# print(dict_)
# -------------------------------------------------
# text = input('Enter text: ')
# print({i:text.count(i) for i in text})
# -------------------------------------------------
# import random

# dict_ = {
#     2:0,
#     3:0,
#     4:0,
#     5:0,
#     6:0,
#     7:0,
#     8:0,
#     9:0,
#     10:0,
#     11:0,
#     12:0
# }
# for i in range(1000):
#     z1 = random.randint(1, 6)
#     z2 = random.randint(1, 6)
#     dict_[z1 + z2] += 1
# print('------------')
# for i in dict_:
#     print(f'|{i:>2} | {round(dict_[i] * 100 / 1000, 2):>4} |')
#     print('------------')
# -------------------------------------------------
# morse_code = {
#     'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',     'F': '..-.', 
#     'G': '--.',   'H': '....',  'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..', 
#     'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',  'Q': '--.-',  'R': '.-.',  
#     'S': '...',   'T': '-',     'U': '..-',   'V': '...-', 'W': '.--',   'X': '-..-', 
#     'Y': '-.--',  'Z': '--..', 

#     '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
#     '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ':' ',
# }

# text = input('Enter text:   ').upper()
# for i in text:
#     print(morse_code[i], end='')
# -------------------------------------------------
# text = 'Hello, World!'
# print(len({i:0 for i in text}))
# -------------------------------------------------
# text1 = 'live'
# text2 = 'veill'
# dict1 = {i:text1.count(i) for i in text1}
# dict2 = {i:text2.count(i) for i in text2}
# print(dict1 == dict2)
# -------------------------------------------------
# text1 = 'I am a weakish speller'.lower().replace(' ', '')
# text2 = 'William Shakespeare'.lower().replace(' ', '')
# dict1 = {i:text1.count(i) for i in text1}
# dict2 = {i:text2.count(i) for i in text2}
# print(dict1 == dict2)
# -------------------------------------------------
# dict_ = {'a':2}
# print(dict_.pop(4, 9))

# list1 = [1, 2, 3]
# list2 = [7, 4, 5]
# print(list1 > list2)