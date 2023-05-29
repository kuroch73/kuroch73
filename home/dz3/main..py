# 1 Какого возраста пользователь
# x = int(input("insert age: "))
# if x >= 0 and x <= 2:
#     print("Child")
# elif x >= 12 and x <= 18:
#     print("Kid")
# elif x > 18 and x < 60:
#     print("adult")
# elif x >= 60:
#     print("Pensioner")
# else:
#     print("We dont know") 
# 2 Соответсвие спецсимвола числу
# x = int(input("insert number 0 to 9 : "))
# if x == 0 :
#     print(")")
# elif x == 1:
#     print("!")
#3 Равны ли цифры в 3значном числе
# x = int(input("insert three-digit number : "))
# a = x // 100
# b = x % 100 // 10
# c = x % 10
# if a == b or a == c or b == c :
#     print("Yes")
# else:
#     print("No")
# Високосный год
# x = int(input("insert year  : "))
# if x % 4 != 0:
#     print("not leap")
# elif  x % 100 == 0 :
#     if x % 400 == 0:
    
#         print("leap")
# else:
#     print("leap")
#5 Полиндром ли 5 значное число
# x = int(input("insert five-digit number : "))
# a = x // 10000
# b = x % 10000 //1000
# d = x % 100 //10
# c = x % 10
# if a == c and b == d:
#     print("Polyndrome")
# else:
#     print("not polyndrome")
# 7 Скидка с суммы покупки
# x = int(input("insert sum of purchase : "))
# if x >= 200 and x <= 300 :
#     a = x - x * 0.03
#     print("with discount: ", a) 
# elif x >300 and x <= 500 :
#     b = x - x * 0.05
#     print("with discount: ", b)  
# elif x > 500:
#     c = x - x * 0.07
#     print("with discount: ", c) 
# else:
#     print(" no discount ")
# вписывается ли окружность в квадрат
# p = float(input("insert square perimeter: "))
# l =  float(input("insert circle lenth: "))
# a = p / 4 # сторона квадрата
# r = l / (2 * 3) # Число Пи округлено до  3 ; r радиус окружности
# if r == a /2 : # радиус вписанной окружности равен половине стороны квадрата
#     print("Yes")
# else:
#     print("No")
# 9 Задача на 3 вопроса с 3 вариантами ответов, за првильный по 2 бала
# a1 = 0
# a2 = 0
# a3 = 0
# s = 0
# a1 = int(input("First question: 2 x 2 = 4 or 3 or 5 "  ))
# a2 = int(input("First question: 3 x 3 = 9 or 8 or 10 "  ))
# a3 = int(input("First question: 4 x 4 = 16 or 17 or 15 "  ))
# if a1 == 4 :
#     s = s + 2
#     print("1 True")
     
#     if a1 ==3 :
#         print("False")
#     elif a1 == 5:
#         print("False")
# else:
#     print("Choose wright variant ")
# if a2 == 9 :
#     s = s + 2
#     print("2 True")
     
#     if a2 == 10 :
#         print("False")
#     elif a2 == 8:
#         print("False")
# else:
#     print("Choose wright variant ")
# if a3 == 16 :
#     s = s + 2
#     print("3 True")
     
#     if a3 == 17 :
#         print("False")
#     elif a1 == 15:
#         print("False")
# else:
#     print("Choose wright variant ")    
# print("Количество ваших баллов " ,s)
