 # 1 вывести карточку пользователя через ФИО гр f
# name = "Misha"
# surname = "Kurochkin"
# datebirth = "29 января 1979"
# age = 44
# print(f"{name} \n {surname}\n {datebirth} \n  {age}")
# #2 выбор пути
# choice = 0
# for i in range(0,2):
     
#         choice = int(input("введите путь: "))
#         if choice == 1:
#             print("Коня потеряешь")
#         elif choice == 2:
#             print("Богатым будешь")
#         else:
#              choice == 3
#              print("смерть надешь ")

# 3 Угадай число
# from random import randint
# x = randint(0,10) 

# for i in range(0,10):
#     number = int(input("введите число "))
#     if number == x :
#          print("вы угадали !")
#     elif number > x :
#          print("ваше число больше заданного")
#     else:
#         if number < x:
#          print("ваше число менньше заданного")
# дни недели и расписание занятий

objectList = [
    {
        "day"  : "понедельник"  ,
        
        "object" : ["Физра", "Лит-ра"  ]
         
    } ,   
    {
        "day"  :   "вторник",
        
        "object" :[  "Мат-ка","Лит-ра" ]
         
    } ,
    {
        "day"  :   "среда",
        
        "object" : [ "Химия","Физика"]
         
    }    
           ]

for i in range(0, len(objectList)):
    #if objectList[i]["day"] == "понедельник":
        print(objectList[i]["day"])
        print(objectList[i]["object"])
         
 
    
 