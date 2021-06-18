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

def one(string):
    new_string=""
    for i in range(0, len(string)):
        new_string += string[i]*3
    return new_string

print(one("one"))
print(one("hihihi"))
