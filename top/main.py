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
# a = int(input("insert first number: "))
# b = int(input("insert second number: "))
# c = int(input("choose 1 - sum, 0 - diff: "))
# if c == 0:
#     print(abs(a - b))
# elif c == 1:
#     print(a + b)
# else:
#     print("введите верные данные")
# Задача 3 Пользователь вводит с клавиатуры номер месяца программа выводит на экран надпись: Winter (если введено
# значение 1,2 или 12), Spring (если введено значение от 3
# до 5), Summer (если введено значение от 6 до 8), Autumn
# (если введено значение от 9 до 11).
# Если пользователь ввел значение не в диапазоне от 1
# до 12 требуется вывести сообщение об ошибке.
# x = int(input("Insert number from 1 to 12: "))
# if x == 1 or x==2 or x== 12:
#     print("winter")
# elif x == 3 or x==4 or x== 5:
#     print("spring")
# elif x == 6 or x==7 or x== 8 :
#     print("summer")
# elif  x == 9 or x==10 or x== 11:
#     print("fall")
# else:
#     print("Error")

# a = int(input("Insert number  "))
# if a % 4 == 0:
#     print("not leap")
# elif a %100 == 0:
#     if a % 400 ==0:
#         print("leap")
# else:
#     print("not leap")
a = int(input("insert first number: "))
b = int(input("insert second number: "))
c = int(input("insert third number: "))
if a + b > c and a + c > b and b + c > a:
    print("Triangle exists")

    if a != b and b != c and a != c:
        print("triangle diff sides")

    elif a == b or b == c or a == c:
        print("triangle равносторонний")
    else:
        print("  равнобедренный")
else:
    print("треугольник не существует")

# print("Выберите пол персонажа:\n", "ж-женский\n", "м-Мужской")
# gender = str(input("Введите ж или м :\n"))
# if gender == "М" or gender == "м":
#   gender = "Мужской"
# elif gender == "Ж" or gender == "ж":
#   gender = "Женский"
# print(f"Вы выбрали {gender} пол")

# print("Выберете расу персонажа ч-человек,\n э-эльф")
# race = str(input("Введите ч или э:\n"))
# if race == "ч" or race == "Ч":
#   race = "Человек"
# elif race == "э" or race == "Э":
#   race = "Эльф"
  
#   print(f"Вы выбрали рассу {race}")

# if race == "Человек":
#   scoreRole = 0  # галочка для выбора класса
#   print("Выберете класс:\n", "1-Воин", "2-Лучник", "3-Жрец", "4-Маг")
#   role = input("введите 1,2,3 или 4 для выбора класса:")
#   if role == "1":
#      role = "Воин\n"
#   elif role == "2":
#     role = "Лучник\n"
#   elif role == "3":
#     role = "Жрец\n"
#   elif role == "4":
#     role = "Маг\n"

# elif race == "Эльф":
#     print("Выберете класс:\n", "1-Воин\n", "2-Лучник\n", "3-Темный Колдун\n",
#           "4-Паладин\n")
#     role = input("введите 1,2,3 или 4 для выбора класса")
#     if role == "1":
#       role = "Воин"
#     elif role == "2":
#       role = "Лучник"
#     elif role == "3":
#       role = "Темный Колдун"
#     elif role == "4":
#       role = "Паладин"
# print(f"Вы выбрали класс:{role}")

# name = str(input("Введите имя вашего персонажа"))
# print("\nИнформация о персонаже:\n"
#         f"пол персонажа {gender}\n"
#         f"Раса персонажа {race}\n"
#         f"Класс:{role}\n"
#         f"Имя:{name}\n")

 