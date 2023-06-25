 # 1 вывести карточку пользователя через ФИО гр f
# name = "Misha" # ввод имени
# surname = "Kurochkin" # ввод фамилии
# datebirth = "29 января 1979" #ввод даты рождения
# age = 44 #ввод возраста
# print(f"{name} \n {surname}\n {datebirth} \n  {age}") # печать через f 
# #2 выбор пути
# choice = 0 # задается переменная для выбора 
# for i in range(0,2): #цикл для трех вариантов выбора
     
#         choice = int(input("введите путь: ")) #ввод варианта выбора
#         if choice == 1:
#             print("Коня потеряешь")
#         elif choice == 2:
#             print("Богатым будешь")
#         else:
#              choice == 3
#              print("смерть надешь ")

# 3 Угадай число
# from random import randint # импорт библиотект генератора рандомных чисел
# x = randint(0,10)  # рандомное число записываем в х

# for i in range(0,10): # задаем интервал ввода рандомного числа
#     number = int(input("введите число ")) # число пользователя записываем в number
#     if number == x : # если чило пользователя совпало с рандомным
#          print("вы угадали !")
#     elif number > x : # если число пользоватнеля больше рандомного
#          print("ваше число больше заданного")
#     else:
#         if number < x: # если число пользователя меньше рандомного
#          print("ваше число менньше заданного")
# 4 дни недели и расписание занятий

# objectList = [                     # массив дней  и предметов
#     {
#         "day"  : "понедельник"  ,  # объект день недели
        
#         "object" : ["Физра", "Лит-ра"  ] # список предметов 
         
#     } ,   
#     {
#         "day"  :   "вторник",
        
#         "object" :[  "Мат-ка","РусЯз" ]
         
#     } ,
#     {
#         "day"  :   "среда",
        
#         "object" : [ "Химия","Физика"]
         
#     }    
#            ]

# for i in range(0, len(objectList)): #перебор элементов массива от 0 до его длины
    
#         print(f" день {objectList[i]['day']}") #  печать днй расписания в цикле
#         print(f" предмет {objectList[i]['object']}") # печать предметов по дням в цикле



    
userList =[
    {
        "userLogin" : "admin",
        "userPassword" : "1111",
        "userName" : "Misha",
        "userFirstName" : "Kuroch",
    },
    {
       "userLogin" : "admin2",
        "userPassword" : "2222",
        "userName" : "Sasha",
        "userFirstName" : "Kulak", 
    }
]
while True:
    x = int(input("Введите : \n1 - Регистрация нового пользователя \n 2- вход в ЛК "))
    if x == 1: #регистрация нового пользователя
        print(" ---- Регистрация----")
        while True:
            regUser = {
                "userLogin" : "",
                "userPassword" : "",
                "userName" : "",
                "userFirstName" : "",

            }
            while True:
                regLogin = input("Введите логин : ")
                if len(userList)>0:
                    for i in range(0,len(userList)):
                        if regLogin != userList[i]["userLogin"] :
                            regUser["userLogin"] = regLogin 
                    else:           
                        print("Данный логин уже занят \n введите другой ") 
                        regUser["userLogin"]="" 
                        break
                else:
                    regUser["userLogin"] = regLogin 
                if len(regUser["userLogin"])> 0 :
                    break
            regUser["userPassword"] = input("Введите пароль ")
            regUser["userName"] = input("введите имя нового пользователя ")
            regUser["userFirstName"] = input("введите фамилию нового пользователя ")
            print("Регистрация завершена ")
            check = int(input("1- подтвердить\n 2- ввести данные снова "))
            if check == 1:
                userList.append(regUser)
                print(userList)
                break
            elif check == 2 :
                print(" --- Регистрация ----")

        
    elif x == 2 :
        print("Вход в ЛК ")
        inLogin = input("введите логин ")
        inPassword = input("введите пароль ")
        for i in range(0, len(userList)):
            if inLogin == userList[i]["userLogin"] and inPassword == userList[i]["userPassword"]:
                print("вход выполнен ")
                while True:
                    infoUser = int(input("1-Просмотр инфо \n2- Редактировать инфо \n3- Выход "))
                    if infoUser == 1 :
                        print( f'Имя : {userList[i]["userName"]}')
                        print(f'Фамилия : {userList[i]["userFirstName"]}')
                        print(f'логин : {userList[i]["userLogin"]}')
                        print(f'пароль : {userList[i]["userPassword"]}')
                    elif infoUser == 2 :
                        print("Редактирование данных ")
                        upDate = int(input("1- Имя\n 2- ФАМИЛИЯ \n 3- пароль"))
                        if upDate == 1 :
                            print(f'ваше имя {userList[i]["userName"]}')
                            userList[i]["userName"] = input("Новое имя :")
                        elif upDate == 2 :
                            print(f'ваша фамилия {userList[i]["userFirstName"]}')
                            userList[i]["userName"] = input("Новая фамилия :") 
                        elif upDate == 3 :
                            print(f'ваш пароль {userList[i]["userPassword"]}')
                            userList[i]["userName"] = input("Новый пароль :" ) 
                    elif infoUser == 3 :                 
                        break
                break
            elif len(userList) - 1 == i:
               print("неверный логин или пароль ")
             

