from .Moderator import *
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