# # Object Orietation

# class MyClass:
#     x = 5
#     y = 7

# # praperte = p

# p1 = MyClass()

# print(p1.x)

# print(MyClass.y)

# class Me() :
    
#     def __init__ (self, fn , ln , age) :
#         self.first_name = fn
#         self.last_name = ln
#         self.age = age

# p1 = Me("amir hossain", "shafiei", 18)

# print(p1.first_name)
# print(p1.last_name)
# print(p1.age)

# class Person() :
#     def __init__(self, Fn , Ln , age) :
#         self.first_name = Fn
#         self.last_name = Ln
#         self.age = age

# person1 = Person("sina" , "behbodei", 18)

# person2 = Person("parham", "aminlo" , 19)

# person3 = Person("hossain", "nazari", 30)

# print(person1.last_name)

# print(person3.age)

# print(person2.first_name)

# class MyClass() :
#     def __init__ (self , Fn , Ln , age) :
#         self.first_name = Fn
#         self.last_name = Ln
#         self.age = age

#     def Age(self) :
#         print(f"i am {self.age}")

#     def fullname(self) :
#         print(self.first_name)
#         print(self.last_name)
    
#     def all_think(self) :
#         print(f"my full name is {self.first_name} {self.last_name} and i am {self.age}.")

# p1 = MyClass("hossain" , "nazarei" , 30)

# p1.Age()

# p1.fullname()

# p1.all_think()

# p2 = MyClass("ghadyg" , "nazarei", 32)

# p2.fullname()

# print(p2.first_name)

# p2.first_name = "hadys"

# p2.fullname()

# print(p2.first_name)

# del p2.age()

# p2.Age()

# class Person() :
#     def __init__ (self , Fn , Ln , city , country , age , *friends , **keywordargument) :
#         self.firstname = Fn
#         self.lastname = Ln
#         self.old = age
#         self.city = city
#         self.country = country
#         self.friends = friends
#         self.taste = keywordargument

#     def Age(self) :
#         print(f"i am {self.old}.")
    
#     def fullname(self) :
#         print(f"my first name is {self.firstname} and my last name is {self.lastname}.")

#     def Friends(self) :
#         print(f"my friend/s is or are : {self.friends}")

#     def Taste(self) :
#         print(self.taste)

#     def location(self) :
#         print(f"i am from {self.city} in the {self.country}")

#     def all_thing(self) :
#         print(f"""Hello, wellcome :)


# your firstname is {self.firstname} and your last name is {self.lastname}.
# you are {self.old} and living in {self.city} in the {self.country}.
# your friend/s is or are : {self.friends}.
# {self.taste}""")

# person1 = Person("amir hossain",  "shafiei", "Qazvin" ,"iran" , 18 , "sina", "sadra",
# "mohammad ali" ,"parham" ,"aghaei" , favorito_music = "dance" , nickname = "amir rt" , gender = "Male")

# person1.all_thing()

# person1.fullname()

# person1.Age()

# person1.location()

# person1.Friends()

# person1.Taste()

# class Person :
#     def __init__ (self , fn , ln , age , **ka) :
#         self.first_name = fn
#         self.last_name = ln
#         self.age = age
#         self.personal = ka
#     def Every_things(self) :
#         print(f"Your name is {self.first_name} {self.last_name} and you are {self.age}. \n{self.personal}")

# p1 = Person("Amir hossain" , "Shaffie" , 20 , favourite_music= "dance" , gender = "Male" , status = "I want to emigrate")

# p1.Every_things()

# p1.age = 18
# p1.personal.clear()

# p1.Every_things()

## az del estefadeh kony error mideh.

# class Cars() :

#     cars_number = 0

#     def __init__(self, Cn , Cp , Py ,Co) :
#         self.car_name = Cn
#         self.car_price = Cp
#         self.production_year = Py
#         self.car_operation = Co
#         self.status = "off"
#         Cars.cars_number += 1

#     def start(self) :
#         if self.status == "off" :
#             self.status = "on"
#             print(f"{self.car_name} is on now.")
#         else :
#             print(f"{self.car_name} was on :( \ndont satart again.")
    
#     def off(self) :
#         if self.status == "on" :
#             self.status = "off"
#             print(f"{self.car_name} is off now.")
#         else :
#             print(f"{self.car_name} is off :( \ndont try again.")

# print(Cars.cars_number)

# car1 = Cars("pezho" , 150 , 1400 , 4000)

# car2 = Cars("samand" , 160 , 1394 , 60000)

# print(Cars.cars_number)

# car3 = Cars("pride" , 100 , 1391 , 45000)

# print(Cars.cars_number)

# print(car2.car_name)

# car2.car_name = "soren"

# print(car2.car_name)

# car1.start()
# car1.start()

# print(car1.status)

# car1.off()
# car1.off()

# print(car1.status)