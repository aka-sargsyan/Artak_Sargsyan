"""FUNCTIONS"""

# 1. We'll say that an element in an array is "alone" if there are values before and after it, and those values are
# different from it. Return a version of the given array where every instance of the given value which is alone is
# replaced by whichever value to its left or right is larger.
# Ենթադրենք տարրը "միայնակ" է, եթե նրանից առաջ կամ հետո գտնվող տարրերի արժեքը տարբերվում է իր արժեքից։ Ստեղծել ֆունկցիա,
# որը կվերցնի լիստ որպես արգումենտ և կվերադարձնի այդ լիստը ձևափոխված այնպես, որ բոլոր միայնակ տարրերը փոխարինված լինեն
# իրենցից աջ կամ ձախ գտնվող առավելագույն արժեք ունեցող տարրով ([4, 4, 1, 3, 3], այստեղ 1-ը կփոխարինվի 4-ով):

# current_lst = [2, 1, 1, 2, 3, 3, 1, 5]
# new_list = current_lst.copy()


# def change_list(lst):
# length = len(lst)

# for index, value in enumerate(lst):
#     if index == 0 or index == length - 1:
#         continue
#     elif lst[index] != lst[index + 1] and lst[index] != lst[index - 1]:
#         lst[index] = max(lst[index - 1], lst[index + 1])
# return lst

# def change_list(lst):
#     length = len(lst)
#
#     for i in range(2, length - 1):
#         if lst[i] != lst[i + 1] and lst[i] != lst[i - 1]:
#             lst[i] = max(lst[i - 1], lst[i + 1])
#
#     return lst
#
#
# print(current_lst, 'list cheang is to')
# print(change_list(new_list), 'list')

# 2. Write a function to create and print a list where the values are square of numbers between 1 and 30
# (both included).
# Ստեղծել ֆունկցիա, որը կստեղծի և կտպի լիստ, որի արժեքները [1, 30] միջակայքում գտնվող թվերի քառակուսիներն են։

# def square_number_list(lst):
#     new_list = []
#     for item in lst:
#         new_list.append(item ** 2)
#     return new_list
#
#
# current_list = [i for i in range(1, 31)]
#
# print(current_list, 'list change is to square of list')
# print(square_number_list(current_list))

# 3. Write a function which will take one argument n. Return a list of size n, that will contain random numbers
# from (-100, 400).
# Ստեղծել ֆունկցիա, որը կվերցնի մեկ արգումենտ՝ n: Վերադարձնել n երկարությամբ լիստ, որը կպարունակի (-100, 400)
# միջակայքում գտնվող պատահական թվեր։

# import random
#
#
# def new_list_random(count_length):
#     list_random = []
#     for i in range(count_length):
#         list_random.append(random.randint(-100, 400))
#     return list_random
#
#
# n = int(input('please enter a number length of list  '))
#
# print(new_list_random(n))
# print(new_list_random(n))

# 4. Write a function, that will take a list of words as an argument and return all the words in the list that start
# with a vowel.
# Ստեղծել ֆունկցիա, որը կվերցնի լիստ որպես արգումենտ (սթրինգերի) և կվերադարձնի մեկ այլ լիստ, որը կպարունակի այդ լիստի
# բոլոր այն բառերը, որոնք սկվում են ձայնավորով։

poem = '''All that is gold does not glitter,
Not all those who wander are lost;
The old that is strong does not wither,
Deep roots are not reached by the frost.

From the ashes a fire shall be woken,
A light from the shadows shall spring;
Renewed shall be blade that was broken,
The crownless again shall be king.'''


# def vowel_list(text):
#     new_list = []
#     lst = text.split()
#     for item in lst:
#         if len(item) > 1 and item not in 'an':
#             if item[0].lower() in ['a', 'e', 'i', 'o', 'u']:
#                 new_list.append(item)
#     return new_list
#
#
# print(vowel_list(poem))


# 5. We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
# Write a function to return the number of small bars to use, assuming we always use big bars before small bars. Return
# -1 if it can't be done.
# Մենք ուզում ենք պատրաստել որոշակի x կշռով շոկոլադ։ Ունենք փոքր և մեծ շոկոլադե սալիկներ, որոնք համապատասխանաբար
# կշռում են 1 և 5 կգ։ x կգ շոկոլադը պատրաստելու համար առաջինը օգտագործելու ենք մեծ սալիկները, ապա փոքր։ Սալիկները
# կտրատել հնարավոր չէ։ Գրել ֆունկցիա, որը կվերադարձնի անհրաժեշտ փոքր սալիկների քանակը։ Եթե հնարավոր չէ տրված սալիկների
# քանակով պատրաստել անհրաժեշտ շոկոլադը՝ վերադարձնել -1։
# Ֆւնկցիայի սահմանումն ունի հետևյալ տեսքը, որտեղ small, big -> հասանելի փոքր և մեծ սալիկների քանակը, իսկ goal-ը
# վերոնշյալ x-ն է։

