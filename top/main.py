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
# a = int(input("insert first number: "))
# b = int(input("insert second number: "))
# c = int(input("insert third number: "))
# if a + b > c and a + c > b and b + c > a:
#     print("Triangle exists")

#     if a != b and b != c and a != c:
#         print("triangle diff sides")

#     elif a == b or b == c or a == c:
#         print("triangle равносторонний")
#     else:
#         print("  равнобедренный")
# else:
#     print("треугольник не существует")

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

# myName = "Denis"
# start = int(input("Введите нач значение"))
# end = int(input("Введите конч значение"))
# k = 0
# for i in range(start,end + 1):
#     k = k + 1
#     print(myName,i)
# print(k)
# for i in myName:
#     print(i)
#     if i == "m":
#         break
# else:
#     print("NO 'm' in Denis")    
# for i in range(0,29):
#     if i % 2 != 0:
#         print(i)
# a = 2
# b = 4
# if a + b == 5:
#  for i in range(0,10):
#   print(i)
# x = int(input("Insert number  "))
# for i in range(2 , x):
#     print(f"делим число {x} на {i}")
#     print(f"остаток {x % i }")
#     if  x % i == 0:
#         print("number is complicated")
#         break
#     elif i == x:
#         print("number is simple")
# вывести каждое четное чсло кратное 6

# x = 1
# for x in range(2,100):
#     if x % 6 == 0 and x % 2 == 0:
#         print(x)

# x = 2
# for i in range(1,10):
#     print(f"{x}  x {i} = {x * i}") 
# 
# i = 0
# b = 10
# while True:
#     print(i)
#     i = i + 1
#     if i > 10:
#         break
# myName = "Denis"
# print(len(myName))
# i = 0
# while i < len(myName):
#     print(i)
#     i += 1
# n = 1
# # x = int(input("insert number "))
# b = x
# for i in range(1,x):
#     x = x*i
# print(f"Факториал от  {b} = "  , x)
# import time    
# for h in range(1,10):
#     for m  in range(1,10): # как часы, минуты, секунды и т.д.
#         for s in range(1,10):
#             print(f" ч {h}, м {m}, с {s}")   
#             time.sleep(1/100)

# h = 0
# while h < 10:
#     m = 0
#     while m < 10:
#         s = 0
#         while s < 10:
#             print(h,m,s)
#             s += 1
#         m += 1
#     h += 1        
# ------------------------------------------------------------------------

# print("Регистрация персонажа")
# genderList = ["Мужской", "Женский"] # 0.1 массив для выбора пола
# raceList = ["Человек", "Эльф", "Гном", "Орк"] # 0.2 массив для выбора расы
# roleList = ["Воин", "лучник", "Маг"] # 0.3 массив для выбора роли
# textRace = ""
# textRole = "" # переменные для вывода высех возможных рас, изначально пустая

# for i in range (0 , len(raceList)):
#     textRace += f"{i} - {raceList[i]}\n" # повторять от 0 до количества рас 
# textRace += f"{len(raceList)} - назад \n"
# #print("регистрация персонажа")
# reg = False # 0.4 глобальная регистрация / все переменные которые имеют приставку reg отвечают   
# while reg == False:
#     reg_gender = False
#     while reg_gender == False:
#         gender = input("Выберите пол \n 1 - Мужской \n 2 - Женский \n : ")
#         if gender == "1":
#             gender = "Мужской"
#             reg_gender = True
#             print("Вы выбрали  ", gender)
#         elif gender == "2":
#             gender = "Женский"
#             reg_gender = True
#             print("Вы выбрали  ", gender)
#         else:
#             print("Выберите из перечисленного")
#         if reg_gender == True:
#             reg_race = False
#             while reg_race == False :
#                 myRace = int(input(f"0 назад Выберите расу :\n  {textRace}"))
#                 if myRace > len(raceList) or myRace < 0 :
#                     print("Ошибка: выберите из перечисленного ")
#                 elif myRace == len(raceList):
#                     reg_gender = False
#                     break
                     
#                 else:
#                     for i in range (0 , len(raceList)):
#                         if myRace == i:
#                             race = raceList[i]
#                             reg_race = True
#                             print("Вы выбрали  ", race)
#                             break
#             if  myRace == len(raceList):
#                 reg_gender = False
#                 break
#                 while reg_role == False :
#                     myRole = int(input(f"0 назад Выберите роль :\n  {textRole}"))
#                     if myRace > len(raceList) or myRace < 0 :
#                         print("Ошибка: выберите из перечисленного ")
#                     elif myRace == len(raceList):
#                         reg_role = False
#                     break
                    
                # else:
                #     for i in range (0 , len(raceList)):
                #         if myRace == i:
                #             race = raceList[i]
                #             reg_race = True
                #             print("Вы выбрали  ", race)
                #             break
                #     if  myRace == len(raceList):
                #         reg_gender = False
                #     break
                    

    # reg = True

# myName = "Denis"
# v = 90
# t = 1
# s = v * t

# genderList = ["Мужской" , "Женский"]
# numberList = [3,1,4,2,8,6,9,5,4]
# newlist = []

# print(len(numberList))
# print(genderList[0])
# raceList = ["Человек", "Эльф"]
# raceList.append("Гном")
# print(raceList)
# raceList.pop(1)
# print(raceList)
# raceList.clear()
# print(raceList
# for i in range (0, len(numberList)):
#     if numberList[i] % 2 != 0 :
#         newlist.append(numberList[i])
       # newlist = numberList(i)
    #numberList[i] = numberList[i]**2
