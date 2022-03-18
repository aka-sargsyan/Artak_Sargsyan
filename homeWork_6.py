# import builtins
#
# def is_builtins(variable_str):
#     variable_list = dir(builtins)
#     if variable_str in variable_list:
#         return True
#     else:
#         return False
#
# print(f'is variable nam builtin {is_builtins("sum")}')
#
# print(globals())

""" OOP """

# 1. Create a calculator class. It will have 2 numerical instance attributes. Then declare 4 methods called add, sub,
# mult, div to respectively add, subtract, multiply and divide the attributes.
# Ստեղծել կալկուլատորի կլաս։ Այն պետք է ունենա երկու instance attribute։ Ապա ստեղծել չորս մեթոդ՝ add, sub,
# mult, div, որոնք համապատասխանաբար կգումարեն, կհանեն, կբազմապատկեն և կբաժանեն այդ ատրիբուտները։

# first version

# class Calculator:
#
#     def __init__(self, number_1, number_2):
#         self.add = number_1 + number_2
#         self.sub = number_1 - number_2
#         self.mult = number_1 * number_2
#         self.div = number_1 / number_2
#
#
# calc = Calculator(7, 6)
#
# print(f'calculate numbers with add {calc.add}')
# print(f'calculate numbers with sub {calc.sub}')
# print(f'calculate numbers with mult {calc.mult}')
# print(f'calculate numbers with div {calc.div}')

# second version

# class Calculator:
#
#     def __init__(self, *numbers):
#
#         current_list = numbers
#         current_add = current_list[0]
#         current_sub = current_list[0]
#         current_mult = current_list[0]
#         current_div = current_list[0]
#
#         for i in range(1, len(current_list)):
#             current_add += current_list[i]
#             current_sub -= current_list[i]
#             current_mult *= current_list[i]
#             current_div /= current_list[i]
#
#         self.add = current_add
#         self.sub = current_sub
#         self.mult = current_mult
#         self.div = current_div
#
#
# calc = Calculator(7, 8, 9)
#
# print(f'calculate numbers with add {calc.add}')
# print(f'calculate numbers with sub {calc.sub}')
# print(f'calculate numbers with mult {calc.mult}')
# print(f'calculate numbers with div {calc.div}')

# 3-th version

# class Calculator:
#
#     add = 0
#     sub = 0
#     mult = 1
#     div = 1
#
#     def __init__(self, *numbers):
#         self.array = numbers
#
#     def add_attribute(self):
#         for item in self.array:
#             self.add += item
#
#     def sub_attribute(self):
#         current_list = self.array
#         self.sub = current_list[0]
#         for i in range(1, len(current_list)):
#             self.sub -= current_list[i]
#
#     def mult_attribute(self):
#         for item in self.array:
#             self.mult *= item
#
#     def div_attribute(self):
#         current_list = self.array
#         self.div = current_list[0]
#         for i in range(1, len(current_list)):
#             if current_list[i] == 0:
#                 raise ValueError('you can not divide by 0 ')
#             else:
#                 self.div /= current_list[i]
#
#
#
# calc = Calculator(7, 8, 5)
# calc.add_attribute()
# calc.sub_attribute()
# calc.mult_attribute()
# calc.div_attribute()
#
# print(f'calculate numbers with add {calc.add}')
# print(f'calculate numbers with sub {calc.sub}')
# print(f'calculate numbers with mult {calc.mult}')
# print(f'calculate numbers with div {calc.div}')


# 2. Create Animal class with three methods - make_noise(), walk() and fly(). The methods shall print what the animal is
# doing. Then, create a Bird and Feline classes which inherit from Animal. Override the superclass methods, so that
# a cat warns us that it can't fly and the bird only wants to fly as it is too lazy to walk.
# Ստեղծել Animal կլասս, որը կունենա երեք մեթոդ՝ make_noise(), walk() և fly()։ Այդ մեթոդները պետք է տպեն, թե ինչ է անում
# կենդանին։ Ապա ստեղծել Bird և Feline կլասեր, որոնք ժառանգում են Animal-ից։ Animal-ի մեթոդները իմպլեմենտացրեք
# այդ կլասերի մեջ, այնպես, որ եթե կատուն փորձի թռչել, կոնսոլում տպվի, որ նա չի կարող թռչել։ Իսկ եթե թռչնի վրա
# կիրառենք walk() մեթոդը, նա ասի, որ ալարում է և միայն կարող է թռչել։

class Animal:
    def make_noise(self, noise):
        print(noise)

    def walk(self, walk):
        print('walking')

    def fly(self):
        print('flying')

class Bird(Animal):
    def walk(self):
        print('only wants to fly as it is too lazy to walk')

class Feline(Animal):
    def fly(self):
        print('cat do not fly')

chicken = Bird()
chicken.walk()
chicken.make_noise('muuu')

cat = Feline()
cat.fly()



# 3. Create a class called Shape. Define methods to calculate the shape's perimeter and the area.
# Ստեղծել Shape անունով կլաս։ Սահմանել մեթոդներ, սակայն չիմպլեմենտացնել (մեթոդի մեջ պարզապես գրել pass) երկու մեթոդ,
# դրանք անվանելով perimeter և area։