# Ֆունկցիան հետևյալ տեսքն ունի

# def make_chocolate(small, big, goal):

    # rem = 0
    # if goal >= big * 5:
    #     rem = goal - big * 5
    # else:
    #     rem = goal % 5
    # if rem <= small:
    #     return rem
    # return -1

#     if small + 5 * big >= goal and goal % 5 <= small:
#         if goal // 5 >= big:
#             return goal - big * 5
#         else:
#             return goal % 5
#     return -1
#
# print(make_chocolate(3, 2, 9))   #-> -1
# print(make_chocolate(3, 2, 8))   #-> 3
# print(make_chocolate(13, 2, 12)) #-> 2
# print(make_chocolate(13, 1, 12)) #-> 7


# def make_chocolate(small, big, goal):
#     small *= 1000
#     big *= 1000
#     goal *= 1000
#     if goal > small:
#         return -1
#     elif big // goal == big / goal and small // goal == small / goal:
#         return big / goal + small / goal
#     else:
#         return -1

    #  can it work in this version

    # if big // goal == big / goal and small // goal == small / goal:
    #     return big / goal + small / goal
    # else:
    #     return -1


# 6. Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other
# is "far", differing from both other values by 2 or more. Return False otherwise.
# Գրել ֆունկցիա, որը կվերցնի երեք ամբողջ թիվ որպես արգումենտ։ Վերադարձնել True, եթե b-ն կամ c-ն իրենց արժեքով
# տարբերվում են a-ից առավելագույնը 1-ով, երբ միաժամանակ մյուս երկուսը տարբերվում են իրարից 2-ով։ Հակառակ դեպքում
# վերադարձնել False։

# def check_numbers(a, b, c):
#     if abs(b - a) <= 1 or abs(c - a) <= 1:
#         if abs(a - b) == 2 or abs(b - c) == 2 or abs(a - c) == 2:
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# print(check_numbers(5, 6, 7))

# 7. Write a function that gets a numerical list as an argument. Find the sum of the elements. If a certain element is
# 13 stop the count and return whatever was the sum before that.
# Ստեղծել ֆունկցիա, որը կգումարի տրված լիստի բոլոր թվերը և կվերադարձնի այն։ Եթե տարրերից մեկը 13 է, դադարեցնել հաշվարկը
# և վերադարձնել մինչև այդ պահը հաշված գումարը։

# def sum_list(lst, number):
#     total = 0
#     for item in lst:
#         if item != number:
#             total += item
#         else:
#             return total
#     return total
#
#
# current_lst = [1, 5, 6, 78, 13, 25]
# print(sum_list(current_lst, 13))

# 8. Write down the following functions in a lambda form
# Գրել հետևյալ ֆունկցիաների լամբդա տարբերակները


# def square(x):
#     return x ** 2
#
#
# def circle_area(r, pi=3.14):
#     return pi * r ** 2
#
#
# def sum_to_power(x, y, p):
#     return (x + y) ** p


# square = lambda x: x ** 2
#
# circle_area = lambda r, pi=3.14: pi * r * 2
#
# sum_to_power = lambda x, y, p: (x + y) ** p
#
# print(sum_to_power(10, 5, 6))

# 9. Create a list from 1-100. Using the filter function, return a new list containing only the numbers ending with 7.
# Ստեղծել 1-100 թվերը պարունակող լիստ։ Օգտագործելով ֆիլտր ֆունկցիան, վերադարձնել նոր լիստ, որը կպարունակի օրիգինալի
# միայն այն թվերը, որոնք վերջանում են 7-ով

# def is_numbers_end(n):
#     if n % 10 == 7:
#         return True
#     else:
#         return False


# lst = [i for i in range(1, 101)]
#
# new_list = filter(is_numbers_end, lst)

# new_list = filter(lambda n: n % 10 == 7, lst)
#
# print(lst)
# print(list(new_list))


# 10. Create a function that will take a string as an argument. Return a new string which is the original string with
# each letter doubled. For example 'cat' will become 'ccaatt'
# Ստեղծել ֆունկցիա, որը կվերցնի սթրինգ։ Վերադարձնել սթրինգ, որը կլինի օրիգինալ սթրինգը, սակայն ամեն տառ կլինի
# կրկնապատկված։ Օրինակ cat—ը կվերադարձնի 'ccaatt'

# def change_text(text):
#     new_text = ''
#     for item in text:
#         new_text += item * 2
#     return new_text
#
#
# current_text = 'cat'
#
# current_text = change_text(current_text)
#
# print(current_text)


# lst = [1, 0, -1, 8, -1]


# sort funtion
# print('hello')
# lst = [1, 0, -1, 8, -1]
# new_lst = []
# while len(lst):
#     min_number = lst[0]
#     for item in lst:
#         if item < min_number:
#             min_number = item
#
#     new_lst.append(min_number)
#     lst.remove(min_number)
#
#
# print(new_lst)



