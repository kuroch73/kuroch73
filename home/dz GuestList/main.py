guest=""    # переменная имя гостя str
list = [] # задан пустой массив для добавления гостей
blacklist = [] # задан пустой массив для добавления черного списка

for i in range (0 , 10): # цикл для перебора гостей 
    
    while len(list) < 10: # гостей не более 10
        print("1 - добавить, 2 - удалить, 3 - просмотр 4 - закончить добавлять список гостей ")
        choice = int(input("введите действие "))
        if choice == 1:
            guest = input("введите имя гостя ")
            list.append(guest) # добавление гостя
        elif choice == 2 :
          guest = input("введите имя гостя ")
          list.remove(guest)    #удаление гостя
        elif choice == 3 :
           print(list) # вывод всего списка
        elif choice == 4:
            if len(list) < 5: # если гостей меньше 5 пригласиьт еще
               print("добавьте еще гостей ")
        elif guest == "Denis":
            blacklist.append(guest) #  добавление в черный список
    else:
        break
        
print(blacklist)
print(list)