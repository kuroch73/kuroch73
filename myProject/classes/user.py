class User(): # объект пользователя имеющий свои данные и свой функционал,может взаимодействовать только с самим собой,вводимые данные
    # характерны для всех пользователей вне зависимости от статуса ("user","moderator","admin")
    # status и blocking  -постоянные значения при создании класса,могут быть изменены тольк о class Moderator и Admin
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
    def update_new_gender(self,new_gender):
        self.gender = new_gender
    def update_new_password(self,new_password):
        if self.password == input("Веведите старый пароль  "):
            self.password = new_password

class Moderator(User): # имеет свойство и методы как User, а также свои доп методблокировки users, blocking наследуется от User(False)
    def __init__(self, user_id, first_name, last_name,  birthday, gender, login, password) -> None:
        
        #self.blocking = False
        super().__init__(user_id, first_name, last_name,  birthday, gender, login, password)
        # блокировка пользователей
        self.status = "moderator"
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
class Admin(Moderator):#имеет свойство и методы как Moderator, а также свои доп методблокировки users, доп метод удаления всех Usera и имеет
    # статус Admin. blocking наследуется от Mpderator(False)
    def __init__(self, user_id, first_name, last_name,  birthday, gender, login, password):
        super().__init__(user_id, first_name, last_name,  birthday, gender, login, password)
        self.status = "admin"
    def delete_user_list(self, users_list):
        users_list.clear()
        print("База данных удалена")
    def create_user_list(self,massiv, users_list): # list просто массив данных
        for i in range(len(users_list),len(massiv)): 
            print(len(users_list))
            users_list.append(User(
                user_id=i+1,
                first_name = massiv[i]['first_name'],
                last_name=massiv[i]['last_name'],
                birthday=massiv[i]['birthday'],
                gender=massiv[i]['gender'],
                login=massiv[i]['login'],
                password=massiv[i]['password']))
            
