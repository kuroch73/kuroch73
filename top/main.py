
# # start = int(input("Введите начальное значение: "))
# # end = int(input("введите конечное значение: "))
# for i in range(0, 29):
#     if i % 2 != 0:
#         print(i)

# for a in range(0,3):
#     print(a)

# x = int(input("Ведите число на проверку простого число"))
# for i in range(2,x+1):
#     print(f"делим число {x} на {i}")
#     print(f"Остаток {x % i}")
#     if x % i == 0 and x != i:
#         print("Число сложное")
#         break
#     elif i == x:
#         print("Число простое")


# for x in range(0,100):
#     if x % 2 == 0 and x % 7 == 0:
#         print(x)

# x = int(input("Введите число: "))
# for i in range(2,10):
#     print(f"{x} * {i} = {x * i}")
# sum = 0
# for i in range(5,8):
#     sum = sum + i
#     print(sum)

# i = 0
# b = 10
# print("первый цикл")
# while True:
#     print(i)
#     i = i + 1
#     if i > 10:
#         break
# print("второй цикл")

# x = True
# while x == True:
#     print(i)
#     i = i + 1
#     if i > 15:
#         x = False


# myName = "denis"
# print(len(myName))
# i = 0
# while i < len(myName):
#     print(i)
#     i+=1


# for i in range(10):
#     print(i)

# x = 5 
# while x > 0:
#     print(x)
#     x = x - 1

# import time
# for h in range(0,24): # h = 0
#     for m in range(0,60): # m = 1
#         for s in range(0,60): # s = 1
#             print(f"ч:{h} м:{m} с:{s}")
#             time.sleep(1/10)
# h = 0
# while h < 24:
#     m = 0
#     while m < 60:
#         s = 0
#         while s < 60:
#             print(f"ч:{h} м:{m} с:{s}")
#             s+=1
#         m+=1
#     h+=1

# dd = int(input("d"))
# mm = int(input("m"))
# yy = int(input("d"))
# if mm == 4 or mm == 6 or mm == 9 or mm == 11:
#     if dd >= 30:
#         mm+=1
#         dd=1

#     elif dd < 30:
#         dd+=1
# elif mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm== 10:
#     if dd >= 31:
#         mm+=1
#         dd=1
#     elif dd < 31:
#         dd+=1
# elif mm == 12:
#     if dd >= 31:
#         mm=1
#         dd=1
#         yy+=1
#     elif dd < 31:
#         dd+=1
# elif mm == 2:
#     if yy % 4 == 0:
#         if dd >= 29:
#             mm+=1
#             dd=1
#         elif dd < 29:
#             dd+=1
#     else:
#         if dd >= 28:
#             mm+=1
#             dd=1
#         elif dd < 28:
#             dd+=1
# print(dd,mm,yy)


# ----------------------------------------------------
# Использование циклов внутри циклов, возрат значений , + условия
# print("Регистрация персонажа")
# reg = 0
# while reg == 0:
#     reg_gender = 0
#     while reg_gender == 0:
#         gender = input("Выберете пол персонажа\n1-муж\n2-жен\n: ")
#         if gender == "1":
#             gender = "Мужской"
#             reg_gender=1
#         elif gender == "2":
#             gender = "Женский"
#             reg_gender=1
#         else:
#             print("Ошибка: Выберете из перечисленного")
#         if reg_gender == 1:
#             reg_race = 0
#             while reg_race == 0:
#                 race = input("0<-назад Выберете рассу пресонажа\n1-Человек\n2-Эльф\n: ")
#                 if race == "1":
#                     race = "Человек"
#                     reg_race = 1
#                 elif race == "2":
#                     race = "Эльф"
#                     reg_race = 1
#                 elif race == "0":
#                     reg_gender = 0
#                     break
#                 else:
#                     print("Ошибка: Выберете из перечисленного")
#                 if reg_race == 1:
#                     reg_role = 0
#                     if race == "Человек":
#                         while reg_role == 0:
#                             role = input("0<-назад Выберете рассу пресонажа\n1-Воин\n2-Лучник\n: ")
#                             if role == "1":
#                                 reg_role == 1
#                     elif race == "Эльф":
#                         pass
                    
#     reg+=1

# myName = "Denis"
# v = 90
# t = 1
# s = v*t
#                0           1 

# print(genderList[0])
#             0 1 2 3 4 5 6 7 8 9

# numberList.sort()
# print(len(numberList))


# print(raceList, "Создали список")
# raceList.append("Гном") 
# print(raceList, "raceList.append(\"Гном\")")
# raceList.pop(1)
# print(raceList, "raceList.pop(1)")
# raceList.clear()
# print(raceList, "raceList.clear()")

