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

#from abc import ABC, abstractmethod

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

# class GrandFather(ABC):
#     @abstractmethod
#     def __init__(self, name, hairColor):
#         self.name = name
#         self.haircolor = hairColor
#     def cookingBorscht(self):
#         print("Готовит вкусный борщ")
#     def repairCar(self):
#         print("ремонтировал авто")

# class Father(GrandFather):
#     def __init__(self, name, hairColor):
#         super().__init__(name, hairColor)

# # Iliya = GrandFather("Илья", "русый")
# # Iliya.cookingBorscht()
# Michail = Father("Михаил","русый")
# Michail.cookingBorscht()

# class Bird():
#     def __init__(self,name,sound):
#         self.name = name
#         self.sound = sound
#     def eat(self):
#         print("кушает")
#     def hunting(self):
#         print("охотятся")
#     def activeSound(self):
#         print(self.sound)

# class noFly(Bird):
#     def __init__(self, name, sound =""):
#         super().__init__(name,sound)
#     def goes(self):
#         print("ходит")

# class fly(noFly):
#     def __init__(self, name, sound = ""):
#         super().__init__(name,sound)
#     def fly(self):
#         print("летает")

# class Crow(fly):
#     def __init__(self, name):
#         super().__init__(name, " Кар")
# crow = Crow("Гриша")
# crow.activeSound()
base_list = [
    {
       "first_name" : "Denis",
       "last_name" : "Kirillov",
       "birthday" : "01.06.2001",
       "gender" : "Male",
       "login" : "denis161",
       "password" : "12345"
            },
            {
        "first_name" : "Maxim",
       "last_name" : "Maximovich",
       "birthday" : "11.04.2000",
       "gender" : "Male",
       "login" : "maks07",
       "password" : "12345"  
            },
            {
        "first_name" : "ruslan",
       "last_name" : "Ruslanov",
       "birthday" : "11.02.2000",
       "gender" : "Male",
       "login" : "russlan",
       "password" : "12345"
            },
            {
        "first_name" : "Kate",
       "last_name" : "Isaeva",
       "birthday" : "25.10.200",
       "gender" : "Female",
       "login" : "ekaterina25",
       "password" : "12345"  
            },
            {
        "first_name" : "Olga",
       "last_name" : "kulakova",
       "birthday" : "23.09.1979",
       "gender" : "Female",
       "login" : "kulak",
       "password" : "12345"
            },

]
registered_users = []
class User():
    def __init__(self,user_id, first_name,last_name,birthday,gender,login,password ) :
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        
        self.birthday = birthday
        self.gender = gender
        self.login = login
        self.password = password
        # ------------------------------
        self.status = "user"
        self.blocking = False
    def update_first_name(self,new_first_name): # update подразумевает изменения какой либо информации
        self.first_name = new_first_name
        print(f"новое имя : {self.first_name}")
    def update_last_name(self,new_last_name):
        self.last_name = new_last_name
    def update_birthday(self,new_bithday):
        self.birthday = new_bithday
    def update_ner_gender(self,new_gender):
        self.gender = new_gender
    def update_new_password(self,new_password):
        if self.password == input("Веведите старый пароль  "):
            self.password = new_password

class Moderator(User):
    def __init__(self, user_id, first_name, last_name,  birthday, gender, login, password) -> None:
        
        #self.blocking = False
        super().__init__(user_id, first_name, last_name,  birthday, gender, login, password)
        # блокировка пользователей
        self.ststus = "moderator"
    def blocking_user(self, users_list): # будем получать список пользователей 
        text_user_list = "id | first_name | blocking | status \n"
        for i in range(0,len(users_list)):
            text_user_list += f"{users_list[i].user_id}   {users_list[i].first_name}     {users_list[i].blocking}    {users_list[i].status}\n"
        print(text_user_list)
        input_user_id = int(input("введите id пользователя для блокировки "))
        for i in range(0,len(users_list)):
            if self.status == "moderator":

                if input_user_id == i and users_list[i]['status'] != "moderator" and  users_list[i]['status'] != "admin":
                    if users_list[i]['blocking'] == True:
                        print("Пользователь уже заблокирован")
                        break
                    else:
                        users_list[i]['blocking'] = True
                        print("Пользователь успешно заблокирован")
                        break
                
            elif self.status == "admin":
                if input_user_id == i :
                    if users_list[i]['blocking'] == True:
                        print("Пользователь уже заблокирован")
                        break
                    else:
                        users_list[i]['blocking'] = True
                        print("Пользователь успешно заблокирован")
                        break
class Admin(Moderator):
    def __init__(self, user_id, first_name, last_name,  birthday, gender, login, password) -> None:
        super().__init__(user_id, first_name, last_name,  birthday, gender, login, password)
        self.status = "admin"
    def delete_user_list(self, user_list):
        user_list.clear()
        print("База данных удалена")
    def create_user_list(self,massiv, user_list): # list просто массив данных
        for i in range(len(user_list),len(massiv)): 
            print(len(user_list))
            user_list.append(User(
                user_id=i+1,
                first_name = massiv[i]['first_name'],
                last_name=massiv[i]['last_name'],
                birthday=massiv[i]['birthday'],
                gender=massiv[i]['gender'],
                login=massiv[i]['login'],
                password=massiv[i]['password']))
            
class Registration():
    def __init__(self):
        pass
    def create_user(self,user_list):
        user_list.append(User(len(user_list),input("введите имя"),
                                     input("введите фамилию"),
                                     input("введите дату рождения"),
                                     input("введите пол"),
                                     input("придумайте логин"),
                                     input("введите пароль")))
class InLog():
    def __init__(self,login,password) :
        self.login = login
        self.password = password
    def log_in_account(self,users_list):

        for i in range(len(users_list)):
            if users_list[i].login == self.login and users_list[i].password == self.password:
                print("вход выполнен ")
                break
            elif i == len(users_list):
                print("ошибка")
class Manager():
    def __init__(self,reg,inlog,userModerAdmin,dataList):
        self.reg = reg
        self.inlog = inlog
        self.userModerAdmin = userModerAdmin
        self.dataList = dataList
    def work(self):
        print(self)

my_Reg = Registration
my_inLog = InLog
my_person_list = [User,Moderator,Admin]
my_base = []
#my_person_list[0](10,"admin","admin","01.01.1970","male","admin","admin")
myManager = Manager(my_Reg,my_inLog,my_person_list,my_base)
myManager.userModerAdmin[0](10,"admin","admin","01.01.1970","male","admin","admin")
myManager.inlog("admin","admin")
# class Manager(Registration,InLog ):
#     def __init__(self):
#         super().__init__()

# proverka = Registration()
# proverka.create_user()

# myAdmin = Admin(10,"admin","admin","01.01.1970","male","admin","admin")
# myAdmin.create_user_list(base_list,registered_users)
#myAdmin.blocking_user(registered_users)
#print(registered_users)
# registered_users[0].update_first_name("Денис")
# print(registered_users[0].first_name)

myLogin = InLog(input("введите логин : "),input("введите пароль :"))
myLogin.log_in_account()
# primer = [
#     User (0, "name", "01.06.2001","мужской", "login","pass"),
#     User (0, "name", "01.06.2001","мужской", "login","pass")
# ]
