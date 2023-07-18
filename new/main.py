
# base_list данных как SQL не может хранить кслассы,фунцкии и т.п
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
registered_users = [] # обработанная база данных с сервера,хранит весь функционал пользователей,модераторов и админа

file = open("text.txt","r")            
print(file.read())



# my_reg = Registration
# my_inLog = InLog
# my_person_list = [User,Moderator,Admin]
# my_base = []
# # #my_person_list[0](10,"admin","admin","01.01.1970","male","admin","admin")
# myManager = Manager(my_reg,my_inLog,my_person_list,my_base)
# myManager.userModerAdmin[0](10,"admin","admin","01.01.1970","male","admin","admin")
# myManager.inlog("admin","admin")
# # class Manager(Registration,InLog ):
# #     def __init__(self):
# #         super().__init__()

# # proverka = Registration()
# # proverka.create_user()

# # myAdmin = Admin(10,"admin","admin","01.01.1970","male","admin","admin")
# myAdmin.create_user_list(base_list,registered_users)
# #myAdmin.blocking_user(registered_users)
# #print(registered_users)
# # registered_users[0].update_first_name("Денис")
# # print(registered_users[0].first_name)

# myLogin = InLog(input("введите логин : "),input("введите пароль :"))
# myLogin.log_in_account()
# # primer = [
# #     User (0, "name", "01.06.2001","мужской", "login","pass"),
# #     User (0, "name", "01.06.2001","мужской", "login","pass")
# # ]