# numberList = [3,1,6,7,9,5,4,2,8,3]
# print(numberList)
# # for i in range (0,len(numberList)):

#     # # numberList[i] = numberList[i]**2
#     # if numberList[i] % 2 != 0:
#     #     numberList.remove(i)
# # print(numberList)

# listN = [ 
#             [1,2,3,4,5],
#             [6,7,8,9,10],
#         ]
# for i in range(0,len(listN)):
#     print(listN[i])
#     for j in range(0,len(listN[i])):
#         print([i],[j] , "=", listN[i][j])

# # 0 - перменные (массивы имеют оканчание list
# # переменные должны быть названы за что отвечают, 
# # есил это массив raceList - список рас)
# # 1 - циклы

# # 0.1 - массив для определния пола персонажа
# genderList = ["Мужской", "Женский"] 
# # 0.2 - массив для выбра расы персонажа
# raceList = ["Человек", "Эльф", "Гном", "Орк","Тролль","Гоблин"]
# # 0.3 - массив для выбра роли персонажа
# roleList = ["Воин","Лучник","Маг"]

# textRace = "" # 0.4 переменная для вывода всех возможных рас (сначала пустая)

# # i = 0
# # while i < len(raceList):
# #     textRace += f"{i} - {raceList[i]}\n"
# #     i += 1


# for i in range ( 0 , len(raceList)): # повторять от 0 до количество рас
#     # в пустую строку каждый раз будет прописываться  
#     # порядковы номер расы и его значение
#     # к примеру вывод после 2х повторений будет выгядить так
#     # № - значение
#     # 0 - Человек
#     # 1 - Эльф
#     # т.к          № 0       № 1
#     # raceList = ["Человек", "Эльф", "Гном", "Орк","Тролль"]
#     textRace += f"{i} - {raceList[i]}\n" # \n - новая строка
#     # textRace = textRace + f"{i} - {raceList[i]}\n"
# # print(len(raceList), "кол-во элементов")
# textRace += f"{len(raceList)} - назад\n" # добавить в конец запись назад
# print("Регистрация персонажа")
# reg = False # 0.4 - глобальная регистрация 
# # reg = False регистрация не завершена
# # reg = True регистрация завершена
# while reg == False: # цикл для регистрации
#     # все перемнные которые имеют приставку reg 
#     # отвечают за  
#     reg_gender = False # 
#     while reg_gender == False:
#         gender = input("Выберете пол персонажа\n1-муж\n2-жен\n: ")
#         if gender == "1":
#             gender = "Мужской"
#             reg_gender=True
#         elif gender == "2":
#             gender = "Женский"
#             reg_gender=True
#         else:
#             print("Ошибка: Выберете из перечис ленного")
#         if reg_gender == True:
#             reg_race = False # созали галочку - (нет)
#             while reg_race == False: # выполнять пока False
#                 # принимает только число
#                 print(12)
#                 myRace = int(input(f"Выберете расу:\n{textRace}"))
#                 if myRace > len(raceList) or myRace < 0:
#                     print("Ошибка: выбери из перечисленного")
#                 else:
#                     i = 0
#                     while i < len(raceList):
#                         if myRace == i:
#                             race = raceList[i]
#                             reg_race = True
#                             print("вы выбрали",race)
#                             break
#                         i += 1
#                     if reg_race == True:
#                         i = 0
#                 if myRace == len(raceList):
#                         reg_gender = False
#                         break
#     reg = True

# # задача
# # Саша и маша собирют яблоки на компот
# # Т.к Саша сильнее Маши он дожен собрать 6 яблок
# # а Маша должа собрать 3 яблока 
# # Для компота нужно 8 яблок
# # Обязательно что бы Маша и Саша принесли 8 яблок
# # 9е могут оставить себе
# x = input ("y или n")
# if x == "y":
#     result = True # False - яблоки не собраны 
# else:
#     result = False # False - яблоки не собраны 
# masha = 0 # Количество собранных яблок
# sasha = 0 # Количество собранных яблок
# # собирать яблоки пока у маши и саши не будет 8 шт
# while result:
#     # если Саша собрал меньше чем 6 яблок 
#     # он должен продолжить собирать
#     sasha = int(input("Сколько яблок собрал Саша?: "))
#     if sasha <= 6: 
#         print(f"Саша должен собрать еще {6 - sasha} яблока")
#     else:
#         print("Саша не может унести яблоки и все потерял")
#         sasha = 0
#     masha = int(input("Сколько яблок собрала Маша?: "))
#     if masha <= 3: 
#         print(f"Маша должена собрать еще {3 - masha} яблока")
#     else:
#         print("Маша не может унести яблоки и все потеряла")
#         masha = 0
#     if masha + sasha >=8:
#         print(f"Компот готов и осталось {(sasha+masha)-8} яблок")
#         break
# x = float(input())
# m = x % 1
# print(m)

