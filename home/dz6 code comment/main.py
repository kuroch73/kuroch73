numberList = [1,2,3,4,5,6,7,8,9,22,11,10,6,5,22]
def delNumber(massiv) :
    print("вошел", massiv , "количество" , len(massiv))
    for i in range(0, len(massiv)):
        if i == len(massiv):
            return massiv
        elif massiv[i] % 2 == 0 :
            massiv.pop(i)
            print("вышел", massiv)
delNumber(numberList)