# print(newlist)

# listN = [ [1,2,3,4,5] 
#          , [6,7,8,9,10]
#          ]
# for i in range(0 , len(listN)):
#     print(listN[i])
#     for j in range(0, len(listN[i])):
#         print(listN[i][j])
# myRace = 0
# genderList = ["Мужской" , "Женский"]
# textGender = ""
# reg_gender = False
# while reg_gender == False:
#     myGender = int(input(f"Выберите пол: \n {textGender} "))  
#     if myGender > len(genderList) or myGender < 0 :
#         print("Ошибка ввода")
#     else:
#         for i in range (0, len(genderList)):
#             if myRace == i:
#                 myRace = genderList[i]
#                 reg_race = True
#                 print("Вы выбрали : " , genderList[i])
# raceList = ["Человек", "Эльф", "Гном", "Орк"]
# roleList = ["Воин", "лучник", "Маг"]
# textRace = ""
# for i in range(0, len(raceList) ):
#     textRace += f"{i} - {raceList[i]}\n"
#     #print(raceList[i])

# reg_race = False # выполнять пока False
# while reg_race == False:
#     myRace = int(input(f"Выберитк  расу: \n {textRace} "))
#     if myRace > len(raceList) or myRace < 0 :
#         print("Ошибка ввода")
#     else:
#         for i in range (0, len(raceList)):
#             if myRace == i:
#                 myRace = raceList[i]
#                 reg_race = True

#                 print("Вы выбрали : " , myRace)
#                 break
#             #print(f"я выбрал {raceList[myRace]} пк сравнивает с {raceList[i]}" )

# result = False
# sum = 0
# while sum <= 8:
#     sum = int(input("введите число "))
#     result = True


# while len(list) < 5:
#     i = 0
#     input("введите имя ", i)
#     if i == 1:
#         list.append(i)
#     break
#     #list.append([i])
#     # input("Введите имя ", i)
    # if i > 5 and i < 10:
    #     if  i == "Денис":
    #        print("Не приглашать")
# reg = False
# list = []
# while reg == False:
#     print("1 - добавить, 2 - удалить, 3 - просмотр ")
#     choice = int(input("введите действие "))
#     if choice == 1:
#         guest = input("введите имя гостя ")
#         list.append(guest)
#        print(list)
#     elif choice == 2:
#         guest = input("введите имя гостя ")
#         list.remove(guest)
#     elif choice == 3:
#         #guest = input("введите имя гостя ")
#         print(list)
#     else:
#         print("Ошибка ввода ")
# reg = True
    
# list = []
# blacklist = []
# for i in range (0 , 3):
#     print("1 - добавить, 2 - удалить, 3 - просмотр ")
#     choice = int(input("введите действие "))
#     if choice == 1:
#         guest = input("введите имя гостя ")
#         list.append(guest)
#             #print(list)
#     elif choice == 2 :
#         guest = input("введите имя гостя ")
#         list.remove(guest)
#     elif choice == 3 :
#         print(list)
#     elif len(list) < 5:
#         print(" Пригласите еще гостей ")
#     elif guest == "Denis":
#         guest = input("введите имя гостя ")
#         blacklist.append(guest)
# print(blacklist)
# print(list, len(list))

# productList = ["Каша", "Вода"]
# print(productList[0])
# infoProduct = {
#     "nameProduct" : "Каша",
#     "price" : 120,
#     "sale" : "20%",
# }
# print(f"{infoProduct['price'] }\n { infoProduct['sale']}")

# myName = input("введите имя ")
# myAge = int(input("скольво вам лет "))
# infoPerson = {
#     "namePerson" : myName,
#     "agePerson" : myAge
# }
# print(infoPerson)

# for key in infoPerson:
#     print(f"Имя  - {infoPerson[key]}")
     
# productList = [
#     {
#         "nameProduct" : "Хлеб",
#         "price" : 55,
#         "count" : 37,
#         "category" : "Хлеб"
#     },
#     {   "nameProduct" : "Молоко",
#         "price" : 101,
#         "count" : 20,
#         "category" : "молочная"

#     },
#     {
#         "nameProduct" : "Кефир",
#         "price" : 10,
#         "count" : 25,
#         "category" : "молочная"
#     }
# ]
# for i in range (0, len(productList)):
#     if productList[i]["category"] == "молочная":
#         productList[i]["price"] = productList[i]["price"] * 2
#         print(f"название товара - {productList[i]['nameProduct']}")
#         print(f" цена - {productList[i]['price']}")
#         print(f"Кол-во товара - {productList[i]['count']}")
#         print("-----------------------------------------")

guestList = []
while True:
    nameGuest = input("Введите имя гостя ")
    ageGuest = int(input("введите возраст "))
    # эти переменные будут добавляться в объект infoGuest
    # и втавляться в соответв ключи
    # infoGuest  хранит данные гостя
    infoGuest = {
        "nameGuest" : nameGuest,
        "ageGuest" : ageGuest
    }
    #print(infoGuest)
    guestList.append(infoGuest)
    if len(guestList) > 3:
        break
print(guestList)
for i in range (0 , len(guestList)):
    print(f"Имя гостя - {guestList[i]['nameGuest']}")
    print(f"Возраст гостя - {guestList[i]['Guest']}")
    print('-------------------------')