# 4. Create a Circle class which will inherit from Shape. Implement the constructor and superclass methods to correctly
# calculate the perimeter and the area of the circle.
# Ստեղծել Circle կլաս, որը կժառանգի Shape-ից։ Իմպլեմենտ արեք կոնստրուկտորը (շրջանագծի դեպքում կունենանք մեկ instance
# attribute` շառավիղը) և Shape-ի երկու մեթոդներն այնպես, որ Circle տիպի օբյեկտի վրա կիրառենք perimeter-ը, կստանանք
# շրջանագծի երկարությունը, իսկ area-ն կիրառելու դեպքում՝ մակերեսը։

# 5. Create a Rectangle class which will inherit from Shape. Implement the constructor and superclass methods to
# correctly calculate the perimeter and the area of the circle.
# Ստեղծել Rectangle կլաս, որը կժառանգի Shape-ից։ Իմպլեմենտ արեք կոնստրուկտորը և Shape-ի երկու մեթոդները ուղղանկյան համար

# 6. Create a Triangle class which will inherit from Shape. Implement the constructor and superclass methods to
# correctly calculate the perimeter and the area of the circle. Note, that you must check whether a triangle with the
# given lengths can exist.
# Ստեղծել Triangle կլաս, որը կժառանգի Shape-ից։ Իմպլեմենտ արեք կոնստրուկտորը և Shape-ի երկու մեթոդները եռանկյան համար։
# Եռանկյուն օբյեկտը ստեղծելուց անպայման ստուգել, թե արդյո՞ք տրված կողմերով եռանկյուն կարող է գոյություն ունենալ։

# 7. a) Create a Vehicle class. The class should have the following instance attributes: name, mileage (defaults to 0),
#    condition, price, max_speed, current_speed and engine_on (defaults to False). It should also have
#    unimplemented methods called start_engine, accelerate (takes a number as an argument), stop.
#    b) Create 2 classes called ElectricVehicle and PetrolVehicle. These classes inherit from the Vehicle class.
#    ElectricVehicle should have the following instance attributes: driving_range, charging_time. PetrolVehicle has the
#    following instance attributes: engine (the volume in litres), transmission, num_of_gears, current_gear. Of course,
#    these classes should call the parent class constructor in their constructor.
#    c) Implement the methods from Vehicle class in each of the child classes accordingly. start_engine should notify us
#    that the engine is on and change the engine_on attribute to True. accelerate method should accelerate the car
#    with the amount of its acceleration attribute and accordingly change the velocity of the car. stop method reduces
#    the speed to 0 and stops the engine. You should also do some checks, e.g. the speed can't be more than max_speed
#    of the car, the car can't start with its engine off etc.
#    d) For the PetrolCar, you should be able to change the transmission gears as well. If the transmission is manual,
#    you should increase the current_gear as the speed increases (current_gear can't be more than the number_of_gears).
#    e) Finally, create some petrol and electric vehicle objects and test your methods.
#
#    a) Ստեղծել Vehicle կլաս։ Կլասը պետք է ունենա հետևյալ instance attribute-ները - name, mileage (նախնական 0 է),
#    condition, price, max_speed, current_speed and engine_on (նախնական False է)։ Կլասը պետք է ունենա նաև երեք
#    չիմպլեմենտացված մեթոդ՝ start_engine, accelerate (ունի մեկ արգումենտ), stop.
#    b) Ստեղծել երկու կլաս՝ ElectricVehicle և PetrolVehicle։ Այս կլասերը ժառանգում են Vehicle—ից։ Էլեկտրական մեքենան
#    պետք է ունենա հետևյալ ատրիբուտները - driving_range, charging_time։ Իսկ վառելիքայինը՝ engine (ծավալը լիտրերով),
#    transmission, num_of_gears, current_gear։ Այս կլասերը պետք է նաև կանչեն Vehicle-ի __init__-ը (super()-ի միջոցով):
#    c) Իմպլեմենտ անել Vehicle-ից ժառանգված բոլոր մեթոդները։ start_engine-ը պետք է զգուշացնի, որ շարժիչը միացված է և
#    engine_on ատրիբուտը դարձնի True. accelerate-ը պետք է բարձրացնի մեքենայի արագությունը, իսկ stop-ը պետք է
#    արագությունն իջեցնի 0-ի և անջատի շարժիչը։ Պետք է նաև կատարել որոշակի վալիդացիա։ Օրինակ՝ արագութոյւնը չի կարող
#    գերազանցել max_speed-ը, մեքենան չի կարող արագանալ, եթե դրա շարժիչը անջատված է և այլն։
#    d) Վառելիքային մեքենայի համար պետք է նաև ներառել որոշակի տրամաբանություն փոխանցման տուփի հետ կապված։ Եթե այն
#    մեխանիկական է, կախված արագությունից պետք է փոխել current_gear-ը (current_gear-ը չի կարող գերազանգել
#    number_of_gears-ը):
#    e) Վերջապես ստեղծել մի քանի էլեկտրական և վառելիքային մեքենա օբյեկտներ և թեստավորել բոլոր մեթոդները։