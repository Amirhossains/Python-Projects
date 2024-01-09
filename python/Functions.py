## shift + alt + dokme paeen == copy az hamon ghat migire

# print("Im from Qazvin , i am 18 and i love dance music :)")
# print("Im from Qazvin , i am 18 and i love dance music :)")
# print("Im from Qazvin , i am 18 and i love dance music :)")

# def me() : 
#     print("Im from Qazvin , i am 18 and i love dance music :)")

# me()
# me()
# me()
## kolan dige me ba on gomle ta rif shode

# def your_name(first_name, last_name) :
#     print(f"Hello, {first_name} {last_name} :) \nhow are you {first_name}.")

# your_name("amir hossain", 'shifiei')
# your_name("sina", "behbodei")

# def fullname(first_name, last_name) :
#     print(f"Hello {first_name} {last_name}. \ngood morning :)")

# fullname(first_name = "amir hossain", last_name = "shafiei")

# def total(a, b) :
#     print(a + b)

# def subtraction(a, b) :
#     print(a - b)

# def multiplication(a, b) :
#     print(a * b)

# def division(a, b):
#     print(a / b)

# total(35, 15)
# total(96, 24)

# subtraction(436, 572)
# subtraction(4297, 2049)

# multiplication(12, 14)
# multiplication(37, 14)

# division(1975, 25)
# division(85, 15)

# # talash aval va gheylei bad :(

# # password  = input("Pleas inter your password : ")
# # password = password.replace(" ", "")
# # while password.count("") > 8 :
#     if int not in password :
#         password = input("your password must have integer :( \nPleas try again : ")          
#     if str not in password :
#         password = input("your password must have string :( \n \Pleas try again : ")
#     print("yes your password seccessfully saved :)")
# # else :
    # password = input("your password must have more than 8 item :( \nPleas try again : ")


# password = "1234"

# print(password.isnumeric())

# password = "1234q"

# print(password.isnumeric())

# password = "amir"

# print(password.isalpha())

# password = "amir3"

# print(password.isalpha())

## age space dashte bashe dar har sort ghalate

# def G_mail_password(password) :
#     if len(password) < 8 :
#         print("your password must be at least 8 char.")
#     elif password.isalpha() :
#         print("your password must have at least one number.")
#     elif password.isnumeric() :
#         print("your password must have at least one letter.")
#     else :
#         print("Yesss your password seccessfully seved :)")

# while True :
#     password = input("inter your password : ")
#     G_mail_password(password)
    
## space nabayad bezanie hanoz nemidinam chikaresh mishe kard

# def hi(name1, name2) :
#     print(f"Hello {name1}. \nHello {name2}.")

# hi("amir", "sina")
# hi("amir", "sina", "sadra")

## ma mighahim be benahayat adam hello kone

# def hi(*name) :
#     print(f"Hello {name}")

# hi("amir", "sina", "sadra", "parham", "mohammad ali", "aghaei")

## hala age beghahim tak tak be hame salam kone :

# def hi(*name) :
#     for Name in name :
#         print(f"Hello {Name}")

# hi("amir", "sina", "sadra", "parham", "mohammad ali", "aghaei")

# def you_and_friends(first_name, last_name, *frinds) :
#     print(f"Hello {first_name} {last_name}")
#     print(f"how are you {first_name}")
#     print(f"your frinds are {frinds}")

# you_and_friends("amir hossain", "shafiei", "sina", "sadra", "parham", "mohammad ali", "aghaei")

## baghahim ghodemon ye serie parametr va argument

# def family(your_first_name, your_last_name, *args, **keywordargument) :
#     print(your_first_name)
#     print(your_last_name)
#     print(args)
#     print(keywordargument)

# family("amir hossain", "shafiei", "sina", "sadra", "parham", "mohammad ali", "aghaei", age = 18, city = "Qazvin")

# def you(first_name, last_name, age, city, country = "iran") :
#     print(f"Hello {first_name} {last_name}.")
#     print(f"you are living in {city} in the {country}.")
#     print(f"you are {age}.")

# you("amir hossain", "shafiei", 18, "Qazvin")

# you("willy", "william", 38, "paris", "farance")

