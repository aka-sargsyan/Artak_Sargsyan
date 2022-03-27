""" Dunder methods and exceptions """
import random

""" Ուշադրությու՛ն։ Ցանկացած տեղ, եթե ցանկանում եք exception raise անել, ստեղծեք ձեր սեփական exception կլասերը և
 աշխատեք դրանց հետ։ """

# 1. Create a Color class. This will hold 3 instance variables, red, green, blue (RGB - info on this here:
# https://en.wikipedia.org/wiki/RGB_color_model).
# We want to be able to get new colors if we add instances of the color class. I'm not sure how much sense it will make
# to also subtract the colors, but lets do it for fun! In summary, we can add 2 or more colors and get a new color
# object with added RGB values (don't forget about the boundaries!), subtract them to get a new color object with
# subtracted values. When printed, we want to have a nice representation of our color (maybe even the color itself?).
# One more fun thing!
# Optional - As colors are quite often represented in hexadecimals, lets override the corresponding function
# such that when hex() is called on our class, we get the hex color code for our color.
# Ստեղծել Color կլաս։ Այն կունենա երեք instance ատրիբուտ՝ red, green, blue (ըստ RGB գունային մոդելի։ Վերջինիս մասին
# ավելի մանրամասն տեսեք այստեղ https://en.wikipedia.org/wiki/RGB_color_model): Մենք պետք է կարողանանք գումարել երկու
# Color տիպի օբյեկտ և ստանանք նոր Color, որի RGB արժեքները կլինեն օպերանդների համապատասխան արժեքների գումարները։
# Սահմանեք նաև տարբերության օպերատորը, որը կանի հակառակ գործողությունը (ուշադիր եղեք սահմաններին։ RGB արժեքները
# գտնվում են (0, 255) տիրույթում): Հավելյալ, մենք ուզում ենք, որ մեր օբյեկտները ունենան գեղեցիկ ներկայացում, երբ նրանց
# սթրինգի փոխակերպենք։ Կարող եք անգամ հենց համապատասխան գույնը տպել կոնսոլում (google-ը ձեզ օգնական :) ):
# Լրացուցիչ։ Գույները շատ հաճախ ներկայացվում են 16-հիմնային համակարգում (hexadecimal)։ Կարո՞ղ եք այնպես անել, որ
# կիրառելով hex() ֆունկցիան մեր օբյեկտի վրա ստանանք համապատասխան գույնի 16-հիմնային ներկայացումը։

# class Color:
#
#     def __init__(self, red, green, blue, text='hello'):
#         self.blue = blue
#         self.green = green
#         self.red = red
#         self.text = text
#
#     def __add__(self, other):
#         if self.red + other.red > 255 or self.green + other.green > 255 or self.blue + other.blue > 255:
#             raise TypeError('please enter less than 255')
#         return Color(self.red + other.red, self.green + other.green, self.blue + other.blue, self.text + ' ' + other.text)
#
#     def __sub__(self, other):
#         if self.red - other.red < 0 or self.green - other.green < 0 or self.blue - other.blue < 0:
#             raise TypeError('please enter positive number')
#         return Color(self.red - other.red, self.green - other.green, self.blue - other.blue, self.text + ' ' + other.text)
#
#
# color_1 = Color(125, 70, 60, 'Artak')
# print(f'\033[38;2;{color_1.red};{color_1.green};{color_1.blue}m{color_1.text}')
#
# color_2 = Color(120, 60, 45, 'Sargsyan')
# print(f'\033[38;2;{color_2.red};{color_2.green};{color_2.blue}m{color_2.text}')
#
# new_color_sum = color_1 + color_2
# print(f'\033[38;2;{new_color_sum.red};{new_color_sum.green};{new_color_sum.blue}m{new_color_sum.text}')
#
# new_color_sub = color_1 - color_2
# print(f'\033[38;2;{new_color_sub.red};{new_color_sub.green};{new_color_sub.blue}m{new_color_sub.text}')



# 2. Create a class named Length. The default unit for length is meter. The class must contain some conversions
# information, e.g. feet -> m, km -> m, yard -> m, mile -> m etc.
#    a) Create a dictionary that will hold the metrics. Keys will be the unit name and their values will be the
#    coefficients for converting that unit to meters.
#    b) The class will have 2 instance attributes. Units and the length value itself.
#    c) Now, we can add lengths of course. So implement that method. But be careful, we can't add yard to meters, so
#    you will need to convert everything before adding.
#    d) Implement the __str__ method. This method must show the length of our Length object in meters.
# Feel free to add some more features if you find them useful.
# Ստեղծեք Length կլաս: Միավորի սկզբնական արժեքը մետրն է։ Կլասը պետք է պարունակի երկարության միավորների կոնվերտացիաների
# հետ կապված որոշակի ինֆորմացիա։ Ավելի կոնկրետ հետևյալ միավորների՝ feet -> m, km -> m, yard -> m, mile -> m (ավելացրեք
# այլ միավորներ, եթե ցանկանում եք)։
#    a) Ստեղծեք dictionary, որը կպարունակի կոնվերտացիայի համար անհրաժեշտ հաստատունները։ key-երը պետք է լինեն
#    միավորների անունները, իսկ արժեքները մետր դարձնելու համար գործակիցները։ {'km': 1000, ...}
#    b) Կլասը պետք է ունենա երկու ատրիբուտ՝ երկարության արժեքը և միավորը։
#    c) Երկարությունները կարող ենք գումարել։ Իմպլեմենտ արեք համապատասխան ֆունկցիան, որպեսզի length օբյեկտների վրա
#    կարողանանք կիրառել + օպերատորը։
#    d) Իմպլեմենտ արեք նաև __str__ մեթոդը։ Երբ մեր օբյեկտները սթրինգ դարձնենք, կուզենք տեսնել դրանց արժեքն ու միավորը։

