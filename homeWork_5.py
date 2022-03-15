# 1. Write a function that sorts a list in ascending. Additionally, the function may take a keyword argument that will
# reverse the sort.
# Գրել ֆունկցիա, որը կվերադարձնի վերցված լիստի աճման կարգով սորտավորված տաարբերակը։ Կարող եք ավելացնել keyword արգումենտ
# որը փոփոխելով կստանանք լիստը սորտավորված նվազման կարգով։

# def sort_to_up(lst, keySortToUp=True):
#
#     new_lst = []
#     while len(lst):
#         min_number = lst[0]
#         for item in lst:
#             if item < min_number:
#                 min_number = item
#
#         new_lst.append(min_number)
#         lst.remove(min_number)
#     if keySortToUp:
#         return new_lst
#     return new_lst[::-1]
#
#
# lst_1 = [1, 0, -1, 8, 5, -1]
#
# print(sort_to_up(lst_1, keySortToUp=True))


# 2. Write a function which will take a list as an argument. If the list is monotonic, return True. Return False
# otherwise.
# Գրել ֆունկցիա, որը կվերադարձնի True, եթե տրված լիստը մոնոտոն է, և False` հակառակ դեպքում։


# def is_monoton(lst):
#     list_item = lst[0]
#     for item in lst:
#         if item < list_item:
#             return False
#         else:
#             list_item = item
#     else:
#         return True
#
# lst_1 = [1, 0, 3, 7, 9, 11]
#
# print(is_monoton(lst_1))


"""MODULES"""

# 1. Hangman!
# Create the hangman game. A list containing random words is provided. Each time the program runs, one random word must
# be selected. Then the user will try to guess the letters of the word. They will have lives equal to the length of the
# word. Now, about the formatting. Say we have the word car. The program must then output underscores equal to the
# length of the word.

# Guess a letter!
# _ _ _
#
# if we input 'a', the program will output:

# Guess a letter!
# _ a _

# and so on.

# Ստեղծում ենք մեր սեփական "Կախաղան" խաղը։ Ծրագիրը պահելու է պատահական բառ տրված "random_words" ֆայլից: Խաղացողը պետք է
# գուշակի տառ։ Եթե տառը բառի մեջ գոյություն չունի, խաղացողը կորցնում է "կյանք" (կյանքերը բառի երկարության չափ են): Եթե
# տառը կա, այն բացվում է և խաղացողը անցնում է հաջորդ տառը գուշակելուն։ Ծրագրի աշխատանքը պետք է հետևյալ տեսքն ունենա։
# Ենթադրենք բառը car է։ Կոնսոլում հետևյալ տեսքստն ենք տեսնելու

# Guess a letter!
# _ _ _

# Եթե ներմուծենք a, կստանանք հետևյալ տեսքստը

# Guess a letter!
# _ a _

# և այդպես շարունակ։ Եթե խաղացողի կյանքերը սպառվեն, տեղեկացրեք նրան և խաղից դուրս եկեք։ Հաղթելու դեպքում տպեք
# շնորհավորանք

# import random

# text_file = open('random_words.txt', 'r')
#
# text_list = text_file.readlines()
#
# text_file.close()
#
# text_list_length = len(text_list)
#
# number_random = random.randint(0, text_list_length - 1)
#
# text_random = text_list[number_random][:-1]
#
# print(text_random)
#
# text_random_length = len(text_random)
#
# correct_text_list = ['-' for i in range(text_random_length)]
#
#
# while text_random_length > 0:
#     correct_text = ' '.join(correct_text_list)
#     print(correct_text)
#     letter = input('please enter a letter.. ')
#     if letter in text_random:
#         print('you write the letter correctly')
#         for i in range(len(text_random)):
#             if text_random[i] == letter:
#                 correct_text_list[i] = letter
#         if '-' not in ''.join(correct_text_list):
#             break
#     else:
#         print('you write the letter do not correctly')
#         text_random_length -= 1
#
# print(f'your correctly word is {" ".join(text_random)}')
#
# if text_random_length < 0 :
#     print('you are lose game :(')
# else:
#     print('congratulation!!!! you are winning the game :)')