# def Hi(frinds) :
#     for item in frinds :
#         print(f"Hello {item}")

# close_friends = ["sina", "sadra", "mohammad ali", "parham"]

# Hi(close_friends)

# Hi("amir")

# Hi(35)

friends = {
    "first" : "sina", 
    "second": "sadra",
    "third" : "mohammad ali",
    "last"  : "parham"
}
# Hi(friends)

# Hi(friends.values())

# def total(a , b) :
#     c = a + b
#     return c

# total(24 , 42)

# print(total(24 , 42))

# result = total(52 , 25)

# print(result)

# def total(a , b) :
#     return a + b

# result = total(72 , 27)

# print(result + 11)

# def number(a , b) :
#     return a , b

# result = number(4 , 2)

# print(result)

# def Fiernds(a) :
#     return a

# friends = "sina", "sadra", "mohammad ali", "parham"

# print(Fiernds(friends))

# def Friends(a , b , c) :
#     a += 2
#     b -= 2
#     c *= 2
#     return a , b , c  

# result = Friends(2 ,8 ,4)

# for item in result :
#     print(item)

# username = input("Pleas inter your user name : ")

# def validation(username) :
#     if 4 <= len(username) < 10 :
#         return True
#     else :
#         return False

# if validation(username) :
#     print("your user name is ok ;)")
# else :
#     print("your user name not is ok :( \nPleas try again.")

def G_mail_password(password) : 
    if 0 <= len(password) <= 4 or  12 < len(password) :
        print("your password must be at least between 5 char and 12 char.")
        return False
    elif password.isalpha() :
        print("your passwored must have at least one number.")
        return False
    elif password.isnumeric() :
        print("your password must have at least one letter.")
        return False 
    else :
        return True

# password = input("Pleas inter your G mail password : ")
# password = password.replace(" ", "")

# while G_mail_password(password) == False :
#     password = input("you wrong :( \ntry again : ")
#     password = password.replace(" ", "")
# else :   
#     print("your G mail password successfully saved :)")

# print(password)


# def uppeer_and_lower(word) :
#     upper_word = 0
#     lower_word = 0
#     for item in word :
#         if item.isupper() :
#             upper_word += 1
#         elif item.islower() :
#             lower_word += 1
#         else :
#             pass

#     print(f"upper cases : {upper_word}.")
#     print(f"lower cases : {lower_word}.")


# while True :
#     word = input("inter some name : ")
#     uppeer_and_lower(word)

# uppeer_and_lower("Amir Hossain Shafiei")


# def number_type(number) :
#     C = number % 2
#     if C == 0 :
#         print("this number is couple.")
#     elif C == 1 :
#         print("this number is odd.")
#     else :
#         print("this number is not integer.")

# while True :
#     Number = int(input("Pleas inter a number : "))
#     number_type(Number)

# # in talash ghodam bod ke ghob bod va dorost :)

# def year_conversion(birth_day , birth_mounth , birth_year) :

#     if birth_mounth < 10 :
#         birth_year += 621
#     elif birth_mounth > 10 :
#         birth_year += 622
#     elif birth_mounth == 10 :
#         if birth_day > 11 :
#             birth_year += 622
#         elif birth_day <= 11 :
#             birth_year +=621
#         else :
#             print("Oh some thing is wrong :( \ntry again.")
#             pass
#     else :        
#         print("Oh some thing is wrong :( \ntry again.")
#         pass
#     print(f"Your birth year is {birth_year} :)")

# birth_day = int(input("Pleas inter your birth day : "))
# birth_mounth = int(input("Pleas inter your birth month : "))
# birth_year = int(input("Pleas inter your birth year : "))

# year_conversion(birth_day , birth_mounth , birth_year)

# # hala be sorat gheylei gholase tar

def Converter(day , month , year) :
    if month > 10 or month == 10 and day > 11 :
        year += 622
    else :
        year += 621
    print(f"your year of the birth day is {year} :)") 

while True :
    day = int(input("Pleas inter your birth day : "))
    month = int(input("Pleas inter your birth month: "))
    year = int(input("Pleas inter your birth year : "))

    # Converter(day , month , year)

# # (--------------------------------------------------)



## continue , you have come far very good , i admire you (respect) ;)