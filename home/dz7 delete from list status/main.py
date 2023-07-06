clientList = [
    {
        "name" : "Misha",
        "status" : "оплачен"
    },
    {
        "name" : "Sasha",
        "status" : "оплачен"
    },
    {
        "name" : "Kate",
        "status" : "не оплачен"
    },
    {
        "name" : "Zina",
        "status" : "оплачен"
    },
    {
        "name" : "Den",
        "status" : "не оплачен"
    },
    {
        "name" : "Max",
        "status" : "оплачен"
    },
            ]
def numberList(massiv): 
    for i in range (0, len(massiv)) :
        if i == len(massiv):
            return massiv
        elif clientList[i]["status"] == "не оплачен":
            massiv.pop(i)
            print("Новый список")
             
            for i in range(0, len(massiv)):
                print(f"Имя :  {clientList[i]['name']}   Статус : {clientList[i]['status']}")
            numberList(massiv)
numberList(clientList)