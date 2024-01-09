def B_M_M() :  
    number1 = int(input("Pleas inter number 1 : "))
    number2 = int(input("Pleas inter number 2 : "))
    
    if number1 > number2 :
        Mi = number2
    else :
        Mi = number1

    r = Mi
        
    while r > 0 :
        if number1 % r == 0 and number2 % r == 0:
            print(f"{r} is BMM.")
            break
        r = r - 1

def K_M_M() :
    
    number1 = int(input("Pleas inter number 1 : "))
    number2 = int(input("Pleas inter number 2 : "))
    
    if number1 > number2 :
        Ma = number1
    else :
        Ma = number2

    r = Ma

    while True :
        if r % number1 == 0 and r % number2 == 0:
            print(f"{r} is KMM.")
            break
        r = r + 1

def just_even() :
    
    y = 1
    l = 0
    
    number = int(input("Pleas inter a number : "))

    while number != 0 :
        number = int(number)
        r = number % 10
        if r % 2 == 0 :
            l = l + (r * y)
            y = y * 10
        
        number = number / 10
    print(l)
    
def G_mail() :
    while True:    
        gmail_password = input("Pleas inter your g mail password : ")
        gmail_password = gmail_password.replace(" ","")

        if len(gmail_password) < 4 :
            print("Your password must have 4 letters at least.")
        elif len(gmail_password) > 12 :
            print("Your password must have 12 letters maximum.")
        elif gmail_password.isnumeric() :
            print("Your password must have one letter.")
        elif gmail_password.isalpha() :
            print("Your password must have one number.")
        else :
            print("Your password seccessfully seved. \nhave fun :)")
            print(gmail_password)
            break

def Math_operations() :
    L1 = []
    p = 0
    h = 0
    y = 0
    grade = 0

    for x in range (0 , 10 , 1) :
        a = int(input("Inter a number : "))
        grade = a + grade
        L1.append(a)
    
    Max = L1[0]
    Min = L1[0]
    grade = grade / 10
    for i in range (0, 10 , 1) :
        if L1[i] > Max :
            Max = L1[i]
        if L1[i] < Min :
            Min = L1[i]
        if L1[i] % 5 == 0 :
            p = p + 1
        if L1[i] % 7 == 0 : 
            h = h + 1
        if L1[i] % 11 == 0 :
            y = y + 1
    print(Max)
    print(Min)
    print(grade)
    print(p)
    print(h)
    print(y)

def Salaey_increase() :

    H = int(input("Pleas inter your H : "))
    Sn = int(input("Pleas inter your Sn : "))
    Sa = int(input("Pleas inter your Sa : "))

    if Sn > 50 and Sa == 25 :   
        H = H + (H * 40 / 100)
    else :
        if Sn > 40 and Sa == 15 :
            H = H + (H * 10 / 100)
        else :
            if Sn > 35 and Sa == 10 :
                H = H + (H * 5 / 100)
    print(H)
    
def Even_odd_numbers() :   
    f =0 
    z =0
    for i in range (0 ,10 ,1) :
        a = int(input("Please inter a number : "))
    
        if (a % 2 == 0) :
            z = z + 1
        else :
            f = f + 1
    print(f"The number of even numbers is : {z} /nand the number of odd numbers is  : {f}")

def Users_password() :
    User = {
        "Amir" : "3817",
        "Ali"  : "8533",
        "Sina" : "6105",
    }

    user_name = input("Please inter your user name : ")
    password = input("Please inter your password : ")

    while user_name not in User or password != User[user_name] :
        print("you are worng :(")
        user_name = input("Please inter your user name : ")
        password = input("Please inter your password : ")
    else : 
        print("Your password is correct.")

def Size_and_coler_of_balls() :

    sizes = ["big" , "small"]
    colers = ["red" , "black" , "white"]
    balls = ["basketball", "vollyeball", "football"]

    for size in sizes :
        for coler in colers :
            for ball in balls :
                if coler == "black" and ball == "vollyeball" or coler == "white" and ball == "basketball" or size == "small" and ball == "vollyeball" :
                    continue
                print(size , coler , ball)

class Person ():
    def __init__ (self ,Fn , Ln , age , ci , co  , *fr , **Ka ) :
        self.first_name = Fn
        self.last_name = Ln
        self.age = age
        self.city = ci
        self.nationality = co
        self.friends = fr
        self.personal = Ka
    def Every_things(self) : 
        print(f"""Your first name is {self.first_name}, 
and your last name is {self.last_name}.
You are {self.age} and from {self.nationality}.
You are living in {self.city} now.
Your friend/s is / are : {self.friends}.
About you : {self.personal}""")
    def Full_name(self) :
        print(f"Your first name is {self.first_name} , \nand your last name is {self.last_name}.")
    def Live(self) :
        print(f"You are from {self.nationality} , \nand you are living in {self.city} now.")
    def Age(self) :
        print(f"You are {self.age}")
    def Friends(self) :
        print(f"Your friend/s is / are : {self.friends}.")
    def Personal(self) :
        print(f"About you : {self.personal}")

person1 = Person("Amir hossain" , "shaffie" , 18 , "Qzvin" , "Iran" , "Sina" , "Sadra" , "Parham" , "Mohammad ali" , "Parham zg" , gender = "Male" , favourite_music = "dance", status = "I want to emigrate.")

person1.Every_things()
# person1.Full_name()
# person1.Age()
# person1.Live()
# person1.Friends()
# person1.Personal()