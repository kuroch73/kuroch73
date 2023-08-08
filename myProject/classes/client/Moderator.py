from .User import*
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