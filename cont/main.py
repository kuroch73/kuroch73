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



name = input("введите имя ")
surname = input("Введите фамилию ")
login = input("введите логин ")
password = input("введите пароль ")
while True :
    userList = []
    massive = {
            "name" : name,
            "surname" : surname,
            "login" : login,
            "password" : password
    }
    userList.append(massive)
     
        
        #print(userList)
    