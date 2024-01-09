# class Citizen:
#     def __init__ (self , fn , ln) :
#         self.first_name = fn
#         self.last_name = ln
#     def Full_name(self) :
#         print(f"Your first name is {self.first_name} , \nand your last name is {self.last_name}.")

# class Teacher(Citizen) :
#     pass

# t1 = Teacher("Amir" , "Amiri")
# t1.Full_name()

# class Student(Citizen) :
#     pass

# s1 = Student("Amir hossain" , "Shaffie")
# s1.Full_name()

# cs = [
#     {
#     "title" : "HTML",
#     "teacher" : "Milad"
#     },
#     {
#     "title" : "PHP",
#     "teacher" : "Ali"
#     },
#     {
#     "title" : "Python",
#     "teacher" : "Amir"
#     },
#     {
#     "title" : "C++",
#     "teacher" : "parham"
#     }
# ]


# class Citizen:
#     def __init__ (self , fn , ln) :
#         self.first_name = fn
#         self.last_name = ln
#     def Full_name(self) :
#         print(f"Your first name is {self.first_name} , \nand your last name is {self.last_name}.")

# class Teacher(Citizen) :
#     def __init__ (self , fn , ln , ag , sc , *sub , **ka) :
#         super().__init__( fn , ln )
#         self.age = ag
#         self.school = sc
#         self.subjects = sub
#         self.about_teacher = ka
#     def Every_things_about_teacher(self) :
#         super().Full_name()
#         print(f"""You are {self.age} and you are taeaching in {self.school}.
# The subjects you teach include {self.subjects}.
# {self.about_teacher}.""")
        
# t1 = Teacher("Amir" , "Amiri" , 37 , "sadra2" , "Math" , "Scince" , "Chemistry" , level_school = "high school" , Marital_status = "single")
# t1.Every_things_about_teacher()

# class Student(Citizen) :
#     def __init__(self , fn , ln , ag , cl , f_s , *fr , **ka) :
#         super().__init__( fn , ln )
#         self.age = ag
#         self.clas = cl
#         self.courses = []
#         self.favourite_subject = f_s
#         self.friend = fr
#         self.about_student = ka
#     def Every_things_about_student(self) :
#         super().Full_name()
#         print(f"""You are {self.age} and you study in class {self.clas}.
# Your favuorite subject is {self.favourite_subject}.
# Your friends/s is / are : {self.friend}.
# {self.about_student}""")
    
#     def Courses(self) :
#         if self.courses :
#             for cours in self.courses :
#                 print(cours["title"])
        
# s1 = Student("Amir hossain" , "Shafiei" , 19 , "01" , "Math" , "Sina" , "Sadra" , "Parham" , "Mohammad ali" , "Parham zg" , best_teacher = "physics" , field = "Math and physics")
# s1.Every_things_about_student()
# s1.courses.append(cs[1] , cs[3])
# s1.Courses()

class Family:
    def __init__ (self , fn , ln , h_m_f) :
        self.first_name = fn
        self.last_name = ln
        self.how_many_family = h_m_f
    def Status(self) :
        print(f"Your first name is {self.first_name} , \nand your last name is {self.last_name}. \nYou are living in family of {self.how_many_family}.")

class Father(Family) :
    def __init__(self , fn , ln , h_m_f , ag , w_n , h_m_c , h_m_y_m , *c_n , **ka) :
        super().__init__( fn , ln  , h_m_f  )
        self.age = ag
        self.wife_name = w_n 
        self.how_many_childeren = h_m_c
        self.how_many_years_married = h_m_y_m
        self.childerens_names = c_n
        self.personal = ka
    def About_father(self) :
        super().Status()
        print(f"""You are {self.age} and you have {self.how_many_childeren} child / childeren. 
Your wife s name is {self.wife_name} and you have been married for {self.how_many_years_married} years.
Your childrens names : {self.childerens_names}
{self.personal}""")
        
# fa1 = Father("Mehran" , "Shafiei" , 3 , 47 , "Akram Nazari" , 1 , 21 , "Amir hossain" , job = "worker" , company = "erish khodro")
# fa1.About_father()

class Mother(Family) :
    def __init__(self , fn , ln , h_m_f , ag , h_n , h_m_c , h_m_y_m , *c_n , **ka) :
        super().__init__( fn , ln  , h_m_f  )
        self.age = ag
        self.husband_name = h_n 
        self.how_many_childeren = h_m_c
        self.how_many_years_married = h_m_y_m
        self.childerens_names = c_n
        self.personal = ka
    def About_Mother(self) :
        super().Status()
        print(f"""You are {self.age} and you have {self.how_many_childeren} child / childeren. 
Your husband s name is {self.husband_name} and you have been married for {self.how_many_years_married} years.
Your childrens names : {self.childerens_names}
{self.personal}""")

# m1 = Mother("Akram" , "Nazari" , 3 , 39 , "Mehran Shafiei" , 1 , 21 , "Amir hossain" , job = "Disput resolution council" , location = "Qazvin")
# m1.About_Mother()

# class Son(Family) :
    # def __init__(self, fn, ln, h_m_f , ag , lo , *fr , **ka):
    #     super().__init__(fn, ln, h_m_f)
    #     self.age = ag
    #     self.location = lo
    #     self.friends = fr
    #     self.personal = ka
    #     if self.age > 7 :
    #         l = input("Which level do you study ? ")
    #         n_s_o_u = input("What is name of your school / university ? ")
    #         c_n = input("What is your class number ? ")
    #         if ag > 18 :
    #             q = input("Do you have job ? ")
    #             if q == "yes" :
    #                 j = input("What is your job ? ")
    #                 w_w = input("Where are you working ? ")
    #             else :
    #                 j = None
    #                 w_w = None
    #     self.level = l
    #     self.nume_sc_or_un = n_s_o_u
    #     self.clas_number = c_n
    #     self.job = j
    #     self.where_work = w_w
    # def About_Son(self) :
    #     super().Status()
    #     print(f"You are {self.age} and you are living in {self.location}.")
    #     if self.level :
    #         print(f"You are studying in {self.nume_sc_or_un} ({self.level}) in class {self.clas_number}.")
    #     if self.job :
    #         print(f"You are working at {self.where_work} and your job is {self.job}.")
    #     print(f"Your friend/s is / are : {self.friends} \n{self.personal}")

# s1 = Son("Amir hossain" , "Shafiei" , 3 , 19 , "Qazvin" , "Sina" , "Sadra" , "Parham" , "Mohammad ali" , "parham zg" , need = "I want to emigrate")
# s1.About_Son()