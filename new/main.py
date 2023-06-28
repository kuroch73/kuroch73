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
def start():
    print("Запуск")
def stop():
    print("Стоп")

Engine = {
   "start" : start,
   "stop" : stop
}
# Engine["start"]()
# Engine["stop"]()
Car = {
    "thisMarka" : "",
    "thisColor" : "",
    "Engine" : ""
}
# auto = Car("audi","green",Engine)
    
# print(auto)
auto = Car
auto["marka"] = "audi"
auto["color"] = "green"
auto["Engine"] = Engine
#print(auto)
auto["Engine"]["start"]()