
print("Регистрация персонажа")
genderList = ["Мужской", "Женский"] # 0.1 массив для выбора пола
raceList = ["Человек", "Эльф", "Гном", "Орк"] # 0.2 массив для выбора расы
roleList = ["Воин", "лучник", "Маг"] # 0.3 массив для выбора роли
textRace = ""
textRole = "" # переменные для вывода высех возможных рас, изначально пустая

for i in range (0 , len(raceList)):
    textRace += f"{i} - {raceList[i]}\n" # повторять от 0 до количества рас 
textRace += f"{len(raceList)} - назад \n"
#print("регистрация персонажа")
reg = False # 0.4 глобальная регистрация / все переменные которые имеют приставку reg отвечают   
while reg == False:
    reg_gender = False
    while reg_gender == False:
        gender = input("Выберите пол \n 1 - Мужской \n 2 - Женский \n : ")
        if gender == "1":
            gender = "Мужской"
            reg_gender = True
            print("Вы выбрали  ", gender)
        elif gender == "2":
            gender = "Женский"
            reg_gender = True
            print("Вы выбрали  ", gender)
        else:
            print("Выберите из перечисленного")
        if reg_gender == True:
            reg_race = False
            while reg_race == False :
                myRace = int(input(f"0 назад Выберите расу :\n  {textRace}"))
                if myRace > len(raceList) or myRace < 0 :
                    print("Ошибка: выберите из перечисленного ")
                elif myRace == len(raceList):
                    reg_gender = False
                    break
                     
                else:
                    for i in range (0 , len(raceList)):
                        if myRace == i:
                            race = raceList[i]
                            reg_race = True
                            print("Вы выбрали  ", race)
                            break
            if  myRace == len(raceList):
                reg_gender = False
                #break
                if reg_race == True:
                    reg_role = False
                while reg_role == False :
                    myRole = int(input(f"0 назад Выберите роль :\n  {textRole}"))
                    if myRole > len(roleList) or myRole < 0 :
                        print("Ошибка: выберите из перечисленного ")
                    elif myRole == len(roleList):
                        reg_race = False
                        break
                        
                    else:
                        for i in range (0 , len(roleList)):
                            if myRole == i:
                                role = roleList[i]
                                reg_role = True
                                print("Вы выбрали  ", role)
                                break
                if  myRole == len(roleList):
                    reg_race = False
                    break
reg = True
                    