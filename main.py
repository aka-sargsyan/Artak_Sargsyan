"""DATA STRUCTURES"""

# 1. Write a program to multiply all the items in a list.
# Գրել ծրագիր, որը կբազմապատկի լիստի բոլոր թվերը։

# n = int(input('please enter the length of the list  '))
# new_list = []
# for i in range(n):
#     new_list.append(int(input(f'please enter list of {i} element  ')))
# print('my list is  ', new_list)
# multiply_list = 1
# for i in range(n):
#     multiply_list *= new_list[i]
# print('multiply all the items in the list is', multiply_list)

# 2. Write a program to count the number of strings where the string length is 2 or more and the first and last
# character are same from a given list of strings.
# Գրել ծրագիր, որը կհաշվի լիստում եղած 2 կամ ավել երկարություն ունեցող լիստերի քանակը, որոնց առաջին և վերջին տառերը
# նույնն են։

# n = int(input('please enter the length of the list  '))

# text_list = []
# for i in range(n):
#     text_list.append(input(f'please enter a string, {i} element  '))
#     total = 0
# for i in range(n):
#     if len(text_list[i]) >= 2 and text_list[i][0] == text_list[i][-1]:
#         total += 1
#     # or this version //start//
#     # if len(text_list[i]) >= 2:
#     #     if text_list[i][0] == text_list[i][-1]:
#     #         total += 1
#     # //end//
# print('count the number of strings where the string length is 2 and the first and last character are same', total)

# 3. Write a program that will remove duplicates from a list. DO NOT use set() method directly on the list.
# Գրել ծրագիր, որը կջնջի դուպլիկատները լիստից։ ՉՕԳՏԱԳՈՐԾԵԼ set() մեթոդը։

# n = int(input('please enter the length of the list  '))
# text_list = []
# new_text_list = []
# for i in range(n):
#     text_list.append(input(f'please enter a string, {i} element  '))
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if text_list[i] == text_list[j]:
#             text_list[j] = ''
# for i in range(n):
#     if text_list[i] == '':
#         text_list.pop(i)
# print(text_list)

# seconde version

# n = int(input('please enter the length of the list  '))
# text_list = []
# new_text_list = []
# for i in range(n):
#     text_list.append(input(f'please enter a string, {i} element  '))
# for i in text_list:
#     if i not in new_text_list:
#         print('i', i)
#         print(i not in new_text_list)
#         new_text_list.append(i)
# print(new_text_list)


# 4. Create a list from 5 user inputs.
# Ստեղծել լիստ 5 ներմուծված թվերից

# count_list = int(input('please enter the count of the list  '))
# new_list = []
# for i in range(count_list):
#     new_list.append(input('please enter element of the list  '))
# print(new_list)

# 5. Given a list of ints, print True if the array contains a 2 next to a 2 somewhere.
# Գրել ծրագիր, որը կտպի True, եթե տրված լիստում ինչ-որ տեղ 2 թվին 2 է հաջորդում։

# count_list = int(input('please enter the count of the list  '))
#
# new_list = []
# for i in range(count_list):
#     new_list.append(int(input('please enter element of the list  ')))
#
# for i in range(1, count_list):
#     if new_list[i - 1] == 2 and new_list[i] == 2:
#         print(True)
#         break
# else:
#     print(False)

# 6. Given a list of ints, print True if every element is a 1 or a 4, and False otherwise.
# Գրել ծրագիր, որը կտպի True, եթե լիստի բոլոր էլեմենտները 1 կամ 4 են։ Հակառակ դեպքում տպել False:

# count_list = int(input('please enter the count of the list  '))
#
# new_list = []
# for i in range(count_list):
#     new_list.append(int(input('please enter element of the list  ')))
#
# for i in new_list:
#     if i != 1 and i != 4:
#         print(False)
#         break
# else:
#     print(True)

# secone version

