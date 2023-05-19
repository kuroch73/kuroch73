# a = 2
# a= str(a)
# print(str(a))
# print(type(a))
# a = float(a)
# print(type(a))
# print(a)

# c = float(input("insert number - we multipy it on two: ")) # input is default string 
# print(c *2)
# 
# myName = "Mick"
# print("Hello" + " " + myName)
# print("Hello", " ", "world")
# print(f"hello {myName}")

# a = int(input("insert number "))
# x1 = a%10
# a = a//10
# x2 = a%10
# a = a//10
# x3 = a%10
# h = x1+x2+x3
# print(x1)
# print(x2)
# print(x3)
# print(h)
# a= 3
# b = 2
# h = a/b*10
# print(int(h))
# a = 9
# b = 7
# c = str(a)+str(b)
# c = int(c)
# print(c)

# a = 5
# b = 10
# if a > b :
#     print ("if done")
# elif a < b :

#     print (" elif done")
# else:

#     print ("else done")

# login = input("Insert login : ")
# password = input ("Insert password: ")
# if login == "admin" or "ADMIN":
#     if password == "admin":
#         print("Enter True")
#     else:
#         print("password or login False")
# else:
#     print("login False")

# q1 = input("Зимой летом одним цветом ")
# score = 0
# if q1 == "елка":
#     print("Ответ верен")
#     score = score + 1
# else:
#     print("Отывт не верный")
    
# q2 = input("Светит но не греет ")

# if q2 == "лампа":
#     print("Ответ верен")
#     score = score + 1
# else:
#     print("Отывт не верный")
    
# q3 = input(" 2 умножить на 2 ")

# if q3 == "4":
#     print("Ответ верен")
#     score = score + 1
# else:
#     print("Отывт не верный ")
    
# q4 = input("Ты программист? ")

# if q4 == "да":
#     print("Ответ верен")
#     score += 1
# else:
#     print("Отывт не верный")
     
# q5 = input("В какой стране живете? ")

# if q5 == "Россия":
#     print("Ответ верен")
#     score = score + 1
# else:
#     print("Отывт не верный")
     
# print("Количество очков  ", score)

# if score >= 3 :
#     x = input("Хотите еще вопрос?")
#     if x == "да":
#         print("Ok")
#         if x == "нет":
#             print("Получите ваши очки")
     
#     else:
#         print("Получите ваши очки")

# x = 5
# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
a = int(input("insert first number: "))
b = int(input("insert second number: "))
c = int(input("choose 1 - sum, 0 - diff: "))
if c == 0:
    print(abs(a - b))
elif c == 1:
    print(a + b)
else:
    print("введите верные данные")
