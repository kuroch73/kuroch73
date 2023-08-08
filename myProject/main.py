from classes.Manager import *

import json

def reg():
    store_list_read = open("store/store.json","r", encoding="utf-8")
    store_list = json.loads(store_list_read.read())
    store_list_read.close()
    print(store_list) 
    regs = Registration()
    regs.create_user(store_list)
    store_list = json.dumps(store_list, ensure_ascii=False) 
    store_list_write = open("store/store.json","w", encoding="utf=8")
    store_list_write.write(store_list)
    store_list_write(store_list)
reg()