# ЗАДАЧА 

    
# print("Список гостей")
# guestsList = [] # список гостей
# reg = False
# # цикл для регистрации
# while reg == False:
#     # если гостей меньше 5 то предлагать завершить регистрацию нельзя
#     if len(guestsList) < 5:
#         choice = int(input("1-добавить гостя\n2-Удалить гостя\n3-просмотр гостей"))
#     else:
#         choice = int(input("1-добавить гостя\n2-Удалить гостя\n3-просмотр гостей\n4- закончить вести список гостей"))
#     # если пользователь выберает 1, то идет проверка на количество гостей
#     # добавить гостя можно только если гостей не больше 10
#     if choice == 1:
#         if len(guestsList) < 10:
#             nameGuest = str(input("введите имя гостя: "))
#             guestsList.append(nameGuest)
#         else:
#             print("Список переполнен: кол-во гостей не может превышать более 10")
#     # Если пользователь выбрал 2, то он может удалить гостя, только если есть хотя бы один гость
#     elif choice == 2:
#         if len(guestsList) > 0:
#             textGuest = ""
#             # Цикл просмотра гостей  
#             for i in range(0,len(guestsList)):
#                 textGuest += f"{i} - {guestsList[i]}"
#             # цикл для проверки гостей т.к мы можем удалить только гостя который есть в списке 
#             print(textGuest)
#             nameGuest = str(input("введите имя гостя: "))
#             for i in range(0,len(guestsList)):
#                 if nameGuest == guestsList[i]:
#                     guestsList.remove(nameGuest)
#                     break
#         else:
#             print("вы не можете удалить гостей, список пуст")
#     elif choice == 3:
#         if len(guestsList) > 0:
#             textGuest = ""
#             # Цикл просмотра гостей  
#             for i in range(0,len(guestsList)):
#                 textGuest += f"{i} - {guestsList[i]}"
#             # цикл для проверки гостей т.к мы можем удалить только гостя который есть в списке 
#             print(textGuest)
#         else:
#             print("список гостей пуст")
#     elif choice == 4:
#         if len(guestsList) > 5 or len(guestsList) < 10:
#             break
#                0       1
# productList = ["Каша", "Вода",]
# print(productList[0])
# infoProduct = {
#     "nameProduct" : "Каша",
#     "price" : 120,
#     "sale" : 0.2,
# }
# print(f"{infoProduct['price']}\n{infoProduct['sale']}")
# myName = input("введи свое имя")
# myAge = int(input("сколько вам лет?"))
# infoPerson = {
#     "namePerson" : "Денис",
#     "agePerson" : 22,
#     "hobbyPerson" : ["Sport", "Programming"]
# }
# print(infoPerson)

# for key in infoPerson:
#     print(f"{key} - {infoPerson[key]}")

# print(f"Имя: {infoPerson['namePerson']}")

# productList = [
#     # 0
#     {
#         "nameProduct" : "Хлеб",
#         "price" : 55,
#         "count" : 37,
#         "category" : "Хлебобулочное" ,
#     },
#     # 1
#     {
#         "nameProduct" : "Молоко",
#         "price" : 101,
#         "count" : 20,
#         "category" : "Молочная",
#     },
#     {
#         "nameProduct" : "Кефир",
#         "price" : 99,
#         "count" : 6,
#         "category" : "Молочная",
#     },
# ]
# for i in range(0,len(productList)):
#     if productList[i]["category"] == "Молочная":
#         productList[i]["price"] = productList[i]["price"] * 2
#         print(f"Название товара - {productList[i]['nameProduct']}")
#         print(f"Цена - {productList[i]['price']}")
#         print(f"Кол-во - {productList[i]['count']}")
#         print("--------------------------")


guestList = []
while True:
    nameGuest = input("Введите имя гостя : ")
    ageGuest = int(input("Введите возраст гостя: "))
    # выше созданные переменные будут добавляться в объект infoGuest
    # и вставляться в соответствующие ключи
    # infoGuest - хранит данные гостя
    infoGuest = {
        "nameGuest" : nameGuest,
        "ageGuest" : ageGuest,
    }
    # print(infoGuest)
    guestList.append(infoGuest)
    if len(guestList) > 3:
        break

for i in range (0,len(guestList)):
    print(f"Имя гостя - {guestList[i]['nameGuest']}")
    print(f"Возраст гостя - {guestList[i]['ageGuest']}")
    print("------------------")

