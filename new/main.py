# Делегирование + мышление ООП
# основная функция

# def Car(marka,color):
#     thisMarka = marka
#     thisColor = color
# #    thisEngine = engine

#     activeList = {
#         "showMarka" : showMarka
#     }
#     showMarka()
#     def showMarka(param):
#         print(param)
# def start():
#     print("Запуск")
# def stop():
#     print("Стоп")

# Engine = {
#    "start" : start,
#    "stop" : stop
# }
# # Engine["start"]()
# # Engine["stop"]()
# Car = {
#     "thisMarka" : "",
#     "thisColor" : "",
#     "Engine" : ""
# }
# # auto = Car("audi","green",Engine)
    
# # print(auto)
# auto = Car
# auto["marka"] = "audi"
# auto["color"] = "green"
# auto["Engine"] = Engine
# #print(auto)
# auto["Engine"]["start"]()

# class Car:
#     def __init__(self, color,marka,engine,tyre,light): #создание переменных для класса (объекта)
#         self.color = color
#         self.marka = marka
#         self.engine = engine
#         self.tyre = tyre
#         self.light = light
#     #методы - дейстаия с определенным классом
#     def showColor(self):
#         print(self.color)
    
# class Engine:
#     def __init__(self, HP , volume):
#         self.HP = HP
#         self.volume = volume
#     def showHP(self):
#          print(self.HP)

#     def start(self):
#         print("запуск")
  
#     def stop(self):
#         print("стоп")

# class Tyre:

#     def right(self):
#         print("поворот вправо")
#     def left(self):
#         print("поворот влево")

# class Light :
    
#     def close(self):
#         print("ближний свет")
#     def far(self):
#         print("дальний свет")
    

# myLight = Light()
# myTyre = Tyre() 
# myEngine = Engine(120, 2)
# twoEngine = Engine(280,2.2)
# myAuto = Car("green","audi", twoEngine,myTyre,myLight)
# print(myAuto)
# myEngine.start()

# myAuto.engine.start()
# myAuto.tyre.right()
# myAuto.light.far()
# print(myAuto.engine.HP)

# # Наследование
# class SportCar(Car) :
#     def __init__(self, color, marka, engine, tyre, light,abs):
#         self.abs = abs
#         super().__init__(color, marka, engine, tyre, light)    

# lamborghiniEngine = Engine(900, 6)
# twoAuto = SportCar("blue" , "lamboghini", lamborghiniEngine, myTyre , myLight , True)

# class TurboEngine (Engine):
#     def __init__(self, HP, volume,turbo):
#         self.turbo = turbo
#         super().__init__(HP, volume)
# twoEngine = TurboEngine(20,2,5)
# twoEngine.showHP() # show тоже наследуется из Engine
# print(twoEngine.turbo)

from abc import ABC, abstractmethod

# class Animal(ABC) :
#     @abstractmethod
#     def __init__(self, name , sound) :
#         self.name = name 
#         self.sound = sound
#     def activeSound(self):
#         print(self.sound)

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name, "Мяу")
#     def purr(self):
#         print("Мурлыкает")

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name, "Гав")
#     def digHole(self):
#         print("Копает яму")



# myCat = Cat("Вася")
# myCat.purr()


# myDonkey = Animal("Осел", "Иа-Иа")
# myDonkey.activeSound()

# class Human(ABC):
#     @abstractmethod
#     def __init__(self, name, nationality):
#         self.name = name
#         name.nationality = nationality

# class Man(Human):
#     def __init__(self, name, nationality):
         
#         self.gender = "мужской"
#         super().__init__(name, nationality)
# class Woman(Human):
#     def __init__(self, name, nationality):
         
#         self.gender = "женский"
#         super().__init__(name, nationality)   

# men = Human("Денис", "китаец")
# Woman = Woman("Денис", "китаец")

class GrandFather(ABC):
    @abstractmethod
    def __init__(self, name, hairColor):
        self.name = name
        self.haircolor = hairColor
    def cookingBorscht(self):
        print("Готовит вкусный борщ")
    def repairCar(self):
        print("ремонтировал авто")

class Father(GrandFather):
    def __init__(self, name, hairColor):
        super().__init__(name, hairColor)

# Iliya = GrandFather("Илья", "русый")
# Iliya.cookingBorscht()
Michail = Father("Михаил","русый")
Michail.cookingBorscht()

class Bird():
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def eat(self):
        print("кушает")
    def hunting(self):
        print("охотятся")
    def activeSound(self):
        print(self.sound)

class noFly(Bird):
    def __init__(self, name, sound =""):
        super().__init__(name,sound)
    def goes(self):
        print("ходит")

class fly(noFly):
    def __init__(self, name, sound = ""):
        super().__init__(name,sound)
    def fly(self):
        print("летает")

class Crow(fly):
    def __init__(self, name):
        super().__init__(name, " Кар")
crow = Crow("Гриша")
crow.activeSound()