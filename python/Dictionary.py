# dict = {
#     "first name" : "amir rt",
#     "last name" : "shafei",
#     "age" : 17,
#     "age" : 18,
#     "age" : 19,
#     "parents name" :["mehran", "akaram"],
#     "you are happy." : False
# }

# print(dict)
# print(type(dict))
# print(len(dict))

## agar Dictionary do ta key dashte bashim dovomei ro chap mikone

# about_me = {
#     "first name" : "amir rt",
#     "last name" : "shafei",
#     "age" : 19,
#     "parents name" :["mehran", "akaram"],
#     "you are happy." : False
# }

# myage = dict["age"]

# print(myage)

## ravesh ba method

# myage = dict.get("age")

# print(myage)

# print(dict.keys())

# dict["city"] = "Qazvin"

# print(dict.keys())

# print(dict)

# dict = {
#     "first name" : "amir rt",
#     "last name" : "shafei",
#     "age" : 19,
#     "parents name" :["mehran", "akaram"],
#     "you are happy." : False
# }

# print(dict.values())

# dict["city"] = "Qazvin"

# print(dict.values())

# dict = {
#     "first name" : "amir rt",
#     "last name" : "shafei",
#     "age" : 16,
#     "parents name" :["mehran", "akaram"],
#     "you are happy." : False
# }

# dict["first name"] = "amir hossain"

# dict["age"] = 18

## ravesh ba method

# dict.update({"age" : 18})

# dict.update({"first name" : "amir hossain"})

# print(dict.items())

## baray in ke tamam key va value ha ro dron yek list va item haro daron yek tuple bezarim az method items estefade mikonim 

# dict = {
#     "first name" : "amir rt",
#     "last name" : "shafei",
#     "age" : 19,
#     "parents name" :["mehran", "akaram"],
#     "you are happy." : False
# }
# print(19 in dict)

# print("city" in dict)

# dict["city"] = "Qazvin"

# print("city" in dict)

# print(dict.items())

## ravesh ba method

# print("city" in dict)

# dict.update({"city" : "Qazvin"})

# print("city" in dict)

# print(dict.items())


# dict = {
#     "first name" : "amir rt",
#     "last name" : "shafei",
#     "age" : 19,
#     "parents name" :["mehran", "akaram"],
#     "you are happy." : False
# }

# dict.pop("you are happy.")

# del dict["parents name"]

# dict.popitem()

# print(dict.items())

# dict.clear()

# print(dict.items())

## dictionary index gozary nashode

# dict1 = {
#     "first name" : "amir rt",
#     "last name" : "shafei",
#     "age" : 19,
#     "parents name" :["mehran", "akaram"],
#     "you are happy." : False
# }

# dict2 = dict1

# print(dict2)

# dict1.pop("parents name")

# print(dict2)

# print(dict1)

## braye inke dict1 va dict2 be ham vabaste naba shan bayad copy begirim

# dict1 = {
#     "first name" : "amir rt",
#     "last name" : "shafei",
#     "age" : 19,
#     "parents name" :["mehran", "akaram"],
#     "you are happy." : False
# }

# dict2 = dict1.copy()

# print(dict2)

# dict1.pop("parents name")

# print(dict2)

# print(dict1)

## also

# dict1 = {
#     "first name" : "amir rt",
#     "last name" : "shafei",
#     "age" : 19,
#     "parents name" :["mehran", "akaram"],
#     "you are happy." : False
# }

# dict2 = dict(dict1)

# print(dict2)

# dict1.pop("age")

# print(dict2)

# print(dict1)

# fam = {
#     "father" : {
#         "first name" : "mehran",
#         "last name" : "shafiei",
#         "age" : 47
#     },
#     "mother" : {
#         "first name" : "akram",
#         "last name" : "nazarei",
#         "age" : 42
#     },
#     "me" : {
#         "first name" : "amir rt",
#         "last name" : "shafiei",
#         "age" : 18
#     }
# }

# fam["me"].update({"first name" : "amir hossain"})

# fam["me"]["first name"] = "amir hossain"

# print(family["me"])

## do ta method mondeh

# x = ('key1', 'key2', 'key3')

# y = 0

# thisdict = dict.fromkeys(x, y)

# print(thisdict)

## ziad bedard boghor nist

# dict1 = {
#     "first name" : "amir",
#     "last name" : "shafiei",
#     "age" : 18
# }

# print(dict1.setdefault("age"))

# dict = {
#     "close_friends" : {
#         "best" : "sina",
#         "second" : "sadra",
#         "last" : "mohammad ali"
#     },
#     "casual_friends" : {
#         "first" : "parham",
#         "second" : "aghaei",
#         "third" : "vanakei"
#     },
#     "family" : {
#         "father" : "mehran",
#         "mother" : "akram",
#         "best uncle" : "ali",
#         "best aunt" : "hadis"
#     }
# }

# dict.pop("casual_friends")

# name_grand_father = dict["family"].setdefault("grand father",  "golam reza")

# print(name_grand_father)

# del name_grand_father

# print(dict.items())

# hala fargh setdefault ba get ro mifahme

# dict.pop("casual_friends")

# name_gramd_father = dict["family"].get("grand father",  "golam reza")

# print(name_gramd_father)

# del name_gramd_father

# print(dict.items())

# family = {
#     "Bahram" : "RIP",
#     "bahram" : {
#         "Ali" : 45,
#         "ali" : {
#             "nora" : 6,
#             "roza" : 6,
#         },
#         "Majid" : 42,
#         "majid" : {
#             "sama" : 13,
#             "selin" : 2,
#         },
#         "mehran" : 47,
#         "hamid" : 40,
#         "hassan": 32,
#         "hossain":32,
#         "Akram" : 37,
#         "akram" : {
#             "amir" : 19,
#         },
#         "Hadis" : 35,
#         "hadis" : {
#             "arash" : 4,
#         }
#     }
# }
# family["bahram"].update({"Ali" : 44})
# family["bahram"]["ali"]["niki"] = 8
# del family["bahram"]["mehran"]
# grand_fhaters_name = [family["Bahram"] , family.setdefault({"Golam reza" : 78}) ]
# print(family.items())
# print(family["bahram"]["ali"])

# #yooooo :)