class Length:
    name_type = {'km': 1000, 'yard' : 0.9144, 'mile': 1609.34, 'm': 1}

    def __init__(self, length, length_type):
        self.length_type = length_type
        self.length = length
        self.meter = None

    def __add__(self, other):
        for key, value in self.name_type.items():
            if self.length_type == key:
                self.meter = value * self.length
            if other.length_type == key:
                other.meter = value * other.length

        measurement = self.name_type[other.length_type]
        # for key, value in other.name_type.items():
        #     if other.length_type == key:
        #         other.meter = value * other.length
        #         break

        return f'{(self.meter + other.meter) / measurement} {other.length_type}'



    def __str__(self):

        return f'{self.length} {self.length_type}'

    # def converter(self, new_self):
    #     for key, value in new_self.name_type.items():
    #         if new_self.length_type == key:
    #             new_self.length = value * new_self.length
    #             break


km = Length(1, 'km')

yard = Length(1, 'yard')

mile = Length(150, 'mile')

print(str(km + yard))
print(str(yard))

# 3. Create an Atom class. We will have predefined atoms for it, which are C - carbon, N - nitrogen, H - hydrogen,
# O - oxygen and P - phosphorus.
#     a) Now, the class has an instance variable called "name".
#     b) If you create an object with a name other than the 5 atoms mentioned, you should get an exception. But not any
#     kind of exception. This exception will be something that we have defined. So, define an exception class called
#     UnknownAtom. This must give us a detailed explanation why it is raised.
#     c) Define a new class called Molecule. The molecule has an instance variable, which is a list.
#     d) implement the __add__ method for our Atom class. Adding two atoms will return, you've guessed it, a Molecule!
#     e) We can also add an atom to a molecule. So implement that functionality as well!
#     f) Finally, do some cosmetic stuff, like implement the __str__ method for both of our classes.
# If you're into chemistry, feel free to add some logic like keeping charges of each atom, tracking valency and raising
# an error if two atoms can't make a molecule.
# Ստեղծել Atom կլաս: Պետք է ունենանք նախապես հայտարարված ատոմների ցուցակ։ Դրանք են C - ածխածին, N - ազոտ, H - ջրածին,
# O - թթվածին and P - ֆոսֆոր։
#     a) Կլասը պետք է ունենա instance ատրիբուտ name։
#     b) Եթե ստեղծեք ատոմ, որի անունը չկա նախապես հայտարարված ցուցակում, պետք է ստանաք exception: Այն չպետք է լինի
#     built-in exception: Ստեղծեք ձեր exception-ը, որը կունենա UnknownAtom անունը և հնարավորինս պարզ կներկայացնի,
#     թե ինչն է սխալ գնացել։
#     c) Ստեղծել նոր կլաս, որի անունը կլինի Molecule: Այն պետք է ունենա մեկ instance ատրիբուտ, որը լինելու է որոշակի
#     լիստ։
#     d) Սահմանեք __add__ մեթոդը ատոմ կլասի համար։ Երկու ատոմ գումարելուց պետք է ստանանք, գուշակեցիք, մոլեկուլ։ Ստացված
#     մոլեկուլը պետք է իր լիստի մեջ պարունակի այն ատոմների անունները ինչից ստացվել է։
#     e) Մոլեկուլներին նույնպես հնարավոր է միացնել ատոմ։ Սահմանեք __add__ մեթոդը մոլեկուլների համար։ Ֆունկցիայի
#     տրամաբանությունը ձեզ վրա է։
#     f) Վերջապես սահմանեք __str__ մեթոդը երկու կլասերի համար և սահմանեք ատոմների ու մոլեկուլների համար գեղեցիկ
#     սթրինգային ներկայացում։
# Եթե քիմիայի սիրահար եք, կարող եք ավելացնել հավելյալ ֆունկցիոնալություն։ Օրինակ պահել ատոմների լիցքը, մոլեկուլ
# ստեղծելուց հաշվի առնել վալենտականությունը և այլն։


class Atom:
    atoms_table = {'C': 'carbon', 'N': 'nitrogen', 'H': 'hydrogen', 'O': 'oxygen', 'P': 'phosphorus'}

    def __init__(self, name):
        self.name = name
        for key in self.atoms_table.keys():
            if key == self.name:
                break
        else:
            raise UnknownAtom

    def __add__(self, other):
        return Molecule([self.name, other.name])

    def __str__(self):
        return f'{self.name} is {self.atoms_table[self.name]}'


class UnknownAtom(Exception):

    def __init__(self, message='there are not atom in table'):
        super().__init__(message)


class Molecule:

    def __init__(self, molecule_list):
        self.molecule_list = molecule_list

    def __add__(self, other):

        def func(some_list):
            text = ''
            for item in some_list:
                rand = random.randint(1, 10)
                text += f'{item}{rand}'
            return text

        return f'{func(self.molecule_list)} + {func(other.molecule_list)}'


# potassium = Atom('K')
# calcium = Atom('Ci')

carbon = Atom('C')
oxygen = Atom('O')

print(carbon + oxygen)
print(oxygen)

molecule_1 = Molecule(['C', 'H', 'O'])
molecule_2 = Molecule(['CH', 'O'])

print(molecule_1 + molecule_2)