# 2. Write a function that will return the longest word in the random words file from the previous exercise.
# Գրել ֆունկցիա, որը կվերադարձնի "random_words" ֆայլի ամենաերկար բառը։

# file = open('random_words.txt', 'r')
#
# word_list = file.readlines()
#
# file.close()
#
# word_length = 0
#
# for item in word_list:
#     if len(item[:-1]) > word_length:
#         word = item[:-1]
#         word_length = len(item[:-1])
#
# print(f'The longest word is {word}')


# 3. Write a function that will take a string containing the path to a file as an argument and return its size in
# kilobytes.
# Գրել ֆունկցիա, որը կվերցնի սթրինգ արգումենտ։ Սթրինգը պետք է լինի որոշակի ֆայլի path-ը։ Ապա վերադարձնել այդ ֆայլի
# չափսերը կիլոբայթերով։ Հուշում՝ օգտվել os մոդուլից:

# import os

# first version with string ***start***

# def size_file_kb(path, kilobyte=True):
#
#     str_path = str(os.stat(path))

#     index_str_path_size = str_path.index('st_size')
#     str_path = str_path[index_str_path_size + 8:]
#     index_str_path_size = str_path.index(',')
#     str_path = str_path[:index_str_path_size]
#     size_kb = int(str_path)

#     if kilobyte:
#         size_kb = size_kb / 1000
#     return size_kb
#
# print(size_file_kb('random_words.txt', kilobyte=True))

# first version with string ***end***

# first version with list ***start***

# def size_file_kb(path, kilobyte=True):
#
#     str_path = list(os.stat(path))
#
#     size_kb = str_path[6]
#     if kilobyte:
#         size_kb = size_kb / 1000
#     return size_kb
#
# print(size_file_kb('random_words.txt', kilobyte=True))

# first version with list ***end***


# 4. Create a random number generator without using random module. The implementation is up to you. You may use
# current timestamp as a random seed.
# Գրել ֆունկցիա, որը կվերադարձնի պատահական թիվ։ Պատահական թվերի գեներատոր պարունակող մոդուլ չօգտագործել։ Իմպլեմենտացիան
# կախված է ձեզնից։ Մտածեք որոշակի ալգորիթմ և ըստ դրա գեներացրեք թիվ։ Կարող եք օգտագործել մեր անցած seed-ի գաղափարը։

# from time import time
#
# def generat_random_number(numbers_digits):
#     """
#         numbers_digits number of digits to generate
#         you can give numbers 0 to 6 [0; 6]
#     """
#     if numbers_digits < 0 or numbers_digits > 6:
#         numbers_digits = 6
#
#
#     numbers_random = time() / 3
#     str_random = str(numbers_random)
#     str_random_index = str_random.index('.')
#     str_random = str_random[str_random_index + 1:str_random_index + 1 + numbers_digits]
#
#     return int(str_random)
#
#
# print(generat_random_number(3))



# 5. Create a file and put your shopping list in it. The file must start with current day's date.
# Ստեղծել ֆայլ, որը կպահի ձեր գնումների ցուցակը (ինչ ապրանք։ քանի հատ)։ Ֆայլը պետք է սկսվի տվյալ օրվա ամսաթվով։

# import datetime
#
# today = str(datetime.date.today())
#
# shopping_list = {'apple': 30, 'banana': 15, 'bread': 15}
#
# file = open('shoppin_list.txt', 'w')
#
# file.write(today)
# file.write('\n' * 3)
#
# for keys, value in shopping_list.items():
#     file.write(f'{keys}-------{value}\n')
#
# file.close()



# 6. Create a function that will take two datetime objects as parameters and return the difference in days between
# these dates.
# Գրել ֆունկիա, որը կվերցնի երկու datetime տիպի պարամետրեր և կվերադարձնի այդ ամսաթվերի միջև տարբերությունը օրերով։
# import datetime
#
#
# def difference_between_days(date_time1, date_time2):
#     days = abs(date_time1 - date_time2)
#     return days
#
#
# def enter_day():
#     year = int(input('please enter the year  '))
#     month = int(input('please enter the month  '))
#     day = int(input('please enter the day  '))
#
#     return datetime.datetime(year, month, day)
#
# date1 = enter_day()
# date2 = enter_day()
#
# print(difference_between_days(date1, date2).days)


