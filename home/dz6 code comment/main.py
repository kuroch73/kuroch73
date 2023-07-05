numberList = [1,2,3,4,5,6,7,8,9,22,11,10,6,5,22]
def delNumber(massiv) : # функция delNumber с параметром massiv - список []
    print("вошел", massiv , "количество" , len(massiv)) # вывод списка с количеством элементов
    for i in range(0, len(massiv)): # цикл от 0 элемента до длины списка
        if i == len(massiv): # если элемент равен длине списка
            return massiv # 
        elif massiv[i] % 2 == 0 : # также если элемент списка четный
            massiv.pop(i) # удалить его из списка
            print("вышел", massiv) # вывод "вышел" и получившийся список
            delNumber(massiv) # вызов функции с выводом списка и количеством элементов
delNumber(numberList) # вызов функции с параметром numberList  т.е. обработанном списком