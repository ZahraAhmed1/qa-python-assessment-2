# def two(number):
#     prime = True 
#     if number < 1:
#         prime = False
#     if number > 1:
#         for i in range (2, number):
#             if number % i == 0:
#                 prime = False

#     return prime

# print( two(3))
# print (two(16))
# print( two(19))

# def three(a):
#     return (a*1111) + (a*111) + (a*11) + (a)

# print (three(5))
# print (three(9))

# def one(string):
#     new_string=""
#     for i in range(0, len(string)):
#         new_string += string[i]*3
#     return new_string

# print(one("one"))
# print(one("hihihi"))

# def four(string1, string2):
#     new_string = ""
#     for i, j  in zip((0, len(string1)), (0, len(string2))):
#         new_string += string[i] + string[j]
    
#     return new_string

# print(four("String","Fridge"))

# def four(string1, string2):
#     new_string = ""
#     for i in range(0, len(string1)):
#         new_string += string1[i] + string2[i]
    
#     return new_string

# print(four("String","Fridge"))
# print(four("return","letter"))


# import random 

# def five():
#     values=[]
#     while len(values) < 5:
#         a = random.randint(100,200)
#         if a % 2 == 0:
#             values.append(a)
#     return values 

# print(five())


# def six(string):
#     if string[-2:] == "py":
#         return True
#     else:
#         return False

# print(six("pyiscool"))
# print(six("welovepy"))

# def seven(a, b, c):
#     return abs(a-b) == abs(b-c)

# print(seven(4,6,2))

def seven(a, b, c):
    num_list = [a,b,c]
    num_list.sort()
    return abs(num_list[1]-num_list[0]) == abs(num_list[2]-num_list[1])

print(seven(2,4,6))

