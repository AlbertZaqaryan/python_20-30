# dict_ = {'a':10, 'b':60}
# for i in dict_:
#     if i == 'b':
#         print(i, dict_[i])
# ----------------------------------------

# dict_ = {'a':10, 'b':60}
# key = input('Enter key: ')
# print(dict_.get(key, 'Chka'))
# ----------------------------------------

# mylist = [7, 4, 5, 6, 9, 8]
# print(sum(mylist) / len(mylist))
# ----------------------------------------

# for i in range(10):
#     print('Python team')
# ----------------------------------------


# dict_ = {"a":10, "b":20}
# new_dict_ = {}
# for i in dict_:
#     new_dict_[dict_[i]] = i
# print(new_dict_)
# ----------------------------------------


# dict_ = {'a':2, 'b':2, 'c':3}
# {2:['a', 'b'], 3:['c']}
# new_dict = {}
# for i in dict_:
#     if dict_[i] in new_dict:
#         new_dict[dict_[i]].append(i)
#     else:
#         new_dict[dict_[i]] = [i]

# print(new_dict)
# ----------------------------------------

# text = 'hello'
# dict_ = {}
# for i in text:
#     if i in dict_:
#         dict_[i] += 1
#     else:
#         dict_[i] = 1
# print(dict_)
# ----------------------------------------

# mylist = [180, -1, 160, 150, -1, -1, 170, 190]
# newlist = [i for i in mylist if i != -1]
# newlist.sort()
# i = 0
# j = 0
# while i < len(mylist):
#     if mylist[i] == -1:
#         i += 1
#     else:
#         mylist[i] = newlist[j]
#         i += 1
#         j += 1
# print(mylist)
# ----------------------------------------
# mylist = [50, 60, 100, 110, 150]
# number1 = 0
# number2 = 0
# for i in range(len(mylist)):
#     if i % 2 == 0:
#         number1 += mylist[i]
#     else:
#         number2 += mylist[i]
# print([number1, number2])
# ----------------------------------------
# mylist = [7, 4, 5, 9, 1, 3, 6, 7]
# print(max([mylist[i] * mylist[i + 1] for i in range(len(mylist) - 1)]))
# ----------------------------------------
