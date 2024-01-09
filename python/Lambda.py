
# result = lambda a : a + 10

# result(3)

# print(result(10))

# x = lambda a , b : a + b

# print(x(4 , 8))

# def total(a , b) :
#     def multiplication(n) :
#         return n * (a + b)
#     return multiplication
    
# M = total(3 , 8)

# print(M(5))

# def subtraction(a , b) :
#     return lambda  c : (a - b) * c

# multiplication = subtraction(17 , 9)

# print(multiplication(5))

# def myfunc(a) : 
#     return lambda b : b * a

# equalizer = myfunc(1)

# for number in range(0 , 11) :
#     print(equalizer(number))

# doubler = myfunc(2)

# for number in range (0, 11) :
#     print(doubler(number))

# tripler = myfunc(3)

# for number in range (0 , 11) :
#     print(tripler(number))


# numbers = [4, 7, 2, 4, 1, 0]

# def myfunc(number) :
#     return number * 2

# x = map(myfunc, numbers)

# print(x)

# print(tuple(x))

# print(list(x))

# print(set(x))

# print(dict(x))

# # ghailei sade tar

# numbers = [4, 7, 2, 4, 1, 0]

# x = map(lambda a : a * 2, numbers) 

# print(tuple(x))

# print(list(x))

# print(set(x))

# print(dict(x))

# numbers = [12 , 1 , 3 , 2 , 9]
# Numbers = [7 , 18 , 6 , 1 , 5]

# x = list(map(lambda a , b : a + b , numbers , Numbers))

# print(x)

# print(tuple(x))

# # agar beghay ba for in caro conei

# numbers = [4, 7, 2, 4, 1, 0]

# N = []

# for number in numbers :
#     N.append(number * 2)

# print(N)

# list1 = [7 , 4 , 5 , 9]
# list2 = [5 , 8 , 6 , 2]
# list3 = [1 , 4 , 7 , 3]

# x = list(map(lambda a ,b , c : a + b - c , list1 , list2 , list3))
# print(x)

# doubler = list(map(lambda a : a * 2 , x))

# print(doubler)

# triple = list(map(lambda a :a * 3 ,x))

# print(triple)