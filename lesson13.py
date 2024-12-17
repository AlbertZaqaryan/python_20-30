# x = 7.646546
# print(round(x, 3))
# print('%.3f' % x)
# ---------------------------------------------------

# fb = {
#     "test@gmail.com":"sgaksakshkasa",
#     "sakjskja@mail.ru":"sjahjksajk",
# }
# ---------------------------------------------------

# {Key:Value}
# ---------------------------------------------------

# dict_ = {
#     'a':[1, 2, 3]
# }
# ---------------------------------------------------


# info = {
#     "11AA111":{"soc":45646656, "prava":"EH464654645", "heraxos":6465456645},
#     "11AA111":{"soc":45646656, "prava":"EH464654645", "heraxos":6465456645},
#     "11AA111":{"soc":45646656, "prava":"EH464654645", "heraxos":6465456645},
#     "11AA111":{"soc":45646656, "prava":"EH464654645", "heraxos":6465456645},
#     "11AA111":{"soc":45646656, "prava":"EH464654645", "heraxos":6465456645},
# }
# ---------------------------------------------------

# test = {
#     'a':8,
#     'b':4,
#     'c':33,
# }
# print(test.keys())
# print(test.values())
# print(test.items())
# ---------------------------------------------------

# x = [('a', 8), ('b', 4), ('c', 33)]
# print(dict(x))
# ---------------------------------------------------

# test = {
#     'a':8,
#     'b':4,
#     'c':33,
# }

# test['e'] = 96
# test.setdefault('e', 96)

# test.clear()
# print(test)
# test.popitem()
# print(test)

# test.pop('a')
# print(test)

# del test['a']
# print(test)

# print(test['a'])
# print(test['Ճ'])
# print(test.get('a'))
# print(test.get('Ճ', 'ՉԿԱ'))
# print(test.get('a', 'ՉԿԱ'))
# test['e'] = 22
# test['a'] = 6
# print(test)
# ---------------------------------------------------



# test1 = {
#     'a':8,
#     'b':4,
#     'c':33,
# }
# test2 = test1.copy()
# test2 = dict(test1)
# test2['e'] = 22
# print(test1)
# ---------------------------------------------------


# dict1 = {'a':1, 'b':3}
# dict2 = {'e':11}
# dict1.update(dict2)
# print(dict1)
# ---------------------------------------------------

# dict_ = {
#     'a':1,
#     2:'b'
# }
# ---------------------------------------------------

# mydict = {'a':1,'b':2,'c':12}
# x = 1
# for i in mydict:
#     x *= mydict[i]
# print(x)
# ---------------------------------------------------

# mydict = {'a':1,'b':2,'c':12}
# for i in mydict:
#     print(mydict[i])
# ---------------------------------------------------

# dict_ = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# keys = sorted(dict_)
# print(keys)
# values = sorted(dict_.values())
# print(values)
# ---------------------------------------------------


# dict_ = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# keys = sorted(dict_, key=dict_.get, reverse=True)[:3]
# newdict = {}
# for i in keys:
#     newdict[i] = dict_[i]
# print(newdict)
# ---------------------------------------------------

# dict_ = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# print({i:dict_[i] for i in sorted(dict_, key=dict_.get, reverse=True)[:3]})
# ---------------------------------------------------


# students = {
#     "Arman":7,
#     "Karen":4,
#     "Hakob":10,
#     "Vardan":5,
#     "Sergo":6,
#     "Gor":8
# }
# good = []
# bad = []
# good = {}
# bad = {}
# summ = 0
# for i in students:
#     summ += students[i]
# mean = round(summ / len(students), 2)
# for i in students:
#     if students[i] >= mean:
#         good[i] = students[i]
#     else:
#         bad[i] = students[i]
# print(good)
# print(bad)
# ---------------------------------------------------
# phone = {
#     '1':'.,?!:',
#     '2':'ABC',
#     '3':'DEF',
#     '4':'GHI',
#     '5':'JKL',
#     '6':'MNO',
#     '7':'PQRS',
#     '8':'TUV',
#     '9':'WXYZ',
#     '0':' '
# }
# text = input('Enter text: ').upper()
# for i in text:
#     for j in phone:
#         if i in phone[j]:
#             print(j * (phone[j].index(i) + 1), end='')
# ---------------------------------------------------
# dict_ = {
#     1 :'AEILNORSTU',
#     2 :'DG',
#     3 :'BCMP',
#     4 :'FHVWY',
#     5 :'K',
#     8 :'JX',
#     10:'QZ',
# }
# name = input('Enter name: ').upper()
# summ = 0
# for i in name:
#     for j in dict_:
#         if i in dict_[j]:
#             summ += j
# print(summ)
# ---------------------------------------------------
# s = 'a,2,b,5,c,8,a,4,e,11'
# {'a':6, 'b':5, 'c':8, 'e':11}