# count_list = int(input('please enter the count of the list  '))
#
# new_list = []
# for i in range(count_list):
#     new_list.append(int(input('please enter element of the list  ')))
#
# for i in new_list:
#     if i not in [1, 4]:
#         print(False)
#         break
# else:
#     print(True)


# 7. Ask for user input and add that input as a key into the dictionary. If the key exists, warn the user about it and
# do nothing. Assign some arbitrary value to it.
# Պահանջել ներմուծել բանալի և ավելացնել այդ բանալին dictionary-ի։ Եթե այն արդեն գոյություն ունի, տպել, որ բանալին արդեն
# կա և ոչինչ չանել։ Որպես արժեք տեղադրել պատահական օբյեկտ

# count_dictionary = int(input('enter count of dictionary  '))
#
# new_dictionary = {}
#
# for i in range(count_dictionary):
#     new_dictionary.update({input('please enter a key  '): input('please enter a value  ')})
#
# new_key = input('pleas enter new key ')
# for i in new_dictionary.keys():
#     if i == new_key:
#         print('there are same key ')
#         break
# else:
#     new_dictionary.update({new_key: ''})
#
# print(new_dictionary)


# 8. Loop through the values of a dictionary and add them to a new list.
# Ցիկլի միջոցով ավելացնել dictionary—ի արժեքները նոր լիստի մեջ։

# count_list = int(input('please enter count of list  '))
#
# list_of_dictionary = []
#
# for i in range(count_list):
#     list_of_dictionary.append({input('please enter a key  '): input('please enter a value  ')})
#
# print(list_of_dictionary)

# 9. Write a script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys.
# Գրել ծրագիր, որը կստեղծի և կտպի dictionary, որի բանալիները [1,15] թվերն են, իսկ արժեքները դրանց քառակուսիները։

# new_dictionary = {}
# for i in range(1, 16):
#     new_dictionary.update({i: i ** 2})
# print(new_dictionary)


"""LOOPS"""

# 1. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a nested loop.
# Օգտագործելով ցիկլեր, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։

# k = 0
# new_list = []
# for i in range(3):
#     new_list.append([])
#     for j in range(3):
#         k += 1
#         new_list[i].append(k ** 2)
# print(new_list)
#
# # second version
#
# new_list = []
# for i in range(1, 10):
#     if i % 3 == 1:
#         new_list.append([])
#     new_list[-1].append(i ** 2)
# print(new_list)

# third version

# new_list = []
# for i in range(0, 3):
#     new_list.append([])
#     for j in range(0, 3):
#         new_list[i].append((j + 3 * i + 1) ** 2)
# print(new_list)

# # 2. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a list comprehension.
# # Օգտագործելով comprehension, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։

# new_list = [[(j + 3 * i + 1) ** 2 for j in range(3)] for i in range(3)]
# print(new_list)

# 3. Count the number of 'b's in the given string. DO NOT use the count() method.
# Հաշվել տրված սթրինգում 'b'-երի քանակը։ Չօգտագործել count() մեթոդը։

# text = input('please enter a string ')
#
# total = 0
# for i in text:
#     if i == 'b':
#         total += 1
# print('count b of the text is', total)


# 4. Write a program that will print the factorial of n.
# Գրել ծրագիր, որը կտպի n թվի ֆակտորիալը։

# n = int(input('please enter a number' ))
# factorial = 1
# for i in range(1, n):
#     factorial *= i
# print(f'factorial {n} is', factorial)

# 5. Write a Python program to construct the following pattern, using a nested for loop.
# Գրել ծրագիր, որը կտպի հետևյալ պատկերը։

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(1, 10):
#     if i <= 5:
#         print('* ' * i)
#     else:
#         print('* ' * (10 - i))

# i = 1
# while i < 10:
#     if i <= 5:
#         print('* ' * i)
#     else:
#         print('* ' * (10 - i))
#     i += 1
# fibonachi

# count_fib = int(input('please enter a count of fibonachi  '))
# fib = [0, 1]
# for i in range(0, count_fib - 2):
#     fib.append(fib[-1] + fib[-2])
# print(fib)
