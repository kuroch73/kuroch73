guestList = []
while True:
    #if len(guestList) <= 5:
        choice = input("Выберите действие \n  1 - Добавить гостя \n 2 - Удалить гостя ")
    #else:
        #choice = input("Выберите действие \n 3 - Посмотреть список\n 4 - закончить приглашать ")
        if choice == "1":
            if len(guestList) < 10:
                nameGuest = input("Введите имя гостя : ")                                               
                ageGuest = int(input("Введите возраст гостя: "))
                infoGuest = {
                "nameGuest" : nameGuest,
                "ageGuest" : ageGuest,
                }
                guestList.append(infoGuest)
            else:
                print("Список гостей полный ")
        elif choice == "2":
            #if len(guestList) > 0 :
                nameGuest = input("Введите имя гостя : ")    
                guestList.remove(nameGuest)
            #else:
                print("список гостей пуст ")
        elif choice == "3":
            if len(guestList) > 0 :
                print("Список гостей : ")
                for i in range (0,len(guestList)):
                    print(f"Имя гостя - {guestList[i]['nameGuest']}")
                    print(f"Возраст гостя - {guestList[i]['ageGuest']}")
                    print("------------------")
            else:
                print("Список пуст ")
        elif 5 < len(guestList) < 10 :
            break

